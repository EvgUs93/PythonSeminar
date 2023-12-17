"""
    Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()

"""
    
    
user_sym = input("введите символы через пробел").split()
new_sym = ""
for symbol in user_sym:
    count = new_sym.count(symbol)
    if new_sym.count(symbol) == 0:
        new_sym += f"{symbol} "
    else:
        new_sym += f"{symbol}_{count} "
print(new_sym)

