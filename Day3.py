def register_check(d : dict):
        count = 0
        try:
            for keys in d :
                    if d[keys].lower() == "yes":
                            count = count + 1
        except:
               pass
        return count
                



n = int(input("Enter the number of students registered in the school\n"))
dictionary = {}
for i in range(n):
        key = input("{} {} ".format("Enter the key number", i))
        value = input("{} {} ".format("Enter the value number", i))
        dictionary.update({key:value})
        i = i+1
print("The number of students in school are "+ str(register_check(dictionary)))