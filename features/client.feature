Feature: client controls the gossiper
  The client sends commands to the gossiper that must receive them ans handle it correctly

  Scenario: Client sends a message to a simple node
    Given a simple node "A"
    When a client sends "A" a message "M"
    Then wait for 0.5 seconds
    Then the node "A" should have logged "CLIENT MESSAGE "M""

  Scenario: Client sends a message to a node
    Given a node "A"
    When a client sends "A" a message "M"
    Then wait for 0.5 seconds
    Then the node "A" should have logged "CLIENT MESSAGE "M""
