from behave import *

from peerster_objects.client import Client, random_string


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


@when('a client sends a random message of size {size} to each gossiper')
def step_impl(context, size):
    for gossiper in context.nodes:
        Client.send_to(gossiper, random_string(int(size)))


@when('a client asks "{name}" to search for "{keywords}" with budget {budget}')
def step_impl(context, name, keywords, budget):
    assert Client(name).search(keywords, budget) == 0


@when('a client asks "{name}" to search for "{keywords}"')
def step_impl(context, name, keywords):
    assert Client(name).search(keywords) == 0
