def recursion():
    num = b(5,2)
    print(num)


def b(n,k):
    if k == 0 or k == n:
        print('Base Case!')
        return 2
    else:
        return b(n-1, k-1) + b(n-1,k)


if __name__ == '__main__':
    recursion()