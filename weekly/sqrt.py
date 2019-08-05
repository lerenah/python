def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 1
        while n != x:
            if (n * n) <= x < ((n + 1) * (n + 1)):
                break
            n += 1

        return n
