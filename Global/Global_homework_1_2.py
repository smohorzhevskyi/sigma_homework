"""
Зібрати всі данні в словник та проіндексувати кожну станцію.
Приклад: Stations - словник
Stations = {'red stations' : { 1: "Академмістечко",
                               2: "Житомирська", ... },
            'blue stations' : {1: ...}, ...
            }

Вивести відсортований по значенням внутрішній словник для червоної гілки метро."""

blue_stations = ("""Героїв Дніпра
                Мінська
                Оболонь
                Почайна
                Тараса Шевченка
                Контрактова площа
                Поштова площа
                Майдан Незалежності
                Площа Льва Толстого
                Олімпійська
                Палац «Україна»
                Либідська
                Деміївська
                Голосіївська
                Васильківська
                Виставковий центр
                Іподром
                Теремки
                Одеська""")

red_stations = ["Академмістечко",
                "Житомирська",
                "Святошин",
                "Нивки",
                "Берестейська",
                "Шулявська",
                "Політехнічний інститут",
                "Вокзальна",
                "Університет",
                "Театральна",
                "Хрещатик",
                "Арсенальна",
                "Дніпро",
                "Гідропарк",
                "Лівобережна",
                "Дарниця",
                "Чернігівська",
                "Лісова"]

green_stations = {}
blue_stations_dict = {}
red_stations_dict = {}
stations = {}
counter = 1

for station in blue_stations.splitlines():
    blue_stations_dict[counter] = station.strip()
    counter += 1

counter = 1
for station in red_stations:
    red_stations_dict[counter] = station
    counter += 1

with open(file="green_stations.txt", encoding="utf-8") as file:
    counter = 1
    for line in file.readlines():
        green_stations[counter] = line.strip()
        counter += 1

stations = {'red stations': red_stations_dict, 'blue stations': blue_stations_dict, "green stations": green_stations}

for key, value in stations.items():
    print(key, value, sep=": ", end='\n')
