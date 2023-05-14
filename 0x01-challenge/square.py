#!/usr/bin/python3

class square():

    width = 0
    height = 0


    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
'''
    def validate(self, name, value):
        """ Validation of the input values to the rectangle class"""
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if name in ['width', 'height']:
            if value <= 0:
                raise ValueError(f'{name} must be > 0')
            else:
                return value
'''

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
