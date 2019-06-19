class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Candy:
    def __init__(self, node):
        self.head = node

    def add_node(self, node):
        if self.head is None:
            self.head = node
            return

        curr = self.head
        while curr:
            if curr.next is None:
                curr.next = node
                break
            curr = curr.next

    def crush(self):
        curr = self.head
        fast = curr.next.next
        slow = curr.next

        prev = curr

        while curr.next:
            if curr.value == slow.value and curr.value == fast.value:
                if curr == self.head:
                    curr = fast.next
                    self.head = fast.next

                if fast.next is None:
                    prev.next = None
                    return False

                else:
                    prev.next = fast.next

                return True

            prev = curr
            curr = curr.next
            slow = slow.next
            fast = fast.next

        return False

    def detect_crush(self):
        while self.crush():
            self.print_list()



    def print_list(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next
