import unittest

from debugtest.dtest import Patient


class DTestTest(unittest.TestCase):    # Vererbung
    @classmethod
    def setUpClass(cls) -> None:
        print("Wird einmal pro Testklasse aufgerufen")

    def setUp(self) -> None:
        print("Wird einmal für jeden Test aufgerufen")
        self.patient = Patient("Herr P", 2002020)
        self.patient.add_intolerance("Gluten")
        self.patient.add_intolerance("Laktose")

    #Testmethoden müssen mit test_ beginnen!
    def test_is_intolerant(self):
        erg1 = self.patient.is_intolerant("Gluten")
        erg2 = self.patient.is_intolerant("Laktose")
        erg3 = self.patient.is_intolerant("Schnitzel")
        # erg sollte True sein
        self.assertTrue(erg1)
        self.assertTrue(erg2)
        self.assertFalse(erg3)
        # alternativ
        #self.assertEqual(True, erg)


    def test_something(self):
        # meinen Code ausfuehren, den ich testen möchte (Ergebnis merken)
        # danach ueberpruefen, ob Ergebnis stimmt
        self.assertEqual(True, True)  # add assertion here

    @classmethod
    def tearDownClass(cls) -> None:
        print("Wird einmal pro Klasse ausgeführt - Ressourcen freigeben")

    def tearDown(self) -> None:
        print("Wird einmal nach jeder Testmethode ausgeführt zum Ressourcen freigeben")

if __name__ == '__main__':
    unittest.main()         # führt alle Testmethoden aus?
