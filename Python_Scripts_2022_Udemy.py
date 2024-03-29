# Python commonly used scripts 2022

#sample class file for reference
# class Generator:
#     def __init__(self, num):
#         self.num = num

#     def divisor(self):
#         print(self.num)

# object1 = Generator(20)
# print(object1.num)
# print(object1.divisor())

# #filter
# x = list(filter(lambda x:x%2==0,[1,2,3,4,5]))
# print(x)

# #map
# x = list(map(lambda x:str(x),[1,2,3,4,5]))
# print(x)

# from functools import reduce
# x = reduce(lambda x,y:x/y,[1,2,3,4,5])
# print(x)

# x = [1,2,3,4,5]
# del x[0]
# x.remove(5)
# print(x)

# ls1 =['Manoj','Kumar']
# ls1.extend(['Ramakrishnan'])
# print(ls1)

# ls =['Manoj','Kumar']
# ls.append(ls1)
# print(ls)

# #map-lambda
# for i in map(lambda i:i**3, [2,3,7]):
#     print(i)

# pop
# x =[1,2,3,4,5]
# print(x.pop(2))
# print(x)

# print(type((1,)))
# n = 10
# result = 1
# for i in range(1,n+1):
#     result *= i
# print(result) 

#list/set/dict comprehension
# my_dict = {k:k**2 for k in range(10) if k%2==0 }
# print(my_dict)

#zip - list of tuples
# list1 = [1,2,3,4,5]
# list2 = (6,7,8,4,0)
# my_list = list(zip(list1,list2))
# print(my_list)

#Excercise - Return all duplicates from a list
# Conventional code
# list_names = ['Manoj','Manoj','Adam','Peter','Rob','Kumar','Adam']
# dup_list = []
# def dup_func(ls):
#     for nm in ls:
#         if ls.count(nm) > 1:
#             if nm not in dup_list:
#                 dup_list.append(nm)
# dup_func(list_names)
# print(dup_list)

#Using Func Programming
# list_names = ['Manoj','Manoj','Adam','Peter','Rob','Kumar','Adam']
# dup_list = list(set([x for x in list_names if list_names.count(x) > 1]))
# print(dup_list)

#Decorators (@classmethod, @staticmethod are inbuilt decorators)
#performance decorator
# import time
# def performance_test(func):
#     def wrapper(*args, **kwargs):
#         t1=time.time()
#         func(*args, **kwargs)
#         t2=time.time()
#         print(f"Total time taken {t2-t1} sec")
#     return wrapper

# @performance_test
# def fib_generator(n):
#     a=0
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b

# @performance_test
# def fib_list(n):
#     a=0
#     b=1
#     ls = []
#     for i in range(n):
#         ls.append(a)
#         a,b=b,a+b
#     return ls

# fib_generator(1000)
# fib_list(1000)

#authenticated decorator
# user_dict = { 'name':'Manoj','valid':False}
# def authenticate_user(func):
#     def wrapper(*args,**kwargs):
#         if args[0]['valid'] is True:
#             func(*args,**kwargs)
#         else:
#             print("You don't have access")
#     return wrapper
# @authenticate_user
# def message_user(user_dict):
#     print(f"Hello {user_dict['name']}")
# message_user(user_dict)

#Error Handling 
# x = [1,2,3]
# counter = 0
# z=0
# while True:
#     try: 
#         y = int(input("Enter the index value - "))
#         print("Fetching the value of the index number in the list")
#         print(x[y])
#     except (ValueError, IndexError) as err:
#         print(f"Error - {err}, Try again")
#     else:
#         z=1
#         print("Thank you, Welcome back")
#         break
#     finally:
#         counter+=1
#         if z!= 1: 
#             print(f"Attempts left - {3 - counter} out of 3")
#             if counter==3:
#                 print("Account locked")
#                 break

#Raise Exception
# x = [1,2,3]
# counter = 0
# z=0
# y = int(input("Enter the index value - "))
# print("Fetching the value of the index number in the list")
# print(x[y])
# raise Exception('Hey Error is thrown')

# Generators (range is an inbuilt generator)
# def generator_func(n):
#     for i in range(n):
#         yield i
# g = generator_func(100)
# print(next(g))
# print(next(g))

