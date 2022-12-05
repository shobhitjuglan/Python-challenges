def odd_even(l:list):
    minodd = float('inf')
    maxeven = float('-inf')
    for i in range(len(l)):
        if l[i]%2 == 0 and l[i] > maxeven:
            maxeven = l[i]
        elif l[i]%2!=0 and l[i] < minodd:
            minodd = l[i]
        else:
            pass
    return (maxeven-minodd)



n = int(input("Type the number of elements in the list : "))
intlist = []
for i in range(n):
    intlist.append(int(input("{}, {}\n".format("Enter the element number", i+1))))
print(odd_even(intlist))
