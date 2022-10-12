

def IntroducirRegistro():
    # Solicitamos datos
    nombre = str(input('Introduce el nombre:     '))
    apellidos = str(input("Introduce tus Apellidos:    "))
    # Solicitamos la fecha de nacimiento 
    cumple = input('Ingrese la fecha de nacimiento (dd/mm/aaaa)?') 
    fecha = cumple.split('/') 
    fecha_nacimiento = int(fecha[0]), int(fecha[1]), int(fecha[2])
    # Solicitamos direccion
    print('Ingrese los direcciones') 
    direccion= input("Ingrese direccion:    ")
    # Solicitamos correo
    correo= input("Ingrese su correo electronico:    ")
    # Solicitamos datos de vehiculo
    modelo = input("Modelo de vehiculo:    ")
    marca = input("Marca de vehiculo:    ")
    color = input("Color de vehiculo:    ")
    patente = int(input("Ingrese la patente:   "))

def ComenzarCarrera():
    import math
    def LatLog():
        latin = float(input("Ingrese la latitud inicial:  "))
        login = float(input("Ingrese longitud inicial:   "))
        latfi = float(input("Ingrese latitud final:   ")) 
        logfi = float(input("Ingrese longitud final:   "))
        latfinal = (latfi - latin)
        logfinal = (logfi - logfin)
        trayecto = (latfinal**2 + logfinal**2)
        recorrido = math.sqrt(trayecto)
        totalkm = int(input("Ingrese total por km: "))
        total = (totalkm * recorrido)
        print ("El monto a pagar es ", total)

    km = 10
    def acelerar():
        acelera = 10 + km
        print("El auto acelero 10km/h ahora su velocidad es"  + km + "km/h")
    def frenar():
        frena = km - 10
        print("El auto redujo la velocidad 10km/h ahora su velocidad es " + km + "km/h")
    def parar():
        print("El auto se detiene")
    def girar():
        print ("El vehiculo gira")
    def encender():
        print ("El vehiculo se enciende")

#Programa principal
print("================")
print("======UBER======")
print("================")
while True:
    print('\nMenú Principal') 
    print('(1) Registro') 
    print('(2) Comenzar carrera') 
    opcion = ("Seleccione opcion:   ")
    if opcion == "0":
        break
    elif opcion == "1":
        nuevo_conductor = IntroducirRegistro()
        print ("Se ha creado nuevo usuario")
    elif opcion == "2":
        carrera = ComenzarCarrera()
        
    else: 
        print('No entendí la opción, por favor elige la correcta') 
# Fin del programa 
print('\nGracias por usar esta aplicación') 