#Fibonacci series - using generator
# def fib_generator(n):
#     a=0
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for i in fib_generator(21):
#     print(i)

#Python Packages

# """Recently, the Python has made Dictionaries ordered by default!
#  So unless you need to maintain older version of Python (older than 3.7), 
#  you no longer need to use ordered dict,
#   you can just use regular dictionaries!"""

#from collections import OrderedDict, Counter, defaultdict
# ls = [1,2,3,4,5]
# sentence = "This is Python tutorial"
# print(Counter(ls))
# print(Counter(sentence))
# dictionary = defaultdict(lambda: 'does not exist',{'a':1,'b':2})
# print(dictionary['e'])
# d = OrderedDict()
# d['a']= 1
# d['b']= 2
# d2 = OrderedDict()
# d2['a']= 2
# d2['b']= 1
# print(d2 == d)

# import datetime
# print(datetime.datetime(2000,2,2))
# print(datetime.date.today())

# from array import array
# arr = array('i',[1,2,3])
# print(arr[0])

#debugging tips
#linting - Allows us to detect some issues with our code
# ide/ editors
# read errors
# pdb - python debugger - allows us to interact with the code
# (pdb) - type help command/ type exit command
# import pdb
# num =1
# str = "abc"
# pdb.set_trace()
# a = 4*5
# b = 6*2
# num+str

#Sample Flask app code
# from flask import Flask
# app = Flask('app')
# @app.route('/')
# def hello_world():
#   return 'Hello, World!'
# app.run(host='0.0.0.0', port=8080)

# my_file = open('Sample.txt',)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# print(my_file.readline())
# print(my_file.readlines())
# my_file.close()

# r -> read, r+ -> readwrite, w -> write, a -> append, seek -> to bring the cursor to the start 
# with open('Sample.txt', mode='r+') as file:
#   text = file.write("Hey it's me")
#   print(text)
#   file.seek(0)
#   print(file.read())
# use pathlib for easy File I/O operations

# code to write a text into a file by checking and removing the files in a directory if present
# if not os.path.exists('.\docs'): os.mkdir('.\docs')
# else: 
#     for file in os.listdir('.\docs'):
#         os.remove(os.path.join('.\docs',file))

# with open('.\docs\sample.txt','w') as file:
#     file.seek(0)
#     file.write(soup.text)

#Python File I/O Translator exercise
# use open source lib 'translate' from PyPI
# Translates text file to German 
# from translate import Translator
# try:
#   trans = Translator(to_lang="de")
#   with open('Sample.txt',mode='r') as file:
#     txt = file.read()
#     trans_txt = trans.translate(txt)
#     print(trans_txt)
#     with open('Translate.txt',mode='w') as file:
#       file.write(trans_txt)
# except Exception as err:
#   print("Error - {0}",err)

# Regular expressions
# import re
# string = "This is a sample string"
# # print("zoo" in string)
# a = re.search("this",string)
# # print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

# import re
# pattern = re.compile('this')
# string = "this is a solid principle, part of this lesson"
# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# if a: print(a.group())
# else: print(f"a has no value")
# if b: print(b)
# else: print(f"b has no value")
# if c: print(c.group())  
# else: print(f"c has no value")
# if d: print(d.group())
# else: print(f"d has no value")

# import re
# pattern  = re.compile(r"[a-zA-Z].([l])") 
# # r stands for raw string
# string = "this is a solid principle, part of this lesson"
# a = pattern.search(string)
# if a: print(a.group())
# else: print(f"a has no value")

# import re
# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = "manojgmail.com"
# s = pattern.search(string)
# a = pattern.match(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# if s: print(s.group())
# else: print(f"s has no value")
# if a: print(a.group())
# else: print(f"a has no value")
# if b: print(b)
# else: print(f"b has no value")
# if c: print(c.group())  
# else: print(f"c has no value")
# if d: print(d.group())
# else: print(f"d has no value")

