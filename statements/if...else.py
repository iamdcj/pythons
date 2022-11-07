if 1 > 2:
    print('yup')
else:
    print('no') 


# -- elif
age = 19

if age > 20:
    print('Come on in')
elif age > 17:
    print('This guest can enter but no drinks')
else:
    print("Piss off, young'un!")

# This guest can enter but no drinks



# -- within function
def returnSomething(intA, intB):
    if intA > intB:
        print(f'{intA} is greater then {intB}') 
    else:
        print(f'{intB} is greater then {intA}') 

returnSomething(3,4) # 4 is greater then 3