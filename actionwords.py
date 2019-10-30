# encoding: UTF-8

class Actionwords:
    def __init__(self, test):
        self.test = test

    def a_node_name(self, name = "A"):
        # starts a named node
        # TODO: Implement action: "Start the node %s" % (name)
        raise NotImplementedError

    def duration_seconds_elapsed(self, duration = "10"):
        # TODO: Implement action: "Wait for %s seconds" % (Duration)
        raise NotImplementedError

    def name_must_be_running(self, name = "A"):
        # TODO: Implement result: "Check %s is running" % (name)
        raise NotImplementedError
