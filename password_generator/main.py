import random
import string
while True:
    n=int(input("Enter the length of the passsword:"))
    print("Select what to include:")
    print("1.uppercase letters")
    print("2.lowercase letters")
    print('3.numbers')
    print('4.special characters')
    choice=input('Enter the choices with space:')

    lower_case=string.ascii_lowercase
    upper_case=string.ascii_uppercase
    number=string.digits
    spl=string.punctuation

    passwd_list=""
    if "1" in choice:
        passwd_list+=upper_case
    if '2' in choice:
        passwd_list+=lower_case
    if '3' in choice:
        passwd_list+=number
    if '4' in choice:
        passwd_list+=spl
    else:
        print('Please enter valid choice')

    passwd="".join(random.sample(passwd_list,n))
    print(passwd)
    ch=input('Want to continur[y/n]:')
    if ch.lower()=='y':
        continue
    else:
        break

