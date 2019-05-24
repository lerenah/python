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



