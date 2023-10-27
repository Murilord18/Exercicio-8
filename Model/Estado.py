class Estado:

    def __init__(self):
        self.__Cidade = []
        self.__Pais = None


    def setCidade(self, Cidade):
        self.__Cidade = Cidade

    def addCidade(self, Cidade):
        self.__Cidade.append(Cidade)

    def removeCidade(self, Cidade):
        self.__Cidade.remove(Cidade)

    def getCidade(self):
        return self.__Cidade 
    

    def setPais(self, Pais):
        self.__Pais = Pais

    def getPais(self):
        return self.__Pais