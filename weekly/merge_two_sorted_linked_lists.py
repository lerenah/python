def mergeTwoLists(self, l1, l2):
  """
  :type l1: ListNode
  :type l2: ListNode
  :rtype: ListNode
  """
  if not l1:
      return l2
  if not l2:
      return l1
  if l1.val < l2.val:
      head = l1
      l1 = l1.next
  else:
      head = l2
      l2 = l2.next
  curr = head
  while curr:
      if l1 and l2:
          if l1.val < l2.val:
              curr.next = l1
              l1 = l1.next
          else:
              curr.next = l2
              l2 = l2.next
      elif l1:
          curr.next = l1
          break
      elif l2:
          curr.next = l2
          break
      curr = curr.next
  return head
