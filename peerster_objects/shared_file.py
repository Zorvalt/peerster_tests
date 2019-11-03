import filecmp
import glob
import hashlib
import os
from math import ceil
from pathlib import Path

from peerster_objects.common import *
from peerster_objects.human_bytes_converter import human2bytes


class SharedFile:
    def __init__(self, size: str):
        byte_size = human2bytes(size)
        self.file_name = random_string()
        self.hashes = []
        with open(SHARE_DIRECTORY_NAME + self.file_name, "w") as fout:
            content = random_string(byte_size)
            fout.write(content)
            self.hashes.append(hashlib.sha256(content.encode()).digest())

        self.metahash = hashlib.sha256(b''.join(self.hashes)).hexdigest()
        self.nb_chunks = len(self.hashes)

    def is_downloaded(self) -> bool:
        return Path(DOWNLOAD_DIRECTORY_NAME + self.file_name).is_file()

    def is_correct(self) -> bool:
        if not self.is_downloaded():
            return False
        return filecmp.cmp(SHARE_DIRECTORY_NAME + self.file_name, DOWNLOAD_DIRECTORY_NAME + self.file_name)

    @staticmethod
    def remove_all_downloads():
        files = glob.glob(os.path.join(DOWNLOAD_DIRECTORY_NAME, "*"))
        for file in files:
            os.remove(file)
