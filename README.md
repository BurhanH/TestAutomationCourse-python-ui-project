# TestAutomationCourse-python-ui-project

Python UI project for Test Automation Course

[![Run Python Tests](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/actions/workflows/run_tests.yml/badge.svg)](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/actions/workflows/run_tests.yml)

## How to run tests from one file

In terminal execute:

```
python -m unittest -v tests/your_test_file.py
```

## How to run specific test (or test method) from test class

```
python tests/your_test_file.py YourClass.test_method -v
```

## How to run all tests
```
python -m unittest discover tests "*.py" -v
```

## How to make a PR with your changes into this repository

- Fork repository in GitHub
- From forked repository make a copy to your local machine
- Create a new branch (use descriptive name)
- Make changes (add tests)
- Commit changes into the branch
- Push changes into forked repsitory
- Make a PR from your forked repository into this repo
- Add reviwers 
- And send a message in our channel with a link to your PR
- Note! If there are failures, please review logs and failed tests, and fix them!

## How can I contrubute to this repository

- There are 2 or more ways to do it
  - Add more UI tests
  - Add test cases as a documentation
  - Improve current repository via adding a new functionality or posting any issues or ideas/improvements on [issues tab](https://github.com/BurhanH/TestAutomationCourse-python-ui-project/issues)
