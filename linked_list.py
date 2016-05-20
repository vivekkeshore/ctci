# Implementing a singly linked list.

class Node(object):

  def __init__(self, data=None):
    self.data = data
    self.next_node = None

  def get_data(self):
    return self.data

  def set_data(self, data):
    self.data = data

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next


class UnorderedList(object):
  def __init__(self, head=None):
    self.head = head

  def isEmpty(self):
    return self.head is None

  def add_node(self, data):
    node = Node(data)
    node.next_node = self.head
    self.head = node

  def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()

    return count

  def search(self, data):
    current = self.head
    while current:
      if current.data == data:
        return current
      current = current.get_next()

    return None

  def remove(self, data):
    if self.isEmpty():
      return

    previous = None
    current = self.head
    found = False
    while not found:
      if current.data == data:
        found = True

    if previous is None:
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next)

  def show_items(self):
    if self.head is None:
      print 'Linked List is empty'

    current = self.head
    while current:
      print current.get_data()
      current = current.get_next()
