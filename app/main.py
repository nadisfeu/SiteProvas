import SiteProvas

cur = SiteProvas.conexao_server()
list = SiteProvas.inserir_academico(cur, 'alexandre@ufop', 'Alexandre', 'Professor', 'UFOP')
SiteProvas.termina_conexao()
