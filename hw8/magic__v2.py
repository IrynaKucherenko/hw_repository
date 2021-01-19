"""
    Реализуйте игру Magic (правила в hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. Создается словарь с данными игрока.
        данные брать из файла data.json,
        если данных об этом игроке в файле нет,
        то создается словарь с дефолтными значениями.

    3. Оперировать с такими данными о пользователе (можно добавить что-то еще):
        name - имя,
        games - кол-во сыграных игр,
        avg_attempts - среднее количество попыток за игру,
        record - рекордное количество попыток (минимальное)

    4. После каждой игры данные о пользователе актуализируются в файле.
        а именно,
        инкрементируется количество сыграных игр,
        пересчитывается среднее количество попыток за игру,
        перезаписывается рекод, если он был побит

    Имя является уникальным идентификатором,
    т.е. в data.json хранятся данные уникальных пользователей без дублей.
"""


import json
import random

players = {}
try:
    with open("test.json", "r") as f:
        data = f.read()
       # print(":" + data)
        players = json.loads(data)
except:
    print("Can't load data")


def main():
    name = input("name: ").title()
    if players.get(name) is None:
        p = {name: {"games": 0, "avg_attempts": 0, "record": 0}}
        players[name] = {"games": 0, "total_attempts": 0, "avg_attempts": 0, "record": 1000000}

    games = get_magic([])
    update(games, players[name])
    print(players[name])
    print("==================================================================")

    with open("test.json", "w") as f:
        f.write(json.dumps(players, indent=4))


def get_magic(games):
    random_number = random.randint(1, 100)
    counter_try = 0
    while True:
        try:
            a = int(input("number: "))
            counter_try += 1
        except ValueError:
            print("You must enter a number.")
            continue

        if a > random_number:
            print("greater than magic")
        elif a < random_number:
            print("less than magic ")
        else:
            games.append(counter_try)
            print("===========")
            print("!!Bingo!!")
            print("Tries: " + str(counter_try))
            print("===========")
            answer = input("Continue? (y/n)")
            if answer == "n":
                print("Game over")
                return games
            else:
                return get_magic(games)


def update(games, oldStats):
    oldStats["games"] += len(games)
    oldStats["total_attempts"] += sum(games)
    oldStats["avg_attempts"] = oldStats["total_attempts"] // oldStats["games"]
    oldStats["record"] = min(oldStats["record"], min(games))


main()
