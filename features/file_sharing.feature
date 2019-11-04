Feature: File sharing
  A node should be able to download a file shared by anoher - direct or indirect - node

  Scenario: A node downloads a small file from a direct peer
    Given a node "A"
    And a node "B" knowing "A"
    And a shared file "F1" of 3kB
    And wait for 0.1 seconds
    When a client asks "A" to share file "F1"
    And wait for 1 seconds
    And a client asks "B" to download file "F1" from "A"
    And wait for 0.1 seconds
    Then the node "B" should have downloaded metafile of "F1" from "A"
    And the node "B" should have downloaded chunks of "F1" from "A"
    And the node "B" should have reconstructed the file "F1"

  Scenario: A node downloads a big file from a direct peer
    Given a shared file "F1" of 2MB
    And a node "A"
    And a node "B" knowing "A"
    And wait for 0.1 seconds
    When a client asks "A" to share file "F1"
    And wait for 1 seconds
    And a client asks "B" to download file "F1" from "A"
    And wait for 10 seconds
    Then the node "B" should have downloaded metafile of "F1" from "A"
    And the node "B" should have downloaded chunks of "F1" from "A"
    And the node "B" should have reconstructed the file "F1"

  Scenario: A node downloads a small file from an indirect peer
    Given a shared file "F1" of 3kB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And wait for 0.1 seconds
    When a client asks "A" to share file "F1"
    And wait for 3 seconds
    And a client asks "C" to download file "F1" from "A"
    And wait for 15 seconds
    Then the node "C" should have downloaded metafile of "F1" from "A"
    And the node "C" should have downloaded chunks of "F1" from "A"
    And the node "C" should have reconstructed the file "F1"

  Scenario: A node downloads a big file from an indirect peer
    Given a shared file "F1" of 2MB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And wait for 0.1 seconds
    When a client asks "A" to share file "F1"
    And wait for 3 seconds
    And a client asks "C" to download file "F1" from "A"
    And wait for 15 seconds
    Then the node "C" should have downloaded metafile of "F1" from "A"
    And the node "C" should have downloaded chunks of "F1" from "A"
    And the node "C" should have reconstructed the file "F1"