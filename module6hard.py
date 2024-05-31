
class Figure:

    def __init__(self, name: object, sides: object, color: object) -> object:
        self.name = name
        self.sides = sides
        self.color = color

    def get_color(self, color):
        self.r = color[0]
        self.g = color[1]
        self.b = color[2]
        print('get_color, color = ',color,'; ','get_color  RGB:   ','r=', self.r, 'g=', self.g, 'b=', self.b)
        return(self.r,self.g,self.b)

    def is_valid_color(self):
#        print('is_valid_color input RGB: ', 'r=', self.r, 'g=', self.g, 'b=', self.b)
        if (0 >= self.r or self.r >= 255) or (0 >= self.g or self.g >= 255) or (0 >= self.b or self.b >= 255):
            self.r = self._color[0]
            self.g = self._color[1]
            self.b = self._color[2]
        print('is_valid_color - RGB: ', 'r=', self.r, 'g=', self.g, 'b=', self.b)
        return(self.r,self.g,self.b)

    def set_color(self):
#        print('set_color - RGB: ','r=', self.r, 'g=', self.g, 'b=', self.b)
        self.color = (self.r, self.g, self.b)
        print('set_color, - color = ',self.color,';','set_color - RGB: ','r=', self.r, 'g=', self.g, 'b=', self.b)
        return (self.color)

    def set_sides(self):
        print('get sides = ',self.sides,';','get sides_count = ', self.sides_count,';','len self.sides = ',len(self.sides))
    #    print('----------------------')
        if (len(self.sides)) != self.sides_count:
            self.sides=[]
            for i in range (0,self.sides_count):
                self.sides.append(1)
        print('self.sides  out = ',self.sides)
        return(self.sides)


class Circle(Figure):
    _color = (200,200,100)
    sides_count = 1
    pi = 3.1415926
    __radius = sides_count / (2*pi)

    def __init__(self):
       super().__init__(self, sides, color=color)

    def radius(self):
        pi = 3.1415926
        radius = round((sides[0]) / (2 * pi), 3)
        print('радиус окружности = ',radius)
        return(radius)

    def get_square(self):
        pi = 3.1415926
        square_ = round((sides[0]**2)/(4*pi),3)
        print('площадь  круга = ',square_)
        return(square_)


print('================== class Circle(Figure) ================== ')
print('--------- my_circle -------------')
color = (123,234,112)
sides = [3,5,7,9,11]

my_circle = Circle()
my_circle.set_sides()
my_circle.radius()
my_circle.get_square()
print('----------------------------------------------------------------------')


my_circle.get_color(color)
my_circle.is_valid_color()
my_circle.set_color()
print('==================================================================')

print('--------- my_circle1 -------------')
color = (111,222,333)
sides = [26]

my_circle1 = Circle()

my_circle1.set_sides()
my_circle1.radius()
my_circle1.get_square()
print('----------------------------------------------------------------------')

my_circle1.get_color(color)
my_circle1.is_valid_color()
my_circle1.set_color()
print('==================================================================')

print()
print('================== class Triangle(Figure) ================== ')
class Triangle(Figure):
    _color = (200, 200, 100)
    sides_count = 3

    def __init__(self):
        super().__init__(self, sides, color=self._color)

    def get_height(self):
        print('get sides = ', self.sides)
        p_ = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        # print('полупериметр = ',p_)
        height = 2 * ((p_ * (p_ - self.sides[0]) * (p_ - self.sides[1]) * (p_ - self.sides[2])) ** 0.5) / (max(self.sides))
        height = round(height, 3)
        print('height  over the  max triangle side  = ', height)
        return(height)

    def get_square(self,height):
        square = round((height * max(self.sides) / 2), 3)
#        print('square = ', square)
        return(square)


sides = [5,7,9]

my_triangle = Triangle()
height = my_triangle.get_height()
print('-----------------------------------------------------------------')
print('Площадь треугольника со сторонами ',sides, ' = ', my_triangle.get_square(height))
print()
print('==================================================================')
print(' + Проверка  на  количество переданных  сторон')
sides = [5,7,9,8,6]

my_triangle = Triangle()

sides = my_triangle.set_sides()
print(sides)

height = my_triangle.get_height()
print(height)
print('------------------')
print('Площадь треугольника со сторонами ',sides, ' = ', my_triangle.get_square(height))

print('-----------------------------------------------------------------')

# ***************************************************************************************
print()
print('================== class Cube(Figure) ================== ')

class Cube(Figure):
    _color = (200, 200, 100)
    sides_count = 12

    def __init__(self):
       super().__init__(self, sides, color=self._color)

    def get_volume(self):
#        print('get sides = ', self.sides)
        volume = self.sides[0] ** 3
#        print('volume of cube  = ', volume)
        return(volume)

    def set_cube_sides(self):
        x = self.sides[0]
        sides = self.set_sides()
#        print(sides)
        for i in range(0,12):
            sides[i] = sides[i]*x
#        print(sides)
        return(sides)

sides = [14,6,9]

my_cube = Cube()
print('------------------------------------------------------------------------------')
sides = my_cube.set_cube_sides()
print(sides)
print('------------------------------------------------------------------------------')
print('Объем куба со  стороной ',sides[0], ' = ', my_cube.get_volume())
print('------------------------------------------------------------------------------')