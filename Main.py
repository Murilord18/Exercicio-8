from Model.Cidade import Cidade 
from Model.Departamento import Departamento
from Model.Empresa import Empresa
from Model.Escolaridade import Escolaridade
from Model.Estado import Estado
from Model.Filial import Filial
from Model.Funcionário import Funcionario
from Model.Grupo import Grupo
from Model.Pais import Pais   

if __name__ == "__main__":

    pais1 = Pais()

    estado1 = Estado()

    cidade1 = Cidade()
    cidade2 = Cidade()

    filial1 = Filial()
    filial2 = Filial()

    departamento1 = Departamento()
    departamento2 = Departamento()

    empresa1 = Empresa()

    grupo1 = Grupo()

    funcionario1 = Funcionario()
    funcionario2 = Funcionario()
    funcionario3 = Funcionario()
    funcionario4 = Funcionario()

    #Escolaridade Funcionarios
    escolaridade1 = Escolaridade()
    escolaridade2 = Escolaridade()

    #INSTANCIAÇÃO

    #Escolaridade
    escolaridade1.setNivelEscolaridade('Médio')
    escolaridade2.setNivelEscolaridade('Superior')

    #Pais
    pais1.setNomePais('Brasil')

    #Estado
    estado1.setSiglaEstado('MG')
    estado1.setPais(pais1.getNomePais())
    pais1.addEstados(estado1.getSiglaEstado())
    
    #Cidade 1
    cidade1.setNomeCidade('Juiz de Fora')
    cidade1.setEstado(estado1.getSiglaEstado())
    estado1.addCidade(cidade1.getNomeCidade())

    #Cidade 2
    cidade2.setNomeCidade('Belo Horizonte')
    cidade2.setEstado(estado1.getSiglaEstado())
    estado1.addCidade(cidade2.getNomeCidade())

    #Grupo
    grupo1.setNomeGrupo('Grupo Azteca')
    grupo1.setPresidente('Everson')
    grupo1.setEscolaridadePresidente(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(grupo1.getPresidente())

    grupo1.setPais(pais1.getNomePais())
    pais1.addSedes(grupo1.getNomeGrupo())

    #Empresa
    empresa1.setNomeEmpresa('Amazonas')
    empresa1.setGrupo(grupo1.getNomeGrupo())
    empresa1.setDiretor('Ibere')
    empresa1.setEscolaridadeDiretor(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(empresa1.getDiretor())
    
    #Departamento 1
    departamento1.setId('#092')
    departamento1.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addDepartamento(departamento1.getId())

    departamento1.setChefe('Roberto')
    departamento1.setEscolaridadeChefe(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(departamento1.getChefe())
    
    #Departamento 2
    departamento2.setId('#134')
    departamento2.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addDepartamento(departamento2.getId())

    departamento2.setChefe('André')
    departamento2.setEscolaridadeChefe(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(departamento2.getChefe())
    
    #Filial 1
    filial1.setNumeroFilial('001')
    filial1.setCoordenador('Renato')
    filial1.setEscolaridadeCoordenador(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(filial1.getCoordenador())

    filial1.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addFilial(filial1.getNumeroFilial())

    filial1.setCidade(cidade1.getNomeCidade())
    cidade1.addFilial(filial1.getNumeroFilial())

    #Filial 2
    filial2.setNumeroFilial('002')
    filial2.setCoordenador('Casimiro')
    filial2.setEscolaridadeCoordenador(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(filial2.getCoordenador())

    filial2.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addFilial(filial2.getNumeroFilial())

    filial2.setCidade(cidade2.getNomeCidade())
    cidade2.addFilial(filial2.getNumeroFilial())

    #Funcionario 1
    funcionario1.setNome('Matosu')
    funcionario1.setEscolaridade(escolaridade1.getNivelEscolaridade())
    escolaridade1.addFuncionario(funcionario1.getNome())

    funcionario1.setFilial(filial1.getNumeroFilial())
    funcionario1.setCoordenador(filial1.getCoordenador())
    filial1.addFuncionario(funcionario1.getNome())

    funcionario1.setDepartamento(departamento1.getId())
    funcionario1.setChefe(departamento1.getChefe())
    departamento1.addFuncionario(funcionario1.getNome())

    funcionario1.setEmpresa(empresa1.getNomeEmpresa())
    funcionario1.setDiretor(empresa1.getDiretor())
    empresa1.addFuncionario(empresa1.getFuncionario())

    funcionario1.setGrupo(grupo1.getNomeGrupo())
    funcionario1.setPresidente(grupo1.getPresidente())
    grupo1.addFuncionario(funcionario1.getNome())

    #Funcionario 2
    funcionario2.setNome('Rodrigo')
    funcionario2.setEscolaridade(escolaridade1.getNivelEscolaridade())
    escolaridade1.addFuncionario(funcionario2.getNome())

    funcionario2.setFilial(filial1.getNumeroFilial())
    funcionario2.setCoordenador(filial1.getCoordenador())
    filial1.addFuncionario(funcionario2.getNome())

    funcionario2.setDepartamento(departamento1.getId())
    funcionario2.setChefe(departamento1.getChefe())
    departamento1.addFuncionario(funcionario2.getNome())

    funcionario2.setEmpresa(empresa1.getNomeEmpresa())
    funcionario2.setDiretor(empresa1.getDiretor())
    empresa1.addFuncionario(funcionario2.getNome())

    funcionario2.setGrupo(grupo1.getNomeGrupo())
    funcionario2.setPresidente(grupo1.getPresidente())
    grupo1.addFuncionario(funcionario2.getNome())

    #Funcionario 3
    funcionario3.setNome('Maria')
    funcionario3.setEscolaridade(escolaridade1.getNivelEscolaridade())
    escolaridade1.addFuncionario(funcionario3.getNome())

    funcionario3.setFilial(filial2.getNumeroFilial())
    funcionario3.setCoordenador(filial2.getNumeroFilial())
    filial2.addFuncionario(funcionario3.getNome())

    funcionario3.setDepartamento(departamento2.getId())
    funcionario3.setChefe(departamento2.getChefe())
    departamento2.addFuncionario(funcionario3.getNome())

    funcionario3.setEmpresa(empresa1.getNomeEmpresa())
    funcionario3.setDiretor(empresa1.getDiretor())
    empresa1.addFuncionario(funcionario3.getNome())
    
    funcionario3.setGrupo(grupo1.getNomeGrupo())
    funcionario3.setPresidente(grupo1.getPresidente())
    grupo1.addFuncionario(funcionario3.getNome())

    #Funcionario 4
    funcionario4.setNome('Fernanda')
    funcionario4.setEscolaridade(escolaridade2.getNivelEscolaridade())
    escolaridade2.addFuncionario(funcionario4.getNome())

    funcionario4.setFilial(filial2.getNumeroFilial())
    funcionario4.setCoordenador(filial2.getNumeroFilial())
    filial2.addFuncionario(funcionario4.getNome())

    funcionario4.setDepartamento(departamento2.getId())
    funcionario4.setChefe(departamento2.getChefe())
    departamento2.addFuncionario(funcionario4.getNome())

    funcionario4.setEmpresa(empresa1.getNomeEmpresa())
    funcionario4.setDiretor(empresa1.getDiretor())
    empresa1.addFuncionario(funcionario4.getNome())
    
    funcionario4.setGrupo(grupo1.getNomeGrupo())
    funcionario4.setPresidente(grupo1.getPresidente())
    grupo1.addFuncionario(funcionario4.getNome())

    #PRINTS

    print('ESCOLARIDADE 1')
    print('Nivel de Escolaridade:', escolaridade1.getNivelEscolaridade())
    print('Funcionarios:')


    print('Cidades Do Estado 1:')
    for Cidade in estado1.getCidade():
        print(Cidade)

