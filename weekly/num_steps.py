def num_steps(n, steps):
    result = 0
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        for i in range(len(steps)):
            result += num_steps(n - steps[i], steps)

    return result
