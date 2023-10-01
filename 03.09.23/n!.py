n = int(input("Введите количество элементов массива"))
arr = [i for i in range(n)]

def fc(a):
    if len(a) == 1:
        yield (a[0],)
    else:
        for i in fc(a[1:]):
            for j in range(len(a)):
                yield i[:j] + (a[0],) + i[j:]

def ofc(a):
    return list(set(fc(a)))

print(ofc(arr))
