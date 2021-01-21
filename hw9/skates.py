"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.

    Напишите программу, которая принимает список доступных размеров коньков и
    список размеров ног желающих.

    И выводит наибольшее количество людей,
    которые смогут покататься одновременно.


    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)

    [out]
    2

    Напишите несколько тестов
"""


def skates(available_sizes, foot_sizes):
    available_sizes = list(map(int, input().split()))
    foot_sizes = list(map(int, input().split()))

    available_sizes = list(filter(lambda x: x >= min(foot_sizes), available_sizes))

    for i in available_sizes:
        for v in foot_sizes:
            if i > v and len(available_sizes) >= len(foot_sizes):
                res1 = len(foot_sizes)
                return res1
            elif i > v and len(available_sizes) <= len(foot_sizes):
                res2 = len(available_sizes)
                return res2
    print(skates(available_sizes, foot_sizes))


available_sizes = 39, 38, 41, 37
foot_sizes = 40, 39, 41
assert skates(available_sizes, foot_sizes) == 2

available_sizes = 40, 39, 41
foot_sizes = 39, 38, 41, 37
assert skates(available_sizes, foot_sizes) == 3

available_sizes = 36, 37, 45, 45, 45, 45
foot_sizes = 40, 40, 40, 40, 40, 40
assert skates(available_sizes, foot_sizes) == 4

print("========ok========")

