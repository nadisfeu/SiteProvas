import SiteProvas

cursor = SiteProvas.cur
connect = SiteProvas.conn

#login ou cadastro
# while(True):
#     opcao = input("\nLogin / Cadastro ?").lower()
#     if opcao == "cadastro":
#         resposta = SiteProvas.login()
#         if resposta == 1:
#             print("Cadastro efetuado com sucesso!")
#             break
#         else:
#             print("\nCadastro nao foi possivel!")
#     elif opcao == "login":
#         usuario = SiteProvas.sign_up()
#         if not usuario:
#             print("\nEsse email nao esta registrado!")
#         else:
#             print("\nLogin realizado com sucesso!")
#             break

SiteProvas.inserir_academico('paulinho@gmail.com', 'rogerio', 'Professor', 'ufop')
SiteProvas.conn.commit()

script = "Select * from academico"
cursor.execute(script)
print(cursor.fetchall())


# list = SiteProvas.pesquisar_aluno_bd('fernando', 'ufop', cur=cur)
# print(list)

cur = SiteProvas.conexao_server()
list = SiteProvas.inserir_academico(cur, 'alexandre@ufop', 'Alexandre', 'Professor', 'UFOP')

SiteProvas.termina_conexao()
