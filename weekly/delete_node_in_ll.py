def deleteNode(self, node):
  """
  :type node: ListNode
  :rtype: void Do not return anything, modify node in-place instead.
  """
  t = node
  if t.next is not None:
      t.val = t.next.val
      t.next = t.next.next
  else:
      t = None
