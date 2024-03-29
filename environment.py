import os
import subprocess
from pathlib import Path

from peerster_objects.shared_file import SharedFile


def before_all(context):
    context.log_path = os.getcwd() + '/logs/'
    os.chdir("..")


def before_feature(context, feature):
    subprocess.call(["killall", "Peerster"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    assert subprocess.call(["go", "build", "-race"]) is 0
    assert subprocess.call(["go", "build"], cwd='./client') is 0


def before_scenario(context, scenario):
    context.nodes = {}
    context.files = {}
    SharedFile.remove_all_shared_files()
    SharedFile.remove_all_downloads()


def after_scenario(context, scenario):
    for node in context.nodes.values():
        node.process.terminate()
    subprocess.call(["killall", "Peerster"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
