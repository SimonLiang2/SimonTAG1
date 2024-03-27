import socket
import pickle
import threading
from Packet import Packet


class ClientSocket:
    def __init__(self, host='127.0.0.1', port=3000, listening=True):
        self.inited = False
        self.id = None
        self.admin = False
        self.player_data = None
        self.round_started = False
        self.round_timer = 90
        self.map_name = "map_1"
        self.lobby_full  = False
        self.it_flag = False
        try:
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_client.connect((host, port))
            self.listening = listening
            self.inited = True
        except:
            self.inited = False 
        return 
    
    def start_thread(self):
        self.socket_thread = threading.Thread(target=self.socket_receive_data)
        self.socket_thread.start()

    def kill_connection(self):
        self.listening = False
        self.socket_client.close()

    def send_data(self,msg,content=None):
            if(self.inited):
                data = Packet(source=self.id, header=msg, data=content)
                data = data.serialize()
                self.socket_client.send(data)

    def socket_receive_data(self):
        while True:
            response = self.socket_client.recv(4096)
            response = self.unpack_packet(response)
            
            if False:
                print("{")
                print(f"source:{response.source},")
                print(f"header:{response.header},")
                print(f"data:{response.data},")
                print("}")
        
            if(response.header == "connected"):
                self.id = response.data[0]
                self.admin = response.data[1]
            elif(response.header == "kill-socket"):
                print("Killing Socket")
                self.inited = False
                break  
            elif(response.header == "lobby-full"):
                self.lobby_full = True
                self.inited = False
                break
            elif(response.header == "become-admin"):
                self.admin = True
            elif(response.header == "server-message"):
                print("----SERVER MESSAGE----")
                print(f"  {response.data}    ")
                print("----------------------")
            elif(response.header == "start-round"): self.round_started = True
            elif(response.header == "player-tick"): self.player_data = response.data
            elif(response.header == "timer-update"): self.round_timer  = response.data
            elif(response.header == "map-update"): self.map_name = response.data
            elif(response.header == "youre-it"): self.it_flag = True

        self.kill_connection()
        return 

    def unpack_packet(self, data):
        return pickle.loads(data)