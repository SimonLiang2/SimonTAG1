import socket
from Packet import Packet
from PlayerData import PlayerData

class PacketHandler:
    def __init__(self, client_conn, clients_conns, clients_data, client_id, packet):
        self.client_conn = client_conn
        self.clients_conns = clients_conns
        self.clients_data = clients_data
        self.client_id = client_id
        self.packet = packet


    def handle_event(self):
        match(self.packet.header):
            case "kill-socket":
                self.kill_socket_event()
            case "player-tick":
                self.clients_data[self.client_id] = [self.packet.data[0],self.packet.data[1],False]
                response = Packet(source=self.packet.source, header="player-tick", data=self.clients_data)
                response = response.serialize()
                self.client_conn.send(response)
            case "player-leave":
                del self.clients_data[self.client_id]
                self.clients_data = self.clients_data
                

    def kill_socket_event(self):
        response = Packet(source=self.packet.source, header="kill-socket", data=self.packet.data)
        response = response.serialize()
        self.client_conn.send(response)
