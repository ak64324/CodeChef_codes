x,y = (input()).split()
#y = float(input())
y = float(y)
ts = int(x) + 0.5
x = int(x)

if x % 5 == 0 and y >= ts:
    bal = y - ts
    print("%.2f" % (bal))

elif x % 5 != 0:
    print(y)

else :
    print(y)

