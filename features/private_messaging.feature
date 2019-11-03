Feature: Private messaging
  A node should be able to send a receive private messages from other peers


  Scenario: A sends a message to C through B
    Given a node "A" knowing "B"
    And a node "B" knowing "A,C"
    And a node "C" knowing "B"
    Then wait for 0.5 seconds
    When a client sends "A" a private message "M" to "C"
    Then wait for 0.5 seconds
    Then the node "A" should have logged "CLIENT MESSAGE "M""