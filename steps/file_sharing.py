from behave import *

from peerster_objects.client import Client
from peerster_objects.shared_file import SharedFile


@given('a shared file "{filename}" of {size}')
def step_impl(context, filename, size):
    if filename in context.files.keys():
        raise ValueError("The same file has been declared twice")
    context.files[filename] = SharedFile(size)


@when('a client asks "{node_name}" to share file "{filename}"')
def step_impl(context, node_name, filename):
    if Client(node_name).share_file(filename) != 0:
        raise EnvironmentError("The client failed to ask {} to share the file {}".format(node_name, filename))


@when('a client asks "{getter_node}" to download file "{filename}" from "{source_node}"')
def step_impl(context, getter_node, filename, source_node):
    file = context.files[filename]
    if Client(getter_node).download_file(file.file_name, file.hash, source_node) != 0:
        raise EnvironmentError("The client failed to ask {} to download the file {} from {}",
                               getter_node, filename, source_node)


@then('the node "{getter_node}" should have downloaded metafile of "{filename}" from "{source_node}"')
def step_impl(context, getter_node, filename, source_node):
    file = context.files[filename]
    log = "DOWNLOADING metafile of {} from {}".format(file.file_name, source_node)
    assert context.nodes[getter_node].search_output(log)


@then('the node "{getter_node}" should have downloaded chunks of "{filename}" from "{source_node}"')
def step_impl(context, getter_node, filename, source_node):
    file = context.files[filename]
    gossiper = context.nodes[getter_node]
    for i in range(1, file.nb_chunk):
        log = "DOWNLOADING {} chunk {} from {}".format(file.file_name, i, source_node)
        assert gossiper.search_output(log)


@then('the file "{filename}" should be present in the download folder')
def step_impl(context, filename):
    assert context.files[filename].is_correct()
