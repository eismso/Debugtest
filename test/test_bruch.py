import unittest

from debugtest.bruch import Bruch

class BruchTest(unittest.TestCase):
    """



    """

    def setUp(self) -> None:
        self.bruch1 = Bruch(2,4)
        self.bruch2 = Bruch(2,3)

    def test_get_decimal_representation(self):
        erg1 = self.bruch1.get_decimal_representation()
        erg2 = self.bruch2.get_decimal_representation()
        self.assertAlmostEqual(2/4, erg1,5)
        self.assertAlmostEqual(0.6, erg2,5)

    def test_add(self):

        erg = self.bruch1.add(self.bruch2)

        #self.assertAlmostEqual(bruch4, erg)
        #self.assertEqual(Bruch(14,12), erg)
        self.assertEqual(erg.zaehler, 14, 'Addition Zaehler')

    def test_multiply(self):
        erg = self.bruch1.multiply(self.bruch2)
        self.assertEqual(erg.zaehler, 4, 'Multi Zahler')


    #def tearDown(self) -> None:


if __name__ == '__main__':
    unittest.main()
