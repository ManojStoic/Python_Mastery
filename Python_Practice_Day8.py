# Exercise - Github Day 8 - Q22
"""Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1"""

# from collections import Counter
# ls = input().split()
# ls = sorted(ls)
# x=Counter(ls)
# for key,value in x.items():
#     print(key,":",value)
# # for i in x:
# #     print(i,":",x[i])

# Exercise - Github Day 8 - Q23
"""Write a method which can calculate square value of number"""

# def SquareNo(num):
#     return num**2
# print(SquareNo(int(input("Enter the numbber : "))))

# Exercise - Github Day 8 - Q24
"""Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
 But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function"""

# import random,math
# print(random.__doc__)
# print(math.__doc__)

# def SquareNo(num):
#     """Function to return the square of the number"""
#     return num**2
# print(SquareNo.__doc__)

# Exercise - Github Day 8 - Q25
"""Define a class, which have a class parameter and have a same instance parameter."""

# class test:
#     num = 5 #class object variables(parameters orattributes)
#     def __init__(self,num):
#         self.num=num #instance variables(parameters or attributes)

# obj = test(1)
# print(f"This is instance parameter call : {obj.num}")
# print(f"This is class parameter call : {test.num}")
