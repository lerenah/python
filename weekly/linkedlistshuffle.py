    def random_display(self):
        elems = []
        names = []
        randomed = []
        if self.head.value is None:
            self.head = self.head.next
        curr = self.head

        while curr.next:
            prev = curr
            curr = curr.next
            prev.next = None
            elems.append(prev.value)
            names.append(prev)
        elems.append(curr.value)
        names.append(curr)
        if None in elems:
            elems.remove(None)
        print(elems)
        print(self.head.value, ' is head')

        def pick_random():
            _random = random.choice(names)
            names.remove(_random)
            return _random

        chosen = []
        el = names[0]
        names.remove(el)
        self.head = el
        randomed.append(self.head)
        while len(names):
            choose = pick_random()
            if choose not in chosen:
                if el.value != choose.value:
                    el.next = choose
                chosen.append(choose)
                randomed.append(el)
                print(el.value)
                print(el.next.value)
                el = el.next
