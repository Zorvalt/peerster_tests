Feature: Private messaging
  A node should be able to send a receive private messages from other peers


  Scenario: A sends a message to C through B
    Given a node "A" knowing "B"
    And a node "B" knowing "A,C"
    And a node "C" knowing "B"
    When a client sends "C" a message "Hi"
    Then the node "A" wait for "RUMOR origin C" or max "100" seconds
    When a client sends "A" a private message "M" to "C"
    Then the node "A" should have logged "CLIENT MESSAGE "M" dest C"
    Then the node "C" wait for "PRIVATE origin A" or max "10" seconds
    Then the node "C" should have logged "PRIVATE origin A hop-limit 9 contents "M""


  Scenario: A sends a message to C through B in weired config
    Given a node "A" knowing "B"
    And a node "B" knowing "A,D,E"
    And a node "D" knowing "D,E,F"
    And a node "E" knowing "C,D,E"
    And a node "F" knowing "E,C"
    And a node "C" knowing "F"

    When a client sends "C" a message "Hi"
    Then the node "A" wait for "RUMOR origin C" or max "100" seconds
    When a client sends "A" a private message "M" to "C"

    Then the node "C" wait for "PRIVATE origin A" or max "100" seconds
    Then the node "C" should have logged "PRIVATE origin A"
    Then the node "A" should have logged "CLIENT MESSAGE "M" dest C"
    Then the node "B" should not have logged "PRIVATE origin A"
    Then the node "C" should have logged "PRIVATE origin A"


  Scenario: A sends a message to L in a too long way
    Given a node "A" knowing "B"
    And a node "B" knowing "A,C"
    And a node "C" knowing "B,D"
    And a node "D" knowing "C,E"
    And a node "E" knowing "D,F"
    And a node "F" knowing "E,G"
    And a node "G" knowing "F,H"
    And a node "H" knowing "G,I"
    And a node "I" knowing "H,J"
    And a node "J" knowing "I,K"
    And a node "K" knowing "J,L"
    And a node "L" knowing "K"

    When a client sends "L" a message "Hi"
    Then the node "A" wait for "RUMOR origin L" or max "100" seconds
    When a client sends "A" a private message "M" to "L"
    Then the node "L" wait for "PRIVATE origin A" or max "100" seconds

    Then the node "A" should have logged "CLIENT MESSAGE "M" dest L"
    Then the node "B" should not have logged "PRIVATE origin A"
    Then the node "C" should not have logged "PRIVATE origin A"
    Then the node "D" should not have logged "PRIVATE origin A"
    Then the node "E" should not have logged "PRIVATE origin A"
    Then the node "F" should not have logged "PRIVATE origin A"
    Then the node "G" should not have logged "PRIVATE origin A"
    Then the node "H" should not have logged "PRIVATE origin A"
    Then the node "I" should not have logged "PRIVATE origin A"
    Then the node "J" should not have logged "PRIVATE origin A"
    Then the node "K" should not have logged "PRIVATE origin A"
    Then the node "L" should not have logged "PRIVATE origin A"


  Scenario: A sends a message to K in a long way
    Given a node "A" knowing "B"
    And a node "B" knowing "A,C"
    And a node "C" knowing "B,D"
    And a node "D" knowing "C,E"
    And a node "E" knowing "D,F"
    And a node "F" knowing "E,G"
    And a node "G" knowing "F,H"
    And a node "H" knowing "G,I"
    And a node "I" knowing "H,J"
    And a node "J" knowing "I,K"
    And a node "K" knowing "J,L"
    And a node "L" knowing "K"

    When a client sends "K" a message "Hi"
    Then the node "A" wait for "RUMOR origin K" or max "100" seconds
    When a client sends "A" a private message "M" to "K"

    Then the node "K" wait for "PRIVATE origin A" or max "100" seconds
    Then the node "A" should have logged "CLIENT MESSAGE "M" dest C"
    Then the node "B" should not have logged "PRIVATE origin A"
    Then the node "C" should not have logged "PRIVATE origin A"
    Then the node "D" should not have logged "PRIVATE origin A"
    Then the node "E" should not have logged "PRIVATE origin A"
    Then the node "F" should not have logged "PRIVATE origin A"
    Then the node "G" should not have logged "PRIVATE origin A"
    Then the node "H" should not have logged "PRIVATE origin A"
    Then the node "I" should not have logged "PRIVATE origin A"
    Then the node "J" should not have logged "PRIVATE origin A"
    Then the node "K" should have logged "PRIVATE origin A hop-limit 0 contents "M""
