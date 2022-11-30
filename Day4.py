def only_floats(num1, num2):
        if int(num1) != num1 and int(num2) != num2:
            return 2
        elif (int(num1) == num1 and int(num2) != num2) or (int(num1) != num1 and int(num2) == num2):
            return 1
        else:
            return 0

n1 = float(input("Type 1st number"))
n2 = float(input("Type 2nd number"))

print(only_floats(n1,n2))