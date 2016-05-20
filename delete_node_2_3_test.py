import unittest
from LinkedList import LinkedList
from delete_node_2_3 import delete_node

class Test(unittest.TestCase):

  def test_delete_nodes(self):
    l = LinkedList([1, 2, 3])
    print l
    delete_node(l.head.next)
    print l
    actual = [node.value for node in l]
    expected = [1, 3]
    self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
