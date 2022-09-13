class Point:
    color = 'red'
    circle = 2

    def set_coords():
        print('method call set_coords')


print(Point.set_coords)

Point.set_coords()

pt = Point()

pt.set_coords()