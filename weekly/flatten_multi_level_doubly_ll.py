def flatten(self, head):
  """
  :type head: Node
  :rtype: Node
  """
  if head is None:
      return head

  def get_last(head):
      curr = head
      prev = None
      while curr:
          if curr.child:
              kid = curr.child
              child = get_last(curr.child)

              if curr.next:
                  child.next = curr.next
                  curr.next.prev = child
                  curr.next = kid
                  kid.prev = curr
                  curr.child = None
              else:
                  curr.next = kid
                  kid.prev = curr
                  curr.child = None
          prev = curr
          curr = curr.next

      return prev

  get_last(head)
  return head


  # faster solution
  def flatten(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    if head is None:
        return head
    curr = head
    while curr:
        if not curr.child:
            curr = curr.next
            continue
        print(curr.val, ' is curr')
        kid = curr.child
        while kid.next:
            print(kid.val)
            kid = kid.next
        kid.next = curr.next
        if curr.next:
            curr.next.prev = kid
        curr.next = curr.child
        curr.child.prev = curr
        curr.child = None
        curr = curr.next
    return head
