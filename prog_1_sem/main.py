import json
from datetime import datetime


def is_date(str):
    if len(str) == 8 and str[2] == "." and str[5] == ".":
        str = str.replace(".", "")
        if str.isdigit():
            return 1
    return 0


def is_num(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def vision(str):
    match str:
        case "start_help":
            print("Чтобы посмотреть список команд введите -help")
        case "not":
            print("Нет такой команды")
        case "wrong":
            print("Команда введена неверно")
        case "not_price":
            print("Цена введена неверно")
        case "no_in":
            print("По этому критерию трат нет")
        case "empty_dict":
            print("Трат не было")
        case "-help":
            print("\n-new Дата; Название траты; Цена; Категория - будет добавлена новая трата, "
                  "дата в формате дд.мм.гг,\n если дата не указана или в другом формате, "
                  "будет присвоена текущая, если поле "
                  "категории пусто,\n будет присвоена категория 'Без категории'\n\n"

                  "-del Дата; Название траты - трата будет удалена, дата в формате дд.мм.гг,\n "
                  "если дата не указана или в другом формате, "
                  "будет присвоена текущая\n\n"

                  "-cat Название категории - будет выведен список трат по категории\n\n"
                  
                  "-dat Дата - будет выведен список трат в эту дату\n\n"

                  "-ful - будет выведен полный список трат\n\n"
                  
                  "-off - выключает программу\n\n"
                  
                  "-srt Значение - значение может быть 'min' или 'max', в первом случае будет "
                  "выполнена \nсортировка по цене от меньшего к большему, во втором - наоборт")


vision("start_help")
current = datetime.now()
now = str(current.day) + '.' + str(current.month) + '.' + str(current.year)[-2:]
while (1):
    f = open("base.json", "r")
    dict = json.load(f)
    new_i = 0
    if len(dict) != 0:
        for i in dict:
            new_i = max(new_i, int(i)+1)
    inp = input("")
    if len(inp) < 4:
        vision("not")
    elif inp == "-help":
        vision("-help")
    else:
        match inp[:4]:
            case "-new":
                inp = inp[5:]
                if inp[-1] == ";":
                    inp += " "
                inp = inp.split("; ")
                if len(inp) != 4:
                    vision("wrong")
                    continue
                if not (is_num(inp[2])):
                    vision("not_price")
                    continue
                if float(inp[2]) < 0:
                    vision("not_price")
                    continue
                if not (is_date(inp[0])):
                    inp[0] = now
                if inp[3] == "":
                    inp[3] = "Без категории"
                dict[new_i] = (inp[0], inp[1], inp[2], inp[3])
                f = open("base.json", "w")
                json.dump(dict, f, ensure_ascii=False)
            case "-del":
                inp = inp[5:]
                inp = inp.split("; ")
                if len(inp) != 2:
                    vision("wrong")
                    continue
                if not (is_date(inp[0])):
                    inp[0] = now
                for i in list(dict):
                    if dict[i][0] == inp[0] and dict[i][1] == inp[1]:
                        del dict[i]
                        f = open("base.json", "w")
                        json.dump(dict, f, ensure_ascii=False)
            case "-off":
                break
            case "-cat":
                inp = inp[5:]
                cnt=0
                for i in list(dict):
                    if dict[i][3] == inp:
                        cnt+=1
                        print(dict[i][0], dict[i][1], dict[i][2])
                if cnt==0:
                    vision("no_in")
            case "-dat":
                inp = inp[5:]
                cnt = 0
                for i in list(dict):
                    if dict[i][0] == inp:
                        cnt += 1
                        print(dict[i][1], dict[i][2], dict[i][3])
                if cnt == 0:
                    vision("no_in")
            case "-ful":
                if len(dict) == 0:
                    vision("empty_dict")
                    continue
                for i in list(dict):
                    print(dict[i][0], dict[i][1], dict[i][2], dict[i][3])
            case "-srt":
                inp = inp[5:]
                if inp != "max" and inp != "min":
                    vision("wrong")
                    continue
                prices = list(dict.values())
                prices.sort(key=lambda x: int(x[2]))
                if inp == "min":
                    for i in prices:
                        print(i[0], i[1], i[2], i[3])
                else:
                    prices = prices[::-1]
                    for i in prices:
                        print(i[0], i[1], i[2], i[3])
            case _:
                vision("wrong")
