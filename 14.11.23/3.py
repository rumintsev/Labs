import random

n = int(input())
N = []

for i in range(n):
    x = random.randint(-100, 100)
    N.append(x)

k = 1
maxi = 0

for i in range(len(N) - 1):
    if N[i+1] > N[i]:
        k += 1
        maxi = max(maxi, k)
    else:
        k = 1
print(maxi)
