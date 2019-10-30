import subprocess

BASE_UI_PORT = 8080


def gossiper_name_to_port(name: str) -> int:
    if len(name) is not 1 or ord(name) < ord('A') or ord(name) > ord('Z'):
        raise ValueError("A gossiper name must be a single capital letter")
    else:
        return BASE_UI_PORT + ord(name) - ord('A')


class Client:
    def __init__(self, gossiper_name: str):
        self.ui_port = gossiper_name_to_port(gossiper_name)

    def send(self, message: str) -> str:
        return Client.send_to_port(self.ui_port, message)

    @staticmethod
    def send_to(gossiper_name: str, message: str) -> str:
        return Client.send_to_port(gossiper_name_to_port(gossiper_name), message)

    @staticmethod
    def send_to_port(ui_port: int, message: str) -> str:
        command = ['./client/client', '-UIPort=' + str(ui_port), '-msg=' + message]
        return subprocess.check_output(command).decode()
