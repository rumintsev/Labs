from math import *
from random import *

n = int(input("Кол-во элементов"))
arr = [i for i in range(n)]

for i in range(factorial(n)):
    arr[randint(0, n - 1)] += i
