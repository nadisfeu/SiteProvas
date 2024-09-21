import psycopg2
import re

hostname = 'localhost'
database = 'SiteProvas'
username = 'postgres'
pwd = '123456'
port_id = 5432
conn = None
cur = None

def verficar_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)


#funcoes de insercao
def _inserir_academico_(email, nome, instituicao, tipo):
    insert_scrip = 'INSERT INTO ACADEMICO (email, nome, instituicao, tipo) VALUES (%s, %s, %s, %s)'
    insert_values = (email, nome, instituicao,tipo)
    cur.execute(insert_scrip, insert_values)

#CORRIGIR ERROS DE GRAMATICA EM ATIVIDADE NO BANCO DE DADOS/SCRIPT!!!!!!!
def inserir_atividade(id, academico_email, instituicao, disciplina, num_request, caminho_arquivo):
    insert_scrip = 'INSERT INTO ATIVIDADE (atvid, academico_email, instituicao, disciplina, numrequest, caminhoarquivo) VALUES (%s, %s, %s, %s, %s, %s)'
    insert_values = (id, academico_email, instituicao, disciplina, num_request, caminho_arquivo)
    cur.execute(insert_scrip, insert_values)

def inserir_lista(id, academico_email, instituicao, disciplina, num_request, caminho_arquivo, gabarito):
    insert_scrip = 'INSERT INTO LISTA (atvid, academico_email, instituicao, disciplina, numrequest, caminhoarquivo, gabarito) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    insert_values = (id, academico_email, instituicao, disciplina, num_request, caminho_arquivo, gabarito)
    cur.execute(insert_scrip, insert_values)

def inserir_prova(id, academico_email, instituicao, disciplina, num_request, caminho_arquivo, tipo):
    insert_scrip = 'INSERT INTO LISTA (atvid, academico_email, instituicao, disciplina, numrequest, caminhoarquivo, tipo) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    insert_values = (id, academico_email, instituicao, disciplina, num_request, caminho_arquivo, tipo)
    cur.execute(insert_scrip, insert_values)


#conexao com o servidor do bd
try:
    conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id) #funcao que estabelece conexao com o bd
    cur = conn.cursor() #funcao para auxiliar nas operacoes sql

    #ler dados: email, nome, etc
    #verificar email
    email = input("\nDigite seu email: ")
    nome = input("\nDigite seu nome: ")
    instituicao = input("\nQual e sua instituicao?")
    curso = input("\nInforme seu curso: ")
    #inserir_aluno('fernando@gmail.com', 'Fernando', 'ufop', 'computacao') #apenas teste
    if verficar_email(email):
        inserir_aluno(email, nome, instituicao, curso)
        print("\nConta registrada com sucesso!")
    else:
        print("\nEmail invalido!")
    conn.commit()



except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
