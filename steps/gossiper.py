from behave import *

from peerster import Gossiper


@given('a node "{name}"')
def step_impl(context, name):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")
    context.nodes[name] = Gossiper(name)


@then('the node "{name}" should have logged the received message "{message}" from a client')
def step_impl(context, name, message):
    assert message in context.nodes[name]["logs"]
