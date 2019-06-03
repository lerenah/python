class Collatz:
    def __init__(self):
        self.steps = []

    def steps_from(self, n):
        if n == 1:
            return 0
        else:
            while n != 1:
                if n % 2 == 0:
                    n /= 2
                    self.steps.append(n)
                elif n % 2 != 0:
                    n = 3*n + 1
                    self.steps.append(n)
        
        return len(self.steps)
