def zeroed(l):
    count = 0
    l[count] = 0
    try:
        while(True):
            l[count + 1]
            count = count + 1
    except:
        l[count] = 0
    return l
        

n = int(input("Enter the number of elements in the list : \n"))
temp_list = []
for i in range(n):
    temp_list.append(int(input("{} {} ".format("Enter the element number", i))))
print(zeroed(temp_list))