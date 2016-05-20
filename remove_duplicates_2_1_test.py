import unittest
from LinkedList import LinkedList
from remove_duplicates_2_1 import remove_duplicates, remove_duplicats_2

class Test(unittest.TestCase):

  def test_remove_duplicates(self):
    l = LinkedList([1, 2, 3])
    actual = remove_duplicates(l)
    actual = [node.value for node in actual]
    expected = [1, 2, 3]
    self.assertEqual(actual, expected)

    l = LinkedList()
    actual = remove_duplicates(l)
    actual = [node.value for node in actual]
    expected = []
    self.assertEqual(actual, expected)

    l = LinkedList([1, 1, 1])
    actual = remove_duplicates(l)
    actual = [node.value for node in actual]
    expected = [1]
    self.assertEqual(actual, expected)

    l = LinkedList([1, 1, 2])
    actual = remove_duplicates(l)
    actual = [node.value for node in actual]
    expected = [1, 2]
    self.assertEqual(actual, expected)

    l = LinkedList([1, 2, 1])
    actual = remove_duplicates(l)
    actual = [node.value for node in actual]
    expected = [1, 2]
    self.assertEqual(actual, expected)

    l = LinkedList([1])
    actual = remove_duplicates(l)
    actual = [node.value for node in actual]
    expected = [1]
    self.assertEqual(actual, expected)

  def test_remove_duplicats_2(self):
    l = LinkedList([1, 2, 3])
    actual = remove_duplicats_2(l)
    actual = [node.value for node in actual]
    expected = [1, 2, 3]
    self.assertEqual(actual, expected)

    l = LinkedList()
    actual = remove_duplicats_2(l)
    actual = [node.value for node in actual]
    expected = []
    self.assertEqual(actual, expected)

    l = LinkedList([1, 1, 1])
    actual = remove_duplicats_2(l)
    actual = [node.value for node in actual]
    expected = [1]
    self.assertEqual(actual, expected)

    l = LinkedList([1])
    actual = remove_duplicats_2(l)
    actual = [node.value for node in actual]
    expected = [1]
    self.assertEqual(actual, expected)

    l = LinkedList([1, 1, 2])
    actual = remove_duplicats_2(l)
    actual = [node.value for node in actual]
    expected = [1, 2]
    self.assertEqual(actual, expected)

    l = LinkedList([1, 2, 1])
    actual = remove_duplicats_2(l)
    actual = [node.value for node in actual]
    expected = [1, 2]
    self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
