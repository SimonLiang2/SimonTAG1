import socket
from Packet import Packet
from PlayerData import PlayerData

class PacketHandler:
    def __init__(self, client_conn, clients_conns, clients_data, client_id, packet, timer):
        self.client_conn = client_conn
        self.clients_conns = clients_conns
        self.clients_data = clients_data
        self.client_id = client_id
        self.packet = packet
        self.timer = timer


    def handle_event(self):
        match(self.packet.header):
            case "kill-socket":
                self.kill_socket_event()
            case "player-tick":
                self.clients_data[self.client_id] = [self.packet.data[0],self.packet.data[1],False]
                response = Packet(source=self.packet.source, header="player-tick", data=self.clients_data)
                response = response.serialize()
                self.client_conn.send(response)
            
                self.round_data = [self.timer.update(), self.timer.map]
                response = Packet(source=self.packet.source, header="update-tick", data=self.round_data)
                response = response.serialize()
                self.client_conn.send(response)
            case "timer-req":
                self.round_data = self.timer.update()
                response = Packet(source=self.packet.source, header="timer-update", data=self.round_data)
                response = response.serialize()
                self.client_conn.send(response)
            case "map-req":
                self.timer.update()
                map_name = self.timer.map
                response = Packet(source=self.packet.source, header="map-update", data=map_name)
                response = response.serialize()
                self.client_conn.send(response)
            case "player-leave":
                del self.clients_data[self.client_id]
                self.clients_data = self.clients_data

                

    def kill_socket_event(self):
        response = Packet(source=self.packet.source, header="kill-socket", data=self.packet.data)
        response = response.serialize()
        self.client_conn.send(response)
