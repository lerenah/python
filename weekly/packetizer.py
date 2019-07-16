class Packetizer:
    def __init__(self):
        self.holding = []
        self.size = None
        self.bits_expected = 0

    def process(self, arr):
        return ' '.join(arr)


    def packetize(self, data):
        while len(data) > 0:
            if self.size is not None:
                # compute number of bytes needed
                bytes_left = self.size - len(self.holding)
                if len(data) >= bytes_left:
                    self.holding.extend(data[:bytes_left])
                    print(self.process(self.holding))
                    self.holding = []
                    self.size = None
                    data = data[bytes_left:]
                else:
                    self.holding.extend(data)
                    data = []
            else:
                # treats first two numbers as a length
                self.size = data[1] * 256 + data[0]
                data = data[2:]

            print(data)
