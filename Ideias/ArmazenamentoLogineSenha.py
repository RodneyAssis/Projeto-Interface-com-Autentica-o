import PySimpleGUI as sg
import FuncoesLoginSenha

NomeUsuario = ['Devensolvedor']
CPFUsuario = ['adm']
SexoMascUsuario = ['adm']
SexoFemininUsuario = ['adm']
Sexo = ['Sexo']
UsuarioLogin = ['adm']
UsuarioSenha = ['adm']

dados = {'Nome': NomeUsuario, 'CPF': CPFUsuario,
         'Masculino': SexoMascUsuario, 'Feminino': SexoFemininUsuario,
         'Usuario': UsuarioLogin, 'Senha': UsuarioSenha}
JanelaLogin, JanelaCadastro, PaginaLogin = FuncoesLoginSenha.JanelasLoginSenha(), None, None
while True:
    windows, event, value = sg.read_all_windows()
    print(event)

    # Para Encerrar o programa.
    if (event == sg.WINDOW_CLOSED) and sg.popup_yes_no("Deseja realmente sair?") == 'Yes':
        break

    # Abrir a janela de cadastro.
    if event == 'Cadastre-se':
        JanelaCadastro = FuncoesLoginSenha.JanelaCadastro()
        JanelaLogin.hide()

    # Retornar a tela principal.
    if event == 'Voltar':
        JanelaCadastro.hide()
        JanelaLogin.un_hide()

    # Efetuar o Logoff.
    if event == "Logoff":
        JanelaInicio.hide()
        JanelaLogin.un_hide()

    # Condições para efetuar o cadastro.
    if event == 'Cadastrar':
        if value['Nome'] == '' or value['CPF'] == '' or value['Usuario'] == '' or value['Senha'] == ''\
                or value['CSenha'] == '':
            sg.popup_ok("Preencha todos os dados obrigatorios.", title="Erro no Cadastro.")
        elif len(value['CPF']) != 11 or not value['CPF'].isnumeric():
            sg.popup_ok("Erro no preenchimento do CPF, tente novamente.\n"
                        "Possiveis Erros:\n"
                        "- CPF não pode ser diferente de 11 digitos\n"
                        "- CPF só pode ser números inteiros",
                        title="Erro no Cadastro.")
        elif len(value['Usuario']) < 8 or value['Usuario'] == value['Nome'] or ' ' in value['Usuario']\
                or value['Usuario'] == value['Senha']:
            sg.popup_ok("Erro no preenchimento do usuario, tente novamente.\n"
                        "Possiveis erros:\n"
                        "- Nome de usuario não pode ser menor quê 8 caracteres.\n"
                        "- Usuario não deve ser igual ao nome do cadastrado.\n"
                        "- Usuario e senha iguais.",
                        title="Erro no Cadastro.")
        elif value['SexoM'] is False and value['SexoF'] is False or value['SexoM'] \
                is True and value['SexoF'] is True:
            sg.popup_ok("Preencha todos os dados obrigatorios.", title="Erro no Cadastro.")
        elif value['CPF'] in CPFUsuario:
            sg.popup_ok("CPF já se encontrar em nosso banco de dados.", title='Erro!')
        elif value['Usuario'] in UsuarioLogin:
            sg.popup_ok("Usuario já se encontra cadastrado em nosso banco de dados"
                        "\nTente novamente.", title='Erro!')
        elif value['Senha'] != value['CSenha']:
            sg.popup_ok("Senha incorreta. Tente novamente", title='Erro!')
        else:
            NomeUsuario.append(value['Nome'].title())
            CPFUsuario.append(value['CPF'])
            SexoMascUsuario.append(value['SexoM'])
            SexoFemininUsuario.append(value['SexoF'])
            UsuarioLogin.append(value['Usuario'])
            UsuarioSenha.append(value['Senha'])
            JanelaCadastro.hide()
            sg.popup_ok("Cadastro concluido!")
            JanelaLogin.un_hide()

    # Condições da tela de login.
    if event == 'Entrar':
        if value['Usuarios'] not in UsuarioLogin:
            sg.popup_ok("Usuario não cadastrado.", title="Erro no Login")
        elif value['Usuarios'] == UsuarioLogin[UsuarioLogin.index(value['Usuarios'])] and \
                value['Senha'] != UsuarioSenha[UsuarioLogin.index(value['Usuarios'])]:
            sg.popup_ok("Problema no Usuario ou senha.", title="Erro!")
        else:
            Indice = UsuarioLogin.index(value['Usuarios'])
            JanelaInicio = FuncoesLoginSenha.PaginaInicial(NomeUsuario, Indice)
            JanelaLogin.hide()

            if event == 'Adicionar Cliente':
                JanelaInicio.un_hide()

print(dados)
