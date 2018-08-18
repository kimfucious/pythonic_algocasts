import unittest
from HtmlTestRunner import HTMLTestRunner
from tests.test_anagrams import AnagramsTests
from tests.test_bst import BinarySearchTreeTests
from tests.test_capitalize import CapitalizeTests
from tests.test_chunk import ChunkTests
from tests.test_fib import FibonacciTests
from tests.test_fib_memoize import FibonacciMemoizedTests
from tests.test_fizzbuzz import FizzBuzzTests
from tests.test_fromlast import FromLastTests
from tests.test_levelwidth import LevelWidthTests
from tests.test_linkedlist_refactored import LinkedListRefactoredTests
from tests.test_linkedlist import LinkedListTests
from tests.test_matrix import MatrixTests
from tests.test_maxchar import MaxCharTests
from tests.test_midpoint import MidpointTests
from tests.test_palindrome import PalindromeTests
from tests.test_pyramid import PyramidTests
from tests.test_pyramid_recursive import PyramidRecursiveTests
from tests.test_qfroms import QueueFromStackTests
from tests.test_queue import QueueTests
from tests.test_reverseint import ReverseIntegerTests
from tests.test_reversestring import ReverseStringTests
from tests.test_sorting import SortingTests
from tests.test_stack import StackTests
from tests.test_steps import StepsTests
from tests.test_steps_recursive import StepsRecursiveTests
from tests.test_tree import TreeNodeTests, TreeTests
from tests.test_validate import ValidateTests
from tests.test_vowels import VowelsTests
from tests.test_weave import WeaveStringTests


loader = unittest.TestLoader()
anagrams = loader.loadTestsFromTestCase(AnagramsTests)
bst = loader.loadTestsFromTestCase(BinarySearchTreeTests)
capitalize = loader.loadTestsFromTestCase(CapitalizeTests)
chunk = loader.loadTestsFromTestCase(ChunkTests)
fib = loader.loadTestsFromTestCase(FibonacciTests)
fib_memoize = loader.loadTestsFromTestCase(FibonacciMemoizedTests)
fizzbuzz = loader.loadTestsFromTestCase(FizzBuzzTests)
fromlast = loader.loadTestsFromTestCase(FromLastTests)
levelwidth = loader.loadTestsFromTestCase(LevelWidthTests)
linkedlist_refactored = loader.loadTestsFromTestCase(LinkedListRefactoredTests)
linkedlist = loader.loadTestsFromTestCase(LinkedListTests)
matrix = loader.loadTestsFromTestCase(MatrixTests)
maxchar = loader.loadTestsFromTestCase(MaxCharTests)
midpoint = loader.loadTestsFromTestCase(MidpointTests)
palindrome = loader.loadTestsFromTestCase(PalindromeTests)
pyramid = loader.loadTestsFromTestCase(PyramidTests)
pyramid_recursive = loader.loadTestsFromTestCase(PyramidRecursiveTests)
qfroms = loader.loadTestsFromTestCase(QueueFromStackTests)
reverseint = loader.loadTestsFromTestCase(ReverseIntegerTests)
reversestring = loader.loadTestsFromTestCase(ReverseStringTests)
sorting = loader.loadTestsFromTestCase(SortingTests)
stack = loader.loadTestsFromTestCase(StackTests)
steps = loader.loadTestsFromTestCase(StepsTests)
steps_recursive = loader.loadTestsFromTestCase(StepsRecursiveTests)
tree = loader.loadTestsFromTestCase(TreeTests)
tree_node = loader.loadTestsFromTestCase(TreeNodeTests)
validate = loader.loadTestsFromTestCase(ValidateTests)
vowels = loader.loadTestsFromTestCase(VowelsTests)
weave = loader.loadTestsFromTestCase(WeaveStringTests)

suite = unittest.TestSuite([
    anagrams,
    bst,
    capitalize,
    chunk,
    fib,
    fib_memoize,
    fizzbuzz,
    fromlast,
    levelwidth,
    linkedlist_refactored,
    linkedlist,
    matrix,
    maxchar,
    midpoint,
    palindrome,
    pyramid,
    pyramid_recursive,
    qfroms,
    reverseint,
    reversestring,
    sorting,
    stack,
    steps,
    steps_recursive,
    tree,
    tree_node,
    validate,
    vowels,
    weave])

kwargs = {
    # "output": "",
    "combine_reports": True,
    "report_name": "test_results",
    "report_title": "Pythonic Algorithms Test Results",
    "add_timestamp": False,
    "verbosity": 0
}

runner = HTMLTestRunner(**kwargs)
runner.run(suite)
