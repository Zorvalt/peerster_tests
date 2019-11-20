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
  Scenario: Gossiper should fine file in direct neighbor
    Given a node "A"
    And a node "B" knowing "A"
    And a shared file "some_file" of size 1kB
    When a client asks "A" to share file "some_file"
    And a client asks "B" to search for "some_file" with budget 2
    Then the node "B" wait for "FOUND match some_file at A" or max "2" seconds
    And the node "B" should have logged "FOUND match some_file at A"
