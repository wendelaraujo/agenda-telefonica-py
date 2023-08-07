agenda = {}
def adicionarContato(nome: str , telefone: str) -> None:
    agenda[nome] = telefone
    print('contato adicionado com sucesso!')
def editarContato(nome: str, telefone: str) -> None:
    if nome in agenda.keys():
        agenda[nome] = telefone
        print('dados alterados com sucesso!')
    else:
        print('O contato não existe: ')
def pesquisarContato(nome: str) -> None:
    if nome in agenda.keys():
        print('\n ----------------')
        print(f'Contato: {nome}')
        print(f'Telefone:{agenda[nome]}')
        print('\n ----------------')
    else:
        print('Contato nçao existente')
def deletarContato(nome: str) -> None:
    if nome in agenda.keys():
        del agenda[nome]
        print('Contato removido da agenda')
    else:
        print('Contato não existe')
def listarTodos():
    for nome in agenda:
        print('\n ----------------')
        print(f'Contato: {nome}')
        print(f'Telefone:{agenda[nome]}')
        print('\n ----------------')


while True:
    print('------ Bem vindo ao Menu ------')
    opcao = int(input('1  - adicionar contato \n'
                      '2 - editar contato \n'
                      '3 - pesquisar contato \n'
                      '4 - deletar contato \n'
                      '5 - listar todos \n'
                      '6 - sair \n'
                      'selecione uma opção:'))
    if opcao == 1:
        nome = input('digite o nome do contato: ')
        tel = input('digite o telefone do contato:')
        adicionarContato(nome,tel)
    elif opcao == 2:
        nome = input('digite o nome do contato que você deseja alterar: ')
        tel = input('digite o novo telefone:')
        editarContato(nome,tel)
    elif opcao ==3:
        nome = input('Digite o nome do contato')
        pesquisarContato(nome)
    elif opcao == 4:
        nome = input('Digite o nome do contato')
        deletarContato(nome)
    elif opcao == 5:
        listarTodos()
    elif opcao == 6:
        break
    else:
        print('Opção invalida!')
