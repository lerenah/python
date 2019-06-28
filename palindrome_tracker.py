class PalTracker:

    def __init__(self):
        self.str = ''
        self.storage = []
        self.increment = -1
        self.palindrome = False

    def track(self, char):
        self.storage.append(char)
        self.str += char
        self.increment += 1
        self.is_palindrome()


    def is_palindrome(self):
        if not len(self.storage):
            return False
        else:
            i = 0
            j = len(self.storage) - 1
            self.palindrome = True
            while i <= j:
                if self.storage[i] != self.storage[j]:
                    return False
                else:
                    i += 1
                    j -= 1

        return self.palindrome


