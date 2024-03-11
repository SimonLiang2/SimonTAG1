import socket
import threading
import pickle
import random
import time
from Packet import Packet
from Handler import PacketHandler

# Multithreaded server that can handle multiple clients
class GameServer:
    def __init__(self, host='127.0.0.1', port=3000, client_max=5, debug=False):
        self.BUFFER_SIZE = 4096
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients_data = {}
        self.clients_conns = {}
        self.client_max = client_max
        self.debug = False

    def gen_uniquie_id(self,length):
        # Define the characters you want in the random string
        characters = "abcdefghijklmnopqrstuvwxyz" 
        characters += characters.capitalize()
        # Generate a random string of the specified length
        random_string = ''.join(random.choice(characters) for _ in range(length))

        return random_string
    
    def server_startup_banner(self):
        banner_lines = [
            "+-------------------------------------+",
            "|       Python Tag Game Server        |",
            "|          Starting Up...             |",
            "+-------------------------------------+"
        ]
        for line in banner_lines:
            print(line)

    # Used to deserialize Packets
    def unpack_packet(self, data):
        return pickle.loads(data)

    # Thread created to handle each client
    def client_thread(self, client_conn, addr,_client_id):
        client_id = _client_id
        while True:
            try:
                # Recv data
                data = client_conn.recv(self.BUFFER_SIZE)
                if not data:
                    # Associate with DISCONNECT
                    del self.clients_conns[client_id]
                    client_conn.close()
                    del self.clients_data[client_id]
                    break

                # Deserialize data into packet
                packet = self.unpack_packet(data)
                if self.debug:
                    print(f"----{addr}----")
                    print(f"Source: \t{packet.source}")
                    print(f"Header: \t{packet.header}")
                    print(f"Data  : \t{packet.data}")
                    print(f"----------------------------")

                packetHandler = PacketHandler(client_conn, self.clients_conns, self.clients_data, client_id, packet)
                packetHandler.handle_event()

            except ConnectionResetError:
                print(f"Client: {client_id}, has closed their connection...")
                del self.clients_conns[client_id]
                del self.clients_data[client_id]
                client_conn.close()
                break

            except Exception as e:
                # this exception is WIP
                print(f"There was an issue with a client: {client_id}, so they are getting removed...")
                del self.clients_conns[client_id]
                del self.clients_data[client_id]
                client_conn.close()
                break

    def run(self):
        self.server_startup_banner()

        # main loop
        while True:
            print("listening for new clients...")

            # client accepted -> continue
            client_conn, addr = self.server.accept()
            id = self.gen_uniquie_id(5)
            print(f"New Client: {id}")
            # Check if lobby is full
            if len(self.clients_conns) < self.client_max:

                for key,client in self.clients_conns.items():
                    response = Packet(source="server", header="server-message", data="Say Hello! A new client has joined!")
                    response = response.serialize()
                    client.send(response)

                self.clients_conns[id] = client_conn
                # Give client a thread
                try:
                    threading.Thread(target=self.client_thread, args=(client_conn, addr,id)).start()
                except Exception as e:
                    # can print error here
                    pass
                
                #this will be the pLayer data
                response = Packet(source="server", header="connected", data=id)
                response = response.serialize()
                self.clients_conns[id].send(response)
            else:
                # Full lobby => no thread
                print("rejecting client => lobby full")
                data = Packet(source= "server", header="lobby-full", data=self.client_max)
                data = data.serialize()
                client_conn.send(data)
                client_conn.close()

            print(f"Lobby Size ({len(self.clients_conns)}/{self.client_max})")

    # forces server to crash by killing server connection
    def kill(self):
        self.server.close()

if __name__ == "__main__":
    server = GameServer(client_max=5,debug=True)
    server_thread = threading.Thread(target=server.run)
    server_thread.start() 
    server_thread.join() 