# EVALUACION 01 CURSO BACKEND
# Profesor Eric Railef Mansilla
# Alumno:Juan Mora
from vehiculo import Vehiculo
from automotora import Automotora

def main():


# 1. Crear una automotora

    automotora1 = Automotora("Automotora Inacap")
    
    
# 2. Crear 2 vehículos y una motocicleta agregarlos a la automotora

    vehiculo1 = Vehiculo("Toyota","SUV",2019,36000000)
    vehiculo2 = Vehiculo("Subaru","Impreza",2009,12000000)
    vehiculo3 = Vehiculo("Pulsar","NS 200",2017,6000000)

# 3. Mostrar la información de la automotora y sus vehículos



# Ejecutar programa principal
if __name__ == "__main__":
    main()