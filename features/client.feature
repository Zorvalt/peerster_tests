Feature: client controls the gossiper
  The client sends commands to the gossiper that must receive them ans handle it correctly

  Scenario: Receive a message in simple mode
    Given a simple node "A"
    When a client sends "A" a message "M"
    Then the node "A" should have logged the received message "M" from a client