# import re
# pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# string = ""
# s = pattern.search(string)
# a = pattern.match(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# if s: print(s.group())
# else: print(f"s has no value")
# if a: print(a.group())
# else: print(f"a has no value")
# if b: print(b)
# else: print(f"b has no value")
# if c: print(c.group())  
# else: print(f"c has no value")
# if d: print(d.group())
# else: print(f"d has no value")

# password checker using Regex
# import re
# pattern = re.compile(r"[a-zA-Z0-9#@$&]{8,}\d")
# password = "suddddc$09"
# s = pattern.fullmatch(password)
# print(s)

# Unit test function samples - Test driven development
# def sum(a=0,b=0):
#   try:
#     if a and b:
#       return int(a)+int(b)
#     else:
#       return "Please return a number"
#   except ValueError as err:
#     return err

# def sub(a,b):
#   if a>b : return a-b
#   else : return b-a


#*********************************************************************************************#
# Instance vs Class vs Static methods


# class Test:
#     def instancemethod(self):
#         return "This is instance method", self

#     @classmethod
#     def classmethod(cls):
#         return "This is class method", cls

#     @staticmethod
#     def staticmethod():
#         return "This is static method"

# Accessing instance methods
# obj = Test()
# print(obj.instancemethod()) #<__main__.Test object at 0x000001DC8AFDEF10> -- object state
# print(Test.instancemethod(obj)) #<__main__.Test object at 0x000001DC8AFDEF10> --object state
# print(Test().instancemethod()) #<__main__.Test object at 0x000001DC8AFDEDF0> -- class state

# # Accessing class methods
# print(obj.classmethod()) #<class '__main__.Test'>
# print(Test.classmethod()) #<class '__main__.Test'>
# print(Test().classmethod()) #<class '__main__.Test'>

# Accessing static methods
# print(obj.staticmethod()) 
# print(Test.staticmethod()) 
# print(Test().staticmethod()) 

# Instance methods need a class instance and can access the instance through self.
# Class methods don’t need a class instance. They can’t access the instance (self) 
#   but they have access to the class itself via cls.
# Static methods don’t have access to cls or self. They work like regular functions
#   but belong to the class’s namespace.
# Static and class methods communicate and (to a certain degree) enforce developer intent
#   about class design. This can have maintenance benefits.

#*********************************************************************************************#
# creating virtual environments to manage package versions 

#Install venv to your host Python by running this command in your terminal
# pip install virtualenv

#To use venv in your project, in your terminal, create a new project folder, 
# cd to the project folder in your terminal, and run the following command
# python<version> -m venv <virtual-environment-name>
# example - python -m venv venv

#Generate a text file listing all your project dependencies by running the code below:
# pip freeze > requirements.txt

#Run the code below to install all your dependencies within their own copy of the project:
# pip install -r requirements.txt

#*********************************************************************************************#
# Doc Notes - Python Flask Framework

#     Web server - Stores and loads all static pages related to a website
#     http.server -> python lib to implement http servers(web servers)
#     Flask -> Python sync framework (analogy - micro-kitchen)
#     Django -> Python sync framework (analogy - macro-kitchen)
#     Never name a python module under Flask framework under the name  'flask.py' to avoid conflict
#     To run the application, use the flask command or python -m flask.
#     Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable.
#     > set FLASK_APP=hello
#     > flask run
#     * Running on http://127.0.0.1:5000/
#     set FLASK_ENV=development    -> to turn on debug mode
#     flask.render_template -> Renders a template from the template folder with the given context.
#     Jinja template - {{4+5}} -> Flask built in templating language to evaluate the expression as python.
#     url_for('folder','filename.ext') -> alternate Flask in built method/safer method for hardcoding the urls  (folder/filename.ext)
#     variable rules -> add variables to the url section by placing the variables within the expression <variables> and pass it
#                         to the jinga expression in html
#     Browsers use the MIME type and not the file extension to determine how to process a URL, so it's important that Web server sends
#         the correct MIME type in the response's Content-Type header (eg - text/javascript, text/html, image/png)
#     Request object - To access incoming request data from client
#     csv - module to write data to a csv file

#     pip freeze > requirements.txt -> pythonic way to automcatically list all dependent libraries/packages
#       into a txt file and use it in any machine instead of creating a new venv and downloading all packages.

#*********************************************************************************************#