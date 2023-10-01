import random, time

def bubble(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return (a)

arr1 = []
for r in range(10_000):
    arr1.append(random.randint(0, 1_000_000))
arr2 = arr1

start = time.time()
bubble(arr1)
endt = time.time()
print(f"Сортировка пузырьком - {endt - start}")

start = time.time()
arr2.sort()
endt = time.time()
print(f"Встроенная сортировка - {endt - start}")