# def check_duplicate(l):
#         count = 0
#         for i in range(len(l)):
#                 for j in range(i,len(l)-1):
#                         if l[i-1] == l[j]:
#                                 return l[i-1]
#                         else :
#                                 pass
#         return "No duplicates"                        
                
def check_duplicate(l:list):
        count = 0
        for i in range(len(l)):
                for j in range(i, len(l)-1):
                        if len(l[i-1]) == len(l[j]):
                                m = len(l[j])
                                temp = 0
                                for k in range(m):
                                        if ord(l[i-1][k-1]) == ord(l[j][k-1]):
                                                temp = temp + 1
                                if m == temp:
                                        return l[i-1]
        return "No Duplicates"
                                         


a = int(input("Enter the number of elements in the list\n"))
listofstrings = []
for i in range(a):
        listofstrings.append(input("{} {}\n".format("Enter element of list number",i+1)))
        i = i+1

returned_string = check_duplicate(listofstrings)

print(returned_string)
