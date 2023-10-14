n = int(input('Введите количество элементов массива'))
arr = [i for i in range(n)]
cnt = 0

# Алгоритм O(n^3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[i] > arr[j] + arr[k]:
                cnt+=1

