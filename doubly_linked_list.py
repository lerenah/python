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

class Node:
    def __init__(self, value):
      self.value = value
      self.next = None

head = Node(1)

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
