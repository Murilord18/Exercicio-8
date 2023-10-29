class Pais:

    def __init__(self):
        self.__nomePais = None
        self.__Sedes = []
        self.__Estados = []

    def setNomePais(self, nomePais):
        self.__nomePais = nomePais

    def getNomePais(self):
        return self.__nomePais

    def SetSedes(Self, Sedes):
        Self.__Sedes = Sedes

    def addSedes(self, Sedes):
        self.__Sedes.append(Sedes)

    def removeSedes(self, Sedes):
        self.__Sedes.remove(Sedes)

    def getSedes(self):
        return self.__Sedes   

    def setEstado(self, Estados):
        self.__Estados = Estados

    def addEstados(self, Estados):
        self.__Estados.append(Estados)

    def removeEstados(self, Estados):
        self.__Estados.remove(Estados)
    
    def getEstado(self, Estados):
        return self.__Estados
    