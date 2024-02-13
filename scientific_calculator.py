import PySimpleGUI as sg
import math

layout = [
    [sg.Input(size=(20, 1), key='-DISPLAY-')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('+'), sg.Button('sin')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-'), sg.Button('cos')],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('*'), sg.Button('tan')],
    [sg.Button('0'), sg.Button('C'), sg.Button('='), sg.Button('/'), sg.Button('sqrt')],
    [sg.Button('log')]
]

window = sg.Window('Scientific Calculator', layout)

expression = ''

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED: 
       break

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', 'sin', 'cos', 'tan', 'log', 'sqrt','C','=']:
        if event == 'C':
            expression = ''
            window['-DISPLAY-'].update('')
        elif event == '=':
            try:
                result = eval(expression)
                window['-DISPLAY-'].update(result)
            except (ZeroDivisionError, SyntaxError, ValueError):
                window['-DISPLAY-'].update('Error')

        elif event == 'sin':
            try:
                result = math.sin(math.radians(float(expression)))
                window['-DISPLAY-'].update(result)
                expression = str(result)
            except (ValueError, ZeroDivisionError):
                window['-DISPLAY-'].update('Error')

        elif event == 'cos':
            try:
                result = math.cos(math.radians(float(expression)))
                window['-DISPLAY-'].update(result)
                expression = str(result)
            except (ValueError, ZeroDivisionError):
                window['-DISPLAY-'].update('Error')

        elif event == 'tan':
            try:
                result = math.tan(math.radians(float(expression)))
                window['-DISPLAY-'].update(result)
                expression = str(result)
            except (ValueError, ZeroDivisionError):
                window['-DISPLAY-'].update('Error')

        elif event == 'log':
            try:
                result = math.log10(float(expression))
                window['-DISPLAY-'].update(result)
                expression = str(result)
            except (ValueError, ZeroDivisionError):
                window['-DISPLAY-'].update('Error')

        elif event == 'sqrt':
            try:
                result = math.sqrt(float(expression))
                window['-DISPLAY-'].update(result)
                expression = str(result)
            except (ValueError, ZeroDivisionError):
                window['-DISPLAY-'].update('Error')
        else:
            expression += event
            window['-DISPLAY-'].update(expression)
