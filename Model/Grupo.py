class Grupo:

    def __init__(self):
        self.__nomeGrupo = None
        self.__Presidente = None
        self.__escolaridadePresidente = None
        self.__Pais = None
        self.__Empresa = []
        self.__Funcionario = []

    def setNomeGrupo(self, nomeGrupo):
        self.__nomeGrupo = nomeGrupo

    def getNomeGrupo(self):
        return self.__nomeGrupo

    def setPais(self, Pais):
        self.__Pais = Pais
    
    def getpais(self):
        return self.__Pais
    
    def setPresidente(self, Presidente):
        self.__Presidente = Presidente
        
    def getPresidente(self):
        return self.__Presidente
    
    def setEscolaridadePresidente(self, escolaridadePresidente):
        self.__escolaridadePresidente = escolaridadePresidente

    def getEscolaridadePresidente(self):
        return self.__escolaridadePresidente

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
    
    def listarEmpresa(self):
        texto = ('')
        for self.__Empresa in self.getEmpresa():
            texto += (self.__Empresa + ' ')
        return texto
    
    def listarFuncionario(self):
        texto = ('')
        for self.__Funcionario in self.getFuncionario():
            texto += (self.__Funcionario + ' ')
        return texto