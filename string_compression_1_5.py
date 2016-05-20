# String Compression

def compress_text(text):
  """
  Returns the compressed string, if length of compressed string is smaller
  than original string length, else returns original string.
  """

  compressed = ''
  count = 1
  for i in range(len(text)):
    try:
      if text[i] == text[i+1]:
        count += 1
      else:
        compressed += text[i] + str(count)
        count = 1
    except IndexError:
      compressed += text[-1] + str(count)

  return min(text, compressed, key=len)
