import unittest
from HtmlTestRunner import HTMLTestRunner
from tests.test_anagrams import AnagramsTests
from tests.test_bst import BinarySearchTreeTests
from tests.test_capitalize import CapitalizeTests
from tests.test_chunk import ChunkTests
from tests.test_circular import CircularTests
from tests.test_fib import FibonacciTests
from tests.test_fib_memoize import FibonacciMemoizedTests
from tests.test_fizzbuzz import FizzBuzzTests
from tests.test_fromlast import FromLastTests
from tests.test_levelwidth import LevelWidthTests
from tests.test_linkedlist import LinkedListTests, ClearTests, ForEachTests, ForInTests, GetAtTests, GetFirstTests, GetLastTests, InsertAtTests, InsertFirstTests, RemoveFirstTests, RemoveLastTests, InsertLastTests, RemoveAtTests, SizeTests
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
circular = loader.loadTestsFromTestCase(CircularTests)
chunk = loader.loadTestsFromTestCase(ChunkTests)
fib = loader.loadTestsFromTestCase(FibonacciTests)
fib_memoize = loader.loadTestsFromTestCase(FibonacciMemoizedTests)
fizzbuzz = loader.loadTestsFromTestCase(FizzBuzzTests)
fromlast = loader.loadTestsFromTestCase(FromLastTests)
levelwidth = loader.loadTestsFromTestCase(LevelWidthTests)
linkedlist = loader.loadTestsFromTestCase(LinkedListTests)
linkedlist_clear = loader.loadTestsFromTestCase(ClearTests)
linkedlist_for_each = loader.loadTestsFromTestCase(ForEachTests)
linkedlist_for_in = loader.loadTestsFromTestCase(ForInTests)
linkedlist_get_at = loader.loadTestsFromTestCase(GetAtTests)
linkedlist_get_first = loader.loadTestsFromTestCase(GetFirstTests)
linkedlist_get_last = loader.loadTestsFromTestCase(GetLastTests)
linkedlist_insert_at = loader.loadTestsFromTestCase(InsertAtTests)
linkedlist_insert_first = loader.loadTestsFromTestCase(InsertFirstTests)
linkedlist_insert_last = loader.loadTestsFromTestCase(InsertLastTests)
linkedlist_remove_first = loader.loadTestsFromTestCase(RemoveFirstTests)
linkedlist_remove_last = loader.loadTestsFromTestCase(RemoveLastTests)
linkedlist_remove_at = loader.loadTestsFromTestCase(RemoveAtTests)
linkedlist_size = loader.loadTestsFromTestCase(SizeTests)
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
    circular,
    fib,
    fib_memoize,
    fizzbuzz,
    fromlast,
    levelwidth,
    linkedlist,
    linkedlist_clear,
    linkedlist_for_each,
    linkedlist_for_in,
    linkedlist_get_at,
    linkedlist_get_first,
    linkedlist_get_last,
    linkedlist_insert_at,
    linkedlist_insert_first,
    linkedlist_insert_last,
    linkedlist_remove_at,
    linkedlist_remove_first,
    linkedlist_remove_last,
    linkedlist_size,
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
