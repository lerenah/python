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
    if current.down:
      end_node = flatten(current.down)
      end_node.set_next(current.get_next())
    current = current.next
  return end_node


