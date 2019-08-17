t = int(input())
my_list = []
while t > 0:
    #my_list = []
    n = int(input())
    my_list.append(n)
    #print(my_list)
    #print(t)
    t = t - 1
len = len(my_list)
x = range(len)
for i in x-1:
    if(my_list[i] < my_list[i+1]):
        my_list[i] = my_list[i+1]

print(*my_list, sep = "\n")
