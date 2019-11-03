from behave import *

from peerster_objects.gossiper import Gossiper


@given('a simple node "{name}"')
def step_impl(context, name):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")
    context.nodes[name] = Gossiper(name, simple=True)
