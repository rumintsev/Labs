arr = [-1, 2, 3.9, 4, 5, 6, 7]
cor = ''

while (cor != '0' and cor != '1'):
    cor = input("Если хотите задать массив для поиска, введите 1, "
                "иначе - 0, во втором случае поиск будет "
                "осуществлён в массиве [-1, 2, 3.9, 4, 5, 6, 7] \n")


# функция проверка на число, число - 1, нет - 0
def isnum(new):
    if new != '':
        if new[0] == '-' and new[1:].isdigit() or \
                new.isdigit() or \
                new.replace('.', '', 1).isdigit() and new[0] != '.' or \
                new[0] == '-' and new[1:].replace('.', '', 1).isdigit():
            return 1
    return 0


# ввод масива
if cor == '1':
    arr = []
    fl = 1
    while (fl):
        new = input("Вводите элементы массива, чтобы закончить ввод, введите не число \n")
        if isnum(new):
            if new.count('.') != 0:
                arr.append(float(new))
            else:
                arr.append(int(new))
        else:
            fl = 0

# ввод числа для поиска
ch = ''
while (not (isnum(ch))):
    ch = input('Введите число для поиска \n')

if ch.count('.') != 0:
    ch = float(ch)
else:
    ch = int(ch)

# начало алгоритма
arr = sorted(arr)
cnt = 0
is_find = 0

st = 0
final = len(arr)

while (st != final):
    cnt += 1
    if arr[(st + final) // 2] == ch:
        is_find = 1
        st = final
    elif ch < arr[(st + final) // 2]:
        final = (final + st) // 2
    else:
        st = (final + st) // 2 + 1

if is_find:
    print("Число нашлось за ", cnt, " шаг/а/ов")
else:
    print('Число не нашлось')
