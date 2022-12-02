names = []
dict_s = {}
n = int(input("Type the number of names in the list\n"))
for k in range(n):
    names.append(input("Enter the name\n"))
print(names[0][0])
for i in range(n):
    if (names[i][0]).lower() == "s":
        count = 1
        for m in dict_s:
            if names[i] == m:
               count = count+dict_s[m]
        dict_s.update({names[i]:count})
print(dict_s) 
