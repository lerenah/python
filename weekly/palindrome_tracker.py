class PalTracker:

    def __init__(self):
        self.str = ''
        self.storage = []
        self.increment = -1
        self.palindrome = False

    def track_palindrome(self):
        if not self.palindrome:
            self.isPalindrome()



    def track(self, char):
        self.storage.append(char)
        self.str += char
        self.increment += 1
        self.track_palindrome()


    def isPalindrome(self):
        if len(self.storage):
            first = self.storage[self.increment]
            self.palindrome = True
        if self.increment + 1 in range(len(self.storage)):
            mover = self.increment + 1
            if first == self.storage[mover]:
                self.palindrome = True


        return self.palindrome
