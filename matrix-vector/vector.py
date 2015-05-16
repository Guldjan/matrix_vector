class DifferentDimensionVectors(BaseException):
	pass


class Vector:
    def __init__(self, *args):
        self.coordinates = list(args)

    @property
    def size(self):
        return len(self.coordinates)


    def __add__(self, other):
        if type(other) is Vector:
            if other.size == self.size:
                return Vector(*[x + y for x, y in
                                zip(self.coordinates, other.coordinates)])
            else:
                raise DifferentDimensionVectors
        else:
            return Vector(*[x + other for x in self.coordinates])
    

    def __sub__(self, other):
        if type(other) is Vector:
            if other.size == self.size:
                return Vector(*[x - y for x, y in
                                zip(self.coordinates, other.coordinates)])
            else:
                raise DifferentDimensionVectors
        else:
            return Vector(*[_ - other for _ in self.coordinates])


    def __iadd__(self, other):
        self = self + other
        return self


    def __isub__(self, other):
        self = self - other
        return self


    def __getitem__(self, key):
    	return self.coordinates[key]


    def __mul__(self, other):
        if type(other) is Vector:
            if other.size == self.size:
                return sum(x * y for x, y in
                               zip(self.coordinates, other.coordinates))
            else:
                raise DifferentDimensionVectors("Can't multipy vectors with different dimensions")
        else:
            return Vector(*[_ * other for _ in self.coordinates])


    def __imul__(self, other):
    	if type(self * other) is Vector:
    		self = self * other
    		return self
    	else:
    		raise TypeError("Can't assign number to Vector class object")


    def __xor__(self, other):
        if self.size == other.size == 3:
            coordinate_x = self[1] * other[2] - self[2] * other[1]
            coordinate_y = self[2] * other[0] - self[0] * other[2]
            coordinate_z = self[0] * other[1] - self[1] * other[0]
            return Vector(coordinate_x, coordinate_y, coordinate_z)
        else:
        	raise TypeError("Vector product only defined for 3 dimensional vectors")
    

    def __truediv__(self, other):
    	try:
    	    return Vector(*[ _ / other for _ in self.coordinates])
    	except ZeroDivisionError:
    		raise


    def __itruediv__(self, other):
    	self = self / other
    	return self


    def __ixor__(self, other):
    	self = self ^ other
    	return self


    @property
    def lenght(self):
    	return sum(_ ** 2 for _ in self.coordinates) ** 0.5


    def normalized(self):
    	return self / self.lenght


    def normalize(self):
    	self = self.normalized()
    	return self


    def print_vector(self):
    	for _ in self.coordinates:
    		print(_, end=' ')
    	print()





