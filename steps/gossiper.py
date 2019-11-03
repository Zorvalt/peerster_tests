from behave import *

from peerster_objects.gossiper import Gossiper


@given('a node "{name}" knowing "{neighbors}"')
def step_impl(context, name, neighbors):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")
    context.nodes[name] = Gossiper(name, peers=neighbors)


@given('a node "{name}"')
def step_impl(context, name):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")
    context.nodes[name] = Gossiper(name)


@then('the node "{name}" should have logged "{message}"')
def step_impl(context, name, message):
    found = context.nodes[name].search_output(message)
    assert found is True


@then('the node "{name}" should not have logged "{message}"')
def step_impl(context, name, message):
    found = context.nodes[name].search_output(message)
    assert found is False


@then('output the log of "{name}" to file "{file}"')
def step_impl(context, name, file):
    context.nodes[name].log_output(file)