class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  # TODO: Write your code here
  if head is None:
    return False
  slow = head
  fast = head
  while fast:
    if slow.value == fast.value:
      return True
    slow = slow.next
    fast = fast.next.next
  return False
