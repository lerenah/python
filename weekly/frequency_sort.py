def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cache = {}
        for letter in s:
            if letter not in cache:
                cache[letter] = 0
            cache[letter] += 1
        letters = sorted(cache.items(), key=lambda x: x[1], reverse=True)
        output = ''
        for key, val in letters:
            output += key * val

        return output
