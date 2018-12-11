correct_password = 'python123'
name = input('Enter name: ')
surname = input('Enter your surname: ')
password = input('Enter password: ')

while correct_password != password:
    password = input('Provide correct password !')

message ='Hi %s %s, you logged in.' % (name, surname)
print(message)