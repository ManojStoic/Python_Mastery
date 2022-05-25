# Exercise - Github Day 7 - Q20
"""Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Suppose the following input is supplied to the program:
7
Then, the output should be:
0
7
14"""

# class seven_generator:
#     def divisblebyseven(self,num):
#         ls = [x for x in range(0,num+1) if x%7==0]
#         for i in ls:
#             yield i

# obj1 = seven_generator()
# g = obj1.divisblebyseven(int(input("Enter the number : ")))
# for i in g:
#     print(i)

# Exercise - Github Day 7 - Q21
"""A robot moves in a plane starting from the original point (0,0).
 The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance
 from current position after a sequence of movement and original point. 
 If the distance is a float, then just print the nearest integer.
 Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2"""

# euclidean distance
# import math
# x,y=0,0
# while True:
#     ls = input().split()
#     if not ls:
#         break
#     if ls[0]=='UP':
#         y += int(ls[1])
#     if ls[0]=='DOWN':
#         y -= int(ls[1])
#     if ls[0]=='LEFT':
#         x += int(ls[1])
#     if ls[0]=='RIGHT':
#         x -= int(ls[1])
# print(round(math.sqrt((x**2)+(y**2))))
