import string
def check(password):
    if len(password)<4:
        return 0
        up=any(char.isupper()for char in password)
        dg=any(char.isdigit()for char in password)
        if password[0]==isdigit():
            return 0
        if any(char==" /" for char in password):
            return 0
        if up and dg:
            return 1
        else:
            return 0
password=input()
print(check(password))
if check(password):
    print("1")
else:
    print("0")