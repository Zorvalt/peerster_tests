import subprocess


def before_feature(context, feature):
    assert subprocess.call(["go", "build"]) is 0
    assert subprocess.call(["go", "build"], cwd='./client') is 0


def before_scenario(context, scenario):
    context.nodes = {}