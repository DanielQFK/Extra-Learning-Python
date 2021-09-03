"""Giving 2 values to an input in one line
when we say so , we mean that we should get two numbers from the person in one line and use the numbers
To do that , we should hive 2 valuables to our input and in () we should ask for two numbers in order to our valuables with a space between numbers 
and the command [.split()] after that...

How?"""
x, y = input("Enter a two values. The first number is for Number of boys and the second number is for Number of girls : ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
"""
Output:
Enter a two values. The first number is for Number of boys and the second number is for Number of girls : 1 2
Number of boys:  1
Number of girls:  2
"""

x, y, z = input("Enter a two values. The first number is for Number of boys and the second number is for Number of girls and the third number is for teachers : ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print("Number of teachers: ", z)
"""
output:
Enter a two values. The first number is for Number of boys and the second number is for Number of girls and the third number is for teachers : 1 2 3
Number of boys:  1
Number of girls:  2
Number of teachers:  3

and ..."""
"""
In this program we want to ask for three classes' number of students to add them for a school trip(I love school trip but It's COVID19 quarentine and I'm leaving
school ≧°◡°≦) """
a, b, c = input("Enter the three classes' number of students : ").split()
a = int(a)
b = int(b)
c = int(c)
Sum = a+b+c
print(f"The sum of students' number is {Sum} .")
"""
output:
Enter the three classes' number of students : 12 13 14
The sum of students' number is 39 ."""

a, b = [int(x) for x in input("Enter two numbers > ").split()]
print(f"The firs number is {a} .")
print(f"The second number is {b} .")
"""
output:
Enter two numbers > 1 2
The firs number is 1 .
The second number is 2 .
"""

a, b, c = [int(z) for z in input("Enter three numbers > ").split()]
print("The first number is {} and the second is {} and the last one is {} .".format(a, b, c))
"""
output:
Enter three numbers > 1 2 3
The first number is 1 and the second is 2 and the last one is 3 .
"""

# And the best one (I think) is:
x = [int(x) for x in input("Enter your numbers with a comma between them > ").split(",")]
print("Your numbers are : " , x)
"""
output:
Enter your numbers with a comma between them > 1,2,3,4,5,6,7,8
Your numbers are :  [1, 2, 3, 4, 5, 6, 7, 8]
"""