import psycopg2
import re

hostname = 'localhost'
database = 'AtividadeBD'
username = 'postgres'
pwd = '123'
port_id = 5432
conn = None
cur = None


def verficar_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)


# funcoes de insercao
def inserir_academico(email, nome, tipo, instituicao):
    insert_scrip = 'INSERT INTO ACADEMICO (email, nome, tipo, instituicao) VALUES (%s, %s, %s, %s);'
    insert_values = (email, nome, tipo, instituicao)
    cur.execute(insert_scrip, insert_values)


def povoar():
    
    insert_script = 'DROP TABLE IF EXISTS academico CASCADE;'
    cur.execute(insert_script)
    inserir_academico('alexandre@ufop', 'Alexandre','Professor', 'UFOP')
    inserir_academico('jao@ufop', 'jao','Aluno', 'UFOP')
    inserir_academico('jorginho@ufop', 'jorge','Aluno', 'UFOP')
    inserir_academico('augusto@ufop', 'augusto','Professor', 'UFOP')
    insert_script = 'DROP TABLE IF EXISTS atividade CASCADE;'
    cur.execute(insert_script)
    inserir_atividade(1,'alexandre@ufop','UFOP','Banco de Dados 1',5,'x.com')
    inserir_atividade(2,'augusto@ufop','UFOP','Redes 1',7,'x.com')
    inserir_atividade(3,'alexandre@ufop','UFOP','Calculo 1',1,'x.com')
    inserir_atividade(4,'augusto@ufop','UFOP','AEDS 2',10,'x.com')
    insert_script = 'DROP TABLE IF EXISTS prova CASCADE;'
    cur.execute(insert_script)
    inserir_prova('P1',1)
    inserir_prova('P3',2)
    insert_script = 'DROP TABLE IF EXISTS lista CASCADE;'
    cur.execute(insert_script)
    inserir_lista(True, 3)
    inserir_lista(False, 4)


# CORRIGIR ERROS DE GRAMATICA EM ATIVIDADE NO BANCO DE DADOS/SCRIPT!!!!!!!
def inserir_atividade(id, academico_email, instituicao, disciplina, num_request, caminho_arquivo):
    insert_scrip = 'INSERT INTO ATIVIDADE (atvid, academico_email, instituicao, disciplina, numQuest, caminhoArquivo) VALUES (%s, %s, %s, %s, %s, %s);'
    insert_values = (id, academico_email, instituicao, disciplina, num_request, caminho_arquivo)
    cur.execute(insert_scrip, insert_values)


def inserir_lista(gabarito, id):
    insert_scrip = 'INSERT INTO LISTA (gabarito, atvid) VALUES (%s, %s);'
    insert_values = (gabarito, id)
    cur.execute(insert_scrip, insert_values)


def inserir_conteudo(materia, id):
    insert_scrip = 'INSERT INTO LISTA (gabarito, atvid) VALUES (%s, %s);'
    insert_values = (materia, id)
    cur.execute(insert_scrip, insert_values)


def inserir_prova(tipo, id):
    insert_scrip = 'INSERT INTO LISTA (tipo, atvid) VALUES (%s, %s);'
    insert_values = (tipo, id)
    cur.execute(insert_scrip, insert_values)


def inserir_pesquisa(id_atividade, email_academico):
    insert_script = 'INSERT INTO PESQUISA (atvid_atividade, email_academico) VALUES (%s, %s);'
    insert_values = (id_atividade, email_academico)
    cur.execute(insert_script, insert_values)


def pesquisa(disciplina, tipo):
    if tipo == 'prova':
        select_script = 'select disciplina, tipo, caminhoArquivo from atividade LEFT JOIN prova where disciplina=' + disciplina + ';'
        cur.execute(select_script)
        dados = cur.fetchall()
        return dados
    elif tipo == 'lista':
        select_script = 'select disciplina, gabarito, caminhoArquivo from atividade LEFT JOIN lista where disciplina=' + disciplina + ';'
        cur.execute(select_script)
        dados = cur.fetchall()
        return dados
    else:
        print("\nNao foi possivel realizar a pesquisa")


def conexao_server():
    # conexao com o servidor do bd
    try:
        conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd,
                                port=port_id)  # funcao que estabelece conexao com o bd
        cur = conn.cursor()  # funcao para auxiliar nas operacoes sql

    except Exception as error:
        print(error)
    return cur


def termina_conexao():
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


def login():
    # ler dados: email, nome, etc
    # verificar email
    email = input("\nDigite seu email: ")
    nome = input("\nDigite seu nome: ")
    instituicao = input("\nQual e sua instituicao?")
    tipo = input("Voce e docente?")
    if not verficar_email(email):
        print("\nEmail invalido!")

    try:
        inserir_academico(email, nome, tipo, instituicao)
        conn.commit()
    except Exception as error:
        print(error)
    # conn.commit()
    while True:
        opcao = input("\nDeseja enviar ou pesquisar uma atividade? Digite sair para encerrar: ").lower()
        print(opcao)
        if opcao == 'sair':
            break
        elif opcao != 'enviar' or opcao != 'pesquisar':
            print("\nOpcao invalida!")
        else:
            if opcao == 'pesquisar' or opcao == "pesquisa":
                tipo = input("\nPesquisar por uma lista ou prova")
                disciplina = input("\nQual disicplina?")
                dados = pesquisa(disciplina, tipo)
                for linha in dados:
                    print(linha)
                # inserir a pesquisa na tabela pesquisa do bd
            elif opcao == 'enviar':
                # input para receber e registrar atividade no bd
                print("a")
            else:
                print("\nOpcao invalida!")


def pesquisar_aluno_bd(cur, nome, instituicao):
    print(f"select * from academico A where A.nome = '{nome}' and A.instituicao = '{instituicao}';")
    select_script = f"select * from academico A where A.nome = '{nome}' and A.instituicao = '{instituicao}';"
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados


def pesquisar_atividade_disciplina(cur, disciplina=str, instituicao=str, tipo=str):
    select_script = f"select * from atividade A, {tipo} T where (A.atvid = T.atvid and A.disciplina = '{disciplina}')" \
                    f" and A.instuicao = '{instituicao}'" \
                    f" and EXISTS (select * from conteudo C where C.atvid = A.atvid);"
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados


def pesquisar_atividade_conteudo(cur, conteudo=str, instituicao=str, tipo=str):
    select_script = f"select * from atividade A, {tipo} T where (A.atvid = T.atvid " \
                    f" and EXISTS (select * from conteudo C where C.materia = {conteudo});" \
                    f" and A.instuicao = '{instituicao}'"
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados

