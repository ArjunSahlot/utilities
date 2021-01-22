from math import atan
from numpy import cross


class Vector:
    """
    A vector class which has many useful vector methods.
    """
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
    
    def get_dir(self):
        return atan(self.y / self.x)
    
    def get_angle(self):
        return self.get_dir()
    
    def copy(self):
        return Vector(self.x, self.y)

    def get_mag(self):
        return self.get_magsq() ** 0.5

    def get_magsq(self):
        return self.x ** 2 + self.y ** 2
    
    def normalize(self):
        self.set_mag(1)
    
    def rem(self, vec):
        if isinstance(vec, Vector):
            self.x %= vec.x
            self.y %= vec.y
    
    def dist(self, vec):
        if isinstance(vec, Vector):
            return ((vec.y - self.y) ** 2 + (vec.x - self.x) ** 2) ** 0.5
    
    def limit(self, min_val=None, max_val=None):
        if min_val is not None:
            self.x = max(min_val, self.x)
            self.y = max(min_val, self.y)
        if max_val is not None:
            self.x = min(max_val, self.x)
            self.y = min(max_val, self.y)

    def get_list(self):
        return [self.x, self.y]
    
    def get_array(self):
        return self.get_list()
    
    def set_mag(self, mag):
        ratio = mag / self.get_mag()
        self.mult(ratio)

    def add(self, vec):
        if isinstance(vec, Vector):
            self.x += vec.x
            self.y += vec.y
        
    def sub(self, vec):
        if isinstance(vec, Vector):
            self.x -= vec.x
            self.y -= vec.y
        
    def div(self, scalar, floor=False):
        if isinstance(scalar, int) or isinstance(scalar, float):
            if floor:
                self.x //= scalar
                self.y //= scalar
            else:
                self.x /= scalar
                self.y /= scalar

    def mult(self, val):
        if isinstance(val, int) or isinstance(val, float):
            self.x *= val
            self.y *= val
        
    def dot(self, vec):
        if isinstance(vec, Vector):
            return self * vec
        
    def cross(self, vec):
        if isinstance(vec, Vector):
            return cross(self.get_list(), vec.get_list())

    def __add__(self, vec):
        if isinstance(vec, Vector):
            return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        if isinstance(vec, Vector):
            return Vector(self.x - vec.x, self.y - vec.y)

    def __truediv__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x // scalar, self.y // scalar)

    def __mul__(self, val):
        if isinstance(val, Vector):
            return self.x * val.x + self.y * val.y
        elif isinstance(val, int) or isinstance(val, float):
            return Vector(self.x * val, self.y * val)

    def __eq__(self, vec):
        if isinstance(vec, Vector):
            return vec.x == self.x and vec.y == self.y

    def __ne__(self, vec):
        if isinstance(vec, Vector):
            return vec.x != self.x and vec.y != self.y

    def __repr__(self):
        return f"Vector at ({self.x}, {self.y})"
