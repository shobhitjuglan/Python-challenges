import math

def divide_or_square(num):
    if (num-5*(int(num/5))) == 0 :
        print(math.sqrt(num))
    else : 
        print(num-5*(int(num/5)))

print("Type a number")

a = int(input())

divide_or_square(a)




