API Automation with Python (TDD approach)

## logger

logging

## What is a Linter in Python?

A linter is a tool that checks your source code for programming errors, bugs, stylistic errors, and suspicious constructs. In Python, there are various linter tools available that help ensure code quality and conformity to a particular style guide.

In the Python universe, some of the most popular linters include Pylint, Flake8, and PyCodeStyle. Each of these linters has its strengths and features that cater to different needs and preferences.

What Are the Benefits of Using a Python Linter?
There are several benefits to using a Python linter:

> **Code Consistency:** Linters enforce a consistent coding style, making it easier for others (and future you) to read and understand your code.

> **Early Error Detection:** They catch potential errors and bugs before runtime, saving you from hours of debugging later.

> **Code Quality:** Linters help ensure that your code is of high quality, adhering to the best practices of the Python community.

> **Learning Tool:** Especially for beginners, linters can serve as a great learning tool, helping them understand and follow Python's coding conventions.

* pylint

**installation**

```shell
  pip install pylint
```
generate rcfile
```shell
  pylint --generate-rcfile > .pylintrc
```
ignore a specific line of code
```python
# pylint: disable=abstract-class-instantiated
```
ignore in rcfile (example)
```editorconfig
  [MESSAGES CONTROL]
  disable=
    wildcard-import,
    method-hidden,
    too-many-lines
```

* flake8

**installation**
```shell
  pip install flake8
```

* pre-commit

**installation**

```shell
  pip install pre-commit
```

**Install the git hook scripts**
```shell
  pre-comit install
```

**Run against all the files**
```shell
  pre-comit run --all-files
```
**Run against specific file**
```shell
  pre-commit run --files utils/logger.py
```

**Skip git commit hook**
```shell
  git commit --no-verify -m "commit message"
```

## Libraries

* Robot
* PyTest
* Unittest
* DocTest
* Nose2
* Testify

## Unittest
Unit Test Framework features:

- **test fixture**. A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
- **test case**. A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
- **test suite**. A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
- **test runner**. A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.

**Example**
```python
import unittest


class TestProject(unittest.TestCase):

    # fixture
    def setUp(self):
        print("Setup")

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")

    def test_three(self):
        print("test three")

    # fixture
    def tearDown(self):
        print("tearDown")
```
## Nose2

Nose2 is a popular Python test runner that can detect and execute unit tests in your project

Nose2 Python is based on unit tests and extends the framework's functionality with a vast plugin ecosystem. In simple terms, Nose2 is a unit test module extension

**installation**

```shell
  pip install nose2
```

## Pytest

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

**Installation**

```shell
  pip install pytest
```

Advantages of pytest

* Pytest can run multiple tests in parallel, which reduces the execution time of the test suite.
* Pytest has its own way to detect the test file and test functions automatically, if not mentioned explicitly.
* Pytest allows us to skip a subset of the tests during execution.
* Pytest allows us to run a subset of the entire test suite.
* Pytest is free and open source.
* Because of its simple syntax, pytest is very easy to start with.

## Anatomy of an automated test

In the simplest terms, a test is meant to look at the result of a particular behavior, and make sure that result aligns with what you would expect. Behavior is not something that can be empirically measured, which is why writing tests can be challenging.
“Behavior” is the way in which some system acts in response to a particular situation and/or stimuli. But exactly how or why something is done is not quite as important as what was done.

You can think of a test as being broken down into four steps:

* **Arrange**. is where we prepare everything for our test. This means pretty much everything except for the “act”. It’s lining up the dominoes so that the act can do its thing in one, state-changing step. This can mean preparing objects, starting/killing services, entering records into a database, or even things like defining a URL to query, generating some credentials for a user that doesn’t exist yet, or just waiting for some process to finish.
* **Act**. is the singular, state-changing action that kicks off the behavior we want to test. This behavior is what carries out the changing of the state of the system under test (SUT), and it’s the resulting changed state that we can look at to make a judgement about the behavior. This typically takes the form of a function/method call.
* **Assert**. is where we look at that resulting state and check if it looks how we’d expect after the dust has settled. It’s where we gather evidence to say the behavior does or does not aligns with what we expect. The assert in our test is where we take that measurement/observation and apply our judgement to it. If something should be green, we’d say assert thing == "green".
* **Cleanup**. is where the test picks up after itself, so other tests aren’t being accidentally influenced by it.

At its core, the test is ultimately the act and assert steps, with the arrange step only providing the context. Behavior exists between act and assert.

**Fixtures**

“Fixtures”, in the literal sense, are each of the arrange steps and data. They’re everything that test needs to do its thing.


## References

> pylint vs flake8: https://www.saashub.com/compare-pylint-vs-flake8, https://www.slant.co/versus/12630/12632/~pylint_vs_flake8

> unittests: https://docs.python.org/3/library/unittest.html

> nose2: https://docs.nose2.io/en/latest/

> pytest: https://docs.pytest.org/en/8.0.x/

> pre-comit https://pre-commit.com/
