import socket
import threading
import pickle
import random
import time
from Packet import Packet
from Handler import PacketHandler
from ServerTimer import ServerTimer

# Multithreaded server that can handle multiple clients
class GameServer:
    def __init__(self, host='127.0.0.1', port=3000, client_max=5, debug=False):
        self.timer = ServerTimer(time=15)
        self.BUFFER_SIZE = 4096
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients_data = {}
        self.clients_conns = {}
        self.client_max = client_max
        self.debug = debug

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
            "|                                     |",
            "+-------------------------------------+"
        ]
        for line in banner_lines: print(line)

    def print_lobby_size(self): print(f">> Lobby Size ({len(self.clients_conns)}/{self.client_max})")

    # Used to deserialize Packets
    def unpack_packet(self, data):
        return pickle.loads(data)
    
    def print_packet_data(self,packet,addr):
        print(f"----{addr}----")
        print(f"Source: \t{packet.source}")
        print(f"Header: \t{packet.header}")
        print(f"Data  : \t{packet.data}")
        print(f"----------------------------")

    # Thread created to handle each client
    def client_thread(self, client_conn, addr,_client_id):
        client_id = _client_id
        while True:
            try:
                # Recv data
                data = client_conn.recv(self.BUFFER_SIZE)
                if not data:
                    # Associate with DISCONNECT
                    if client_id in self.clients_conns: del self.clients_conns[client_id] 
                    if client_id in self.clients_data: del self.clients_data[client_id]
                    client_conn.close()
                    print(f">> client disconnect")
                    self.print_lobby_size()
                    break

                # Deserialize data into a packet
                packet = self.unpack_packet(data)

                # If in debug mode-> print packet data
                if self.debug:self.print_packet_data(packet, addr)

                # Send a response using the packethandler utility
                packetHandler = PacketHandler(client_conn, self.clients_conns, 
                                              self.clients_data, client_id, 
                                              packet, self.timer)
                packetHandler.handle_event()

            except ConnectionResetError:
                print(f">> Client: {client_id}, has closed their connection...")
                if client_id in self.clients_conns: del self.clients_conns[client_id] 
                if client_id in self.clients_data: del self.clients_data[client_id]
                client_conn.close()
                break

            except Exception as e:
                print(f">> There was an issue with a client: {client_id}, so they are getting removed...")
                if client_id in self.clients_conns:del self.clients_conns[client_id] 
                if client_id in self.clients_data: del self.clients_data[client_id]
                client_conn.close()
                break
    
    def update_timer(self):
        while True: 
                self.timer.update()

    def run(self):
        self.server_startup_banner() # print the startup banner

        #keeps timer ticking while server is running
        try: threading.Thread(target=self.update_timer).start()
        except Exception as e: pass

        # main loop
        while True:
            print(">> Waiting for a new client to join...")

            # client accepted -> continue
            client_conn, addr = self.server.accept()
            id = self.gen_uniquie_id(5)
            print(f">> A new client has connected with the id: {id}")

            # Check if lobby is full
            if (len(self.clients_conns) < self.client_max) and (not self.timer.round_started):

                # A broadcasted message to all connected clients
                for key,client in self.clients_conns.items():
                    response = Packet(source="server", header="server-message", 
                                      data="A new client has joined")
                    response = response.serialize()
                    client.send(response)

                # Append new client to list of clients
                # Mapping id->socket connection
                self.clients_conns[id] = client_conn
                
                # Give the client a thread
                try: threading.Thread(target=self.client_thread, args=(client_conn, addr,id)).start()
                except Exception as e: pass # can print error here
                
                # Inform the client of its id
                player_count = len(self.clients_conns.items())
                response = Packet(source="server", header="connected", data=[id,player_count==1])
                response = response.serialize()
                self.clients_conns[id].send(response)
            else:
                # Full lobby => no thread
                print(">> rejecting client => lobby full or round_started")
                data = Packet(source= "server", header="lobby-full", data=self.client_max)
                data = data.serialize()
                client_conn.send(data)
                client_conn.close()
            self.print_lobby_size()

    # forces server to crash by killing server connection
    def kill(self): self.server.close()

if __name__ == "__main__":
    server = GameServer(host='127.0.0.1',client_max=5,debug=False)
    server_thread = threading.Thread(target=server.run)
    server_thread.start() 
    server_thread.join() 