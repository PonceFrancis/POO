import csv
from clase_vehiculos import vehiculos
from clase_autobuses import autobus
from clase_vanes import vane
class lista:              
    __lista_veh:list
    def __init__(self):
        self.__lista_veh = []
    def agregar (self,unvehiculo):
        self.__lista_veh.append(unvehiculo)

    def cargar(self):
        salto = True
        archivo=open('Vehiculos.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if salto:
                salto = not salto
            else:
                if (fila[0] == "A"):
                    self.agregar(autobus(*fila[1:]))
                else:
                    self.agregar(vane(*fila[1:9]))
        archivo.close()
        
    def opcion1(self):
        try:
            tipo=input("ingrese tipo de vehiculo < A:autobus ; V:vane >: ")
            marc=input("ingrese la marca del vehiculo ")
            mod=input("ingrese el modelo del vehiculo ")
            anio=input("ingrese el anio ")
            cap=int(input("ingrese la capacidad del vehiculo "))
            nplaza=int(input("ingrese el numero de plaza "))
            dis=float(input("ingrese la distancia recorrida "))
            tar=float(input("ingrese la tarifa del vehiculo"))
            if (tipo == "A"):
                tip_s=input("ingrese el tipo de servicio del autobus")
                turn=input("ingrese el turno ")
                self.agregar(autobus(marc, mod, anio, cap, nplaza, dis, tar, tip_s, turn))
            elif(tipo == "V"):
                tcarroceria=input("ingrese el tipo de carroceria ")
                self.agregar(vane(marc, mod, anio, cap, nplaza, dis, tar, tcarroceria))
        except ValueError:
            print("HAS INGRESADO UN DATO INVALIDO")
            
    def opcion2(self, pos):
        i=0
        if (pos >= 0 and pos < len(self.__lista_veh)):
            while(i<len(self.__lista_veh)):
                if(i == pos):
                    if(isinstance(self.__lista_veh[i],autobus)):
                        print("el tipo de vehiculo del posicion ingresado es autobus")
                    elif(isinstance(self.__lista_veh[i],vane)):
                        print("el tipo del vehiculo es de tipo vane ")
                i+=1
                
    def opcion3(self):
        contA=0
        contV=0
        for i in range (len(self.__lista_veh)):
            if (isinstance(self.__lista_veh[i], autobus)):
                contA += 1
            elif(isinstance(self.__lista_veh[i],vane)):
                contV +=1
        print("la cantidad de vehiculo autobus son ",contA)
        print("la cantidad de vehiculos vane son ",contV)
     
    def opcion4(self):
        for i in range (len(self.__lista_veh)):
            print("modelo ", self.__lista_veh[i].get_modelo())
            print("anio de fabricacion ", self.__lista_veh[i].get_anio())
            print("capacidad de pasajeros ", self.__lista_veh[i].get_capacidad())
            print("tarifa del servicio ", self.__lista_veh[i].tarifa_servicio())
        

