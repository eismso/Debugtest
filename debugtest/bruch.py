class Bruch:
    """
    Bruch dargestellt als x/y.

    Attributes
    ----------
    zaehler: int
        Zaehler des Bruchs.

    nenner: int
        Nenner des Bruchs.


    Methods
    -------
    get_decimal_representation()
        Stellt Bruch in dezimaler Form dar.


    """
    @property
    def zaeler(self):
        return self.__zaehler

    @zaeler.setter
    def zaeler(self, value):
        self.__zaehler = value

    @property
    def nenner(self):
        return self.__nenner

    @nenner.setter
    def nenner(self, value):
        if value != 0:
            self.__nenner = value

    def __init__(self, zaehler : int, nenner: int):
        self.zaehler = zaehler
        self.nenner = nenner

    def get_decimal_representation(self) -> float:
        """
        Wandelt Bruch in einen float Wert und liefert diesen als Rückgabewert.

        Returns
        -------
        float
            Bruch als Dezimalzahl.
        """
        return self.zaehler / self.nenner

    def add(self, bruch2: 'Bruch') -> 'Bruch': # 'Bruch' weil noch nicht erkannt wird
        bruch2_neuer_zaehler = bruch2.zaehler * self.nenner
        erg_nenner = bruch2.nenner * self.nenner
        self_neuer_zaehler = self.zaehler * bruch2.nenner
        erg_zaehler = bruch2_neuer_zaehler + self_neuer_zaehler
        return Bruch(erg_zaehler,erg_nenner)
        #alternativ
        # return Bruch(bruch2.zaehler * self.nenner + self.zaehler * bruch2.nenner,bruch2.nenner * self.nenner)

    def multiply(self, bruch2: 'Bruch') -> 'Bruch':
        """
        Multipliziert zwei Brueche miteinander und gibt als Ergebnis als neuen Bruch aus.

        Parameters
        ----------
        bruch2: Bruch
            Zweiter Operand der Multiplikation.

        Returns
        -------
        Bruch
            Liefert einen neuen Bruch mit dem Ergebnis der Multiplikation.
        """
        erg_zaehler = self.zaehler * bruch2.zaehler
        erg_nenner = self.nenner * bruch2.nenner
        return Bruch(erg_zaehler,erg_nenner)
        #alternativ
        #return Bruch(self.zaehler * bruch2.zaehler,self.nenner * bruch2.nenner)



    def __repr__(self):
        return f'Bruch({self.zaehler}/{self.nenner})'

if __name__ == '__main__':
    b1 = Bruch(2,3)
    print(b1)
    print(b1.get_decimal_representation())
    b2 = Bruch(3,4)
    print(b2)
    print(b2.get_decimal_representation())
    print(b1.add(b2))
    print(b1.multiply(b2))