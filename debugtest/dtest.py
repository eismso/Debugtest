class Patient:
    # Nahrungsmittel (Liste)
    # Name (hier wäre property nicht unbedingt notwendig, weil Namen sich ändern können, hier nur zum ueben)
    # SV Nr
    @property
    def name(self):
        print("name get")
        return self.__name

    @name.setter
    def name(self, value):
        print("name set")
        if len(value) > 0 and value is not None:
            self.__name = value
            #self.name = value          hier würde es wieder auf zeile 12 hüpfen (rekursion) -> stack overflow

    @property
    def ssn(self):
        return self.__ssn


    def __init__(self, name, ssn):
        #self.__name = "Hansi"      # auch möglich, aber nicht über setter
        self.name = name            # zugriff über setter
        self.__ssn = ssn            # bei get property immer zugriff ueber __ notwendig
        self.__intolerance = []

    def add_intolerance(self, i : str):
        self.__intolerance.append(i)

    def is_intolerant(self, ingredient: str) -> bool:
        return ingredient in self.__intolerance

if __name__ == '__main__':
    p = Patient("Herr P", 2345131280)
    print(dir(p))
    print(p.name)
    print(p.ssn)
    #p.snn = 12                     # funktioniert nicht
