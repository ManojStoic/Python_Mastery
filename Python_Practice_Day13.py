## Exercise - Github Day 13 - Q47
"""Define a class named Circle which can be constructed by a radius. 
The Circle class has a method which can compute the area."""

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14*self.radius**2

# obj = Circle(2)
# print(obj.area())

## Exercise - Github Day 13 - Q48
"""Define a class named Rectangle which can be constructed by a length and width.
 The Rectangle class has a method which can compute the area"""

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length*self.breadth

# obj = Rectangle(2,3)
# print(obj.area())

## Exercise - Github Day 13 - Q49
"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
 Both classes have a area function which can print the area of the shape where Shape's area is 0 by default."""

# class Shape:
#     def __init__(self,ln=0) -> None:
#         self.ln = ln
    
#     def area(self) -> int:
#         return self.ln*2

    
# class Square(Shape):
#     def __init__(self,length,ln) -> None:
#         super().__init__(self) #To use parent class init attributes
#         self.length=length
#         self.ln=ln

#     def area(self) -> int:
#         return self.length*2

# obj = Square(4,5)
# print(obj.area())
# print(obj.length)
# print(obj.ln)
# print(Shape().area())

## Exercise - Github Day 13 - Q50
"""Please raise a RuntimeError exception."""

# raise TypeError("Test")

