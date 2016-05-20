class BinaryTree:
  def __init__(self, root):
    self.root = root
    self.left_child = None
    self.right_child = None

  def insert_left(self, new_node):
    if self.left_child is None:
      self.left_child = BinaryTree(new_node)

    else:
      t = BinaryTree(new_node)
      t.left_child = self.left_child
      self.left_child = t

  def insert_right(self, new_node):
    if self.right_child is None:
      self.right_child = BinaryTree(new_node)

    else:
      t = BinaryTree(new_node)
      t.right_child = self.right_child
      self.right_child = t

  def get_right_child(self):
    return self.right_child

  def get_left_child(self):
    return self.left_child

  def set_root(self, obj):
    self.key = obj

  def get_root(self):
    return self.key


def preorder(tree):
  if tree:
    print(tree.get_root())
    preorder(tree.get_left_child())
    preorder(tree.get_right_child())

def postorder(tree):
  if tree:
    preorder(tree.get_left_child())
    preorder(tree.get_right_child())
    print(tree.get_root())

def inorder(tree):
  if tree:
    preorder(tree.get_left_child())
    print(tree.get_root())
    preorder(tree.get_right_child())
