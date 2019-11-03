import time

from behave import *

from peerster_objects.client import Client


@when('a client sends "{sender}" a private message "{message}" to "{destination}"')
def step_impl(context, sender, message, destination):
    """
    :param destination:
    :param message:
    :param sender:
    :type context: behave.runner.Context
    """
    Client.send_private_to(sender, message, destination)


@when('a client sends "{name}" a message "{message}"')
def step_impl(context, name, message):
    Client.send_to(name, message)


@then('the node "{name}" wait for "{message}" or max "{s}" seconds')
def step_impl(context, name, message, s):
    count = 0
    while not context.nodes[name].search_output(message) and count/10 < int(s):
        time.sleep(0.1)
        count += 1
