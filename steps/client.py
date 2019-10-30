from behave import *


@given('a node "{name}"')
def step_impl(context, name):
    context.nodes[name] = {'logs': ""}


@when('a client sends "{name}" a message "{message}"')
def step_impl(context, name, message):
    context.nodes[name]["logs"] += message
