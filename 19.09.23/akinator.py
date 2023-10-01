from csv import *
reader = reader(open('csv.csv', encoding='utf-8'))

arr = {}
for row in reader:
    key = row[0]
    if key in arr:
        pass
    arr[key] = row[1:]

qw = ["Мужчина?","Есть 18 лет?","Местный? (Из Санкт-Петербурга)","Уровень английского - B2 или выше?",
      "Окончили школу с медалью?","Умеет готовить?","Карие глаза?","Есть домашнее животное?","Часто читает книги?",
      "Есть проблемы со зрением?","День рождения - нечётное число?"]
print("Квиз: отвечайте «Да» или «Нет»")

i = 0
fl = 0
while(len(arr)>1):
    res = ''
    while(res!='Да' and res!='Нет'):
        res = input(qw[i] + "\n")
    for j in list(arr):
        if arr[str(j)][i+1] != res:
            del arr [str(j)]
    i+=1
    if len(arr) == 1: fl = 1

if fl == 1:
    print(arr[list(arr)[0]][0], )
else: print("У нас в группе нет такого человека")