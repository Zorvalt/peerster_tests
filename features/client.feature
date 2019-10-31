Feature: client controls the gossiper
  The client sends commands to the gossiper that must receive them ans handle it correctly

  Scenario: Client sends a message to a simple node
    Given a simple node "A"
    When a client sends "A" a message "M"
    Then wait for 0.2 seconds
    Then the node "A" should have logged the received message "CLIENT MESSAGE M" from a client

  Scenario: Client sends a message to a node
    Given a node "A"
    When a client sends "A" a message "M"
    Then wait for 0.2 seconds
    Then the node "A" should have logged the received message "CLIENT MESSAGE M" from a client

  Scenario: Node shares a received message
    Given a node "A" knowing "B"
    Given a node "B"
    When a client sends "A" a message "M"
    Then wait for 0.2 seconds
    Then the node "B" should have logged the received message "RUMOR origin A from 127.0.0.1:5000 ID 1 contents M" from node "A"