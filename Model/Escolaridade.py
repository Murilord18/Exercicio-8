class Escolaridade:

    def __init__(self):
        self.__nivelEscolaridade = None
        self.__Funcionario = []

    def setNivelEscolaridade(self, nivelEscolaridade):
        self.__nivelEscolaridade = nivelEscolaridade

    def getNivelEscolaridade(self):
        return self.__nivelEscolaridade

    def setFuncionario(self, Funcionario):
        self.__Funcionario = Funcionario

    def addFuncionario(self, Funcionario):
        self.__Funcionario.append(Funcionario)

    def removeFuncionario(self, Funcionario):
        self.__Funcionario.remove(Funcionario)

    def getFuncionario(self):
        return self.__Funcionario
    
