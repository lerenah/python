def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 0:
        return 0
    if n == 1:
        return ["()"]
    output = []
    curr_str = '(' * n + ')' * n

    def check_validity(s):
        stack = []
        for parens in s:
            if parens == '(':
                stack.append(parens)
            elif parens == ')':
                if len(stack):
                    if stack.pop() != '(':
                        return False
                else:
                    return False
        return len(stack) == 0

    def perms(arr, soFar):
        if len(arr) == 0:
            if check_validity(soFar):
                if ''.join(soFar) not in output:
                    output.append(''.join(soFar))
        for j, parens in enumerate(arr):
            result = soFar + [parens]
            rest = arr[:j] + arr[j + 1:]
            perms(rest, result)

        return soFar

    perms([p for p in curr_str], [])
    return output
