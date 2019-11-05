Feature: A lots of nodes

  Scenario: 26 nodes gossiping heavily
    Given a node "A" knowing "5" of "A" to "Z"
    And a node "B" knowing "5" of "A" to "Z"
    And a node "C" knowing "5" of "A" to "Z"
    And a node "D" knowing "5" of "A" to "Z"
    And a node "E" knowing "5" of "A" to "Z"
    And a node "F" knowing "5" of "A" to "Z"
    And a node "G" knowing "5" of "A" to "Z"
    And a node "H" knowing "5" of "A" to "Z"
    And a node "I" knowing "5" of "A" to "Z"
    And a node "J" knowing "5" of "A" to "Z"
    And a node "K" knowing "5" of "A" to "Z"
    And a node "L" knowing "5" of "A" to "Z"
    And a node "M" knowing "5" of "A" to "Z"
    And a node "N" knowing "5" of "A" to "Z"
    And a node "O" knowing "5" of "A" to "Z"
    And a node "P" knowing "5" of "A" to "Z"
    And a node "Q" knowing "5" of "A" to "Z"
    And a node "R" knowing "5" of "A" to "Z"
    And a node "S" knowing "5" of "A" to "Z"
    And a node "T" knowing "5" of "A" to "Z"
    And a node "U" knowing "5" of "A" to "Z"
    And a node "V" knowing "5" of "A" to "Z"
    And a node "W" knowing "5" of "A" to "Z"
    And a node "X" knowing "5" of "A" to "Z"
    And a node "Y" knowing "5" of "A" to "Z"
    And a node "Z" knowing "5" of "A" to "Z"

    When wait for 60 seconds
    Then all nodes should be running
