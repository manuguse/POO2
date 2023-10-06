#from data_DAO import DataDAO
from system_view import SystemView

class System:
    def __init__(self):
        #self.__data_DAO = DataDAO()
        self.__screen = SystemView()

    def start(self):
        self.__screen.show_screen()
        while True:
            event, values = self.__screen.get_events()
            
            if event == sg.WIN_CLOSED:
                break
            
            