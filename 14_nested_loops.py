## Nested Loops :
# Nested Loops Means USing Anther loop inside loop means using more loops inside a loop\
# Here First we will understnad that when to use the nested loop\
# ANd then How we can use the nested loop


# here we will that how the nested loops is worked
# here we will write a program in which we will take input frm the user and if the
# user give the number 10 the 10 time * will be printed as mush input that much *
# here if 10 rows given then 10 * will be printed in the row

rows = int(input('Enter the Number of Rows: '))
for i in range(1,rows + 1):
    for j in range(0,i):
        print('*',end=' ')
    else:
        print('')


# here lets understnd the loop 
# first we take number of rows from the user that how many rows he wants to print 
# then we declare that the loop will start from 1 to rows + 1 means it will strat from 1 and if the user
# wants 5 row so it will run from 1 to 6 means 5 times

# the second loop is that print the * depneds on the user input number of rows 