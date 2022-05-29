## Exercise - Github Day 11 - Q38
"""With a given tuple (1,2,3,4,5,6,7,8,9,10),
 write a program to print the first half values in one line and the last half values in one line."""

# print(tuple(range(1,11)[:5]),'\n',tuple(range(1,11)[-5:]))

## Exercise - Github Day 11 - Q39
"""Write a program to generate and print another
 tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)."""

# print(tuple([i for i in range(1,11) if i%2==0]))

## Exercise - Github Day 11 - Q40
"""Write a program which accepts a string as input to print "Yes" 
if the string is "yes" or "YES" or "Yes", otherwise print "No"."""

# if input() in ['yes','YES','Yes']:print("Yes") 
# else:print("No")

## Exercise - Github Day 11 - Q41
"""Write a program which can map() to make a list whose
 elements are square of elements in [1,2,3,4,5,6,7,8,9,10]."""

# print(list(map(lambda x:x**2, range(1,11))))

## Exercise - Github Day 11 - Q42
"""Write a program which can map() and filter() to make a list
 whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]."""

# print(list(map(lambda x:x**2,filter(lambda i:i%2==0,range(1,11)))))

## Exercise - Github Day 11 - Q43
"""Write a program which can filter() to make a list whose elements
 are even number between 1 and 20 (both included)."""

# print(list(filter(lambda x:x%2==0, range(1,21))))