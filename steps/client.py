from behave import *

from peerster import Client


@given('a node "{name}"')
def step_impl(context, name):
    context.nodes[name] = {'logs': ""}


@when('a client sends "{name}" a message "{message}"')
def step_impl(context, name, message):
    output = Client.send_to(name, message)
    print(output)
