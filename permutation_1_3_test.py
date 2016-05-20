import unittest
from permutation_1_3 import permutation

class Test(unittest.TestCase):
  TEST_DATA = [
    (['vivek', 'keviv'], True),
    (['a', 'aa '], False),
    (['a', ''], False),
    (['', 'a'], False),
    (['vivek', 'vivek '], False)
  ]

  def test_is_unique(self):
    for texts, expected_result in self.TEST_DATA:
      self.assertEqual(permutation(texts[0], texts[1]), expected_result)

if __name__ == "__main__":
    unittest.main()