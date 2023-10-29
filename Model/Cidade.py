class Cidade:

    def __init__(self):
        self.__nomeCidade = None
        self.__Filial = []
        self.__Estado = None

    def setNomeCidade(self, nomeCidade):
        self.__nomeCidade = nomeCidade

    def getNomeCidade(self):
        return self.__nomeCidade

    def setFilial(self, Filial):
        self.__Filial = Filial

    def addFilial(self, Filial):
        self.__Filial.append(Filial)

    def removeFilial(self, Filial):
        self.__Filial.remove(Filial)

    def getFilial(self):
        return self.__Filial
    
    def setEstado(self, Estado):
        self.__Estado = Estado

    def getEstado(self):
        return self.__Estado