import PySimpleGUI as sg

sg.theme('DarkAmber')


def JanelasLoginSenha():
    PaginaLogin = [
        [sg.Text("Bem-Vindo ao Msn!", size=(31, 2), justification='center')],
        [sg.Text("Usuario: ", size=(6, 1)), sg.Input(key='Usuarios', size=(25, 1))],
        [sg.Text("Senha: ", size=(6, 1)), sg.Input(key='Senha', password_char='*', size=(25, 1))],
        [sg.Button("Entrar"), sg.Button("Cadastre-se")]
    ]

    return sg.Window("Msn.exe", PaginaLogin, finalize=True)


def JanelaCadastro():
    PaginaCadastro = [
        [sg.Text("Cadastro", size=(37, 2), justification='center')],
        [sg.Text("Nome: ", size=(12, 1)), sg.Input(key='Nome', size=(25, 1))],
        [sg.Text("CPF: ", size=(12, 1)), sg.Input(key='CPF', size=(25, 1))],
        [sg.Text("Sexo"), sg.Radio("Masculino", 'Sexo', key="SexoM"), sg.Radio("Feminino", 'Sexo', key="SexoF")],
        # [sg.Text("Sexo:"), sg.Checkbox("Masculino", key='Masculino'), sg.Checkbox("Feminino", key='Feminino')]
        [sg.Text("Usuario: ", size=(12, 1)), sg.Input(key='Usuario', size=(25, 1))],
        [sg.Text("Senha: ", size=(12, 1)), sg.Input(key='Senha', password_char='*', size=(25, 1))],
        [sg.Text("Conf.. senha: ", size=(12, 1)), sg.Input(key='CSenha', password_char='*', size=(25, 1))],
        [sg.Button("Cadastrar"), sg.Button("Voltar")]
    ]

    return sg.Window("Cadastro", PaginaCadastro, finalize=True)


def PaginaInicial(Nome, Indice):
    d = ''
    Name = Nome[Indice]
    Primeiro_Nome = []
    for i in range(len(Nome[Indice])):
        Primeiro_Nome.append(Name[i])
        if Name[i] == ' ':
            break
    PagInicial = [
        [sg.Text(f"Bem-Vindo, {d.join(Primeiro_Nome)}.\nQual procedimento desenha realizar?")],
        [sg.Text("\n")],
        [sg.Button("Adicionar Cliente"), sg.Button("Remover Cliente"), sg.Button('Logoff')]
    ]
    return sg.Window("PaginaInicial", PagInicial, finalize=True)
