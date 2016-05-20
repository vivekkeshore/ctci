import unittest
from LinkedList import LinkedList
from list_sum_2_5 import sum_list

class Test(unittest.TestCase):

  def test_sum_list(self):
    actual = sum_list(LinkedList([1, 2, 3, 4, 5]), LinkedList([1, 2, 3, 4, 5]))
    actual = [node.value for node in actual]
    expected = [2, 4, 6, 8, 0, 1]
    self.assertEqual(actual, expected)

    actual = sum_list(LinkedList([1, 2, 3, 4, 5]), LinkedList())
    actual = [node.value for node in actual]
    expected = [1, 2, 3, 4, 5]
    self.assertEqual(actual, expected)

    actual = sum_list(LinkedList([1, 2, 3, 4, 5]), LinkedList([1]))
    actual = [node.value for node in actual]
    expected = [2, 2, 3, 4, 5]
    self.assertEqual(actual, expected)

    actual = sum_list(LinkedList([5]), LinkedList([5]))
    actual = [node.value for node in actual]
    expected = [0, 1]
    self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
