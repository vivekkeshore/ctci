import unittest
from string_compression_1_5 import compress_text

class Test(unittest.TestCase):
  TEST_DATA = [
    ('abcdef', 'abcdef'),
    ('abcdeff', 'abcdeff'),
    ('abcdeffffffff', 'a1b1c1d1e1f8'),
    ('aabcccccaaa', 'a2b1c5a3'),
    ('aabcccccaaaaa', 'a2b1c5a5'),
    ('aaaaaabbb', 'a6b3'),
    ('aaaaaa', 'a6'),
    ('', ''),
    ('a', 'a'),
    ('aa', 'aa')
  ]

  def test_is_unique(self):
    for text, expected_result in self.TEST_DATA:
      self.assertEqual(compress_text(text), expected_result)

if __name__ == "__main__":
    unittest.main()
