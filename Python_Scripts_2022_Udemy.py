# Python commonly used scripts 2022

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

