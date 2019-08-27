# dummy = 0
#     curr = 1, prev = 0 | prev = 1, curr = 2 | prev = 2, curr = 6 | prev = 2, prev.next = 3, curr = 3
#     0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
#     prev = 3, curr = 4 | prev = 4, curr = 5 | prev = 5, curr = 6
#     prev.next = None, prev = 5, curr = None
#     0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None
#     '''
'''
    dummy = 0
    0 -> 1
    prev = 0, curr = 1 |
    prev.next = None
    curr = None
    0 -> none
    dummy variable is the key -> do not move prev if you have found val to delete, previous cannot move forward until current gets processed. Then on the next iteration.
    '''


def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    curr = head  # 1
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return dummy.next
