### If Else Statements 

# here in python the progra runs line by line and the logic that we want to execute tat can br go by branches like if
# or else . so let see

# Example : You want to login from the user It  have two possibilities either the user enter the Right Credential
# so he will login otherwise he can't . sofor this you have to write the if else statements.


# here lets make a dummpy login for user and the senerio will be if the user gives the email campusx@gmail.com and the possword
# is 1234 then login otherwise show him an error

# email = input('apna email bata :')
# password = input('apna password b bata :')

# if email == 'campusx@gmail.com' and password == '1234':
#     print('Welcome')
# else:
#     print('Wrong Credentioal')
    
    
# here suppose you give the code to your manager but the manager said that we want to improve the code
# Like if the the user gives the correct email but gives the wrong password so we have to give one more chance
# to give the password 

# so here your code have not only two branches now the code have 3 branchses and sometime it becames 100
# branches So in that case Here is elif function is used


# email = input('apna email bata :')
# password = input('apna password b bata :')

# if email == 'campusx@gmail.com' and password == '1234':
#     print('Welcome')
# elif email == 'campusx@gmail.com' and password != '1234':
#     print('Password Incorrect')
#     password = input('Password pir se bol :')
#     if password == '1234':
#         print('Finally Correct')
#     else:
#         print('still Incorrect')
# else:
#     print('Incorrect Credentioal')
    
# here in the above code we give one more chance to the user to give password

# now if the manager said one more thing to the code that if in the email if there is no @ then the code
# should automatically said that email.is wrong .


# email = input('Apna Email Bata: ')
# if '@' in email:
#     password = input('Apna Password B Bata: ')

#     if email == 'campusx@gmail.com' and password == '1234':
#         print('Welcome')
#     elif email == 'campusx@gmail.com' and password != '1234':
#         print('Password Incorrect')
#         password = input('Password pir se bol: ')
#         if password == '1234':
#             print('Finally Correct')
#         else:
#             print('Still Incorrect')
#     else:
#         print('Credentioal Incorrect')
# else:
#     print('Ghalat Email Sehi Likho')

# Practus ::

# email = input('Apna Email Bata: ')
# if '@' in email:
#     password = input('Apna Password B Bata: ')

#     if email == 'atiqk3802@gmail.com' and password == '1234':
#         print('Welcome')
#     elif email =='atiqk3802@gmail.com' and password != '1234':
#         print('Passwrod Incorrect')
#         password = input('Password Pir se bol: ')
#         if password == '1234':
#             print('Finally Correct')
#         else:
#             print('Still Wrong')
#     else:
#         print('Wrong Credentioal')
# else:
#     print('Ghalat Email Sehi Likho')


# here lets see the if else 

email = input('apna email bata :')
password = input('apna password bata :')

if email == 'atiq@gmail.com' and password=='1234':
    print('Welcome')
    
elif email == 'atiq@gmail.com' and password != 1234:
    print('Still Wrong')
    password == input('enetr password again')
    if password == 1234:
        print('Welcome agein')
    else:
        print('Now way')
else:
    print('Wrong Credintial')

