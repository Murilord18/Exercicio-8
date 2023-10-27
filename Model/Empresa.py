class Empresa:


    def __init__(self):
        self.__Funcionario = None
        self.__Filial = []
        self.__Departamento = []

    

    def setFuncionario(self,Funcionario):
        self.__Funcionario = Funcionario

    def getFuncionario(self):
        return self.__Funcionario



    def setFilial(self, Filial):
        self.__Filial = Filial

    def addEscola(self, Filial):
        self.__Filial.append(Filial)

    def removeEscola(self, Filial):
        self.__Filial.remove(Filial)

    def getFilial(self):
        return self.__Filial
    



    def SetDepartamento(self, Departamento):
        self.__Departamento = Departamento

    def addDepartamento(self, Departamento):
        self.__Departamento.append(Departamento)

    def removeDepartamento(self, Departamento):
        self.__Departamento.remove(Departamento)

    def getDepartamento(self):
        return self.__Departamento
    