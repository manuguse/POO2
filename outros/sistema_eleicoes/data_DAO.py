import pickle

class DataDAO:
    
    def __init__(self):
        self.__datasource = 0 #datasource
        self.__cache = {}
        #try:
        #    self.__load()
        #except:
        #    self.__dump()
            
    