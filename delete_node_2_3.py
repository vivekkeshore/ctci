# Implement an algorithm to delete a node in the middle of a singly linked list,
# given only access to that node.

def delete_node(node):
  """
  Deletes the given node in a linked list without access to head.
  """
  node.value = node.next.value
  node.next = node.next.next
