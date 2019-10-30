# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestPeerster(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_peerster_must_not_crash_in_10_seconds(self):
        # Given a node "A"
        self.actionwords.a_node_name(name = "A")
        # When "10" seconds elapsed
        self.actionwords.duration_seconds_elapsed(duration = "10")

    def test_2_peersters_must_not_crash_in_10_seconds_copy(self):
        # Given a node "B"
        self.actionwords.a_node_name(name = "B")
        # Given a node "A"
        self.actionwords.a_node_name(name = "A")
        # When "10" seconds elapsed
        self.actionwords.duration_seconds_elapsed(duration = "10")
        # And "B" must be running
        self.actionwords.name_must_be_running(name = "B")
        # And "A" must be running
        self.actionwords.name_must_be_running(name = "A")
