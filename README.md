# Pythonified Coding Interview Bootcamp Exercises

This repo contains Pythonic versions of exercises based on **Stephen Grider's** [_The Coding Interview Bootcamp: Algorithms + Datastructures_](https://www.udemy.com/coding-interview-bootcamp-algorithms-and-data-structure/?couponCode=4MORE1234) found on Udemy.

This repo is not intended to be a rip off of Stephen's work or a replacement for his very informative course targeted at JavaScript. Consider it more of a Pythonic ode.

This repo is also not a substitute for the ton of material he covers throughout the course lectures. So go buy it, if you really want a good start toward learning these the concepts behind these exercises (in JavaScript).

## Features

- Oodles of exercises to practice challenging coding questions
- Extensive unit tests to verify your solutions

## Requirements

- Python 3: some tests won't work if you use Python 2
- An testing framework: nose, pytest, or unnitest
- A text editor: Atom, Sublime Text, Vim, Visual Studio Code, etc.
- A terminal

> :point_up: If you're running Windows 10 try [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

## Repo Contents

> :point_up: Do not remove any of the `__init__.py` files from within the repo, or it will break test discovery.

### Completed

Examples of completed exercises that you can use to compare against your own work or to peek at when you're stuck

### Exercises

Starter files for each exercise with instructions that describe what the solution should be.

While you can, for the most part, approach these exercises in any order. The course does tend to build upon itself, so you may want to follow the order in which the lectures are covered in Stephen's course

#### Order of exercises

1. String Reversal (reversestring)
2. Palindromes
3. Integer Reversal (reverseint)
4. MaxChars
5. FizzBuzz
6. Array Chunking (chunk)
7. Anagrams
8. Sentance Capitalization (capitalize)
9. Printing Steps (steps)
10. Two Sided Steps (pyramid)
11. Vowels
12. Matrix Spiral (matrix)
13. Fibonacci (fib and fib_memoized)
14. Queue
15. Weave
16. Stack
17. Queue From Stack (qfroms)
18. Linked Lists (linkedlist)
19. Midpoint
20. Circular
21. From Last (from last)
22. Tree
23. Level Width (levelwidth)
24. Binary Search Tree (bst)
25. Validating Binary Search Trees (validate)
26. Events
27. Bubble Sort, Selection Sort, and Merge Sort (sorting)

### Helpers

Some of the exercies rely on pre-built components (probably not the right word), like: classes, linked lists, queues, and stacks. You'll build such things as you work through the excercises; however, these helpers are in place for exercises with a different, specific focus.

### Misc

There are two html files in here:

1.  The `events_example.html` file is for the events exercise. Frankly, you won't get much out of this, unless you have access to Stephen's course.
2.  The `linkedlist_directions.html` file is a set of instructions for the fairly long linked list exercise.

### Tests

There is one test file for each exercise. The naming convention should make it evident as to what tests what.

All of the test files should be considered done, meaning that you should not need to edit any of them. They should _just work_ are just there to test the solutions that you create for the exercises.

> :bug: If you find any mistakes in the tests or have any recomendations to improve them, please raise an issue.

Some of the test files contain one or more test cases (i.e. Classes) and these can contain one to several test methods. See the Testing section for more info on tests.

## Testing

Note that the `__init__py` files that you see in the directory structure (and the directory structure itself) are there to enable test discovery. Don't move things around or delete any `__init__.py` files, unless you know that you really want to.

### Test Frameworks

At the risk of sounding redundant, all tests have been tested using both `unittest` and `pytest`.

While `unittest` is built in to Python, pytest requires installation.

Here's some documentation:

- [pytest installation](https://docs.pytest.org/en/latest/getting-started.html)
- [Official Python Documentation on unittest](https://docs.python.org/3/library/unittest.html)

### Test Discovery

To discover all tests, if you're using `unittest`, you can run discovery by doing the following:

1.  Navigate to the root directory of this repo in your terminal
2.  Run `python3 -m unittest discover`

As far as I know, `pytest` doesn't have a discovery option, nor is it needed. And, along those lines, `python3 -m unittest` will also discover tests, so take that for what it is.

### Running Tests

To run all unit tests:

1.  Navigate to the root directory of this repo in your terminal
2.  Do one of the below:

> :point_up: Remember that we're using Python 3. Don't forget to type `python`, and don't forget the `-m` bit.

#### pytest

```shell
python3 -m pytest
```

#### unittest

```shell
python3 -m unittest
```

To run an individual unit test:

#### pytest

1.  Navigate to `tests` directory
2.  Run `python3 -m pytest test_excercise.py`, where exercise is the name of the thing you're trying to test. For example, test_anagrams.py

#### unittest

Apparently, you can't run a single unit test using unittest, without knowing the Class name of the test case. With that in mind, you might decide to either use `pytest` or simply run all tests. The ability to skip tests, makes running all tests, not that bad of a thing. See below for more on that.

### Skipping and Un-skipping Tests

You'll have noticed that all of the tests are skipped when you first try to run them. This is so that you don't see a crap load of failures and/or errors on exercises that you haven't event attempted to work on yet.

The following line (i.e. decorator) in a test file will skip an entire test case (multiple methods) or single test cases depending on where it's located.

```python
@unittest.skip("skip the following stuff")
```

In most of the test files, there is one skip decorator located just above the Class defining the test case. In other, more lengthy test files, like Linked List, there might be more cases and, thus, more skip decorators, allowing you to open up the test cases slowly as you progress through the exercises.

To allow a test case to run, simply comment out the decorator, like this (or delete it if you're feeling bold):

```python
# @unittest.skip("skip the following stuff")
```
