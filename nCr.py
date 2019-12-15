table = [[-1]*50 for _ in range(50)]#Global variable

def nCr(n, r):
    if table[n][r] != -1:
        nr = table[n][r]
    elif n == r:
        nr = 1
    elif r == 1:
        nr = n
    else:
        nr = nCr(n-1, r) + nCr(n-1, r-1)

    table[n][r] = nr
    return nr


if __name__ == "__main__":
    while True:
        n, r = map(int, input().split())
        res = nCr(n, r)
        print(res)
