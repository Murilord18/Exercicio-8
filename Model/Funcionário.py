class Funcionario:

    def __init__(self):
        self.__Grupo = []
        self.__Departamento = None
        self.__Empresa = []
        self.__Escolaridade = None
        self.__Filial = None



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
    