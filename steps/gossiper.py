from behave import *

from peerster import Gossiper


@given('a node "{name}"')
def step_impl(context, name):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")
    context.nodes[name] = Gossiper(name)


@given('a node "{name} knowing {neighbors}"')
def step_impl(context, name, neighbors):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")
    context.nodes[name] = Gossiper(name, peers=neighbors)


@then('the node "{name}" should have logged the received message "{message}" from a client')
def step_impl(context, name, message):
    found = context.nodes[name].search_output("CLIENT MESSAGE "+message)
    assert found is True


@then('the node "{receiver}" should have logged the received message "{message}" from node "{sender}"')
def step_impl(context, receiver, message, sender):
    found = context.nodes[receiver].search_output("CLIENT MESSAGE " + message)
    assert found is True
