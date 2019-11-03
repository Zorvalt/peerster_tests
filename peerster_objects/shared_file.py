from peerster_objects.common import *


class SharedFile:
    def __init__(self, size: str):
        self.file_name = random_string()
        # TODO Create the file in SHARE_DIRECTORY_NAME folder
        # TODO Fill the file with `size` random bytes
        pass

    def is_downloaded(self) -> bool:
        # TODO Check if file is present in DOWNLOAD_DIRECTORY_NAME folder
        return False

    def is_correct(self) -> bool:
        if not self.is_downloaded():
            return False

        # TODO Compare files in SHARE_DIRECTORY_NAME with the one in DOWNLOAD_DIRECTORY_NAME
        return False
