# Matrix rotation

# [1, 2, 3, 4, 5],
# [6, 7, 8, 9, 10],
# [11, 12, 13, 14, 15],
# [16, 17, 18, 19, 20],
# [21, 22, 23, 24, 25]
#
# [21, 16, 11, 6, 1],
# [22, 17, 12, 7, 2],
# [23, 18, 13, 8, 3],
# [24, 19, 14, 9, 4],
# [25, 20, 15, 10, 5]

def rotate_matrix(matrix):
  """
  Rotates the edges of matrix by 90 degree.
  """
  rows = len(matrix)
  cols = len(matrix[0])

