# Partition a linked list around a value x, such that all nodes less than x
# come before all nodes greater than or equal to x.


def partition_list(link_list, x):
  """
  Partition a linked list around a value x, such that all nodes less than
  come before alt nodes greater than or equal to x.
  """

  current = link_list.tail = link_list.head

  while current:
    nextNode = current.next
    current.next = None
    if current.value < x:
      current.next = link_list.head
      link_list.head = current
    else:
      link_list.tail.next = current
      link_list.tail = current
    current = nextNode
