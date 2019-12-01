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
        command = ['./client/client', '-UIPort=' + str(ui_port), '-msg=' + message + '']
        return subprocess.check_output(command).decode()

    def send_private(self, message: str, dest: str) -> str:
        return Client.send_private_to_port(self.ui_port, message, dest)

    @staticmethod
    def send_private_to(gossiper_name: str, message: str, dest: str) -> str:
        return Client.send_private_to_port(BASE_UI_PORT + gossiper_name_to_port_offset(gossiper_name), message, dest)

    @staticmethod
    def send_private_to_port(ui_port: int, message: str, dest: str) -> str:
        command = ['./client/client', '-UIPort=' + str(ui_port), '-msg=' + message+'', '-dest='+dest]
        return subprocess.check_output(command).decode()

    def share_file(self, filename):
        command = ['./client/client', '-UIPort=' + str(self.ui_port), '-file=' + filename + '']
        return subprocess.call(command)

    def download_file(self, filename, hash_str, source_node=None):
        command = [
            './client/client',
            '-UIPort=' + str(self.ui_port),
            '-file={}'.format(filename),
            '-request={}'.format(hash_str)
        ]
        if source_node is not None:
            command.append('-dest={}'.format(source_node))

        return subprocess.call(command)

    def search(self, keywords, budget=None):
        command = ['./client/client', '-UIPort=' + str(self.ui_port), '-keywords=' + keywords + '']
        if budget is not None:
            command.append('-budget=' + str(budget))
        return subprocess.call(command)
