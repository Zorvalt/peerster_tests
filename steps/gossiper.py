from behave import *


@then('the node "{name}" should have logged the received message "{message}" from a client')
def step_impl(context, name, message):
    assert message in context.nodes[name]["logs"]
