def lcs(x,y):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    else:
        if x[-1] == y[-1]:
            return lcs(x[:m-1],y[:n-1]) + 1
        else:
            return max(lcs(x[:m-1],y),lcs(x,y[:n-1]))
