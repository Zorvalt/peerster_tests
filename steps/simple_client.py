from behave import *


@given('a simple node "{name}"')
def step_impl(context, name):
    context.nodes[name] = {'logs': ""}


@when('a simple client sends "{name}" a message "{message}"')
def step_impl(context, name, message):
    context.nodes[name]["logs"] += message