
saldo_atual = 0.0
saques_consecutivos = 0

while True:
    print("\nMenu:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = int(input("Escolha uma opção (1/2/3/4): "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo_atual += valor_deposito
        print("Depósito realizado com sucesso!")

    elif opcao == 2:
        if saques_consecutivos >= 3:
            print("Limite máximo de 3 saques consecutivos atingido. Aguarde a próxima operação.")
        else:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if saldo_atual >= valor_saque and valor_saque <= 500.00:
                saldo_atual -= valor_saque
                saques_consecutivos += 1
                print("Saque realizado com sucesso!")
            elif saldo_atual < valor_saque:
                print("Saldo insuficiente!")
            else:
                print("Valor de saque excede o limite máximo de R$ 500.00!")

    elif opcao == 3:
        print(f"Saldo atual: R${saldo_atual:.2f}")

    elif opcao == 4:
        print("Obrigado por utilizar o caixa eletrônico. Volte sempre!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
