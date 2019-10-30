import subprocess


def before_feature(context, feature):
    subprocess.call(["killall", "Peerster"])
    assert subprocess.call(["go", "build"]) is 0
    assert subprocess.call(["go", "build"], cwd='./client') is 0


def before_scenario(context, scenario):
    context.nodes = {}


def after_scenario(context, scenario):
    for node in context.nodes.values():
        node.process.terminate()
    subprocess.call(["killall", "Peerster"])
