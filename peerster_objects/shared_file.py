import filecmp
import glob
import os
from pathlib import Path

from peerster_objects.common import *


class SharedFile:
    def __init__(self, size: str):
        self.file_name = random_string()
        with open(SHARE_DIRECTORY_NAME + self.file_name, "w") as fout:
            fout.write(random_string(size))

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
