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

    #Coordenadores
    funcionario5 = Funcionario()
    funcionario6 = Funcionario()

    #Chefes
    funcionario7 = Funcionario()
    funcionario8 = Funcionario()

    #Diretor
    funcionario9 = Funcionario()

    #Presidente
    funcionario10 = Funcionario()

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
    pais1.setEstado(estado1.getSiglaEstado())
    
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
    funcionario10.setNome('Everson')
    grupo1.addFuncionario(funcionario10.getNome())
    grupo1.setPresidente(funcionario10.getNome())

    funcionario10.setGrupo(grupo1.getNomeGrupo())
    funcionario10.setEscolaridade(escolaridade2.getNivelEscolaridade())
    grupo1.setEscolaridadePresidente(funcionario10.getEscolaridade())
    escolaridade2.addFuncionario(funcionario10.getNome())

    grupo1.setPais(pais1.getNomePais())
    pais1.setSedes(grupo1.getNomeGrupo())

    #Empresa
    empresa1.setNomeEmpresa('Amazonas')
    empresa1.setGrupo(grupo1.getNomeGrupo())
    grupo1.addEmpresa(empresa1.getNomeEmpresa())

    funcionario9.setNome('Ibere')
    empresa1.setDiretor(funcionario9.getNome())
    empresa1.addFuncionario(funcionario9.getNome())
    grupo1.addFuncionario(funcionario9.getNome())
    funcionario9.setEscolaridade(escolaridade2.getNivelEscolaridade())
    empresa1.setEscolaridadeDiretor(funcionario9.getEscolaridade())
    escolaridade2.addFuncionario(funcionario9.getNome())
    
    #Departamento 1
    departamento1.setId('#092')
    departamento1.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addDepartamento(departamento1.getId())

    funcionario8.setNome('Roberto')
    departamento1.setChefe(funcionario8.getNome())
    departamento1.addFuncionario(funcionario8.getNome())
    empresa1.addFuncionario(funcionario8.getNome())
    grupo1.addFuncionario(funcionario8.getNome())
    funcionario8.setEscolaridade(escolaridade2.getNivelEscolaridade())
    departamento1.setEscolaridadeChefe(funcionario8.getEscolaridade())
    escolaridade2.addFuncionario(funcionario8.getNome())
    
    #Departamento 2
    departamento2.setId('#134')
    departamento2.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addDepartamento(departamento2.getId())

    funcionario7.setNome('André')
    departamento2.setChefe(funcionario7.getNome())
    departamento2.addFuncionario(funcionario7.getNome())
    empresa1.addFuncionario(funcionario7.getNome())
    grupo1.addFuncionario(funcionario7.getNome())
    funcionario7.setEscolaridade(escolaridade2.getNivelEscolaridade())
    departamento2.setEscolaridadeChefe(funcionario7.getEscolaridade())
    escolaridade2.addFuncionario(funcionario7.getNome())
    
    #Filial 1
    filial1.setNumeroFilial('001')
    funcionario6.setNome('Renato')
    filial1.setCoordenador(funcionario6.getNome())
    funcionario6.setEscolaridade(escolaridade2.getNivelEscolaridade())
    filial1.setEscolaridadeCoordenador(funcionario6.getEscolaridade())
    escolaridade2.addFuncionario(funcionario6.getNome())

    empresa1.addFuncionario(funcionario6.getNome())
    grupo1.addFuncionario(funcionario6.getNome())

    filial1.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addFilial(filial1.getNumeroFilial())

    filial1.setCidade(cidade1.getNomeCidade())
    cidade1.setFilial(filial2.getNumeroFilial())

    #Filial 2
    filial2.setNumeroFilial('002')
    funcionario5.setNome('Casimiro')
    filial2.setCoordenador(funcionario5.getNome())
    funcionario5.setEscolaridade(escolaridade2.getNivelEscolaridade())
    filial2.setEscolaridadeCoordenador(funcionario5.getEscolaridade())
    escolaridade2.addFuncionario(funcionario5.getNome())

    empresa1.addFuncionario(funcionario5.getNome())
    grupo1.addFuncionario(funcionario5.getNome())

    filial2.setEmpresa(empresa1.getNomeEmpresa())
    empresa1.addFilial(filial2.getNumeroFilial())

    filial2.setCidade(cidade2.getNomeCidade())
    cidade2.setFilial(filial2.getNumeroFilial())

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
    empresa1.addFuncionario(funcionario1.getNome())

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
    funcionario3.setCoordenador(filial2.getCoordenador())
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
    funcionario4.setCoordenador(filial2.getCoordenador())
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
    print('------------------------------------------')
    print()
    print('ESCOLARIDADE 1')
    print()
    print('Nivel de Escolaridade:', escolaridade1.getNivelEscolaridade())
    print('Funcionarios:')
    for Funcionario in escolaridade1.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('ESCOLARIDADE 2')
    print()
    print('Nivel de Escolaridade:', escolaridade2.getNivelEscolaridade())
    print('Funcionarios:')
    for Funcionario in escolaridade2.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('GRUPO')
    print()
    print('Nome do Grupo:', grupo1.getNomeGrupo())
    print('Pais:', grupo1.getpais())
    print('Presidente:', grupo1.getPresidente())
    print('Escolaridade do Presidente:', grupo1.getEscolaridadePresidente())
    print('Empresas:')
    for Empresa in grupo1.getEmpresa():
        print(Empresa)
    print('Funcionarios:')
    for Funcionario in grupo1.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('EMPRESA')
    print()
    print('Nome da Empresa:', empresa1.getNomeEmpresa())
    print('Grupo:', empresa1.getGrupo())
    print('Diretor:', empresa1.getDiretor())
    print('Escolaridade do Diretor:', empresa1.getEscolaridadeDiretor())
    print('Departamentos:')
    for Departamento in empresa1.getDepartamento():
        print(Departamento)
    print('Filiais:')
    for Filial in empresa1.getFilial():
        print(Filial)
    print('Funcionarios:')
    for Funcionario in empresa1.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('DEPARTAMENTO 1')
    print()
    print('Id do Departamento', departamento1.getId())
    print('Empresa:', departamento1.getEmpresa())
    print('Chefe:', departamento1.getChefe())
    print('Escolaridade do Chefe:', departamento1.getEscolaridadeChefe())
    print('Funcionarios:')
    for Funcionario in departamento1.getFuncionario():
        print(Funcionario)
    print()
    
    print('------------------------------------------')
    print()
    print('DEPARTAMENTO 2')
    print()
    print('Id do Departamento', departamento2.getId())
    print('Empresa:', departamento2.getEmpresa())
    print('Chefe:', departamento2.getChefe())
    print('Escolaridade do Chefe:', departamento2.getEscolaridadeChefe())
    print('Funcionarios:')
    for Funcionario in departamento2.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('FILIAL 1')
    print()
    print('Número da Filial:', filial1.getNumeroFilial())
    print('Cidade:', filial1.getCidade())
    print('Empresa:', filial1.getEmpresa())
    print('Coordenador:', filial1.getCoordenador())
    print('Escolaridade do Coordenador:', filial1.getEscolaridadeCoordenador())
    print('Funcionarios:')
    for Funcionario in filial1.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('FILIAL 2')
    print()
    print('Número da Filial:', filial2.getNumeroFilial())
    print('Cidade:', filial2.getCidade())
    print('Empresa:', filial2.getEmpresa())
    print('Coordenador:', filial2.getCoordenador())
    print('Escolaridade do Coordenador:', filial2.getEscolaridadeCoordenador())
    print('Funcionarios:')
    for Funcionario in filial2.getFuncionario():
        print(Funcionario)
    print()

    print('------------------------------------------')
    print()
    print('FUNCIONARIO 1')
    print()
    print('Nome:', funcionario1.getNome())
    print('Escolaridade do Funcionario:', funcionario1.getEscolaridade())
    print('Grupo:', funcionario1.getGrupo())
    print('Presidente:', funcionario1.getPresidente())
    print('Empresa:', funcionario1.getEmpresa())
    print('Diretor:', funcionario1.getDiretor())
    print('Departamento:', funcionario1.getDepartamento())
    print('Chefe:', funcionario1.getChefe())
    print('Filial:', funcionario1.getFilial())
    print('Coordenador:', funcionario1.getCoordenador())
    print()

    print('------------------------------------------')
    print()
    print('FUNCIONARIO 2')
    print()
    print('Nome:', funcionario2.getNome())
    print('Escolaridade do Funcionario:', funcionario2.getEscolaridade())
    print('Grupo:', funcionario2.getEmpresa())
    print('Presidente:', funcionario2.getPresidente())
    print('Empresa:', funcionario2.getEmpresa())
    print('Diretor:', funcionario2.getDiretor())
    print('Departamento:', funcionario2.getDepartamento())
    print('Chefe:', funcionario2.getChefe())
    print('Filial:', funcionario2.getFilial())
    print('Coordenador:', funcionario2.getCoordenador())
    print()

    print('------------------------------------------')
    print()
    print('FUNCIONARIO 3')
    print()
    print('Nome:', funcionario3.getNome())
    print('Escolaridade do Funcionario:', funcionario3.getEscolaridade())
    print('Grupo:', funcionario3.getGrupo())
    print('Presidente:', funcionario3.getPresidente())
    print('Empresa:', funcionario1.getEmpresa())
    print('Diretor:', funcionario3.getDiretor())
    print('Departamento:', funcionario3.getDepartamento())
    print('Chefe:', funcionario3.getChefe())
    print('Filial:', funcionario3.getFilial())
    print('Coordenador:', funcionario3.getCoordenador())
    print()

    print('------------------------------------------')
    print()
    print('FUNCIONARIO 4')
    print()
    print('Nome:', funcionario4.getNome())
    print('Escolaridade do Funcionario:', funcionario4.getEscolaridade())
    print('Grupo:', funcionario4.getGrupo())
    print('Presidente:', funcionario4.getPresidente())
    print('Empresa:', funcionario4.getEmpresa())
    print('Diretor:', funcionario4.getDiretor())
    print('Departamento:', funcionario4.getDepartamento())
    print('Chefe:', funcionario4.getChefe())
    print('Filial:', funcionario4.getFilial())
    print('Coordenador:', funcionario4.getCoordenador())
    print()

    print('------------------------------------------')
    print()
    print('CIDADE 1')
    print()
    print('Nome:', cidade1.getNomeCidade())
    print('Estado:', cidade1.getEstado())
    print('Filial:', cidade1.getFilial())
    print()

    print('------------------------------------------')
    print()
    print('CIDADE 2')
    print()
    print('Nome:', cidade2.getNomeCidade())
    print('Estado:', cidade2.getEstado())
    print('Filial:', cidade1.getFilial())
    print()

    print('------------------------------------------')
    print()
    print('ESTADO')
    print()
    print('Sigla do Estado:', estado1.getSiglaEstado())
    print('Pais:', estado1.getPais())
    print('Cidades:')
    for Cidade in estado1.getCidade():
        print(Cidade)
    print()
    
    print('------------------------------------------')
    print()
    print('PAIS')
    print()
    print('Nome:', pais1.getNomePais())
    print('Estado:', pais1.getEstado())
    print('Grupo:', pais1.getSedes())
    print()

    print('------------------------------------------')