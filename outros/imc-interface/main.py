import PySimpleGUI as sg

fonte = ('Gill Sans MT', 11)
fonte_titulo = ('Gill Sans MT Negrito', 13)
sg.theme('LightBlue3')
sg.set_options(font=fonte)

def verifica_condicao(imc):
    condicoes = {18.5: 'Abaixo do peso', 25: 'Peso normal', 30: 'Sobrepeso', 35: 'Obesidade grau 1', 40: 'Obesidade grau 2'}
    for valor in condicoes:
        if imc < valor:
            return condicoes[valor]
    return 'Obesidade grau 3'

layout = [
    [sg.Text('Calculadora de IMC', font=fonte_titulo, key='-TITULO-', 
             expand_x=True, justification='center')],
    [sg.Text('Peso (kg):', size=(12,1)), sg.Input(key='peso')],
    [sg.Text('Altura (m):', size=(12,1)), sg.Input(key='altura')],
    [sg.Button('Enviar', size=(7,1)), sg.Button('Sair', size=(7,1))]]
    

window = sg.Window('Calculadora de IMC', layout)

while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    peso = float(values['peso'])
    altura = float(values['altura'])
    imc = peso / (altura ** 2)
    sg.Popup(f'Seu IMC é: {imc:.2f}\n{verifica_condicao(imc)}')
window.close()

