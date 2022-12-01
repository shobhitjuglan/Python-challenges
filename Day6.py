def user_name(str):
    username = ""
    for i in range(len(str)):
        if str[i] != "@":
            username = username +str[i]
        else:
            return username

print(user_name(input("Enter your mail id:\n")))
