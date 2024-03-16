import PySimpleGUI as sg
from math import sin,cos,log,tan,sqrt

layout = [
    [sg.Input(size=(20, 1), key='-DISPLAY-')],
    [sg.Button('('), sg.Button(')'),],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('+'), sg.Button('sin')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-'), sg.Button('cos')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('*'), sg.Button('tan')],
    [sg.Button('0'), sg.Button('Clear'), sg.Button('='), sg.Button('/'), sg.Button('sqrt')],
    [sg.Button('log'), sg.Button('.')]
]

window = sg.Window('Scientific Calculator', layout, finalize=True)
window['-DISPLAY-'].bind("<Return>", "_Enter")
expression = ''

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED: 
       break

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', 'sin', 'cos', 'tan', 'log','.','(',')', 'sqrt','Clear','=','-DISPLAY-_Enter']:
        if event == 'Clear':
            expression = ''
            window['-DISPLAY-'].update('')
        elif event == '-DISPLAY-_Enter' or event == '=':
            try:
                result = eval(values['-DISPLAY-'])
                window['-DISPLAY-'].update(result)
            except (ZeroDivisionError, SyntaxError, ValueError, NameError):
                window['-DISPLAY-'].update('')
                sg.popup("This cannot be calculated!")

        elif event in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            expression += event
            expression += '('
            window['-DISPLAY-'].update(expression)
        else:
            expression += event
            window['-DISPLAY-'].update(expression)
        
