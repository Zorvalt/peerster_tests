Feature: File sharing
  A node should be able to download a file shared by anoher - direct or indirect - node

  Scenario: A node downloads a small file from a direct peer
    Given a node "A"
    And a node "B" knowing "A"
    And a shared file "F1" of size 3kB
    When a client asks "A" to share file "F1"
    Then the node "B" wait for "RUMOR origin A" or max "5" seconds
    When a client asks "B" to download file "F1" from "A"
    Then the node "B" wait for "RECONSTRUCTED" or max "10" seconds
    And the node "B" should have downloaded metafile of "F1" from "A"
    And the node "B" should have downloaded chunks of "F1" from "A"
    And the node "B" should have reconstructed the file "F1"

  Scenario: A node downloads a big file from a direct peer
    Given a shared file "F1" of size 2MB
    And a node "A"
    And a node "B" knowing "A"
    When a client asks "A" to share file "F1"
    Then the node "B" wait for "RUMOR origin A" or max "5" seconds
    When a client asks "B" to download file "F1" from "A"
    Then the node "B" wait for "RECONSTRUCTED" or max "20" seconds
    And the node "B" should have downloaded metafile of "F1" from "A"
    And the node "B" should have downloaded chunks of "F1" from "A"
    And the node "B" should have reconstructed the file "F1"

  Scenario: A node downloads a small file from an indirect peer
    Given a shared file "F1" of size 3kB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    When a client asks "A" to share file "F1"
    Then the node "B" wait for "RUMOR origin A" or max "5" seconds
    When a client asks "C" to download file "F1" from "A"
    Then the node "C" wait for "RECONSTRUCTED" or max "15" seconds
    And the node "C" should have downloaded metafile of "F1" from "A"
    And the node "C" should have downloaded chunks of "F1" from "A"
    And the node "C" should have reconstructed the file "F1"

  Scenario: A node downloads a big file from an indirect peer
    Given a shared file "F1" of size 2MB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    When a client asks "A" to share file "F1"
    Then the node "B" wait for "RUMOR origin A" or max "5" seconds
    When a client asks "C" to download file "F1" from "A"
    Then the node "C" wait for "RECONSTRUCTED" or max "20" seconds
    And the node "C" should have downloaded metafile of "F1" from "A"
    And the node "C" should have downloaded chunks of "F1" from "A"
    And the node "C" should have reconstructed the file "F1"

  Scenario: A node downloads a small file from an indirect peer separated by 8 other nodes
    Given a shared file "F1" of size 3kB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And a node "D" knowing "C"
    And a node "E" knowing "D"
    And a node "F" knowing "E"
    And a node "G" knowing "F"
    And a node "H" knowing "G"
    And a node "I" knowing "H"
    And a node "J" knowing "I"
    And a node "K" knowing "J"
    When a client asks "A" to share file "F1"
    Then the node "K" wait for "RUMOR origin A" or max "5" seconds
    When a client asks "K" to download file "F1" from "A"
    Then the node "K" wait for "RECONSTRUCTED" or max "60" seconds
    And the node "K" should have downloaded metafile of "F1" from "A"
    And the node "K" should have downloaded chunks of "F1" from "A"
    And the node "K" should have reconstructed the file "F1"

  Scenario: A node downloads a big file from an indirect peer separated by 8 other nodes
    Given a shared file "F1" of size 2MB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And a node "D" knowing "C"
    And a node "E" knowing "D"
    And a node "F" knowing "E"
    And a node "G" knowing "F"
    And a node "H" knowing "G"
    And a node "I" knowing "H"
    And a node "J" knowing "I"
    And a node "K" knowing "J"
    When a client asks "A" to share file "F1"
    Then the node "K" wait for "RUMOR origin A" or max "5" seconds
    When a client asks "K" to download file "F1" from "A"
    Then the node "K" wait for "RECONSTRUCTED" or max "60" seconds
    And the node "K" should have downloaded metafile of "F1" from "A"
    And the node "K" should have downloaded chunks of "F1" from "A"
    And the node "K" should have reconstructed the file "F1"