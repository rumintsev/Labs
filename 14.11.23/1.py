n, m, k = int(input()), int(input(), int(input() # количество экспонатов; количество заходов; вес, который может унести вор за один заход
weights = [int(i) for i in input().split()] # список с весом экспонатов
prices = [int(i) for i in input().split()] # список со стоимостью экспонатов
is_item_stolen = [False for i in range(n)] # чтобы вор не украл то, что было украдено ранее; после каждого подхода надо запоминать, какие предметы уже были украдены
total_price = 0 # цена украденного
for w in range(m): # проходимся по всем заходам вора
    dp = [[[0, []] for a in range(k + 1)] for b in range(n + 1)] # создаем таблицу из n+1 строк и k+1 нулевых значений; строки нумеруем индексом b, столбцы - индексом a
                                                                 # [0, []] - это пара [итоговая стоимость вещей, [список взятых вещей]]
    for i in range(1, n + 1): # при i = 0 мы бы посмотрели первые 0 предметов и получили бы 0 веса
        for j in range(k + 1): # смотрим массу экспонатов от 0 до k включительно
            dp[i][j] = [dp[i - 1][j][0], list(dp[i - 1][j][1])] # в состоянии dp[i][j] будем хранить возможно ли получить из первых i предметов набор веса j и
                                                                # максимальную суммарную стоимость такого набора; если такой набор нельзя получить, то dp[i][j] = 0.
                                                                # переносим состояние, когда мы рассмотрели i - 1 предметов в состояние, когда мы посмотрели i предметов (мы не взяли его)"
            if is_item_stolen[i - 1]: # предмет украден, идем к следующей итерации
                continue
            if (weights[i - 1] <= j and
                dp[i][j][0] < dp[i - 1][j - weights[i - 1]][0] + prices[i - 1]):
                dp[i][j] = [
                    dp[i - 1][j - weights[i - 1]][0] + prices[i - 1],
                    dp[i - 1][j - weights[i - 1]][1] + [i]]
            # если вор может украсть экспонат и стоимость украденных ранее экспонатов меньше стоимости украденных вещей с массой; 
            # j - (минус) масса предмета плюс стоимость предмета, то вор крадем его и сохраняем состояние
    max_item = [0, []] # набор экспонатов с максимальной стоимостью
    for i in dp[n]: # ищем такой набор краденных экспонатов, у которого максимальная стоимость
        if i[0] > max_item[0]:
            max_item = i
    total_price += max_item[0]
    for i in max_item[1]: # цикл, в результате которого мы выводим максимальную цену украденного
        is_item_stolen[i] = True
print(total_price)
stolen_items = [] # создаем пустой массив, куда будем помещать украденные экспонаты
for i in range(n):
    if is_item_stolen[i]:
        stolen_items.append(i)
print(*stolen_items)