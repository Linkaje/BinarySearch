ls = [1,3,2,4,5,6,9,8,7,10]
ls.sort()
first = 0
last = len(ls) - 1
mid = (first+last) // 2
item = int(input("Enter the number to be searched: "))
found = False
while (first <= last and not found):
    mid = (first + last) // 2
    if ls[mid] == item:
        print(f"Found at location {mid}")
        found = True
    else:
        if item < ls[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found == False:
    print("Number not found")