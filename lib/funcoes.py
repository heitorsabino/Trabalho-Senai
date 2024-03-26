from database import *

def gerenciar_equipamentos():
    while True:
        print("\n=== Menu Equipamentos ===")
        print("1. Cadastrar Equipamento")
        print("2. Consultar Equipamento")
        print("3. Atualizar Equipamento")
        print("4. Apagar Equipamento")
        print("5. Emitir Relatórios")
        print("0. Voltar")

        opcao = input("Escolha uma opção para Equipamentos: ")

        if opcao == '1':
            cadastrar_equipamento()
        elif opcao == '2':
            consultar_equipamento()
        elif opcao == '3':
            atualizar_equipamento()
        elif opcao == '4':
            apagar_equipamento()
        elif opcao == '5':
            emitir_relatorios_equipamentos()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def gerenciar_salas():
    while True:
        print("\n=== Menu Salas ===")
        print("1. Cadastrar Sala")
        print("2. Atualizar Sala")
        print("3. Mostrar Sala")
        print("0. Voltar")

        opcao = input("Escolha uma opção para Salas: ")

        if opcao == '1':
            cadastrar_sala()
        elif opcao == '2':
            atualizar_sala()
        elif opcao == '3':
            mostrar_todas_salas()
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def cadastrar_equipamento():
    print("\n=== Cadastrar Equipamento ===")
    tombamento = input("Informe o número de tombamento do equipamento: ")
    descricao = input("Informe a descrição do equipamento: ")
    sala_id = input("Informe o ID da sala onde o equipamento está localizado: ")

    # Converte sala_id para inteiro
    sala_id = int(sala_id)

    # Encontra o maior ID atual e incrementa em 1 para definir o novo ID do equipamento
    novo_id = max([equipamento['ID'] for equipamento in dados_equipamentos]) + 1

    # Cria um novo dicionário representando o equipamento
    novo_equipamento = {"ID": novo_id, "Tombamento": tombamento, "Descricao": descricao, "SalaID": sala_id}

    # Adiciona o novo equipamento à lista de equipamentos
    dados_equipamentos.append(novo_equipamento)

    print("Equipamento cadastrado com sucesso.")

def consultar_equipamento():
    print("\n=== Consultar Equipamento ===")
    tombamento = input("Informe o número de tombamento do equipamento: ")

    # Procura o equipamento pelo número de tombamento
    equipamento_encontrado = None
    for equipamento in dados_equipamentos:
        if equipamento['Tombamento'] == tombamento:
            equipamento_encontrado = equipamento
            break

    # Se o equipamento foi encontrado, exibe suas informações
    if equipamento_encontrado:
        print("Informações do equipamento:")
        print("ID:", equipamento_encontrado['ID'])
        print("Tombamento:", equipamento_encontrado['Tombamento'])
        print("Descrição:", equipamento_encontrado['Descricao'])
        print("ID da Sala:", equipamento_encontrado['SalaID'])
    else:
        print("Equipamento não encontrado.")

def atualizar_equipamento():
    print("\n=== Atualizar Equipamento ===")
    tombamento = input("Informe o número de tombamento do equipamento que deseja atualizar: ")

    # Procura o equipamento pelo número de tombamento
    equipamento_encontrado = None
    for equipamento in dados_equipamentos:
        if equipamento['Tombamento'] == tombamento:
            equipamento_encontrado = equipamento
            break

    # Se o equipamento foi encontrado, permite atualizar suas informações
    if equipamento_encontrado:
        print("Equipamento encontrado. Insira os novos dados:")
        novo_tombamento = input("Novo número de tombamento (deixe em branco para manter o mesmo): ")
        nova_descricao = input("Nova descrição (deixe em branco para manter a mesma): ")
        novo_sala_id = input("Novo ID da sala (deixe em branco para manter o mesmo): ")

        # Atualiza as informações do equipamento, se o usuário inseriu novos dados
        if novo_tombamento:
            equipamento_encontrado['Tombamento'] = novo_tombamento
        if nova_descricao:
            equipamento_encontrado['Descricao'] = nova_descricao
        if novo_sala_id:
            equipamento_encontrado['SalaID'] = int(novo_sala_id)

        print("Equipamento atualizado com sucesso.")
    else:
        print("Equipamento não encontrado.")

def apagar_equipamento():
    print("\n=== Apagar Equipamento ===")
    tombamento = input("Informe o número de tombamento do equipamento que deseja apagar: ")

    # Procura o equipamento pelo número de tombamento
    for equipamento in dados_equipamentos:
        if equipamento['Tombamento'] == tombamento:
            dados_equipamentos.remove(equipamento)
            print("Equipamento apagado com sucesso.")
            return

    print("Equipamento não encontrado.")


def emitir_relatorios_equipamentos():
    print("\n=== Emitir Relatórios de Equipamentos ===")
    # Aqui você pode implementar a lógica para emitir relatórios de equipamentos
    # Por exemplo, você pode exibir todos os equipamentos cadastrados com suas informações
    for equipamento in dados_equipamentos:
        print("ID:", equipamento['ID'])
        print("Tombamento:", equipamento['Tombamento'])
        print("Descrição:", equipamento['Descricao'])
        print("ID da Sala:", equipamento['SalaID'])
        print("--------------------------")


#salas


def cadastrar_sala():
    print("\n=== Adicionar Sala ===")
    numero_identificador = input("Informe o número identificador da sala: ")
    descricao = input("Informe a descrição da sala: ")

    # Encontra o maior ID atual e incrementa em 1 para definir o novo ID da sala
    novo_id = max([sala['ID'] for sala in dados_salas]) + 1

    # Cria um novo dicionário representando a sala
    nova_sala = {"ID": novo_id, "NumeroIdentificador": numero_identificador, "Descricao": descricao}

    # Adiciona a nova sala à lista de salas
    dados_salas.append(nova_sala)

    print("Sala adicionada com sucesso.")

def atualizar_sala():
    print("\n=== Atualizar Sala ===")
    id_sala = int(input("Informe o ID da sala que deseja atualizar: "))  # Convertendo para inteiro

    # Procura a sala pelo ID
    for sala in dados_salas:
        if sala['ID'] == id_sala:
            print("Sala encontrada. Insira os novos dados:")
            novo_numero_identificador = input("Novo número identificador (deixe em branco para manter o mesmo): ")
            nova_descricao = input("Nova descrição (deixe em branco para manter a mesma): ")

            # Atualiza as informações da sala, se o usuário inseriu novos dados
            if novo_numero_identificador:
                sala['NumeroIdentificador'] = novo_numero_identificador
            if nova_descricao:
                sala['Descricao'] = nova_descricao

            print("Sala atualizada com sucesso.")
            return

    print("Sala não encontrada.")

def mostrar_todas_salas():
    print("\n=== Lista de Todas as Salas ===")
    if dados_salas:
        for sala in dados_salas:
            print("ID:", sala['ID'])
            print("Número Identificador:", sala['NumeroIdentificador'])
            print("Descrição:", sala['Descricao'])
            print("--------------------------")
    else:
        print("Não há salas cadastradas.")