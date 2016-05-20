# Identical char count.

def permutation(text1, text2):
  """
  Returns true if both texts are anagram of each other, else false.
  """
  # Assumptions: Text contains only ascii chars.
  if len(text1) != len(text2):
    return False

  char_count = [0 for _ in range(256)]
  for char in text1:
    char_num = ord(char)
    char_count[char_num] += 1

  for char in text2:
    char_num = ord(char)
    char_count[char_num] -= 1
    if char_count[char_num] < 0:
      return False

  return True
