import random
import string

BASE_UI_PORT = 8080
BASE_GOSSIP_PORT = 5000
SHARE_DIRECTORY_NAME = '_SharedFolder'
DOWNLOAD_DIRECTORY_NAME = '_Downloads'


def gossiper_name_to_port_offset(name: str) -> int:
    if len(name) is not 1 or ord(name) < ord('A') or ord(name) > ord('Z'):
        raise ValueError("A gossiper name must be a single capital letter")
    else:
        return ord(name) - ord('A')


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(string_length))
