
def distance1(x1, y1, x2=0, y2=0):
    '''  Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2)
    функция возвращает расстояние между точкой (x1,y1) и (x2,y2).
    '''

    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def distance2(p1, p2=(0,0)):
    '''  Даны две точки на плоскости p1 и p2
    функция возвращает расстояние между точкой p1 и p2.
    '''

    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


print(distance1(1, 1))
print(distance2((1, 1)))

print(distance1(3, 0, 0, 4))
print(distance2((3, 0), (0,4)))

print(distance1(3, 0, y2=4))
print(distance2((3, 0), p2=(0,4)))


