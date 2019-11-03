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

  Scenario: Node shares a received message
    Given a node "A" knowing "B"
    Given a node "B"
    When a client sends "A" a message "M"
    Then wait for 0.5 seconds
    Then the node "B" should have logged "RUMOR origin A from 127.0.0.1:5000 ID 2 contents "M""

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
