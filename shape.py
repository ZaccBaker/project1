import math
#Perimeter
def p_square(side) -> float:
    if side < 0:
        raise TypeError
    return 4 * side

def p_rectangle(length,width) -> float:
    if length < 0 or width < 0:
        raise TypeError
    return 2 * (length + width)

def p_triangle(a,b,c) -> float:
    if a < 0 or b < 0 or c < 0:
        raise TypeError
    return a + b + c

def p_circle(radius) -> float:
    if radius < 0:
        raise TypeError
    return 2 * (math.pi * radius)

#Area
def a_square(side) -> float:
    if side < 0:
        raise TypeError
    return side ** 2

def a_rectangle(length,width) -> float:
    if length < 0 or width < 0:
        raise TypeError
    return length * width

def a_triangle(base,height) -> float:
    if base < 0 or height < 0:
        raise TypeError
    return (base * height) / 2

def a_circle(radius) -> float:
    if radius < 0:
        raise TypeError
    return math.pi * (radius ** 2)

#Volume
def v_square(side) -> float:
    if side < 0:
        raise TypeError
    return side ** 3

def v_rectangle(length,width,height) -> float:
    if length < 0 or width < 0 or height < 0:
        raise TypeError
    return length*width*height

def v_triangle(base,height,length) -> float:
    if base < 0 or height < 0 or length < 0:
        raise TypeError
    return (base * height * length) / 2

def v_circle(radius) -> float:
    if radius < 0:
        raise TypeError
    return (4/3) * (math.pi * (radius ** 3))
