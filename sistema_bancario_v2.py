def menu():
    menu = '''
            ====================================
                        [d]  - Depositar
                        [s]  - Sacar
                        [e]  - Extrato
                        [nu] - Novo Usuario
                        [nc] - Nova Conta
                        [lc] - Listar Contas
                        [q]  - sair

            ====================================
        '''
    return input(menu)

def depositar(saldo, deposito, extrato, /,):
    if deposito > 0:
        print(f"Valor depositado com sucesso. {deposito:.2f}\n")
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"            
    else:
         print("Operação invalida: Não é possivel depositar valores negativos")
    
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, saques_realizados, limite_diario):
    sem_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = saques_realizados >= limite_diario

    if sem_saldo:
        print("Operação cancelada: Saldo insuficiente!")

    elif excedeu_limite:
        print("Operação cancelada: Excedeu o limite de saques!")

    elif excedeu_saques:
        print("Operação cancelada: Excedeu quantidade de saques")
            
    elif saque > 0:
        print(f"Saque realizado com sucesso R$ {saque:.2f}\n")
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        saques_realizados += 1
    else:
        print("Operação cancelada: valor invalido")
    
    return saldo, extrato

def imprimir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO =================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n==========================================\n")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Ja existe um usuario com este CPF.")
        return
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}

    print("Usuario não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = ""
    saques_realizados = 0
    LIMITE_DIARIO = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        
        opcao = menu()

        if opcao == 'd':
            deposito = float(input("Digite um valor para depositar: "))

            saldo, extrato = depositar(saldo, deposito, extrato)
    
        elif opcao == 's':
            saque = float(input("Digite um valor para saque: "))
            saldo, extrato = sacar(saldo = saldo, saque = saque, extrato = extrato, limite=limite, saques_realizados=saques_realizados, limite_diario=LIMITE_DIARIO)
        
        elif opcao == 'e':
            imprimir_extrato(saldo, extrato=extrato)

        elif opcao == 'q':
            break

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao =='nc':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1
        
        elif opcao =='lc':
            listar_contas(contas)

        else:
            print("Selecione novamente uma opção valida.")

main()
