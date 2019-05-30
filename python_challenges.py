class Linked_List:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.down = None

  def get_next(self):
    return self.next

  def set_next(self, node):
    self.next = node

  def has_next(self):
    if self.next != None:
      return True
    else:
      return False

  def get_down(self):
    return self.down

  def set_down(self, node):
    self.down = node

  def has_down(self):
    if self.down != None:
      return True
    else:
      return False

node_values = [1,2,3,4,5,6,7,8,9,10]
node_list = []

for val in node_values:
  node_list.append(Linked_List(val))


def flatten(node):
  current = node
  end_node = node
  while current != None:
    if current.has_down():
      last_down = flatten(current.down)
      last_down.set_next(current.get_next())
      current.set_next(current.get_down())
      current.set_down(None)
    end_node = current
    current = current.next
  return end_node


def circle_of_kids(n, m):
    last_kid = 0
    count = 0
    start = 0
    kids = []
    for i in range(1, n + 1):
        kids.append(i)

    while count <= m and len(kids) > 1:
        count += 1
        if count == m:
            if count <= len(kids):
                kids.remove(kids[count - 1])
                start = count - 1
            else:
                start = m - (len(kids) + 1)
                kids.remove(kids[start])
            if start < len(kids):
                last_kid = kids[start]
                kids = kids[start:] + kids[:start]
            count = 0

    return last_kid

class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

head = Node(1)

class DoubleNode:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, value):
    if self.head is None:
      self.head = DoubleNode(value)
      self.tail = self.head
      return
    else:
      self.tail.next = DoubleNode(value)
      self.tail.next.previous = self.tail
      self.tail = self.tail.next
      return


def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    for num in input_list:
      if head is None:
        head = Node(num)
        tail = head
      else:
        tail.next = Node(num)
        tail = tail.next
    return head

class Linked_List2:
  def __init__(self):
    self.head = None

  def prepend(self, value):
    '''Prepending to the beginning of the list.'''
    if self.head is None:
      self.head = Node(value)
      return
    else:
      old_head = self.head
      self.head = Node(value)
      self.head.next = old_head
      return

class Binary_Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Binary_Tree:
  def __init__(self, root):
    self.root = Binary_Node(root)

  def add_node(self, value):
    if self.root is None:
      self.root = Binary_Node(value)
    else:
      node = self.root
      if not node.left:
        node.left = Binary_Node(value)
      elif not node.right:
        node.right = Binary_Node(value)
      else:
        node.left.left = Binary_Node(value)

  def preorder_traversal(self, node):
    if node:
      print(str(node.value) + '<-->')
      self.preorder_traversal(node.left)
      self.preorder_traversal(node.right)


  def postorder_traversal(self, node):
    if node:
      self.postorder_traversal(node.left)
      self.postorder_traversal(node.right)
      print(str(node.value) + '<-->')

  def inorder_traversal(self, node):
    if node:
      self.inorder_traversal(node.left)
      print(str(node.value) + '<-->')
      self.inorder_traversal(node.right)












