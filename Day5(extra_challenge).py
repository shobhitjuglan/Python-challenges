n = int(input("Enter the number of people in the school staff\n"))
m=0
f=0

for i in range(n):
    gender = input("{} {} ".format("Enter the string number", i+1))
    if gender.lower() == "male":
        m = m+1
    else:
        f = f+1
males= ["Male",m]
females = ["female",f]
list_final = [tuple(males), tuple(females)]
print(list_final)

