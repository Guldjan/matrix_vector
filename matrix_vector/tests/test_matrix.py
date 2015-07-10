from unittest import TestCase
import matrix_vector as m


class TestMatrix(TestCase):
    def test_rows(self):
        self.assertEqual(m.Matrix([1, 2, 3],
                                  [5, 6, 7],
                                  [8, 9, 10]).rows(), 3)

    def test_colums(self):
        self.assertEqual(m.Matrix([1, 2, 3],
                                  [5, 6, 7],
                                  [8, 9, 10]).colums(), 3)

    def test_get_row(self):
        a = m.Matrix([1, 2, 3],
                     [5, 6, 7],
                     [8, 9, 10])
        self.assertEqual(a.get_row(1), m.Vector(5, 6, 7))

    def test_get_row_out_of_range(self):
        a = m.Matrix([1, 2, 3],
                     [5, 6, 7],
                     [8, 9, 10])
        with self.assertRaises(IndexError):
            a.get_row(3)

    def test_get_colum(self):
        a = m.Matrix([1, 2, 3],
                     [5, 6, 7],
                     [8, 9, 10])
        self.assertEqual(a.get_colum(1), m.Vector(2, 6, 9))

    def test_get_colum_out_of_range(self):
        a = m.Matrix([1, 2, 3],
                     [5, 6, 7],
                     [8, 9, 10])
        with self.assertRaises(IndexError):
            a.get_colum(3)

    def test_same_dimension_true(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a2 = m.Matrix([1, -2, 3],
                      [5, 3, 7],
                      [-8, 9, 10])
        self.assertEqual(a1.is_same_dimension(a2), True)

    def test_same_dimension_false(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7])
        a2 = m.Matrix([1, -2, 3],
                      [5, 3, 7],
                      [-8, 9, 10])
        self.assertEqual(a1.is_same_dimension(a2), False)

    def test_add_number(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        self.assertEqual(a1 + 2, m.Matrix([3, 4, 5],
                                          [7, 8, 9],
                                          [10, 11, 12]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [5, 6, 7],
                                      [8, 9, 10]))

    def test_add_matrix(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a2 = m.Matrix([1, -2, 3],
                      [5, 3, 7],
                      [-8, 9, 10])
        self.assertEqual(a1 + a2, m.Matrix([2, 0, 6],
                                           [10, 9, 14],
                                           [0, 18, 20]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [5, 6, 7],
                                      [8, 9, 10]))

    def test_add_different_dimension(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7])
        a2 = m.Matrix([1, -2, 3],
                      [5, 3, 7],
                      [-8, 9, 10])
        with self.assertRaises(m.matrix.MatrixDimensionError):
            a1 + a2

    def test_i_add_number(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a1 += 2
        self.assertEqual(a1, m.Matrix([3, 4, 5],
                                      [7, 8, 9],
                                      [10, 11, 12]))

    def test_i_add_matrix(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a1 += m.Matrix([1, -2, 3],
                       [5, 3, 7],
                       [-8, 9, 10])
        self.assertEqual(a1, m.Matrix([2, 0, 6],
                                      [10, 9, 14],
                                      [0, 18, 20]))

    def test_sub_number(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        self.assertEqual(a1 - 2, m.Matrix([-1, 0, 1],
                                          [3, 4, 5],
                                          [6, 7, 8]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [5, 6, 7],
                                      [8, 9, 10]))

    def test_sub_matrix(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a2 = m.Matrix([1, -2, 3],
                      [5, 3, 7],
                      [-8, 9, 10])
        self.assertEqual(a1 - a2, m.Matrix([0, 4, 0],
                                           [0, 3, 0],
                                           [16, 0, 0]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [5, 6, 7],
                                      [8, 9, 10]))

    def test_sub_different_dimension(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7])
        a2 = m.Matrix([1, -2, 3],
                      [5, 3, 7],
                      [-8, 9, 10])
        with self.assertRaises(m.matrix.MatrixDimensionError):
            a1 - a2

    def test_i_sub_number(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a1 -= 2
        self.assertEqual(a1, m.Matrix([-1, 0, 1],
                                      [3, 4, 5],
                                      [6, 7, 8]))

    def test_i_sub_matrix(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a1 -= m.Matrix([1, -2, 3],
                       [5, 3, 7],
                       [-8, 9, 10])
        self.assertEqual(a1, m.Matrix([0, 4, 0],
                                      [0, 3, 0],
                                      [16, 0, 0]))

    def test_get_item_1(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        self.assertEqual(a1[1], m.Vector(5, 6, 7))

    def test_get_item_2(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        self.assertEqual(a1[1][2], 7)

    def test_transpose(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        a1.transpose()
        self.assertEqual(a1, m.Matrix([1, 5, 8],
                                      [2, 6, 9],
                                      [3, 7, 10]))

    def test_transposed(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        self.assertEqual(a1.transposed(), m.Matrix([1, 5, 8],
                                                   [2, 6, 9],
                                                   [3, 7, 10]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [5, 6, 7],
                                      [8, 9, 10]))

    def test_multiply_number(self):
        a1 = m.Matrix([1, 2, 3],
                      [5, 6, 7],
                      [8, 9, 10])
        self.assertEqual(a1 * 2, m.Matrix([2, 4, 6],
                                          [10, 12, 14],
                                          [16, 18, 20]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [5, 6, 7],
                                      [8, 9, 10]))

    def test_multiply_matrix_1(self):
        a1 = m.Matrix([1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9])
        self.assertEqual(a1 * a1, m.Matrix([30, 36, 42],
                                           [66, 81, 96],
                                           [102, 126, 150]))

    def test_multiply_matrix_2(self):
        a1 = m.Matrix([1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9])
        a2 = m.Matrix([1, 2],
                      [3, 4],
                      [5, 6])
        self.assertEqual(a1 * a2, m.Matrix([22, 28],
                                           [49, 64],
                                           [76, 100]))
        self.assertEqual(a1, m.Matrix([1, 2, 3],
                                      [4, 5, 6],
                                      [7, 8, 9]))

    def test_multiply_matrix_unsutable(self):
        a1 = m.Matrix([1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9])
        a2 = m.Matrix([1, 2],
                      [3, 4])
        with self.assertRaises(m.matrix.MatrixDimensionError):
            a1 * a2

    def test_multiply_vector(self):
        a1 = m.Matrix([1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9])
        a2 = m.Vector(1, 2, 3)
        self.assertEqual(a1 * a2, m.Vector(14, 32, 50))

    def test_multiply_vector_unsutable(self):
        a = m.Matrix([1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9])
        v = m.Vector(1, 2, 3, 4)
        with self.assertRaises(m.matrix.MatrixDimensionError):
            a * v

    def test_minor(self):
        a = m.Matrix([1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9])
        self.assertEqual(a.minor(1, 1), m.Matrix([1, 3],
                                                 [7, 9]))

    def test_minor_out_of_range(self):
        a = m.Matrix([1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9])
        with self.assertRaises(IndexError):
            a.minor(3, 3)

    def test_determinant_1(self):
        a = m.Matrix([1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9])
        self.assertEqual(a.determinant(), 0)

    def test_determinant_2(self):
        a = m.Matrix([1, 3, 5],
                     [-4, 7, 1],
                     [5, -2, 1])
        self.assertEqual(a.determinant(), -99)

    def test_determinant_3(self):
        a = m.Matrix([5, 4, 9, -1],
                     [-2, 5, 1, 3],
                     [2, -3, 4, 1],
                     [8, 3, -3, 0])
        self.assertEqual(a.determinant(), 1943)

    def test_determinant_not_square(self):
        a = m.Matrix([1, 3], [-4, 7], [5, -2])
        with self.assertRaises(m.matrix.MatrixDimensionError):
            a.determinant()

    def test_inversed(self):
        a = m.Matrix([1, 3, 5],
                     [-4, 7, 1],
                     [5, -2, 1])
        self.assertEqual(a.inversed().round(2), m.Matrix([-0.09, 0.13, 0.32],
                                                         [-0.09, 0.24, 0.21],
                                                         [0.27, -0.17, -0.19]))
        self.assertEqual(a, m.Matrix([1, 3, 5],
                                     [-4, 7, 1],
                                     [5, -2, 1]))

    def test_inversed_zero_det(self):
        a = m.Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
        with self.assertRaises(ZeroDivisionError):
            a.inversed()

    def test_round(self):
        a = m.Matrix([-0.093, 0.131, 0.323],
                     [-0.092, 0.242, 0.211],
                     [0.272, -0.173, -0.192]).round(2)
        self.assertEqual(a.round(2), m.Matrix([-0.09, 0.13, 0.32],
                                              [-0.09, 0.24, 0.21],
                                              [0.27, -0.17, -0.19]))
