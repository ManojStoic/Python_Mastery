## Exercise - Github Day 15 - Q51
"""Write a function to compute 5/0 and use try/except to catch the exceptions."""

# def div():
#     try:
#         5/0
#     except ZeroDivisionError as err:
#         print("Error" ,err)

# div()

## Exercise - Github Day 15 - Q52
"""Define a custom exception class which takes a string message as attribute."""

# class CustomException(Exception):
#     """Exception raised for custom purpose

#     Attributes:
#         message -- explanation of the error
#     """

#     def __init__(self, message):
#         self.message = message

# num = int(input())
# try:
#     if num < 10:
#         raise CustomException("Input is less than 10")
#     elif num > 10:
#         raise CustomException("Input is grater than 10")
# except CustomException as ce:
#     print("The error raised: " + ce.message)

## Exercise - Github Day 15 - Q53
"""Assuming that we have some email addresses in the "username@companyname.com" format, 
please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john"""

# email = "john@google.com"
# email = email.split('@')
# print(email[0])

# import re
# email = "john@google.com elise@python.com"
# pattern = "(\w+)@\w+.com"
# ans = re.findall(pattern,email)
# print(ans)