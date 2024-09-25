import psycopg2
import re
import random


hostname = 'localhost'
database = 'SiteProvas'
username = 'postgres'
pwd = '123456'
port_id = 5432
conn = None
cur = None
email_geral = None

try:
    conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd,
                            port=port_id)  # funcao que estabelece conexao com o bd
    cur = conn.cursor()  # funcao para auxiliar nas operacoes sql

except Exception as error:
    print(error)


def termina_conexao():
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


def verificar_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)


# funcoes de insercao
def inserir_academico(email, nome, tipo, instituicao):
    insert_scrip = "INSERT INTO academico (email, nome, tipo, instituicao) VALUES (%s, %s, %s, %s);"
    insert_values = (email.lower(), nome.lower(), tipo.lower(), instituicao.upper())
    cur.execute(insert_scrip, insert_values)
    conn.commit()


def inserir_atividade(id, academico_email, instituicao, disciplina, num_quest, caminho_arquivo):
    insert_scrip = 'INSERT INTO atividade (atvid, academico_email, instituicao, disciplina, numquest, caminhoarquivo) ' \
                   'VALUES (%s, %s, %s, %s, %s, %s);'
    insert_values = (id, academico_email.lower(), instituicao.upper(), disciplina.lower(), num_quest, caminho_arquivo)
    cur.execute(insert_scrip, insert_values)
    conn.commit()


def inserir_lista(gabarito, id):
    insert_scrip = 'INSERT INTO lista (gabarito, atvid) VALUES (%s, %s);'
    insert_values = (gabarito, id)
    cur.execute(insert_scrip, insert_values)
    conn.commit()


def inserir_conteudo(materia, id):
    insert_scrip = 'INSERT INTO conteudo (materia, atvid) VALUES (%s, %s);'
    insert_values = (materia, id)
    cur.execute(insert_scrip, insert_values)
    conn.commit()


def inserir_prova(tipo, id):
    insert_scrip = 'INSERT INTO prova (tipo, atvid) VALUES (%s, %s);'
    insert_values = (tipo, id)
    cur.execute(insert_scrip, insert_values)
    conn.commit()


def inserir_pesquisa(id_atividade, email_academico):
    insert_script = 'INSERT INTO pesquisa (atvid_atividade, email_academico) VALUES (%s, %s);'
    insert_values = (id_atividade, email_academico)
    cur.execute(insert_script, insert_values)
    conn.commit()
    
    # Pesquisas

def pesquisa(disciplina, tipo):
    if tipo == 'prova':
        select_script = 'select disciplina, tipo, caminhoarquivo from atividade LEFT JOIN prova where disciplina=' + disciplina + ';'
        cur.execute(select_script)
        dados = cur.fetchall()
        return dados
    elif tipo == 'lista':
        select_script = 'select disciplina, gabarito, caminhoarquivo from atividade LEFT JOIN lista where disciplina=' + disciplina + ';'
        cur.execute(select_script)
        dados = cur.fetchall()
        return dados
    else:
        print("\nNao foi possivel realizar a pesquisa")


def pesquisar_aluno_bd(nome, instituicao):
    print(f"select * from academico A where A.nome = '{nome}' and A.instituicao = '{instituicao}';")
    select_script = f"select * from academico A where A.nome = '{nome}' and A.instituicao = '{instituicao}';"
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados


def pesquisar_por_disciplina(disciplina=str, instituicao=str, tipo=str,  email=str):
    select_script = f"select A.caminhoarquivo from atividade A, {tipo} T where (A.atvid = T.atvid and A.disciplina = '{disciplina}')" \
                    f" and A.instituicao = '{instituicao}'" \
                    f" and EXISTS (select * from conteudo C where C.atvid = A.atvid);"
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados


def pesquisar_por_conteudo(conteudo=str, instituicao=str, tipo=str):
    select_script = f"select * from atividade A, {tipo} T where (A.atvid = T.atvid " \
                    f" and EXISTS (select * from conteudo C where C.materia = {conteudo});" \
                    f" and A.instuicao = '{instituicao}'"
    cur.execute(select_script)
    dados = cur.fetchall()
    return dados


