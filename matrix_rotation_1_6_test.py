import unittest
from matrix_rotation_1_6 import rotate_matrix

class Test(unittest.TestCase):
  data = [
      ([
          [1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]
      ], [
          [21, 16, 11, 6, 1],
          [22, 17, 12, 7, 2],
          [23, 18, 13, 8, 3],
          [24, 19, 14, 9, 4],
          [25, 20, 15, 10, 5]
      ])
  ]

  def test_rotate_matrix(self):
    for test_matrix, expected in self.data:
      self.assertEqual(rotate_matrix(test_matrix), expected)

if __name__ == "__main__":
    unittest.main()