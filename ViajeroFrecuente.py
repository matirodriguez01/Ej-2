class viajerofrec:
    __numviajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millas = 0

    def __init__(self,num,dni,nom,ape,mill):
        self.__numviajero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ape
        self.__millas = mill

    def retornamill (self):
        return self.__millas

    def acummillas (self,acum):
        self.__millas += acum

    def canjearmillas (self,mill):

        if mill <= self.__millas:
            self.__millas -= mill
            print("\nMillas canjeadas exitosamente")
        else:
            print("\nNo posee la cantidad de millas necesarias para realizar el canje")

    def getnumero(self):
        return int(self.__numviajero)

    def getnombre(self):
        return str(self.__nombre)
