# url_descryption.py
## @file
# URL's do sistema SIGAA. USADAS PARA ACESSAR E VERIFICAR SE O USUÁRIO ESTÁ LOGADO.

MAIN_PAGE = "https://sigaa.unb.br/sigaa"
LOGIN_PAGE = "https://sigaa.unb.br/sigaa/verTelaLogin"
EXTENSION_PAGE = "https://sigaa.unb.br/sigaa/extensao/Atividade/lista.jsf"

pages_valid = {
    'discente' : ["https://sigaa.unb.br/sigaa/portais/discente/discente.jsf", "https://sigaa.unb.br/sigaa/telaAvisoLogon.jsf"],
    'docente' : ["https://sigaa.unb.br/sigaa/portais/docente/docente.jsf"]
}