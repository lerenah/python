class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head = node


    def change_next(self, node):
        node.next = None
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

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
            nodes = []
            curr = self.head

            while curr:
                nodes.append(curr)
                curr = curr.next

            nodes = sorted(nodes, key=lambda node: node.value)
            nodes[0].next = None
            newList = LinkedList(nodes[0])

            for node in nodes[1:]:
                newList.change_next(node)

            return newList.print_list()
        return
