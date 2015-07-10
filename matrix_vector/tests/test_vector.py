from unittest import TestCase
import matrix_vector as m


class TestVector(TestCase):
    def test_size(self):
        self.assertEqual(m.Vector(1, 2, 3).size, 3)

    def test_add_number(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(v + 3, m.Vector(4, 5, 6))
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_add_vector(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(v + m.Vector(4, 5, 6), m.Vector(5, 7, 9))
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_add_different_dimension(self):
        with self.assertRaises(m.vector.DifferentDimensionVectors):
            m.Vector(1, 2, 3) + m.Vector(4, 5, 6, 7)

    def test_i_add_vector(self):
        v = m.Vector(1, 2, 3, 4)
        v += m.Vector(1, 2, 3, 4)
        self.assertEqual(v, m.Vector(2, 4, 6, 8))

    def test_i_add_number(self):
        v = m.Vector(1, 2, 3, 4)
        v += 2
        self.assertEqual(v, m.Vector(3, 4, 5, 6))

    def test_sub_number(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(v - 3, m.Vector(-2, -1, 0))
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_sub_vector(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(v - m.Vector(4, 5, 6), m.Vector(-3, -3, -3))
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_sub_different_dimension(self):
        with self.assertRaises(m.vector.DifferentDimensionVectors):
            m.Vector(1, 2, 3) - m.Vector(4, 5, 6, 7)

    def test_i_sub_vector(self):
        v = m.Vector(1, 2, 3, 4)
        v -= m.Vector(1, 2, 3, 4)
        self.assertEqual(v, m.Vector(0, 0, 0, 0))

    def test_i_sub_number(self):
        v = m.Vector(1, 2, 3, 4)
        v -= 2
        self.assertEqual(v, m.Vector(-1, 0, 1, 2))

    def test_get_item(self):
        v = m.Vector(3, 2, 4, 6, 8)
        self.assertEqual(v[3], 6)

    def test_get_item_out_of_range(self):
        v = m.Vector(3, 2, 4, 6, 8)
        with self.assertRaises(IndexError):
            v[6]

    def test_multipy_number(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(v * 2, m.Vector(2, 4, 6))
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_i_multiply_number(self):
        v = m.Vector(1, 2, 3)
        v *= -2
        self.assertEqual(v, m.Vector(-2, -4, -6))

    def test_scalar_product(self):
        v1 = m.Vector(2, 3, -2)
        v2 = m.Vector(-1, 2, 3)
        self.assertEqual(v1 * v2, -2)

    def test_scalar_different_dimension(self):
        with self.assertRaises(m.vector.DifferentDimensionVectors):
            m.Vector(1, 2, 3) * m.Vector(4, 5, 6, 7)

    def test_cross_product(self):
        v1 = m.Vector(1, 2, 3)
        v2 = m.Vector(4, 5, 6)
        self.assertEqual(v1 ^ v2, m.Vector(-3, 6, -3))
        self.assertEqual(v1, m.Vector(1, 2, 3))

    def test_i_cross_product(self):
        v1 = m.Vector(1, 2, 3)
        v2 = m.Vector(4, 5, 6)
        v1 ^= v2
        self.assertEqual(v1, m.Vector(-3, 6, -3))

    def test_cross_product_3d(self):
        with self.assertRaises(TypeError):
            m.Vector(1, 2, 3, 4) ^ m.Vector(3, 4, 5, 6)

    def test_number_division(self):
        v = m.Vector(2, 4, 6)
        self.assertEqual(v / 2, m.Vector(1, 2, 3))
        self.assertEqual(v, m.Vector(2, 4, 6))

    def test_i_number_division(self):
        v = m.Vector(2, 4, 6)
        v /= 2
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            m.Vector(4, 3, 2, 1) / 0

    def test_length(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(round(v.length, 4), 3.7417)

    def test_normalize(self):
        v = m.Vector(1, 2, 3)
        v.normalize()
        self.assertEqual(v.round(4), m.Vector(0.2673, 0.5345, 0.8018))

    def test_normalized(self):
        v = m.Vector(1, 2, 3)
        self.assertEqual(v.normalized().round(4),
                         m.Vector(0.2673, 0.5345, 0.8018))
        self.assertEqual(v, m.Vector(1, 2, 3))

    def test_round(self):
        v = m.Vector(1.345, 2.438, 3.535)
        v.round(2)
        self.assertEqual(v, m.Vector(1.34, 2.44, 3.54))
