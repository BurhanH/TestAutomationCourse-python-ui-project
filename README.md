# TestAutomationCourse-python-ui-project

Python UI project for Test Automation Course

[![Run Python Tests](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/actions/workflows/run_tests.yml/badge.svg?branch=main)](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/actions/workflows/run_tests.yml)

[![code standard check by pylint](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/actions/workflows/code-standard-checker.yml/badge.svg)](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/actions/workflows/code-standard-checker.yml)

## How to run tests from one file - pytest

In terminal execute:
```
pytest -v tests/your_test_file.py
```

## How to run tests by category (markers) - pytest

### Run only tests with marker smoke
```
pytest -m smoke -v
```
### Run only tests with marker regression
```
pytest -m regression -v
```
### How to use markers for pytest
For the reference see files [test_dummy.py](tests/test_dummy.py) and [pytest.ini](pytest.ini).
Basically, you need to add a new marker with a description into the pytest.ini file or use an existing one and use it in your test suite, see samples in test_dummy.py.
You can apply many markers for each test as you can depend on your needs.

## How to run tests from one file - unittest
```
python -m unittest -v tests/your_test_file.py
```

## How to run specific test (or test method) from test class - unittest
```
python tests/your_test_file.py YourClass.test_method -v
```

## How to run all tests - unittest
```
python -m unittest discover tests "*.py" -v
```

## How run pylint static code analyser
```
pylint tests/your_test_file.py 
```
[pylint](https://pylint.pycqa.org/) will analyse your code, check errors, enforces a coding standard, and
probably will make suggestions about how the code could be refactored.

## How to make a PR with your changes into this repository

- Fork repository in GitHub
- From forked repository make a copy to your local machine
- Create a new branch (use descriptive name)
- Make changes (add tests)
- Commit changes into the branch
- Push changes into forked repository
- Make a PR from your forked repository into this repo
- Add reviewers 
- And send a message in our channel with a link to your PR
- Note! If there are failures, please review logs and failed tests, and fix them!

## How can I contribute to this repository

- There are 2 or more ways to do it
  - Add more UI tests
  - Add test cases as a documentation
  - Improve current repository via adding a new functionality or posting any issues or ideas/improvements on [issues tab](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/issues)