# Povoar
def povoar():
    inserir_academico('jao@ufop', 'jao', 'Aluno', 'UFOP')

    inserir_link_provas_drive(1, 'jao@ufop', 'ufop', 'fisica', 4,
                              'https://drive.google.com/file/d/1U4IFIr-Bs5DcG6w06NYh7m-7s7vN_HOU/view?usp=sharing',
                              1, ['vetor', 'mecanica', 'aceleracao', 'deslocamento'])


def inserir_link_provas_drive(id, email, instituicao, disciplina, num_quest, caminho, tipo, conteudo=list):
    inserir_atividade(id=id, academico_email=email, instituicao=instituicao,
                      disciplina=disciplina, num_quest=num_quest, caminho_arquivo=caminho)
    inserir_prova(tipo=tipo, id=id)
    for conte in conteudo:
        inserir_conteudo(id=id, materia=conte)


def inserir_link_listas_drive(id, email, instituicao, disciplina, num_quest, caminho, gabarito=bool, conteudo=list):
    inserir_atividade(id=id, academico_email=email, instituicao=instituicao,
                      disciplina=disciplina, num_quest=num_quest, caminho_arquivo=caminho)
    inserir_lista(gabarito=gabarito, id=id)
    for conte in conteudo:
        inserir_conteudo(id=id, materia=conte)
        

def novo_login():
    
    while (True):
     email_informado = input("Informe seu email: ")
     script = f"SELECT F.email FROM academico F WHERE EXISTS (SELECT * FROM academico Q WHERE Q.email = '{email_informado}' AND Q.email = F.email) ;"
     cur.execute(script)
     dados = cur.fetchall()
     if not dados:
        print('Cadastro não encontrado')
        nome = input("Digite seu nome: ")
        instituicao = input("Qual e sua instituicao?")
        tipo = input("Voce é aluno ou professor?")
        if not verificar_email(email_informado):
            print("\nEmail invalido!")
            resposta = 0

        else: 
            try:
                inserir_academico(email_informado, nome, tipo, instituicao)
                resposta = 1
            except Exception as error:
                print(error)
        if resposta == 1:
            print("Cadastro efetuado com sucesso!")
            break
        else:
            print("\nCadastro nao foi possivel!")

     else: 
        print('Login efetuado com sucesso')
        break
    email_geral = email_informado
    return email_geral

def resetar_tabelas():

    fd = open(r"C:\Users\PP\Documents\BD\SiteProvas\sql\CriacaoTabela100PorcentoAtualizado.sql",'r')
    arquivo = fd.read()
    fd.close()

    arquivo = arquivo.split(';')

    for comandos in arquivo: 
        try:
            cur.execute(comandos)
        except Exception as error:
            print(error)

def adicionar_prova_usuario(email):
    id = random.random()
    select_script = f"SELECT * FROM atividade F WHERE F.atvid = {id};"
    while cur.execute(select_script):  # verifica se existe alguma atividade com o id
        id = random.random()

    select_script = f"select A.instituicao from academico A where A.email = '{email}'"
    cur.execute(select_script)
    instituicao = cur.fetchall()[0][0]
    disciplina = input("Digite a disciplina da prova: ")
    num_quest = int(input("Digite o numero de questoes: "))
    caminho = input("Cole o link do drive (o link deverá está público):")
    tipo = int(input("Qual o tipo da prova? (1,2,3...)"))
    conteudotemp = input("Digite os conteudos (Ex: algebra linear, integracao,... ")
    conteudo = conteudotemp.split(',')

    inserir_link_provas_drive(id=id, academico_email=email, instituicao=instituicao,
                              disciplina=disciplina, num_quest=num_quest, caminho_arquivo=caminho,
                              tipo=tipo, conteudo=conteudo)
