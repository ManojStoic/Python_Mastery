
#Exercise - Github Day2-Q4
"""Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program"""

# ls_str = input("Enter the list of numbers - ")
# ls = ls_str.split(",")
# ls_tuple = tuple(ls)
# print(ls)
# print(ls_tuple)

#Exercise - Github Day2-Q5
""" Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods"""

# class StringOperation():
#     def __init__(self) -> None:
#         self.str_name = ""

#     def getstring(self):
#         self.str_name = input("Enter the string : ")

#     def printstring(self):
#         print(self.str_name)

# test_obj = StringOperation()
# test_obj.getstring()
# test_obj.printstring()

#Exercise - Github Day2-Q6
"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:"""

# from math import sqrt
# C,H=50,30
# ls_input = input("Enter the list of values to : ").split(",")
# ls = []
# for D in ls_input:
#    ls.append(str(round(sqrt((2*C*int(D))/H))))
# print(",".join(ls))

#****************************** Exercise - Github Day2-Q7 *******************************************
"""Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j
Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"""

# x,y = map(int,input("Enter the two digits : ").split(","))
# ls=[]
# for i in range(x):
#     tmp=[]
#     for j in range(y):
#         tmp.append(i*j)
#     ls.append(tmp)
# print(ls)

# Exercise - Github Day2-Q8 
"""Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world 
Then, the output should be:
bag,hello,without,world"""

# ls = input("Enter the words : ").split(",")
# ls.sort()
# print(",".join(ls))

# Exercise - Github Day2-Q9 
"""Write a program that accepts sequence of lines as input and prints the lines 
after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""

# def upper_func():
#     ls=[]
#     while True:
#         s = input("Enter the line : ")
#         if not s:
#             break
#         else:
#             ls.append(s)
#             return s
# for i in map(str.upper, upper_func()):
#     print(i,end="")
