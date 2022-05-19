
#Exercise - Github Day1-Q1
"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
 between 2000 and 3200 (both included).The numbers obtained should be printed in a 
 comma-separated sequence on a single line."""
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i, end=', ')

#Exercise - Github Day1-Q2
"""Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320"""

# def factorial(num):
#     a=1
#     for i in range(1,num+1):
#         a *= i
#     return a
# n = int(input("Enter the number - "))
# print(factorial(n))

# Factorial using reduce - method 2
# from functools import reduce
# a=1
# num = int(input("Enter the number - "))
# factorial = reduce(lambda x,a:x*a,range(1,num+1))
# print(factorial)

#Exercise - Github Day1-Q3
"""With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
 such that is an integral number between 1 and n (both included).
 and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
"""
# num = int(input("Enter the number - "))
# dict_multiply = {k:k*k for k in range(1,num+1)}
# print(dict_multiply)