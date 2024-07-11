from clase_vehiculos import vehiculos
class vane(vehiculos):
    __tipo_carr:str
    def __init__(self, xm, xmod, xanio, cap, np, dis, tar,tc):
        super().__init__(xm, xmod, xanio, cap, np, dis, tar)
        self.__tipo_carr = tc
    def get_tipo_carr(self):
        return self.__tipo_carr
    def tarifa_servicio(self):
        tarifa_base= self.get_tarifa()
        if (self.get_tipo_carr() == "minivan"):
            descuento=(10*tarifa_base)//100
            tarifa_base -= descuento
        else:
            adicional=(2.5*tarifa_base)//100
            tarifa_base += adicional
        return tarifa_base