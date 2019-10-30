from behave import *


@given('a simple node "{name}"')
def step_impl(context, name):
    context.nodes[name] = {'logs': ""}
