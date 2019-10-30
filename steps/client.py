from behave import *

from peerster import Client


@when('a client sends "{name}" a message "{message}"')
def step_impl(context, name, message):
    Client.send_to(name, message)
