import unittest
from LinkedList import LinkedList
from k_to_last_2_2 import k_to_last

class Test(unittest.TestCase):

  def test_remove_duplicates(self):
    l = LinkedList([1, 2, 3])
    actual = k_to_last(l, 1)
    self.assertEqual(actual.value, 3)

    l = LinkedList()
    actual = k_to_last(l, 0)
    self.assertEqual(actual, None)

    l = LinkedList([1, 2, 3, 4, 5])
    actual = k_to_last(l, 2)
    self.assertEqual(actual.value, 4)

    l = LinkedList([1, 2, 3, 4, 5])
    actual = k_to_last(l, 6)
    self.assertEqual(actual, None)

if __name__ == "__main__":
    unittest.main()
