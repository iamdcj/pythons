from datetime import date

yearOfBirth = input("What year were you born?")

currentYear =  date.today().year

age = currentYear - int(yearOfBirth)

print(f'You are {age} years old')

if age > 30:
    print("You wrinkly motherfucker")