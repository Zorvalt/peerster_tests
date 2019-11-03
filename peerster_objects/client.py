import subprocess

from peerster_objects.common import *


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
        command = ['./client/client', '-UIPort=' + str(ui_port), '-msg="' + message+'"']
        return subprocess.check_output(command).decode()
