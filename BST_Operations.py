a=input()
arr=[float(number) for number in a.split()]
if arr[0]%5 == 0:
    if arr[0]+0.50 <= arr[1]:
        arr[1]=arr[1]-arr[0]-0.50
print("%.2f" % arr[1])