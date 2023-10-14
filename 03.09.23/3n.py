n = int(input('Введите количество элементов массива'))
arr = [i for i in range(n)]

# Алгоритм O(3*n)
for i in range(n):
    arr[i] += 10
    arr[i] *= 2
    arr[i] //= 4

