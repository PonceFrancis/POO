class vehiculos:
    __marca:str
    __modelo_a:str
    __anio_fabric:int
    __capacidad:int
    __num_plaza:int
    __distancia:float
    __tarifa:float
    def __init__(self, xm, xmod, xanio, cap, np, dis, tar):
        self.__marca = xm
        self.__modelo_a = xmod
        self.__anio_fabric = int(xanio)
        self.__capacidad = int(cap)
        self.__num_plaza = int(np)
        self.__distancia = float(dis)
        self.__tarifa = float(tar)
    
    def tarifa_servicio(self):
        pass
    def get_tarifa(self):
        return self.__tarifa
    
    def get_modelo(self):
        return self.__modelo_a
    def get_anio(self):
        return self.__anio_fabric
    def get_capacidad (self):
        return self.__capacidad
