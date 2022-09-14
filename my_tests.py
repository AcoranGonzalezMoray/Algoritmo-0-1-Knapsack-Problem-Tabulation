import unittest

from ks_utils    import *
from solve       import *

class TestKSP(unittest.TestCase):
    def test_from_data_to_item(self):
        content = """3 10
                    45 5
                    48 8
                    35 3
                    """
        items, capacity = from_data_to_items(content)
        self.assertEqual(10, capacity)
        self.assertEqual([Item(1, 45, 5), Item(2, 48, 8), Item(3, 35, 3)], items)
        return
    
    def test_1(self):
        content = """1 10
                     3 4
                    """
        items, capacity = from_data_to_items(content)
        value, taken = solve_memoization(items, capacity)

        #self.assertEqual(value, 3)
        #self.assertEquals(taken, [1])
        return
