import unittest
from calculatrice import additionner, soustraire, multiplier, diviser, carre, modulo, puissance


class TestAdditionner(unittest.TestCase):

    # Cas nominaux
    def test_additionner_deux_entiers_positifs_retourne_leur_somme(self):
        self.assertEqual(additionner(2, 3), 5)
        self.assertEqual(additionner(100, 200), 300)
        self.assertEqual(additionner(1.5, 2.5), 4.0)

    def test_additionner_positif_et_negatif_retourne_la_difference(self):
        self.assertEqual(additionner(10, -3), 7)
        self.assertEqual(additionner(-10, 3), -7)

    # Cas à la marge
    def test_additionner_zero_et_zero_retourne_zero(self):
        self.assertEqual(additionner(0, 0), 0)

    def test_additionner_un_nombre_avec_zero_retourne_le_nombre(self):
        self.assertEqual(additionner(5, 0), 5)
        self.assertEqual(additionner(0, 5), 5)

    def test_additionner_deux_negatifs_retourne_un_negatif(self):
        self.assertEqual(additionner(-4, -6), -10)
        self.assertEqual(additionner(-1, -1), -2)

    def test_additionner_grands_nombres_retourne_leur_somme(self):
        self.assertEqual(additionner(10**9, 10**9), 2 * 10**9)
        self.assertEqual(additionner(10**18, 1), 10**18 + 1)

    # Cas d'erreur
    def test_additionner_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            additionner("a", 1)
        with self.assertRaises(TypeError):
            additionner(1, "b")
        with self.assertRaises(TypeError):
            additionner(None, 1)


class TestSoustraire(unittest.TestCase):

    # Cas nominaux
    def test_soustraire_deux_entiers_positifs_retourne_leur_difference(self):
        self.assertEqual(soustraire(10, 4), 6)
        self.assertEqual(soustraire(100, 1), 99)
        self.assertEqual(soustraire(1.5, 0.5), 1.0)

    def test_soustraire_nombre_plus_grand_retourne_un_negatif(self):
        self.assertEqual(soustraire(3, 7), -4)
        self.assertEqual(soustraire(0, 5), -5)

    # Cas à la marge
    def test_soustraire_un_nombre_par_lui_meme_retourne_zero(self):
        self.assertEqual(soustraire(5, 5), 0)
        self.assertEqual(soustraire(-3, -3), 0)

    def test_soustraire_un_nombre_par_zero_retourne_le_nombre(self):
        self.assertEqual(soustraire(5, 0), 5)
        self.assertEqual(soustraire(0, 5), -5)

    def test_soustraire_deux_negatifs_retourne_leur_difference(self):
        self.assertEqual(soustraire(-5, -2), -3)
        self.assertEqual(soustraire(-2, -5), 3)

    def test_soustraire_grands_nombres_retourne_leur_difference(self):
        self.assertEqual(soustraire(10**9, 10**9), 0)
        self.assertEqual(soustraire(10**18, 10**18 - 1), 1)

    # Cas d'erreur
    def test_soustraire_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            soustraire("a", 1)
        with self.assertRaises(TypeError):
            soustraire(1, "b")
        with self.assertRaises(TypeError):
            soustraire(None, 1)


class TestMultiplier(unittest.TestCase):

    # Cas nominaux
    def test_multiplier_deux_entiers_positifs_retourne_leur_produit(self):
        self.assertEqual(multiplier(3, 4), 12)
        self.assertEqual(multiplier(7, 8), 56)
        self.assertEqual(multiplier(1.5, 2.0), 3.0)

    def test_multiplier_positif_par_negatif_retourne_un_negatif(self):
        self.assertEqual(multiplier(-2, 5), -10)
        self.assertEqual(multiplier(5, -2), -10)

    # Cas à la marge
    def test_multiplier_par_zero_retourne_zero(self):
        self.assertEqual(multiplier(99, 0), 0)
        self.assertEqual(multiplier(0, 99), 0)

    def test_multiplier_par_un_retourne_le_nombre(self):
        self.assertEqual(multiplier(7, 1), 7)
        self.assertEqual(multiplier(1, 7), 7)

    def test_multiplier_deux_negatifs_retourne_un_positif(self):
        self.assertEqual(multiplier(-3, -3), 9)
        self.assertEqual(multiplier(-1, -1), 1)

    def test_multiplier_grands_nombres_retourne_leur_produit(self):
        self.assertEqual(multiplier(10**6, 10**6), 10**12)

    # Cas d'erreur
    def test_multiplier_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            multiplier("a", "b")
        with self.assertRaises(TypeError):
            multiplier(None, 2)


