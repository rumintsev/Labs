import timeit
import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    oporn = arr[0]
    left = list(filter(lambda x: x < oporn, arr))
    mid = [i for i in arr if i == oporn]
    right = list(filter(lambda x: x > oporn, arr))

    return quick_sort(left) + mid + quick_sort(right)

arr = []
for i in range(100):
    arr.append(random.randint(0,100))

start = timeit.default_timer()
quick_sort(arr)
print("Время выполнения:", timeit.default_timer() - start, "секунд")

