def smallify_list(l:list):
        tuples = []
        for k in range(len(l)):
                if l[k].lower() == l[k]:
                        tuples.append(l[k])
                else:
                        pass
        return tuple(tuples)
                        

a = int(input("Enter the number of items in the tuple\n"))
old_list = []
for i in range(a):
        i = i+1
        old_list.append(input("{} {} {}\n".format("Enter the",i,"th value in the list")))

print(smallify_list(old_list))