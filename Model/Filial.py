class Filial:

    def __init__(self):
        self.__Coordenador = None
        self.__escolaridadeCoordenador = None
        self.__numeroFilial = None
        self.__Funcionario = []
        self.__Cidade = None
        self.__Empresa = None
    
    def setCoordenador(self, Coordenador):
        self.__Coordenador = Coordenador

    def getCoordenador(self):
        return self.__Coordenador
    
    def setEscolaridadeCoordenador(self, escolaridadeCoordenador):
        self.__escolaridadeCoordenador = escolaridadeCoordenador

    def getEscolaridadeCoordenador(self):
        return self.__escolaridadeCoordenador

    def setNumeroFilial(self, numeroFilial):
        self.__numeroFilial = numeroFilial

    def getNumeroFilial(self):
        return self.__numeroFilial
    
    def setFuncionario(self, Funcionario):
        self.__Funcionario = Funcionario

    def addFuncionario(self, Funcionario):
        self.__Funcionario.append(Funcionario)

    def removeFuncionario(self, Funcionario):
        self.__Funcionario.remove(Funcionario)

    def getFuncionario(self):
        return self.__Funcionario       

    def setCidade(self, Cidade):
        self.__Cidade = Cidade

    def getCidade(self):
        return self.__Cidade
    
    def setEmpresa(self,Empresa):
        self.__Empresa = Empresa

    def getEmpresa(self,):
        return self.__Empresa
    
    def listarFuncionario(self):
        texto = ('')
        for self.__Funcionario in self.getFuncionario():
            texto += (self.__Funcionario + ' ')
        return texto