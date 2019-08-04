class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        if not len(self.stack):
            self.min = x
        else:
            self.min = min(self.min, x)

        self.stack.append(x)



    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack):
            self.stack.pop()
            if len(self.stack):
                self.min = min(self.stack)
            else:
                self.min = self.min
        else:
            raise Exception('Stack is currently Empty.')


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack):
            return self.stack[-1]
        else:
            return 'No items in stack.'


    def getMin(self):
        """
        :rtype: int
        """
        return self.min
