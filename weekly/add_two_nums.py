def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def get_numbers(l):
            s = ''
            curr = l
            while curr:
                s = str(curr.val) + s
                curr = curr.next
            return s

        first_num = int(get_numbers(l1))
        second_num = int(get_numbers(l2))

        total = first_num + second_num
        string_total = str(total)

        l3 = ListNode(int(string_total[-1]))
        head = l3
        s = len(string_total) - 2
        while s >= 0:
            head.next = ListNode(int(string_total[s]))
            head = head.next
            s -= 1

        return l3
