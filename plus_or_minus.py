def plusMinus(arr):
    l = len(arr)
    positive = [1 for x in arr if x > 0]
    minus = [-1 for x in arr if x < 0]
    zeros = [1 for x in arr if x == 0]
    print(f'{sum(positive) / l:.6f}')
    print(f'{-1 * sum(minus) / l:.6f}')
    print(f'{sum(zeros) / l:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
