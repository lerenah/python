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
            first = self.storage[0]
            self.palindrome = True
            i = 0
            mid = len(self.storage) // 2
            while i in range(len(self.storage)) and (mid + i) in range(len(self.storage)):
                next_letter = self.storage[self.increment]
                if first != next_letter:
                    self.palindrome = False
                    return self.palindrome
                else:
                    left_of_mid = mid - i
                    right_of_mid = mid + i
                    if self.storage[left_of_mid] != self.storage[right_of_mid]:
                        self.palindrome = False
                        return self.palindrome
                    i += 1

        return self.palindrome


