def string_range(num):
    st = "0"
    for i in range(1,num):
        st = st + "."
        st = st + str(i)
        i = i+1
    return st

a = int(input("Enter a number\n"))
print(string_range(a))