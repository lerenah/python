def find_cycle_start(head):
  # TODO: Write your code here
  if head is None:
    return head
  fast, slow = head, head
  while fast:
    if fast.value == slow.value:
      return slow
    fast = fast.next.next
    slow = slow.next
  return head
