"""
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""

n = 7
def func_1(n):
    fibo_p, fibo_n = 0, 1
    for i in range(n):
        fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
    return fibo_n
print(func_1(n))

def func_2(n):
    if n < 3:
        return n
    return func_2(n-1) + func_2(n-2)
print(func_2(n))