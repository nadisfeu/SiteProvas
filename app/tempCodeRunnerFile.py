script = "Select * from academico"
# cur.execute(script)
# print(cur.fetchall())



# login ou cadastro
while (True):
    opcao = input("\nLogin / Cadastro ? ").lower()
    if opcao == "cadastro":
        resposta = SiteProvas.sign_up()
        if resposta == 1:
            print("Cadastro efetuado com sucesso!")
            break
        else:
            print("\nCadastro nao foi possivel!")
    elif opcao == "login":
        usuario = SiteProvas.login()
        if not usuario:
            print("\nEsse email nao esta registrado!")
        else:
            print("\nLogin realizado com sucesso!")
            break
    else:
        print("\nOpcao invalida!!!")

# Pesquisar ou enviar atividade
while (True):
    opcao = input("\nPesquisar / Enviar ? \nDigite x para sair").lower()
    if opcao == "x":
        print("\nEncerrando...")
        break
    elif opcao == "Pesquisar":
        # ler parametros de pesquisa e chamar funcoes
        print()  # print temporario para remover erro de indentacao
    elif opcao == "enviar":
        # receber pdf como upload do usuario com bibliotecas como flask (web) ou tkinter (app)
        print()
    else:
        print("\nOpcao invalida!!!")

