a = 10
b = 25

def sum(a, b):
    a += 1
    b -= 1
    if b > 0:
        return sum(a, b)
    else:
        return a
    
print(sum(a, b))