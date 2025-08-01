# Here There are Two Types Of Type Convertion 
#  1 -  Impicit 
#  2 - Explicit 

# 1- Implicit : impicit type convertion is that type of convertion which is done automatically by python 
# you dont need to convert the datatype by self


# 2 - Explict : it is that type of convertion that as proggramer u tell the python to convert the datatype
# from this to that.


# 1 - Impicit Type Convertion Example : 

# print(4 + 5.5)
# so here the python is intalligent enough that how to perform the question
# here we give to different datatypes values and it automatically added by the python 


# 2 - Explicit Example : 

# first_num = input('Enter first Num : ')
# second_num = input('Enter Second Num : ')

# result = first_num + second_num
# print(result)

# so here python concatenate the values rather then addition
# so for thier addition we progarammer tell to python to canvert the datatype form this to that

first_num = int(input('Enter first Num : '))
second_num = int(input('Enter Second Num : '))

result = first_num + second_num
print(result)
# now the python will add the values rather than concatenate
# here the int function will convert any data type to integer like if we give float number then it will be
# converted to integer