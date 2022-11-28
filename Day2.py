def convert_add(l : list):
        sum = 0
        i = 0
        while(True):
                try:        
                        sum = sum + int(l[i])
                        i = i+1
                except:
                        break 
        return sum       

listofstring = []
a = int(input("Type the number of elements in the list"))
for i in range(a) : 
        listofstring.append(input("{} {} = ".format("Enter the string number",i)))
print(convert_add(listofstring))