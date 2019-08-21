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

def find_cycle_start(head):
  # TODO: Write your code here
  if head is None:
    return head
  fast, slow = head, head
  seen = {}
  while fast is not None and fast.next is not None:
    seen[fast] = True
    slow = slow.next
    fast = fast.next.next
    if fast in seen or fast == slow:
      return fast
  return head


def has_cycle(head):
  # TODO: Write your code here
  if head is None:
    return False
  slow = head
  fast = head
  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return True
  return False
