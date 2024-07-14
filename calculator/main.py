def get_input():
    a=float(input("Enter the first number:"))
    b=float(input("Enter the second number:"))
    return a,b

def addn(a,b):
    c=a+b
    return c
def subn(a,b):
    c=a-b
    return c
def muln(a,b):
    c=a*b
    return c
def divn(a,b):
    c=a/b
    return c

print('WELCOME TO CALCULATOR:')
print('------------------------')

while True:
    print('Menu:')
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    n = int(input("Enter the choice(1,2,3,4):"))
    if n==1:
        a,b=get_input()
        print("The sum of the two numbers is:",addn(a,b))
    elif n==2:
        a, b = get_input()
        print("The difference of the two numbers is:",subn(a,b))
    elif n==3:
        a, b = get_input()
        print("The product of the two numbers is:", muln(a,b))
    elif n==4:
        a, b = get_input()
        print("The quotient of the two numbers is:", divn(a,b))
    else:
        print("invalid input")

    ch = input('Want to continue[y/n]:')
    if ch.lower() == 'y':
        continue
    else:
        break




