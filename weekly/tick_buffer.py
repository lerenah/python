class Buffer:
    def __init__(self):
        self.memory = 800
        self.size_t = []


    def double_buffer(self):
        if len(self.size_t) == self.memory:
            copy = self.size_t[:]
            doubled_arr = [] * len(copy)
            self.size_t = copy + doubled_arr
        