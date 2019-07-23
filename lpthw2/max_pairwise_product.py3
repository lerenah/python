
def max_pairwise_product(n, arr):
    res = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] * arr[j] > res:
                res = arr[i] * arr[j]
    return res


def max_pairwise_product_fast(n, numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    assert (len(arr) == n)

    print(max_pairwise_product_fast(n, arr))
