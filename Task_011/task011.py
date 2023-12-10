"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
"""


A = 5
n = 0

fibo_p, fibo_n = 0, 1
count = 2
while fibo_n < A:
    fibo_p, fibo_n = fibo_n, fibo_n + fibo_p
    count += 1
if fibo_n == A:
    print(count)
else:
    print(-1)