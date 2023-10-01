n = int(input('Введите количество элементов массива'))
arr = [i for i in range(n)]
acc = 0

# Алгоритм O(3*log(n))
while (n != 0):
    acc += arr[(n - 1) // 2]
    arr[(n - 1) // 2] = -1
    n = (n - 1) // 2