import timeit
import random

def comb_sort(array):
    length = len(array)
    factor = 1.247331
    step = length - 1

    while True:
        i = 0
        is_not_sorted = False
        while i + step < length:
            if array[i] > array[i + step]:
                array[i], array[i + step] = array[i + step], array[i]
                is_not_sorted = True
            i += 1
        if step == 1 and not is_not_sorted:
            break
        if step > 1:
            step = int(step / factor)

arr = []
for i in range(100):
    arr.append(random.randint(0,100))

start = timeit.default_timer()
comb_sort(arr)
print("Время выполнения:", timeit.default_timer() - start, "секунд")