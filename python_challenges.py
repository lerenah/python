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
