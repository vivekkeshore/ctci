import unittest
from IsUnique_1_1 import is_unique

class Test(unittest.TestCase):
  TEST_DATA = [
    ('a', True),
    ('aa', False),
    ('ab', True),
    ('ab ', True),
    ('', True),
    (' ', True),
    ('  ', False),
    ('qwerty', True),
    ('qwerte', False)
  ]

  def test_is_unique(self):
    for text, expected_result in self.TEST_DATA:
      self.assertEqual(is_unique(text), expected_result)

if __name__ == "__main__":
    unittest.main()
