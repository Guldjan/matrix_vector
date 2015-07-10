# matrix_vector
A python package for matrices and vectors operations.
The package implements two classes - Vector and Matrix.

  class Vector:
  # Vector#__init__(self, *args)
     Initialize a Vector object.

        Example:
        >> Vector(1, 2, 3)
        => <matrix_vector.vector.Vector object>

        Arguments:
        N numbers

  # Vector#size(self)
     Returns the size of the vector(number of coordinates).
        Example:

        >> Vector(1, 2, 3).size
        => 3

        Arguments:
        No arguments

  # Vector#__add__(self, other)
     Adds two vectors or adds a number to the elements of vector. Returns a new object.
     
     Example:
       >> Vector(1, 2, 3) + Vector(4, 5, 6)
       => Vector(5, 7, 9)
    
     Example:
       >> Vector(1, 2, 3) + 3
       => Vector(4, 5, 6)
    
     Arguments:
       vector : (Vector)
       or
       number : (Numeric)

  # Vector#__sub__(self, other)
     Substracts two vectors or substracts a number from the elements of the vector. Returns a new object.
     
     Example:
       >> Vector(1, 2, 3) - Vector(4, 5, 6)
       => Vector(-3, -3, -3)
    
     Example:
       >> Vector(1, 2, 3) - 3
       => Vector(-2, -1, 0)
    
     Arguments:
       vector : (Vector)
       or
       number : (Numeric)

  # Vector#__iadd__(self, other)
     Adds two vectors or adds a number to the elements of the vector. Changes the object.

        Example:
        >> Vector(1, 2, 3) += Vector(4, 5, 6)
        => Vector(5, 7, 9)

        Example:
        >> Vector(1, 2, 3) += 3
        => Vector(4, 5, 6)

        Arguments:
        vector : (Vector)
        or
        number : (Numeric)

  # Vector#__isub__(self, other)
     Substracts two vectors or substracts a number from the elements of the vector. Changes the object.

        Example:
        >> Vector(1, 2, 3) -= Vector(4, 5, 6)
        => Vector(-3, -3, -3)

        Example:
        >> Vector(1, 2, 3) -= 3
        => Vector(-2, -1, 0)

        Arguments:
        vector : (Vector)
        or
        number : (Numeric)

  # Vector#__getitem__(self, key)
     Access elements of the vector with [] operator

        Example:
        >> Vector(1, 2, 3)[2]
        => 3

        Arguments:
        number : (int)

  # Vector#__mul__(self, other)
     Depending on the argument either multiplies a number with the elements of the vector or finds the scalar product of two vectors.
        Example:
        >> Vector(1, 2, 3) * 2
        => Vector(2, 4, 6)

        Example(scalar product):
        >> Vector(1, 2, 3) * Vector(2, 2, 2)
        => 12

        Arguments:
        number : (Numeric)
        or
        vector : (Vector)

  # Vector#__imul__(self, other)
     Multiplies a number with the elements of the vector changing the object.

        Example:
        >> Vector(1, 2, 3) * 2
        => Vector(2, 4, 6)

        Arguments:
        number : (Numeric)

  # Vector#__xor__(self, other)
     Returns the cross product of two 3-dimension vectors. Returns new object.

        Example:
        >> Vector(1, 2, 3) ^ Vector(4, 5, 6)
        => Vector(-3, 6, -3)

        Arguments:
        vector : (Vector)

  # Vector#__ixor__(self, other)
     Returns the scalar product of two 3-dimension vectors. Changes the object.

        Example:
        >> Vector(1, 2, 3) ^ Vector(4, 5, 6)
        => Vector(-3, 6, -3)

        Arguments:
        vector : (Vector)

  # Vector#__truediv__(self, other)
      Divides the elements of the vector by a nubmer. Returns new object.

        Example:
        >> Vector(3, 9, 6) / 3
        => Vector(1, 3, 2)

        Arguments:
        number : (Numeric)

  # Vector#__itruediv__(self, other)
        Divides the elements of the vector by a nubmer. Changes the object.

        Example:
        >> Vector(3, 9, 6) / 3
        => Vector(1, 3, 2)
        
        Arguments:
        number : (Numeric)   

  # Vector#length(self)
      Returns the length of the vector.
        
        Example:
        >> Vector(1, 2, 3).length
        => 3.7416

        Arguments:
        No arguments

  # Vector#normalized(self)
      Returns the normalized vector of the vector.

        Example:
        >> Vector(1, 2, 3).normalized()
        => Vector(0.2673, 0.5345, 0.8018)

        Arguments:
        No arguments

  # Vector#normalize(self)
      Normalizes the vector. Changes the object.

        Example:
        >> Vector(1, 2, 3).normalize()
        => Vector(0.2673, 0.5345, 0.8018)

        Arguments:
        No arguments

   # Vector#round(self, number):
        Rounds the coordinates of the vector. Changes the object.

        Example:
        >> Vector(1.345, 2.438, 3.535).round(2)
        => Vector(1.34, 2.44, 3.53)

        Arguments:
        number : (int)



 class Matrix:
 # Matrix#__init__(self, *rows)
	 Initialize Matrix object.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
		=> <matrix_vector.matrix.Matrix object>

		Example:
		>> Matrix(Vector(1, 2, 3), Vector(4, 5, 6), Vector(7, 8, 9))
		=> <matrix_vector.matrix.Matrix object>

		Arguments:
		N sequences or N vectors of the same size
  
 # Matrix#rows(self)
	  Returns the number of rows of the matrix.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).rows()
		=> 3

		Arguments:
		No arguments

 # Matrix#colums(self)
	  Returns the number of colums of the matrix.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).colums()
		=> 3

		Arguments:
		No arguments

 # Matrix#get_colum(self, number)
	 Returns the n-th colum of the matrix as an object of class Vector.
		
		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).get_colum(1)
		=> Vector(2, 5, 8)

		Arguments:
		number : (int)

 # Matrix#get_row(self, number)
	 Returns the n-th row of the matrix as an object of class Vector.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).get_row(1)
		=> Vector(4, 5, 6)

		Arguments:
		number : (int)

 # Matrix#is_same_dimension(self, matrix)
	 Boolean method checkig if two matrices have the same dimensions.

		Example:
		>> Matrix([1, 2], [4, 5]).is_same_dimension(Matrix([3, 2], [6, 7]))
		=> True

		Arguments:
		matrix : (Matrix)

 # Matrix#__add__(self, other)
	 Depending on the argument either adds a number to the elements of the matrix or adds two matrices. Returns a new object.

		Example(number):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + 2
		=> Matrix([3, 4, 5], [6, 7, 8], [9, 10, 11])
		
		Example(matrix):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
		=> Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])

		Arguments:
		number : (Numeric)
		or
		matrix : (Matrix)

 # Matrix#__iadd__(self, other)
	 Depending on the argument either adds a number to the elements of the matrix or adds two matrices. Changes the object.

		Example(number):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + 2
		=> Matrix([3, 4, 5], [6, 7, 8], [9, 10, 11])

		Example(matrix):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) + Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
		=> Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])

		Arguments:
		number : (Numeric)
		or
		matrix : (Matrix)

 # Matrix#__sub__(self, other)
	 Depending on the argument either substracts a number from the elements of the matrix or substracts two matrices. Returns a new object.
		
		Example(number):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - 2
		=> Matrix([-1, 0, 1], [2, 3, 4], [5, 6, 7])

		Example(matrix):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - Matrix([1, 1, 3], [2, 5, 7], [2, 3, 4])
		=> Matrix([0, 1, 0], [2, 0, -1], [5, 5, 5])

		Arguments:
		number : (Numeric)
		or
		matrix : (Matrix)

 # Matrix#__isub__(self, other)
	 Depending on the argument either substracts a number from the elements of the matrix or substracts two matrices. Changes the object.

		Example(number):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - 2
		=> Matrix([-1, 0, 1], [2, 3, 4], [5, 6, 7])

		Example(matrix):
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) - Matrix([1, 1, 3], [2, 5, 7], [2, 3, 4])
		=> Matrix([0, 1, 0], [2, 0, -1], [5, 5, 5])

		Arguments:
		number : (Numeric)
		or
		matrix : (Matrix)

 # Matrix#__getitem__(self, index)
	 Access the elements of the matrix with the [] operator.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])[1]
		=> Vector(4, 5, 6)

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])[1][2]
		=> 6

		Arguments:
		number : (int)

 # Matrix#transposed(self)
	 Tranposes a matrix. Returns a new object.
		
		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).transposed()
		=> Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9])

		Arguments:
		No arguments

 # Matrix#transpose(self)
	 Tranposes a matrix. Changes the object.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).transpose()
		=> Matrix([1, 4, 7], [2, 5, 8], [3, 6, 9])
		Arguments:
		No arguments

 # Matrix#__mul__(self, other)
	 Depending on the argument eigher multiplies the matrix elements with a number or mlultiplies two matrices.
		
		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) * 2
		=> Matrix([2, 4, 6], [8, 10, 12], [14, 16, 18])
		
		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]) * Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
		=> Matrix([30, 36, 42], [66, 81, 96], [102, 126, 150])
		Arguments:
		number : (Numeric)
		matrix : (Matrix)

 # Matrix#minor(self, i, j)
	 Returns a matrix without the row and the colum given as arguments.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).minor(0, 1)
		=> Matrix([4, 6], [7, 9])

		Arguments:
		number1 : (int)
		number2 : (int)

 # Matrix#determinant(self)
	 Finds the determinant of a square matrix.

		Example:
		>> Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9]).determinant()
		=> 0

		Example:
		>> Matrix([1, 3, 5], [-4, 7, 1], [5, -2, 1]).determinant()
		=> -99

		Arguments:
		no arguments

 # Matrix#inversed(self)
	 Finds the inverse of a square matrix.

		Example:
		>> Matrix([3, 4], [5, 2]).inversed()
		=> Matrix([-0.1428, 0.2857], [0.3571 ,-0.2142])

		Arguments:
		no arguments

 # Matrix#round(self, number)
	 Rounds the elements of the matrix. Changes the object.

        Example:
        >> Matrix([-0.093, 0.131, 0.323], [-0.092, 0.242, 0.211], [0.272, -0.173, -0.192]).round(2)
        => Matrix([-0.09, 0.13, 0.32], [-0.09, 0.24, 0.21], [0.27, -0.17, -0.19])

        Arguments:
        number : (int)