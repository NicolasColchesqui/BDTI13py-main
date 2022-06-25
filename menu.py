import operacoes
import this
this.opcao = -1
this.codigo = 0
this.campo = {}

def menu():
    print('\nEscolha uma das opções abaixo: \n\n' +
          '1. Cadastrar\n'                        +
          '2. Consultar\n'                        +
          '3. Atualizar nome\n'                   +
          '4. Atualizar telefone\n'               +
          '5. Atualizar endereço\n'               +
          '6. Atualizar data de nascimento\n'     +
          '7. Excluir\n'                          +
          '0. Sair\n')
    this.opcao = int(input())

def operacao():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Informe seu nome: ')
            nome = input()
            print('Informe seu telefone: ')
            telefone = input()
            print('Informe seu endereço: ')
            endereco = input()
            print('Informe sua data de nascimento: ')
            dtNasc   = input()
            #Chamar o método inserir
            operacoes.inserir(nome, telefone, endereco, dtNasc)
            print('aperte qualquer botao para prosseguir')
            
        elif this.opcao == 2:
            operacoes.consultar()
        elif this.opcao == 3:
            print('informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('informe o novo nome')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'nome', this.campo)
        elif this.opcao == 4:
            print('informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('informe o novo telefone')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'telefone', this.campo)
        elif this.opcao == 5:
            print('informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('informe o endereço')
            this.campo = input()
            operacoes.atualizar(this.codigo, 'endereço', this.campo)
        elif this.opcao == 6:
            print('informe o codigo que deseja atualizar')
            this.codigo = int(input())
            print('informe sua data de nascimento')
            operacoes.atualizar(this.codigo, 'dataDeNascimento', operacoes.tratarData(this.campo))
            this.campo = input()
        elif this.opcao == 7:
            operacoes.excluir()
        else:
            print('Opção escolhida não é válida!')
