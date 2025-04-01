# login program and indentation
# email -> ajay.sh@gmail.com
# password -> 1234

email = input('Enter email: ')
password = input('Enter Password: ')
if email == 'ajay.sh@gmail.com' and password == '1234':
    print('Welcome')
elif email == 'ajay.sh@gmail.com' and password != '1234' :
    print('Incorrect Password')
    password = input("Password Enter Again: ")
    if password == '1234' :
        print('Welcome !')
    else : 
        print('Beta tumse na ho Paayega !')
else :
    print('Not Correct')