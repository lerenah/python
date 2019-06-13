class Tracker:
    def __init__(self):
        self.storage = []

    def add(self, n, value):
        self.storage.append({n: value})
        print(self.storage)

    def recall(self, num):
        if any(num in seq for seq in self.storage):
            for datum in self.storage:
                k = datum
                for el in k:
                    if el == num:
                        return datum
        else:
            return False

    def print(self):
        ordered = []
        for i in range(1, len(self.storage) + 1):
            datum = self.recall(i)
            if datum:
                ordered.append(datum)
            if not self.recall(i + 1):
                return ordered
        return ordered
