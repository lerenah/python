# nums = [int(x) for x in input('Enter 2 digits').split()]


def sum_nums(a, b):
    return a + b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_nums(a, b))
