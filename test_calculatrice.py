import unittest
from calculatrice import additionner, soustraire, multiplier, diviser, carre, modulo, puissance


class TestAdditionner(unittest.TestCase):

    # Cas nominaux
    def test_deux_positifs(self):
        self.assertEqual(additionner(2, 3), 5)

    def test_positif_et_negatif(self):
        self.assertEqual(additionner(10, -3), 7)

    # Cas à la marge
    def test_deux_zeros(self):
        self.assertEqual(additionner(0, 0), 0)

    def test_avec_zero(self):
        self.assertEqual(additionner(5, 0), 5)

    def test_deux_negatifs(self):
        self.assertEqual(additionner(-4, -6), -10)

    def test_grands_nombres(self):
        self.assertEqual(additionner(10**9, 10**9), 2 * 10**9)

    # Cas d'erreur
    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            additionner("a", 1)


class TestSoustraire(unittest.TestCase):

    # Cas nominaux
    def test_positif_moins_positif(self):
        self.assertEqual(soustraire(10, 4), 6)

    def test_resultat_negatif(self):
        self.assertEqual(soustraire(3, 7), -4)

    # Cas à la marge
    def test_meme_nombre(self):
        self.assertEqual(soustraire(5, 5), 0)

    def test_avec_zero(self):
        self.assertEqual(soustraire(0, 0), 0)

    def test_deux_negatifs(self):
        self.assertEqual(soustraire(-3, -3), 0)

    def test_grands_nombres(self):
        self.assertEqual(soustraire(10**9, 10**9), 0)

    # Cas d'erreur
    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            soustraire("a", 1)


class TestMultiplier(unittest.TestCase):

    # Cas nominaux
    def test_deux_positifs(self):
        self.assertEqual(multiplier(3, 4), 12)

    def test_negatif_et_positif(self):
        self.assertEqual(multiplier(-2, 5), -10)

    # Cas à la marge
    def test_par_zero(self):
        self.assertEqual(multiplier(99, 0), 0)

    def test_par_un(self):
        self.assertEqual(multiplier(7, 1), 7)

    def test_deux_negatifs(self):
        self.assertEqual(multiplier(-3, -3), 9)

    def test_grands_nombres(self):
        self.assertEqual(multiplier(10**6, 10**6), 10**12)

    # Cas d'erreur
    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            multiplier("a", "b")


class TestDiviser(unittest.TestCase):

    # Cas nominaux
    def test_division_entiere(self):
        self.assertEqual(diviser(10, 2), 5.0)

    def test_division_decimale(self):
        self.assertEqual(diviser(7, 2), 3.5)

    def test_negatif_sur_positif(self):
        self.assertEqual(diviser(-9, 3), -3.0)

    # Cas à la marge
    def test_zero_sur_nombre(self):
        self.assertEqual(diviser(0, 5), 0.0)

    def test_nombre_sur_lui_meme(self):
        self.assertEqual(diviser(7, 7), 1.0)

    def test_grands_nombres(self):
        self.assertEqual(diviser(10**9, 10**3), 10**6)

    # Cas d'erreur
    def test_division_par_zero(self):
        with self.assertRaises(ValueError):
            diviser(10, 0)

    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            diviser("a", 2)


class TestCarre(unittest.TestCase):

    # Cas nominaux
    def test_positif(self):
        self.assertEqual(carre(3), 9)

    def test_negatif(self):
        self.assertEqual(carre(-4), 16)

    # Cas à la marge
    def test_zero(self):
        self.assertEqual(carre(0), 0)

    def test_un(self):
        self.assertEqual(carre(1), 1)

    def test_grand_nombre(self):
        self.assertEqual(carre(10**6), 10**12)

    # Cas d'erreur
    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            carre("a")


class TestModulo(unittest.TestCase):

    # Cas nominaux
    def test_reste_non_nul(self):
        self.assertEqual(modulo(10, 3), 1)

    def test_reste_nul(self):
        self.assertEqual(modulo(9, 3), 0)

    # Cas à la marge
    def test_zero_sur_nombre(self):
        self.assertEqual(modulo(0, 5), 0)

    def test_nombre_inferieur_au_diviseur(self):
        self.assertEqual(modulo(3, 7), 3)

    def test_grands_nombres(self):
        self.assertEqual(modulo(10**9 + 1, 10**9), 1)

    # Cas d'erreur
    def test_modulo_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(5, 0)

    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            modulo("a", 2)


class TestPuissance(unittest.TestCase):

    # Cas nominaux
    def test_exposant_positif(self):
        self.assertEqual(puissance(2, 3), 8)

    def test_base_negative(self):
        self.assertEqual(puissance(-2, 3), -8)

    # Cas à la marge
    def test_exposant_zero(self):
        self.assertEqual(puissance(5, 0), 1)

    def test_base_zero(self):
        self.assertEqual(puissance(0, 5), 0)

    def test_base_un(self):
        self.assertEqual(puissance(1, 100), 1)

    def test_exposant_negatif(self):
        self.assertAlmostEqual(puissance(2, -1), 0.5)

    # Cas d'erreur
    def test_type_invalide(self):
        with self.assertRaises(TypeError):
            puissance("a", 2)


if __name__ == "__main__":
    unittest.main()
