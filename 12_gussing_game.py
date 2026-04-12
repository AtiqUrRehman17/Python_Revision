# GUSSING GAME IN PYTHON 
# 1. here we have covred the if else statments and also the while loop
# 2. so this game is the good implementation of both of these two
# 3. the Functionality of the program is when u run the program it will automatically pick a nmber from 1 to 100 randomly
# 4. and that number will be the jackport number the user will guss the number 
# 5. here in the game suppose the jackport number is 50 and the user give the number 20 so the program
# 6. will ask to pick number higher the user give 20 agin program ask to pick higher the user give 30 and this
# 7. process will contineu and also the program will count the number of attempts.
# 8. here first we have to understand that how the random numbers is generated :
# 9. so in python is  a madule which is called random we will use this madule
# 10. here first we have to import the madule
# import random
# # so in this madule thare are many function but the function which we need is 'randint' in which two 
# # number can given.
# jackpot = random.randint(1,100)
# # here we generate the numbers from 1 to 100 and save it into a variable
# # now we have to ask input from user
# # guess = int(input('Guess Kar: '))
# # # now here we dont know that how amny times the user can gusee so we dont know
# # # so for that we will use the while loop untill the condition is false
# # import random
# # jackpot = random.randint(1,100)

# # guess = int(input('Guess Kar : '))
# # counter = 1

# # while guess != jackpot:
# #     if guess < jackpot:
# #         print('Guess Higher')
# #     else:
# #         print('Guess Lower')
# #     guess = int(input('Guess Kar : '))
# #     counter+=1
# # print('Sahi Jawaab')
# # print('You Took',counter,'attempts')

# # NOW it works fine but we have to add one more thing that is to add how many time the user take the attempts
# # now for that we add one more varibale that first is 1 and do it increment after each the user give the guess
    
# # # here we u came out form the loop that means u guess it right but if u r in the loop it means still wrong.
# # # and if u are still wrong then it have two possibilites or u guess lower or higher
# # print('Sehi Jwab')


# # HERE IS THE RIGHT CODE ::::::;;;;;:::::::::::::::::
import random
jackpot = random.randint(1,100)

guess = int(input('Guess Kar : '))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print('Guess Higher')
    else:
        print('Guess Lower')
    guess = int(input('Guess Kar : '))
    counter+=1
print('Sahi Jawaab')
print('You Took',counter,'attempts')

# NOW it works fine but we have to add one more thing that is to add how many time the user take the attempts
# now for that we add one more varibale that first is 1 and do it increment after each the user give the guess




        