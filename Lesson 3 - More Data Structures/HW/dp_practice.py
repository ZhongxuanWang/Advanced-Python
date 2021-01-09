import sys


def f(n):
    if n <= 2:
        return 1
    if dp[n - 1] is None:
        dp[n - 1] = f(n - 1)

    if dp[n - 2] is None:
        dp[n - 2] = f(n - 2)

    return dp[n - 1] - dp[n - 2] + n


if __name__ == '__main__':
    # Input
    ipt = 2018

    sys.setrecursionlimit(ipt + 1)
    dp = [None] * ipt
    print(f(ipt))
