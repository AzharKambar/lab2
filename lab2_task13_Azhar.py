#код в котором может возникнуть исключение помещено в try
try:
    #вводим стороны треугольника
    a=int(input())
    b=int(input())
    c=int(input())
    #задаем условие чтобы определить какой треугольник
    #для разностороннего
    if a == b == c:
        print('Equilateral')
    elif a != b != c and a != c != b:
        print('Versatile')
    else:
        print('Isosceles')
except ValueError:
    print('Input is not correct')