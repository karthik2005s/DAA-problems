def lcs(X, Y):
    m = len(X)
    z = len(Y)
    L = [[None] * (z + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(z + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][z]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", lcs(X, Y))
