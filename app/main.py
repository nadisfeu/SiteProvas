import SiteProvas
import os

connect = SiteProvas.conn
cursor = SiteProvas.cur
opcao = None

os.system("cls")
#SiteProvas.resetar_tabelas()
#SiteProvas.povoar()

email = SiteProvas.novo_login()
print(email)
os.system('PAUSE')
while(True):

    os.system("cls")
    print()
    print("\n\n\t>>>>>>>>>>>>>>>>>>>>>>> OPCOES DE MENU <<<<<<<<<<<<<<<<<<<<<<<<");
    print("\n\n\t1. Pesquisar por disciplina")
    print("  \n\t2. Pesquisar por conteudo")
    print("  \n\t3. Adicionar prova")
    print("  \n\t4. IMPRIMIR")
    print("  \n\t5. INVERTER")
    print("  \n\t6. COPIAR UMA FILA")
    print("  \n\t5. SAIR")
    
    opcao = int(input('Informe a sua opcao: '))

    if opcao == 1:
            disciplina = input("Informe qual disciplina deseja pesquisar: ")
            tipo = input("Informe se é uma lista ou uma prova: ")
            inst = input("Informe a instituicao: ").upper()
            resposta = SiteProvas.pesquisar_por_disciplina(disciplina,inst,tipo)
            SiteProvas.imprime_saida_disciplina(resposta)
            os.system("PAUSE")
    if opcao == 2:
          conteudo = input("Informe qual conteudo deseja pesquisar: ")
          tipo = input("Informe se é uma lista ou uma prova: ")
          inst = input("Informe a instituicao: ").upper()
          resposta = SiteProvas.pesquisar_por_conteudo(conteudo,inst,tipo)
          SiteProvas.imprime_saida_conteudo(resposta)
          os.system("PAUSE")
    if opcao == 3:
          SiteProvas.adicionar_prova_usuario(email)
    if opcao == 9898:
          SiteProvas.resetar_tabelas()
          SiteProvas.povoar()

    if opcao == 5:
          break
    

#SiteProvas.termina_conexao()
