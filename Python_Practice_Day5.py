# Exercise - Github Day 5 - Q16
"""Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. 
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81"""

# input_list = input("Enter the list of numbers : ").split(",")
# for i in input_list:
#     out_list = [str(int(x)**2) for x in input_list if int(x)%2!=0]
# print(",".join(out_list))

# Exercise - Github Day 5 - Q16
"""Write a program that computes the net amount of a bank account 
based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

# total = 0
# while True:
#     input_str = input().split()
#     if not input_str:
#         break
#     if input_str[0] == 'D':
#         total += int(input_str[1])
#     elif input_str[0] == 'W':
#         total = total - int(input_str[1])
#     else:
#         print("no valid transaction")
# print(total)