import math

def prime_numbers(num):
    prime_list = []
    for i in range(2,num):
        issqrt = 0
        for m in range(2,int(math.sqrt(i+2))+1):#+2 to prevent exception in 2's case
            if float(i)/float(m) != 1 and i%m == 0:
                issqrt = issqrt + 1
        if issqrt == 0:
            prime_list.append(i)
    return prime_list




print(prime_numbers(int(input("Enter the number under which you want to see all the prime numbers : "))))


