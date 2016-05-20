# Remove duplicates from an unsorted linked list.
# By using hash map - O(n)
# Without using hashmap, using two pointers - O(n^2)

from LinkedList import LinkedList


def remove_duplicates(link_list):
  """
  Removes the repeating element from the linked list and returns it.
  O(n)
  """
  items = {}
  prev = None
  for node in link_list:
    try:
      items[node.value]
      prev.next = node.next

    except KeyError:
      items[node.value] = node.value
      prev = node

  return link_list

def remove_duplicats_2(link_list):
  """
  Removes duplicate elements from linked list without using extra memory.
  O(n^2)
  """
  for node in link_list:
    current = node.next
    prev = node
    while current:
      if current.value == node.value:
        prev.next = current.next
      else:
        prev = current

      current = current.next

  return link_list
