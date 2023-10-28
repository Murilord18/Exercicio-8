class Grupo:

    def __init__(self):
        self.__Presidente = None
        self.__Pais = None
        self.__Empresa = []
        self.__Funcionario = []

    def setPais(self, Pais):
        self.__Pais = Pais
    
    def getpais(self):
        return self.__Pais
    
    def setPresidente(self, Presidente):
        self.__Presidente = Presidente
        
    def getPresidente(self):
        return self.__Presidente
    

    
    def setEmpresa(self,Empresa):
        self.__Empresa = Empresa
    
    def addEmpresa(self, Empresa):
        self.__Empresa.append(Empresa)

    def removeEmpresa(Self, Empresa):
        Self.__Empresa.remove(Empresa)

    def getEmpresa(self):
        return self.__Empresa
    


    def setFuncionario(self, Funcionario):
        self.__Funcionario = Funcionario

    def addFuncionario(self, Funcionario):
        self.__Funcionario.append(Funcionario)

    def removeFuncionario(self, Funcionario):
        self.__Funcionario = Funcionario
    
    def getFuncionario(self):
        return self.__Funcionario