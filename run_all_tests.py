import unittest
import HtmlTestRunner
from tests.test_anagrams import AnagramsTests
from tests.test_bst import BinarySearchTreeTests
from tests.test_capitalize import CapitalizeTests


loader = unittest.TestLoader()
anagrams = loader.loadTestsFromTestCase(AnagramsTests)
bst = loader.loadTestsFromTestCase(BinarySearchTreeTests)
capitalize = loader.loadTestsFromTestCase(CapitalizeTests)

suite = unittest.TestSuite([anagrams, bst, capitalize])

# kwargs = {
#     "output": "",
#     "combine_reports": True,
#     "report_name": "Test Results",
# }

runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True)
runner.run(suite)
