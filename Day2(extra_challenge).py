def check_duplicate(l):
        count = 0
        for i in range(len(l)):
                # for j in range(len(l[i-1])):e
                for j in range(i,len(l)-1):
                        if l[i-1] == l[j]:
                                return l[i-1]
                        else :
                                pass
        return "No duplicates"                        
                

a = int(input("Enter the number of elements in the list\n"))
listofstrings = []
for i in range(a):
        listofstrings.append(input("{} {}\n".format("Enter element of list number",i+1)))
        i = i+1

returned_string = check_duplicate(listofstrings)

print(returned_string)
