from clase_vehiculos import vehiculos
class autobus(vehiculos):
    __tipo_serv:str
    __turno:str
    def __init__(self, xm, xmod, xanio, cap, np, dis, tar, xtip, xt):
        super().__init__(xm, xmod, xanio, cap, np, dis, tar)
        self.__tipo_serv = xtip
        self.__turno = xt
    def get_turno (self):
        return self.__turno
    
    def get_tipo_s(self):
        return self.__tipo_serv
    
    def tarifa_servicio(self):
        tarifa_base= self.get_tarifa()
        if (self.get_tipo_s() == "turista" and self.get_turno() == "nocturno"):
            adicional=(20*float(tarifa_base))//100
            tarifa_base += adicional
        else:
            adicional=(5*tarifa_base)//100
            tarifa_base += adicional
        return tarifa_base