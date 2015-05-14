from vector import Vector 
class Matrix:
	def __init__(self, *rows):
		if len(set(len(_) for _ in rows)) <= 1:
		    self.elements = [Vector(*row) for row in rows]
		else:
			raise TypeError("All rows must be the same length")


	def rows(self):
		return len(self.elements)


	def colums(self):
		return self.elements[0].size

    
	def same_dimension(self, matrix):
		return self.rows() == matrix.rows() and self.colums() == matrix.colums()


	def add_matrix(self, matrix):
		result = []
		for x, y in zip(self.elements, matrix.elements):
		    z = x + y
		    result.append(z.coordinates)
		return Matrix(*result)


	def add_number(self, number):
		result = []
		for x in self.elements:
			y = x + number
			result.append(y.coordinates)
		return Matrix(*result)


	def sub_matrix(self, matrix):
		result = []
		for x, y in zip(self.elements, matrix.elements):
		    z = x - y
		    result.append(z.coordinates)
		return Matrix(*result)


	def sub_number(self, number):
		result = []
		for x in self.elements:
			y = x - number
			result.append(y.coordinates)
		return Matrix(*result)


	def __add__(self, other):
		if type(other) is Matrix:
		    if self.same_dimension(other):
		    	return self.add_matrix(other)
		    else:
		    	raise TypeError("Can't add matrices with different dimensions")
		else:
			return self.add_number(other)


	def __iadd__(self, other):
		self = self + other
		return self


	def __sub__(self, other):
		if type(other) is Matrix:
		    if self.same_dimension(other):
		    	return self.sub_matrix(other)
		    else:
		    	raise TypeError("Can't add matrices with different dimensions")
		else:
			return self.sub_number(other)


	def __isub__(self, other):
		self = self - other
		return self


	def __getitem__(self, index):
		return self.elements[index]


	def print_matrix(self):
		for element in self.elements:
			element.print_vector()


m = Matrix([1,2,3], [4,5,6], [7,8,9])
m2 = Matrix([1,2,3], [4,5,6], [7,8,9])
m -= m2
m.print_matrix()

print (m.rows())
print (m.colums())