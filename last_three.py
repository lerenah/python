import time

class Called:
    def __init__(self):
        self.times = []
        self.count = 0

    def counter(self):
        self.count += 1
        return self.count

    def last_three(self):
        self.times.append(time.time())
        amt = self.counter()
        if amt <= 3:
            return False
        elif self.times[-1] - self.times[-2] <= 3 and amt > 3:
            return True

func = Called()

print(func.last_three())
print(func.last_three())
print(func.last_three())
print(func.last_three())
