t = int(input())
while t > 0:
    n = int(input())
    if n == 0 or n == 1:
        fact = 1
        print(fact)
    elif n > 1:
        fact = 1
        while n != 0:
            fact = fact * n
            n = n - 1
        print(fact)
    t = t-1
