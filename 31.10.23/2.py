transfer_stations = [
    i.split(' - ')
    for i in [
        'Гостиный двор - Невский проспект',
        'Спасская - Садовая - Сенная площадь',
        'Технологический институт I - Технологический институт II',
        'Пушкинская - Звенигородская',
        'Владимирская - Достоевская',
        'Маяковская - Площадь восстания',
        'Площадь Александра Невского I - Площадь Александра Невского II',]
]
class Station:
    counter = 0
    def __init__(self, name, line):
        self.name = name
        self.line = line
        self.number = Station.counter
        self.linked_stations = []
        Station.counter += 1
    def __repr__(self):
        return f'Станция "{self.name}"'

lists = [
    (
        'Девяткино',
        'Гражданский проспект',
        'Академическая',
        'Политехническая',
        'Площадь мужества',
        'Лесная',
        'Выборгская',
        'Площадь ленина',
        'Площадь восстания',
        'Владимирская',
        'Пушкинская',
        'Технологический институт I',
        'Балтийская',
        'Нарвская',
        'Кировский завод',
        'Автово',
        'Ленинский проспект',
        'Проспект ветеранов'
    ),
    (
        'Парнас',
        'Проспект просвещения',
        'Озерки',
        'Удельная',
        'Пионерская',
        'Черная речка',
        'Петроградская',
        'Горьковская',
        'Невский проспект',
        'Сенная площадь',
        'Технологический институт II',
        'Фрунзенская',
        'Московские ворота',
        'Электросила',
        'Парк победы',
        'Московская',
        'Звёздная',
        'Купчино',
    ),
    (
        'Беговая',
        'Зенит',
        'Приморская',
        'Василеостровская',
        'Гостиный двор',
        'Маяковская',
        'Площадь Александра Невского I',
        'Елизаровская',
        'Ломоносовская',
        'Пролетарская',
        'Обухово',
        'Рыбацкое'
    ),
    (
        'Спасская',
        'Достоевская',
        'Лиговский проспект',
        'Площадь Александра Невского II',
        'Новочеркасская',
        'Ладожская',
        'Проспект Большевиков',
        'Улица Дыбенко'
    ),
    (
        'Комендантский проспект',
        'Старая деревня',
        'Крестовский остров',
        'Чкаловская',
        'Спортивная',
        'Адмиралтейская',
        'Садовая',
        'Звенигородская',
        'Обводный канал',
        'Волковская',
        'Бухарестская',
        'Международная',
        'Проспект славы',
        'Дунайская',
        'Шушары'
    )
]

stations = {}
for line in range(len(lists)):
    line_stations = lists[line]
    for i in range(len(line_stations)):
        station = Station(line_stations[i], line)
        stations[line_stations[i].lower()] = station
        if i > 0:
            station.linked_stations.append(stations[line_stations[i - 1].lower()])
            stations[line_stations[i - 1].lower()].linked_stations.append(station)

for i in transfer_stations:
    for j in i:
        station = stations[j.lower()]
        for transfer_station in i:
            transfer_station = stations[transfer_station.lower()]
            if transfer_station.number == station.number:
                continue

            station.linked_stations.append(transfer_station)

first_station = input()
next_station = input()

class VisitedPoint:
    def __init__(self, point: str, steps: int):
        self.point = point
        self.steps = steps

class Walker:
    def __init__(self, stations: 'dict[str, set[str]]'):
        self.visited_points = {}
        self.stations = stations
        self.path = None

    def solve(self, current: str, to: str, number: int = 0):
        value: VisitedPoint = self.visited_points.get(current)
        if not value or value.steps > number:
            self.visited_points[current] = VisitedPoint(current, number)
        else:
            return
        if current == to:
            return
        for station in self.stations[current]:
            self.solve(station, to, number + 1)

    def breadth_first_search(self, from_station, to_station):
        if isinstance(from_station, str):
            from_station = stations[from_station.lower()]
        if isinstance(to_station, str):
            to_station = stations[to_station.lower()]

        to_browse = [(from_station,)]
        while to_browse:
            path = to_browse[0]
            del to_browse[0]
            for i in path[-1].linked_stations:
                if i.number == to_station.number:
                    self.path = path + (i,)
                    return self.path
                if i in path:
                    continue
                to_browse.append(path + (i,))

    def depth_first_search(self, from_station, to_station, path=()):
        if isinstance(from_station, str):
            from_station = stations[from_station.lower()]
        if isinstance(to_station, str):
            to_station = stations[to_station.lower()]

        path += (from_station, )

        for i in path[-1].linked_stations:
            if i.number == to_station.number:
                return path + (i,)

            if i in path:
                continue

            result = self.depth_first_search(i, to_station, path)
            if result:
                if self.path is None:
                    self.path = result
                    return result
                elif len(self.path) > len(result):
                    self.path = result
                    return result

walker = Walker(stations)

print(walker.breadth_first_search(first_station, next_station))
walker.depth_first_search(first_station, next_station)
print(walker.path)
