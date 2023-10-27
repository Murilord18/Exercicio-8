class Escolaridade:

    def __init__(self):
        self.__Funcionario = []


    def setFuncionario(self, Funcionario):
        self.__Funcionario = Funcionario

    def addFuncionario(self, Funcionario):
        self.__Funcionarios.append(Funcionario)

    def removeFuncionario(self, Funcionario):
        self.__Funcionarios.remove(Funcionario)

    def getFuncionario(self):
        return self.__Funcionarios
    
