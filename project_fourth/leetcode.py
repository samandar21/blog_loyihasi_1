class Sam:
    def __init__(self,km,name) :
        self.__km=km
        self.name=name
        
    def get_km(self):
        return self.__km
        
av=Sam(1,'hello')
print(av.get_km())

