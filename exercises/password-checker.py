
userName = input("Enter your username: ")
password = input("Enter password: ")

passwordLength = len(password)

if passwordLength < 5:
    print("Password too short")
else:
    starredPassword = '*' * passwordLength
    print(f'{userName}, your password {starredPassword} is {passwordLength} characters in length.')
