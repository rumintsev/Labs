import sys

def mcm(dims):
    n = len(dims)
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]

    for l in range(2, n + 1):   

        for i in range(1, n - l + 2):
            j = i + l - 1
            c[i][j] = sys.maxsize
            k = i

            while j < n and k <= j - 1:
                cost = c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < c[i][j]:
                    c[i][j] = cost
                k = k + 1

    return c[1][n - 1]
 
dims = [50, 110, 40, 80, 70, 90] #в данном случае подрузвмевается матрица размером dims[i] x dims[i+1]
print(mcm(dims))
