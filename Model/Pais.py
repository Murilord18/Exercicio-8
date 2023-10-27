class Pais:


    def __init__(self):
        self.__Sedes = []

    def SetSedes(Self, Sedes):
        Self.__Sedes = Sedes

    def addSedes(self, Sedes):
        self.__Sedes.append(Sedes)

    def removeSedes(self, Sedes):
        self.__Sedes.remove(Sedes)

    def getSedes(self):
        return self.__Sedes   

