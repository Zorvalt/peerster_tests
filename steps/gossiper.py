import random
import time

from behave import *

from peerster_objects.gossiper import Gossiper


@given('a node "{name}" knowing "{number}" of "{first_neighbor}" to "{last_neighbor}"')
def step_impl(context, name, number, first_neighbor, last_neighbor):
    if name in context.nodes.keys():
        raise EnvironmentError("The same node has been asked twice")

    neighbors = []
    for i in range(ord(first_neighbor), ord(last_neighbor) + 1):
        neighbors.append(chr(i))
    selected_neighbors = random.sample(neighbors, int(number))
    context.nodes[name] = Gossiper(name, peers=','.join(selected_neighbors))


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


@then('the node "{name}" wait for "{message}" or max "{s}" seconds')
def step_impl(context, name, message, s):
    count = 0
    while not context.nodes[name].search_output(message) and count/10 < int(s):
        time.sleep(0.1)
        count += 1


@step('output the log of "{name}"')
def step_impl(context, name):
    context.nodes[name].log_output(context.log_path + name + '.log')


@then('output the log of "{name}" to file "{file}"')
def step_impl(context, name, file):
    context.nodes[name].log_output(file)


@then('all nodes should be running')
def step_impl(context):
    failed = []
    for name, node in context.nodes.items():
        if not node.is_running():
            failed.append(name)

    if len(failed) != 0:
        print("Failed nodes: {}".format(','.join(failed)))
        assert False
