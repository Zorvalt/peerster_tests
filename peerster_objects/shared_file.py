import filecmp
import glob
import hashlib
import os
from pathlib import Path

from peerster_objects.common import *
from peerster_objects.human_bytes_converter import human2bytes


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


class SharedFile:
    def __init__(self, name: str, size: str):
        byte_size = human2bytes(size)
        self.file_name = name
        self.hashes = []
        with open(SHARE_DIRECTORY_NAME + self.file_name, "w") as fout:
            content = random_string(byte_size)
            fout.write(content)
            self.hashes = divide_chunks(content, CHUNK_SIZE)

        self.hashes = list(map(lambda chunk: hashlib.sha256(chunk.encode()).digest(), self.hashes))
        self.metahash = hashlib.sha256(b''.join(self.hashes)).hexdigest()
        self.nb_chunks = len(self.hashes)

    def is_downloaded(self) -> bool:
        return Path(DOWNLOAD_DIRECTORY_NAME + self.file_name).is_file()

    def is_correct(self) -> bool:
        if not self.is_downloaded():
            return False
        return filecmp.cmp(SHARE_DIRECTORY_NAME + self.file_name, DOWNLOAD_DIRECTORY_NAME + self.file_name)

    @staticmethod
    def remove_all_shared_files():
        files = glob.glob(os.path.join(SHARE_DIRECTORY_NAME, "*"))
        for file in files:
            os.remove(file)

    @staticmethod
    def remove_all_downloads():
        files = glob.glob(os.path.join(DOWNLOAD_DIRECTORY_NAME, "*"))
        for file in files:
            os.remove(file)
