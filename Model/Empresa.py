class Empresa:

    def __init__(self):
        self.__Diretor = None
        self.__escolaridadeDiretor = None
        self.__nomeEmpresa = None
        self.__Funcionario = []
        self.__Filial = []
        self.__Departamento = []

    def setDiretor(self, Diretor):
        self.__Diretor = Diretor

    def getDiretor(self):
        return self.__Diretor
    
    def setEscolaridadeDiretor(self, escolaridadeDiretor):
        self.__escolaridadeDiretor = escolaridadeDiretor

    def getEscolaridadeDiretor(self):
        return self.__escolaridadeDiretor

    def setNomeEmpresa(self, nomeEmpresa):
        self.__nomeEmpresa = nomeEmpresa

    def getNomeEmpresa(self):
        return self.__nomeEmpresa

    def setFuncionario(self,Funcionario):
        self.__Funcionario = Funcionario
    
    def addFuncionario(self, Funcionario):
        self.__Funcionario.append(Funcionario)

    def removeFuncionario(self, Funcionario):
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
    