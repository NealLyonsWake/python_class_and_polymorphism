class MyMath():

    def area_of_triangle(b,h):
        return 0.5 * b * h

    def area_of_square(l):
        return MyMath.area_of_triangle(l,l)

    def area_of_rectangle(l,b):
        return l * b


area1 = MyMath.area_of_triangle(10,5)
area2 = MyMath.area_of_square(10)
area3 = MyMath.area_of_rectangle(10,5)

print(f'{area1}{area2}{area3}')