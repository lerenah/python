'''
You are given n balls. Each of these balls are of one the three colors: Red, Green and Blue. They are arranged randomly in a line. Your task is to rearrange them such that all balls of the same color are together and their collective color groups are in this order: Red balls first, Green balls next and Blue balls last.



This combination of colors is similar to the Dutch National Flag, hence the problem name.
'''


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dutch_flag_sort(balls):
    r = 0
    b = len(balls) - 1
    i = 0
    while i in range(b + 1):
        if balls[i] == 'R':
            swap(balls, r, i)
            i += 1
            r += 1
        elif balls[i] == 'B':
            swap(balls, b, i)
            b -= 1
        else:
            i += 1

    return balls
