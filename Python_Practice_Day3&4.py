# Exercise - Github Day 3 - Q10
"""Write a program that accepts a sequence of whitespace separated words as input 
and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world"""


# inp = list(set(input().split()))
# inp.sort()
# for i in inp:
#     print(i,end=" ")

# Exercise - Github Day 3 - Q11
"""Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not.
 The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010"""

# # code to print values separated by whitespace
# ls = map(int, input().split(','))
# for i in filter(lambda x: x%5==0,ls):
#     print(i,end=" ")

# # code to print values separated by comma
# ls = input().split(',')
# ls = list(filter(lambda x: int(x)%5==0,ls))
# print(",".join(ls))

# Exercise - Github Day 3 - Q12
"""Write a program, which will find all such numbers between 1000 and 3000 (both included)
 such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line."""

# chr() -> converts integer to character | ord() -> converts character to integer
# ls = [str(x) for x in range(1000,3001)]
# ls = filter(lambda z:all(int(j)%2==0 for j in z),ls)
# print(",".join(ls))

# ls = [str(x) for x in range(1000,3001)]
# ls = filter(lambda z:all(ord(j)%2==0 for j in z),ls)
# print(",".join(ls))

# Exercise - Github Day 3 - Q13
"""Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3"""

# line = input().split()
# line = "".join(line)
# digits=[]
# letters=[]
# for word in line:
#     if word.isdigit():
#         digits.append(word)
#     elif word.isalpha():
#         letters.append(word)
# print(f"LETTERS : {len(letters)}")
# print(f"DIGITS : {len(digits)}")

# Exercise - Github Day 4 - Q14
"""Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"""

# line = input().split()
# line = "".join(line)
# Uppercase=0
# Lowercase=0
# for word in line:
#     if word.isupper():
#         Uppercase += 1
#     elif word.islower():
#         Lowercase += 1
# print(f"UPPER CASE {Uppercase}")
# print(f"LOWER CASE {Lowercase}")

# Exercise - Github Day 4 - Q15
"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106"""

# a = input("Enter a number : ")
# aaaa = int(a*4)
# aaa = int(a*3)
# aa = int(a*2)
# formula =  int(a)+aa+aaa+aaaa
# print(formula)