import subprocess
import time
import tempfile
from peerster_objects.common import *


class Gossiper:
    def __init__(self, name: str, peers: str = "", simple=False):
        offset = gossiper_name_to_port_offset(name)
        gossip_port = BASE_GOSSIP_PORT + offset
        ui_port = BASE_UI_PORT + offset

        command = [
            './Peerster',
            '-name=' + name,
            '-v',
            '-gossipAddr=127.0.0.1:' + str(gossip_port),
            '-UIPort=' + str(ui_port),
            '-GUIPort=' + str(ui_port),
        ]
        if simple:
            command.append('-simple')

        if len(peers) > 0:
            peers_str = ""
            for peer in peers.split(","):
                peers_str += "127.0.0.1:" + str(BASE_GOSSIP_PORT + gossiper_name_to_port_offset(peer)) + ","
            command.append('-peers=' + peers_str[:-1])

        output_file = tempfile.NamedTemporaryFile('w+')
        self.process = subprocess.Popen(command, stdout=output_file, stderr=output_file)
        self.output_file = open(output_file.name, 'r')

        # Waits for gossiper init
        print("Waiting for gossiper {} to start...".format(name))
        while not self.search_output("Gossiper running"):
            time.sleep(0.1)
        print("\tStarted!")

    def search_output(self, needle: str) -> bool:
        self.output_file.seek(0)
        return needle in self.output_file.read()
