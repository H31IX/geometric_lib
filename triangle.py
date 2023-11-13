def area(a, h):
    '''
    Принимает значение 2 переменных (сторона фигуры(треугольника) и высота фигуры(треугольника)) и выводит площадь фигуры(треугольника)
            Параметры: a(int/float) - десятичное число
                       h(int/float) - десятичное число
            Возвращаемое значение: area(int/float): десятичное число(площадь фигуры(треугольника))
            Пример вызова: print(area(3, 5)) -> 7.5
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает значение 3 переменных (сторона фигуры(треугольника) и высота фигуры(треугольника)) и выводит периметр фигуры(треугольника)
            Параметры: a(int/float) - десятичное число
                       b(int/float) - десятичное число
                       c(int/float) - десятичное число
            Возвращаемое значение: perimeter(int/float): десятичное число(периметр фигуры(треугольника))
            Пример вызова: print(perimeter(3, 4, 5)) -> 12
    '''
    return a + b + c
