Feature: File search
  Gossiper can search for files in their neighbordhood. A search is composed of:
  A list of keywords(with * as a wildcard) and a budget representing the number of node to browse.

  # Client test
  Scenario: Client should accept the keywords option alone
    When a client asks "A" to search for "some_file"
    # Then nothing, this should pass

  Scenario: Client should accept the keywords and the budget options together
    When a client asks "A" to search for "some_file" with budget 20
    # Then nothing, this should pass

  # Gossiper tests
  Scenario Outline: Gossiper should find file "<file>" in direct neighbor with keywords "<keywords>"
    Given a node "A"
    And a node "B" knowing "A"
    And a shared file "<file>" of size 1kB
    When a client asks "A" to share file "<file>"
    And a client asks "B" to search for "<keywords>" with budget 2
    Then the node "B" wait for "FOUND match <file> at A" or max "1" seconds
    And the node "B" should have logged "FOUND match <file> at A"
    Examples:
      | file    | keywords   |
      | target  | target     |
      | target  | a,target,b |
      | target  | *get       |
      | target  | a,*get,b   |
      | target  | tar*       |
      | target  | a,tar*,b   |
      | target  | t*t        |
      | target  | a,t*t,b    |

  Scenario Outline: Gossiper should NOT find file "<file>" in direct neighbor with keywords "<keywords>"
    Given a node "A"
    And a node "B" knowing "A"
    And a shared file "<file>" of size 1kB
    When a client asks "A" to share file "<file>"
    And a client asks "B" to search for "<keywords>" with budget 2
    Then the node "B" wait for "FOUND match <file> at A" or max "1" seconds
    And the node "B" should not have logged "FOUND match <file> at A"
    Examples:
      | file    | keywords   |
      | target  | targett     |
      | target  | a,targett,b |
      | target  | *gett       |
      | target  | a,*gett,b   |
      | target  | ttar*       |
      | target  | a,ttar*,b   |
      | target  | t*tt        |
      | target  | a,tt*t,b    |

  Scenario: Gossiper should NOT find file in indirect neighbor budget 2
    Given a node "A"
    And a node "B" knowing "A"
    And a node "C" knowing "B"
    And a shared file "some_file" of size 1kB
    When a client asks "A" to share file "some_file"
    And a client asks "C" to search for "some_file" with budget 2
    Then the node "C" wait for "FOUND match some_file at A" or max "1" seconds
    And the node "C" should not have logged "FOUND match some_file at A"

  Scenario: Gossiper should find file in indirect neighbor budget 4
    Given a node "A" knowing "B"
    And a node "B" knowing "A,C"
    And a node "C" knowing "B"
    And a shared file "some_file" of size 1kB
    When a client asks "A" to share file "some_file"
    And a client asks "C" to search for "some_file" with budget 4
    Then the node "C" wait for "FOUND match some_file at A" or max "1" seconds
    And the node "C" should have logged "FOUND match some_file at A"

  Scenario: Gossiper should find file in indirect neighbor budget 7 even if direct has two matching files
    Given a node "A" knowing "B"
    And a node "B" knowing "A,D"
    And a node "C" knowing "D"
    And a node "D" knowing "B,C"
    And a shared file "target" of size 1kB
    When a client asks "A" to share file "target"
    And a client asks "B" to share file "target"
    And a client asks "C" to share file "target"
    And a client asks "D" to search for "target" with budget 7
    Then the node "D" wait for "FOUND match target at A" or max "1" seconds
    And output the log of "A"
    And output the log of "B"
    And output the log of "C"
    And output the log of "D"
    And the node "D" should have logged "FOUND match target at B"
    And the node "D" should have logged "FOUND match target at C"
    And the node "D" should have logged "FOUND match target at A"
