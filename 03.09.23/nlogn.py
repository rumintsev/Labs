n = int(input('Введите количество элементов массива'))
arr = [i for i in range(n)]

# Алгоритм O(n*log(n))
for i in range(n):
    c = n
    while c != 0:
        arr[(c - 1) // 2] -= 1
        c = (c - 1) // 2