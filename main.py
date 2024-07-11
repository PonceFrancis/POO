from gestor_lista import lista
from clase_autobuses import autobus
from clase_vanes import vane

def interfaz(GV):
    opcion = -1
    while(opcion != 5):
        try:
            opcion=int(input("""
                            Menu de Opciones
            1.- agregar a la coleccion vehiculos.
            2.- mostrar el tipo del vehiculo segun la posicion ingresada.
            3.- cantidad de vehiculos de cada tipo.
            4.- listado de vehiculos.
            5.- Salir del Menu.
            Ingrese una opcion: """))
            match opcion:
                case 1:    
                    GV.opcion1()
                case 2:
                    pos=int(input("ingrese alguna posicion "))
                    GV.opcion2(pos)
                case 3:
                    GV.opcion3()
                case 4:
                    GV.opcion4()
                case 5:
                    print("saliendo")
                case _:
                    print("opcion no registrada.")
        except ValueError:
            print("ERROR, has ingresado un dato invalido")

if __name__=="__main__":
    GV=lista()
    GV.cargar()
    interfaz(GV)