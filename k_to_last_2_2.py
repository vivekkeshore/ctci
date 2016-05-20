# Implement an algorithm to find the kth to last element of a singly linked list.

def k_to_last(link_list, k):
  """
  Returns the kth node from the last of the link_list.
  """
  if k > len(link_list):
    return
  runner = current = link_list.head
  for _ in range(k):
      runner = runner.next

  while runner:
    current = current.next
    runner = runner.next

  return current
