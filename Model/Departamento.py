class Departamento:

    def __init__(self):
        self.__Id = None
        self.__Chefe = None
        self.__escolaridadeChefe = None
        self.__Funcionario = []
        self.__Empresa = None

    def setId(self, Id):
        self.__Id = Id

    def getId(self):
        return self.__Id
    
    def setChefe(self, Chefe):
        self.__Chefe = Chefe

    def getChefe(self):
        return self.__Chefe
    
    def setEscolaridadeChefe(self, escolardiadeChefe):
        self.__escolaridadeChefe = escolardiadeChefe

    def getEscolaridadeChefe(self):
        return self.__escolaridadeChefe

    def setFuncionario(self,Funcionario):
        self.__Funcionario = Funcionario

    def addFuncionario(self, Funcionario):
        self.__Funcionario.append(Funcionario)

    def removeFuncionario(self, Funcionario):
        self.__Funcionario = Funcionario

    def getFuncionario(self):
        return self.__Funcionario    

    def setEmpresa(self,Empresa):
        self.__Empresa = Empresa

    def getEmpresa(self,):
        return self.__Empresa
    
    def listarFuncionario(self):
        texto = ('')
        for self.__Funcionario in self.getFuncionario():
            texto += (self.__Funcionario + ' ')
        return texto