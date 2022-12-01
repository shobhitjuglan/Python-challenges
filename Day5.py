def my_discount():
    p = int(input("enter the price"))
    d = int(input("enter the discount"))
    return p*(1-d/100)

print(my_discount())


