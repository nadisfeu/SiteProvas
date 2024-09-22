import SiteProvas

cur = SiteProvas.conexao_server()
list = SiteProvas.pesquisar_aluno_bd('fernando', 'ufop', cur=cur)
print(list)
SiteProvas.termina_conexao()
