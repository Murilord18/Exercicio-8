class Funcionario:

    def __init__(self):
        self.__Diretor = None
        self.__Presidente = None
        self.__Coordenador = None
        self.__Chefe = None
        self.__Nome = None
        self.__Grupo = []
        self.__Departamento = None
        self.__Empresa = []
        self.__Escolaridade = None
        self.__Filial = None

    def setDiretor(self, Diretor):
        self.__Diretor = Diretor

    def getDiretor(self):
        return self.__Diretor

    def setPresidente(self, Presidente):
        self.__Presidente = Presidente
        
    def getPresidente(self):
        return self.__Presidente

    def setCoordenador(self, Coordenador):
        self.__Coordenador = Coordenador

    def getCoordenador(self):
        return self.__Coordenador

    def setChefe(self, Chefe):
        self.__Chefe = Chefe

    def getChefe(self):
        return self.__Chefe

    def setNome(self, Nome):
        self.__Nome = Nome

    def getNome(self):
        return self.__Nome

    def setGrupo(self, Grupo):
        self.__Grupo = Grupo

    def addGrupo(self, Grupo):
        self.__Grupo.append(Grupo)

    def removeGrupo(self, Grupo):
        self.__Grupo.remove(Grupo)

    def getGrupo(self):
        return self.__Grupo

    def setDepartamento(self, Departamento):
        self.__Departamento = Departamento

    def getDepartamento(self):
        return self.__Departamento
    
    def setEmpresa(self, Empresa):
        self.__Empresa = Empresa

    def addEmpresa(self, Empresa):
        self.__Empresa.append(Empresa)

    def removeEmpresa(self, Empresa):
        self.__Empresa.remove(Empresa)

    def getEmpresa(self):
        return self.__Empresa

    def setEscolaridade(self,Escolaridade):
        self.__Escolaridade = Escolaridade

    def getEscolaridade(self):
        return self.__Escolaridade

    def setFilial(self,Filial):
        self.__Filial = Filial

    def getFilial(self):
        return self.__Filial
    