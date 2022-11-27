def longest_value(dict):
    largest_val = None
    maxsize = 0
    for key in dict:
        size = 0
        try:
            for k in dict[key]:
               size+=1 
        except:
            pass
        if size>maxsize:
            maxsize = size
            largest_val = D[key]
        # print(dict[key],size) ; used for debugging the code :)
    return largest_val


a = int(input("Enter the number of objects : "))
D = {}
i=0
for i in range(a) : 
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    D.update({key : value})
print(longest_value(D))
