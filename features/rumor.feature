Feature: Rumor
  A rumor should propagate between nodes

  Scenario: A rumor should propagate to a direct node
    Given a node "A" knowing "B"
    And a node "B"
    When a client sends "A" a message "M"
    And wait for 0.5 seconds
    Then the node "B" should have logged "RUMOR origin A from 127.0.0.1:5000 ID 2 contents M"