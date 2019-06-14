import random

class LLNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        self.head = LLNode()

    def add_node(self, value):
        new_node = LLNode(value)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next:
            total+=1
            curr = curr.next
        return total

    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next:
            if curr_node is not None:
                elems.append(curr_node.value)
                curr_node = curr_node.next
        elems.append(curr_node.value)


        print(elems)

    def list_shuffle(self):
        names = []
        if self.head.value is None:
            self.head = self.head.next
        curr = self.head

        while curr.next:
            prev = curr
            curr = curr.next
            prev.next = None
            names.append(prev)
        names.append(curr)

        def pick_random():
            _random = random.choice(names)
            names.remove(_random)
            return _random

        el = names[0]
        names.remove(el)
        while len(names):
            choose = pick_random()
            el.next = choose
            el = el.next
