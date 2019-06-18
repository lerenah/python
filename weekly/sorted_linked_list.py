class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node

    def insert_node(self, node):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def print_list(self):
        if self.head:
            curr = self.head
            while curr:
                print(curr.value)
                curr = curr.next

    def sort(self):
        if self.head:
            curr = self.head
            min = curr

            lft_of_min = curr
            old_prev = curr

            while curr.next:
                # check for min value first to set as head
                if curr.next.value < min.value:
                    min = curr.next
                    lft_of_min = curr
                # traverse and swap the rest of the list
                elif curr.next.value < curr.value:
                    temp = curr.next
                    prev = curr
                    curr = temp
                    prev.next = curr.next
                    curr.next = prev
                    old_prev.next = curr

                old_prev = curr
                curr = curr.next

            if min.next is None:
                min.next = self.head
                lft_of_min.next = None
                self.head = min
            else:
                lft_of_min.next = min.next
                min.next = self.head
                self.head = min




node = Node(2)
ll = LinkedList(node)
ll.insert_node(Node(5))
ll.insert_node(Node(4))
ll.insert_node(Node(7))
ll.insert_node(Node(1))

ll.print_list()
ll.sort()
ll.print_list()
