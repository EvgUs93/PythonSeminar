"""
Задача 8: Требуется определить, можно ли от шоколадки размером n
× m долек отломить k долек, если разрешается сделать один разлом по
прямой между дольками (то есть разломить шоколадку на два
прямоугольника).
3 2 4 -> yes
3 2 1 -> no
"""

UserLength = int(input("Сколько долек вдоль шоколадки?"))
UserWidth = int(input("Сколько долек в ширину?"))
UserNumber = int(input("Сколько долек вы хотите отломить?"))

if (UserNumber <= UserLength * UserWidth) and ((UserNumber % UserLength == 0) or (UserNumber % UserWidth == 0)):
    print("yes")
else:
    print("no")