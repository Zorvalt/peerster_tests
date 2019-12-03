# Peerster tests

Collection of tests for the Peerster project of the CS438 course at EPFL.

There are currently [29 scenarios testing 6 features](#implemented-scenarios-by-feature).

## Disclamer

Those tests are not guaranteed to be correct nor complete.
You might pass all of them and still have issues in your code.
Given the complexity of the handout, some tests may even be based on wrong assumptions.

If you see any mistake or possible improvement, please signal it.

## Overview
This project uses [behave](https://pypi.org/project/behave/) to implement steps that can be used in [Gherkin](https://www.guru99.com/gherkin-test-cucumber.html) feature files.

When declaring a gossiper, the port is computed with the base value (5000 or 8080) + the position of the letter in the alphabet, starting at 0.

Example :
```gherkin
Feature: File search
    Scenario: Gossiper should find file in indirect neighbor budget 4
        Given a node "A" knowing "B"
        And a node "B" knowing "A,C"
        And a node "C" knowing "B"
        And a shared file "some_file" of size 1kB
        Then wait for "A" knowing "C" or max "1" seconds
        When a client asks "A" to share file "some_file"
        And a client asks "C" to search for "some_file" with budget 4
        Then the node "C" wait for "FOUND match some_file at A" or max "1" seconds
        And output the log of each running node
        And the node "C" should have logged "FOUND match some_file at A"
```

## Prerequisites

Your gossiper needs to accept an option `-v` and output `Gossiper running` when it is up.
This allows the tests to wait for your gossiper to be initialized.

Then, you need is python 3 and behave.
https://behave.readthedocs.io/en/latest/install.html

### On ubuntu:
```shell script
sudo apt install python3-behave
```

### On mac:
```shell script
brew install pip # or `brew upgrade pip` if it is already installed
pip install behave
pip install pathlib
```

## Installing

Just clone this repository inside your Peerster project, **next to your gossiper main.go file**.
```shell script
cd your_project
git clone https://github.com/Zorvalt/peerster_tests.git
```

## Running the tests

```shell script
cd your_project/peerster_tests
behave
```

### Implemented scenarios by feature
* Client
  * Client sends a message to a simple node
  * Client sends a message to a node
* Concurrency
  * 26 nodes gossiping should not crash
* File search
  * Client should accept the keywords option alone
  * Client should accept the keywords and the budget options together
  * Gossiper should find file in direct neighbor with different keywords
  * Gossiper should NOT find file in direct neighbor with different keywords
  * Gossiper should NOT find file in indirect neighbor budget 2
  * Gossiper should find file in indirect neighbor budget 4
  * Gossiper should find file in indirect neighbor budget 7 even if direct has two matching files
  * Gossiper should NOT find file in indirect neighbor if direct has two matching files
  * Expanding ring should work FAR
  * Expanding ring should not work too FAR
  * A node should be able to download a file from an implicit direct source after a search
  * A node should be able to download a file from an implicit indirect source after a search
  * Chunks must have the right format
* File sharing
  * A node downloads a small file from a direct peer
  * A node downloads a big file from a direct peer
  * A node downloads a small file from an indirect peer
  * A node downloads a big file from an indirect peer
  * A node downloads a small file from an indirect peer separated by 8 other nodes
  * A node downloads a big file from an indirect peer separated by 8 other nodes
  * A node downloading a file should then share it
* Private messaging
  * A sends a message to neighbour B
  * A sends a message to C through B
  * A sends a message to D through B and C routed by route rumors
  * D sends a message to A through B and C routed by route rumors
  * A sends a message to C through B in weired config
  * A sends a message to L in a long way
  * A sends a message to M in a too long way
* Rumor
  * A rumor should propagate to a direct node

## Adding new tests
You can either use existing steps or implement new ones.
To do so, please read the [behave documentation](https://behave.readthedocs.io/en/latest/tutorial.html#features).

Directory explaination:
* features
  * The tests in Gherkin language
* peerster_objects
  * The interface to interact with the Peerster and client executables
* steps
  * The steps implementation
  
## Implemented steps
* Client related
  * `@when('a client sends "{sender}" a private message "{message}" to "{destination}"')`
  * `@when('a client sends "{name}" a message "{message}"')`
  * `@when('a client sends a random message of size {size} to each gossiper')`
  * `@when('a client asks "{name}" to search for "{keywords}" with budget {budget}')`
  * `@when('a client asks "{name}" to search for "{keywords}"')`
* File sharing related
  * `@given('a shared file "{filename}" of size {size}')`
  * `@when('a client asks "{node_name}" to share file "{filename}"')`
  * `@when('a client asks "{getter_node}" to download file "{filename}" from "{source_node}"')`
  * `@when('a client asks "{getter_node}" to download file "{filename}" from an implicit source')`
  * `@when("all downloaded files are removed from the directory")`
  * `@then('the node "{getter_node}" should have downloaded metafile of "{filename}" from "{source_node}"')`
  * `@then('the node "{getter_node}" should have downloaded chunks of "{filename}" from "{source_node}"')`
  * `@then('the node "{getter_node}" should have reconstructed the file "{filename}"')`
 * Gossiper related
  * `@given('a node "{name}" knowing "{number}" of "{first_neighbor}" to "{last_neighbor}"')`
  * `@given('a node "{name}" knowing "{neighbors}"')`
  * `@given('a node "{name}"')`
  * `@then('the node "{name}" should have logged "{message}"')`
  * `@then('the node "{name}" should not have logged "{message}"')`
  * `@then('the node "{name}" wait for "{message}" or max "{s}" seconds')`
  * `@then('wait for "{receiptient}" knowing "{sender}" or max "{s}" seconds')`
  * `@step('output the log of "{name}"')`
  * `@step('output the log of each running node')`
  * `@then('output the log of "{name}" to file "{file}"')`
  * `@then('all nodes should be running')`
* Gossiper in simple mode related
  * `@given('a simple node "{name}"')`
* Utils
  * `@given('wait for {n} seconds')`
  * `@when('wait for {n} seconds')`
## Authors

* **Sylvain Willy** - *Initial setup, several scenarios and steps* - [Zorvalt](https://github.com/Zorvalt)
* **Marc Gay-Balmaz** - *Several scenarios and steps* - [Foebus](https://github.com/Foebus)
* **Thomas Ibanez** - *Mac OS setup* - [ProtectedVariable](https://github.com/ProtectedVariable)

## License

This project is licensed under the GPLv3 License - see the [LICENSE.md](LICENSE.md) file for details