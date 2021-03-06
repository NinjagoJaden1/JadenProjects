def is_right_triangle(a,b,c):
    '''is_right_triangle(a,b,c) -> bool
    returns True if a,b,c is a right triangle with hypotenuse c'''
    return a*a + b*b == c*c or b*b + c*c == a*a or a*a + c*c == b*b
a=int(input("Enter any positive number: "))
b=int(input("Enter any positive number: "))
c=int(input("Enter any positive number: "))
print(is_right_triangle(a,b,c))