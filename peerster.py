import subprocess
import time
import tempfile

BASE_UI_PORT = 8080
BASE_GOSSIP_PORT = 5000


def gossiper_name_to_port_offset(name: str) -> int:
    if len(name) is not 1 or ord(name) < ord('A') or ord(name) > ord('Z'):
        raise ValueError("A gossiper name must be a single capital letter")
    else:
        return ord(name) - ord('A')


class Client:
    def __init__(self, gossiper_name: str):
        self.ui_port = BASE_UI_PORT + gossiper_name_to_port_offset(gossiper_name)

    def send(self, message: str) -> str:
        return Client.send_to_port(self.ui_port, message)

    @staticmethod
    def send_to(gossiper_name: str, message: str) -> str:
        return Client.send_to_port(BASE_UI_PORT + gossiper_name_to_port_offset(gossiper_name), message)

    @staticmethod
    def send_to_port(ui_port: int, message: str) -> str:
        command = ['./client/client', '-UIPort=' + str(ui_port), '-msg=' + message]
        return subprocess.check_output(command).decode()


class Gossiper:
    def __init__(self, name: str, peers: str = None):
        offset = gossiper_name_to_port_offset(name)
        gossip_port = BASE_GOSSIP_PORT + offset
        ui_port = BASE_UI_PORT + offset

        self.output_file = tempfile.TemporaryFile('w+')
        self.output_buffer = []
        self.process = subprocess.Popen([
            './Peerster',
            '-name=' + name,
            '-gossipAddr=127.0.0.1:' + str(gossip_port),
            '-UIPort=' + str(ui_port),
            '-GUIPort=' + str(ui_port),
        ], stdout=self.output_file)
        time.sleep(1)

    def search_output(self, needle: str) -> bool:
        self.output_file.seek(0)
        return needle in self.output_file.read()
