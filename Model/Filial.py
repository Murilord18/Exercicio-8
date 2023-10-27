class Filial:

    def __init__(self):
        self.__Funcionario = []
        self.__Cidade = None

    
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