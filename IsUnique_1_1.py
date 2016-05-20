# O(n)
__author__ = 'vkishore'

def is_unique(text):
  """
  Returns True if all chars are unique, else returns False.
  """
  # Assuming that text contains only ASCII chars.
  if len(text) > 256:
    return False

  else:
    all_unique = [False for _ in range(256)]
    for char in text:
      char_num = ord(char)
      if all_unique[char_num]:
        return False

      all_unique[char_num] = True

    return True