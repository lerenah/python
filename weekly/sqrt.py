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

# optimal solution
        # n = x
        # start = 1
        # while start <= n:
        #     ans = (start + n) // 2
        #     if (ans**2) == x:
        #         return ans
        #     elif (ans**2) <= x:
        #         start = ans + 1
        #     else:
        #         n = ans - 1

        # return n
