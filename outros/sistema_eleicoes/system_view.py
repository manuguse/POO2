import PySimpleGUI as sg

class SystemView:
    
    def __init__(self) -> None:
        self.__container = []  
        self.__WIDTH = 600
        self.__HEIGHT = 500
        self.__window = sg.Window('Sistema de Apuração de Eleições', self.__container, size=(self.__WIDTH, self.__HEIGHT), element_justification='c')
        
        
    def show_screen(self):
        sg.theme = 'DarkAmber'
        self.__container = [
            [sg.Text('Sistema de Apuração de Eleições', size=(self.__WIDTH, 1), justification='center', font=("Poppins Bold", 16), pad=(6, 20))],
        ]
        self.__window = sg.Window('Sistema de Apuração de Eleições', self.__container, size=(self.__WIDTH, self.__HEIGHT), element_justification='c')
        
    def get_events(self):
        return self.__window.read()