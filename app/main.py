import SiteProvas

cur = SiteProvas.conexao_server()
list = SiteProvas.povoar(cur)
SiteProvas.termina_conexao()
