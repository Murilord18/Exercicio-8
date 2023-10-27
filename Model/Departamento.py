class Departamento:


    def __init__(self):
        self.__Funcionario = None
        self.__Empresa = None

    def setFuncionario(self,Funcionario):
        self.__Funcionario = Funcionario

    def getFuncionario(self):
        return self.__Funcionario
    


    def setEmpresa(self,Empresa):
        self.__Empresa = Empresa

    def getEmpresa(self,):
        return self.__Empresa
    