def word_index(l:list):
    for i in range(len(l)):
        for j in range(i, len(l)-1):
            if l[i] == l[j]:
                return 1
            else :
                return 0


listnew = []
a = int(input("Enter number of strings"))
for i in range(a):
    listnew.append(input("{} {} ".format("Enter the string number", i)))

print(word_index(listnew))