## Exercise - Github Day 9 - Q26
"""Define a function which can compute the sum of two numbers"""

# #using normal function
# def sum2num(num1,num2):
#     return num1+num2
# print(sum2num(5,5))

# # using lambda function
# sum = lambda x,y : x+y 
# print(sum(1,2))

## Exercise - Github Day 9 - Q27
"""Define a function that can convert a integer into a string and print it in console."""

# conv = lambda x: print(str(x))
# conv(2)

## Exercise - Github Day 9 - Q28
"""Define a function that can receive two integer numbers in string form and compute their sum and then print it in console."""

# convsum = lambda x,y: int(x)+int(y)
# print(convsum('2','5'))

## Exercise - Github Day 9 - Q29
"""Define a function that can accept two strings as input and concatenate them and then print it in console."""

# convstrsum = lambda x,y: str(x)+str(y)
# print(convstrsum('Manoj','Kumar'))

## Exercise - Github Day 9 - Q30
"""Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line."""

# def strlen(*args,**kwargs):
#     if len(args[0])>len(args[1]):
#         return args[0]
#     elif len(args[0])<len(args[1]):
#         return args[1]
#     else:
#         return list(args)

# val = strlen("Man","Ramk")
# if type(val)==list:
#     for i in val: print(i)
# else:
#     print(val)

#using Lambda function
# func = lambda x,y: print(max([x,y],key=len)) if len(x)!=len(y) else print(x+'\n'+y)
# func("Mano","Kum")