class TestDiviser(unittest.TestCase):

    # Cas nominaux
    def test_diviser_deux_entiers_retourne_un_quotient_entier(self):
        self.assertEqual(diviser(10, 2), 5.0)
        self.assertEqual(diviser(100, 4), 25.0)

    def test_diviser_deux_entiers_retourne_un_quotient_decimal(self):
        self.assertEqual(diviser(7, 2), 3.5)
        self.assertEqual(diviser(1, 3), 1/3)

    def test_diviser_negatif_par_positif_retourne_un_negatif(self):
        self.assertEqual(diviser(-9, 3), -3.0)
        self.assertEqual(diviser(9, -3), -3.0)

    # Cas à la marge
    def test_diviser_zero_par_un_nombre_retourne_zero(self):
        self.assertEqual(diviser(0, 5), 0.0)
        self.assertEqual(diviser(0, -5), 0.0)

    def test_diviser_un_nombre_par_lui_meme_retourne_un(self):
        self.assertEqual(diviser(7, 7), 1.0)
        self.assertEqual(diviser(-4, -4), 1.0)

    def test_diviser_grands_nombres_retourne_leur_quotient(self):
        self.assertEqual(diviser(10**9, 10**3), 10**6)

    # Cas d'erreur
    def test_diviser_par_zero_leve_value_error(self):
        with self.assertRaises(ValueError):
            diviser(10, 0)
        with self.assertRaises(ValueError):
            diviser(-5, 0)
        with self.assertRaises(ValueError):
            diviser(0, 0)

    def test_diviser_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            diviser("a", 2)
        with self.assertRaises(TypeError):
            diviser(2, "b")


class TestCarre(unittest.TestCase):

    # Cas nominaux
    def test_carre_entier_positif_retourne_son_carre(self):
        self.assertEqual(carre(3), 9)
        self.assertEqual(carre(5), 25)
        self.assertEqual(carre(1.5), 2.25)

    def test_carre_entier_negatif_retourne_un_positif(self):
        self.assertEqual(carre(-4), 16)
        self.assertEqual(carre(-1), 1)

    # Cas à la marge
    def test_carre_de_zero_retourne_zero(self):
        self.assertEqual(carre(0), 0)

    def test_carre_de_un_retourne_un(self):
        self.assertEqual(carre(1), 1)
        self.assertEqual(carre(-1), 1)

    def test_carre_grand_nombre_retourne_son_carre(self):
        self.assertEqual(carre(10**6), 10**12)

    # Cas d'erreur
    def test_carre_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            carre("a")
        with self.assertRaises(TypeError):
            carre(None)


class TestModulo(unittest.TestCase):

    # Cas nominaux
    def test_modulo_retourne_le_reste_non_nul(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(7, 4), 3)
        self.assertEqual(modulo(17, 5), 2)

    def test_modulo_retourne_zero_quand_divisible(self):
        self.assertEqual(modulo(9, 3), 0)
        self.assertEqual(modulo(100, 10), 0)

    # Cas à la marge
    def test_modulo_de_zero_retourne_zero(self):
        self.assertEqual(modulo(0, 5), 0)
        self.assertEqual(modulo(0, 1), 0)

    def test_modulo_nombre_inferieur_au_diviseur_retourne_le_nombre(self):
        self.assertEqual(modulo(3, 7), 3)
        self.assertEqual(modulo(1, 100), 1)

    def test_modulo_grands_nombres_retourne_le_reste(self):
        self.assertEqual(modulo(10**9 + 1, 10**9), 1)

    def test_modulo_avec_negatif_retourne_le_reste_signe(self):
        self.assertEqual(modulo(-10, 3), 2)
        self.assertEqual(modulo(10, -3), -2)

    # Cas d'erreur
    def test_modulo_par_zero_leve_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(5, 0)
        with self.assertRaises(ZeroDivisionError):
            modulo(0, 0)

    def test_modulo_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            modulo("a", 2)
        with self.assertRaises(TypeError):
            modulo(2, "b")


class TestPuissance(unittest.TestCase):

    # Cas nominaux
    def test_puissance_base_positive_exposant_positif_retourne_la_puissance(self):
        self.assertEqual(puissance(2, 3), 8)
        self.assertEqual(puissance(3, 3), 27)
        self.assertEqual(puissance(10, 4), 10000)

    def test_puissance_base_negative_exposant_impair_retourne_un_negatif(self):
        self.assertEqual(puissance(-2, 3), -8)

    def test_puissance_base_negative_exposant_pair_retourne_un_positif(self):
        self.assertEqual(puissance(-2, 2), 4)

    # Cas à la marge
    def test_puissance_exposant_zero_retourne_un(self):
        self.assertEqual(puissance(5, 0), 1)
        self.assertEqual(puissance(-5, 0), 1)
        self.assertEqual(puissance(0, 0), 1)

    def test_puissance_base_zero_retourne_zero(self):
        self.assertEqual(puissance(0, 5), 0)
        self.assertEqual(puissance(0, 1), 0)

    def test_puissance_base_un_retourne_toujours_un(self):
        self.assertEqual(puissance(1, 100), 1)
        self.assertEqual(puissance(1, 0), 1)

    def test_puissance_exposant_negatif_retourne_inverse(self):
        self.assertAlmostEqual(puissance(2, -1), 0.5)
        self.assertAlmostEqual(puissance(4, -1), 0.25)
        self.assertAlmostEqual(puissance(2, -2), 0.25)

    # Cas d'erreur
    def test_puissance_avec_type_invalide_leve_type_error(self):
        with self.assertRaises(TypeError):
            puissance("a", 2)
        with self.assertRaises(TypeError):
            puissance(2, "b")


if __name__ == "__main__":
    unittest.main()
