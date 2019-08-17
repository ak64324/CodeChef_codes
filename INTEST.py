n , k = (input()).split()
n = int(n)
k = int(k)
c = 0
while n > 0:
    ti = int(input())

    if ti % k == 0:
        c = c+1
    n = n-1
print(c)
