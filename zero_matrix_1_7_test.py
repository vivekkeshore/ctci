import unittest
from zero_matrix_1_7 import zero_matrix

class Test(unittest.TestCase):
  data = [
      ([
          [1, 2, 3, 4, 0],
          [6, 0, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 0, 18, 19, 20],
          [21, 22, 23, 24, 25]
      ], [
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [11, 0, 13, 14, 0],
          [0, 0, 0, 0, 0],
          [21, 0, 23, 24, 0]
      ]),
    ([
          [1, 2],
          [3, 4],
          [0, 5]
      ], [
          [0, 2],
          [0, 4],
          [0, 0]
      ])
  ]

  def test_zero_matrix(self):
    for test_matrix, expected in self.data:
      self.assertEqual(zero_matrix(test_matrix), expected)

if __name__ == "__main__":
    unittest.main()