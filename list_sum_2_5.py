# two numbers represented by a linked list, where each node contains a
# single digit. The digits are stored in reverse order, such that the 1 's digit is at the head
# of the list. Write a function that adds the two numbers and returns the sum as a
# linked list.
from LinkedList import LinkedList

def sum_list(l1, l2):
  """
  returns a list which contains the addition of input two lists.
  """
  lsum = LinkedList()
  carry = 0
  l1_node = l1.head
  l2_node = l2.head

  while l1_node or l2_node:
    val = carry
    if l1_node:
      val += l1_node.value
      l1_node = l1_node.next

    if l2_node:
      val += l2_node.value
      l2_node = l2_node.next

    lsum.add(val % 10)
    carry = val / 10
  if carry:
    lsum.add(carry)

  return lsum
