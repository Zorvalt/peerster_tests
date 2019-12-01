from behave import *

from peerster_objects.client import Client
from peerster_objects.shared_file import SharedFile


@given('a shared file "{filename}" of size {size}')
def step_impl(context, filename, size):
    if filename in context.files.keys():
        raise ValueError("The same file has been declared twice")
    context.files[filename] = SharedFile(filename, size)


@when('a client asks "{node_name}" to share file "{filename}"')
def step_impl(context, node_name, filename):
    file = context.files[filename]
    if Client(node_name).share_file(file.file_name) != 0:
        raise EnvironmentError("The client failed to ask {} to share the file {}".format(node_name, filename))


@when('a client asks "{getter_node}" to download file "{filename}" from "{source_node}"')
def step_impl(context, getter_node, filename, source_node):
    file = context.files[filename]
    if Client(getter_node).download_file(file.file_name, file.metahash, source_node) != 0:
        raise EnvironmentError("The client failed to ask {} to download the file {} from {}",
                               getter_node, filename, source_node)


@when('a client asks "{getter_node}" to download file "{filename}" from an implicit source')
def step_impl(context, getter_node, filename):
    file = context.files[filename]
    if Client(getter_node).download_file(file.file_name, file.metahash) != 0:
        raise EnvironmentError("The client failed to ask {} to download the file {} from an implicit source",
                               getter_node, filename)


@when("all downloaded files are removed from the directory")
def step_impl(context):
    SharedFile.remove_all_downloads()


@then('the node "{getter_node}" should have downloaded metafile of "{filename}" from "{source_node}"')
def step_impl(context, getter_node, filename, source_node):
    file = context.files[filename]
    log = "DOWNLOADING metafile of {} from {}".format(file.file_name, source_node)
    assert context.nodes[getter_node].search_output(log)


@then('the node "{getter_node}" should have downloaded chunks of "{filename}" from "{source_node}"')
def step_impl(context, getter_node, filename, source_node):
    file = context.files[filename]
    gossiper = context.nodes[getter_node]
    for i in range(1, file.nb_chunks+1):
        log = "DOWNLOADING {} chunk {} from {}".format(file.file_name, i, source_node)
        assert gossiper.search_output(log)


@then('the node "{getter_node}" should have reconstructed the file "{filename}"')
def step_impl(context, getter_node, filename):
    file = context.files[filename]
    log = "RECONSTRUCTED file {}".format(file.file_name)
    assert context.nodes[getter_node].search_output(log)
    assert context.files[filename].is_correct()
