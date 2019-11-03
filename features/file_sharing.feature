Feature: File sharing
  A node should be able to download a file shared by anoher - direct or indirect - node

  Scenario: A node downloads a small file from a direct peer
    Given a shared file "F1" of 3kB
    And a node "A"
    And a node "B" knowing "A"
    And the node "A" shares file "F1"
    When a client asks "B" to download "F1" from "A"
    Then the node "B" should have downloaded metafile of "F1" from "A"
    And the node "B" should have downloaded chunks of "F1" from "A"
    And the file "F1" should be present in the download folder

  Scenario: A node downloads a big file from a direct peer
    Given a shared file "F1" of 2MB
    And a node "A"
    And a node "B" knowing "A"
    And the node "A" shares file "F1"
    When a client asks "B" to download "F1" from "A"
    Then the node "B" should have downloaded metafile of "F1" from "A"
    And the node "B" should have downloaded chunks of "F1" from "A"
    And the file "F1" should be present in the download folder

  Scenario: A node downloads a small file from an indirect peer
    Given a shared file "F1" of 3kB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And the node "A" shares file "F1"
    When a client asks "C" to download "F1" from "A"
    Then the node "C" should have downloaded metafile of "F1" from "A"
    And the node "C" should have downloaded chunks of "F1" from "A"
    And the file "F1" should be present in the download folder

  Scenario: A node downloads a big file from an indirect peer
    Given a shared file "F1" of 2MB
    And a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And the node "A" shares file "F1"
    When a client asks "C" to download "F1" from "A"
    Then the node "C" should have downloaded metafile of "F1" from "A"
    And the node "C" should have downloaded chunks of "F1" from "A"
    And the file "F1" should be present in the download folder