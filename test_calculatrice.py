import unittest
from calculatrice import additionner, soustraire, multiplier, diviser, carre, modulo, puissance


class TestCalculatrice(unittest.TestCase):

    def test_additionner(self):
        self.assertEqual(additionner(2, 3), 5)
        self.assertEqual(additionner(-1, 1), 0)
        self.assertEqual(additionner(0, 0), 0)

    def test_soustraire(self):
        self.assertEqual(soustraire(10, 4), 6)
        self.assertEqual(soustraire(0, 5), -5)
        self.assertEqual(soustraire(-3, -3), 0)

    def test_multiplier(self):
        self.assertEqual(multiplier(3, 4), 12)
        self.assertEqual(multiplier(-2, 5), -10)
        self.assertEqual(multiplier(0, 99), 0)

    def test_diviser(self):
        self.assertEqual(diviser(10, 2), 5.0)
        self.assertEqual(diviser(7, 2), 3.5)

    def test_diviser_par_zero(self):
        with self.assertRaises(ValueError):
            diviser(10, 0)

    def test_carre(self):
        self.assertEqual(carre(3), 9)
        self.assertEqual(carre(-4), 16)
        self.assertEqual(carre(0), 0)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(9, 3), 0)
        self.assertEqual(modulo(7, 2), 1)

    def test_puissance(self):
        self.assertEqual(puissance(2, 3), 8)
        self.assertEqual(puissance(5, 0), 1)
        self.assertEqual(puissance(3, 2), 9)


if __name__ == "__main__":
    unittest.main()
