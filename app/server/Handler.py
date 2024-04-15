
import socket
import random 
from Packet import Packet

class PacketHandler:
    def __init__(self, client_conn, clients_conns, clients_data, client_id, packet, timer):
        self.client_conn = client_conn
        self.clients_conns = clients_conns
        self.clients_data = clients_data
        self.client_id = client_id
        self.packet = packet
        self.timer = timer
        self.assiged_tagger = False

    # Packets recv by server should call this event
    # Function determines proper response during event
    def handle_event(self):
        match(self.packet.header):
            case "kill-socket":
                self.kill_socket_event()
            case "player-tick":
                self.clients_data[self.client_id] = self.packet.data
                response = Packet(source=self.packet.source, header="player-tick", data=self.clients_data)
                response = response.serialize()
                self.client_conn.send(response)

                self.round_data = [self.timer.time, self.timer.map]
                response = Packet(source=self.packet.source, header="update-tick", data=self.round_data)
                response = response.serialize()
                self.client_conn.send(response)
            case "map-req":
                self.timer.time
                map_name = self.timer.map
                response = Packet(source=self.packet.source, header="map-update", data=map_name)
                response = response.serialize()
                self.client_conn.send(response)
            case "start-round":
                players = self.clients_conns.items()
                if(not self.timer.round_started):
                    it_player = random.choice(list(players))[1]
                    response = Packet(source="Server", header="youre-it", data=None)
                    response = response.serialize()
                    it_player.send(response)
                self.timer.round_started = True
                for key,client in players:
                        response = Packet(source="Server", header="start-round", data=None)
                        response = response.serialize()
                        client.send(response)
            case "player-leave":
                if self.client_id in self.clients_data: del self.clients_data[self.client_id]
                self.clients_data = self.clients_data  
            case "get-admin":
                 players = self.clients_conns.items()
                 player_count = len(self.clients_conns.items())
                 if(player_count > 1):
                         for key,client in players:
                                if(key != self.packet.source):
                                      response = Packet(source="Server", header="become-admin", data=None)
                                      response = response.serialize()
                                      client.send(response)
                                      break
            case "get-new-tagger":
                    players = self.clients_conns.items()
                    if(len(players) > 1):
                        it_player = random.choice(list(players))
                        response = Packet(source="Server", header="youre-it", data=None)
                        response = response.serialize()
                        it_player[1].send(response)
            case _: # default case -> packet header is not known
                print(">> The server just recieved a bad header!")
                response = Packet(source=self.packet.source, header="bad-header", data="invalid header")
                response = response.serialize()
                self.client_conn.send(response)

    def kill_socket_event(self):
        player_count = len(self.clients_conns.items())
        player_count-=1
        print(player_count)
        if(player_count <= 0):
            self.timer.round_started = False
            self.timer.reset()
        response = Packet(source=self.packet.source, header="kill-socket", data=self.packet.data)
        response = response.serialize()
        self.client_conn.send(response)