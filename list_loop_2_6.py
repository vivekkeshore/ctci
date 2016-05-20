# A circular linked list, implement an algorithm which returns the node at the
# beginning of the loop.

def find_loop_node(link_list):
  """
  Returns the node where the loop starts in a link list.
  """
  try:
    tortoise = link_list.head
    hare = link_list.head.next
    while tortoise != hare:
      tortoise = tortoise.next
      hare = hare.next.next
  except AttributeError:
    return None

  tortoise = link_list.head
  while tortoise != hare.next:
    tortoise = tortoise.next
    hare = hare.next

  return tortoise
