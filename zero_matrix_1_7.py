# if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zero_matrix(matrix):
  """
  Returns a matrix having entire row or column as zero if it had zero element.
  """
  rows = [False] * len(matrix)
  cols = [False] * len(matrix[0])
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if matrix[row][col] == 0:
        rows[row] = True
        cols[col] = True

  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if rows[row] or cols[col]:
        matrix[row][col] = 0

  return matrix
