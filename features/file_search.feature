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