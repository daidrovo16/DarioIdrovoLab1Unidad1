#Titulo
print("Reloj Despertador")
def RelojDesp():
    #Se inicializan los objetivos, en este caso son 3 locaciones 
    #Al inicializar lo objetivos, se indica los estados despierto 0 y dormido 1
    #Al activar la alarma se encontrara en el estado activado 0 y desactivado 1
    habitaciones = {'habitacion_1':'0','habitacion_2':'0','habitacion_3':'0'}
    horaDespertar =  0
    
    ubicacion_habitacion = input('Ingrese habitacion: ')#Ingreso de habitacion en el que el despertador se activara
    activarAlarma = input('Estado del usuario en la habitacion: ' + ubicacion_habitacion)#Estado en el que se encuentra el estado en la habitacion
    complemento_activoAlarma = input('Ingreso del estado de los usuario en las otras habitaciones: ')
    print("Estado objetivo de las habitaciones" + str(habitaciones))
    
    if ubicacion_habitacion == 'habitacion_1':
        print('Ingrese el estado de la alarma : ' + ubicacion_habitacion)
        print("\nAccion de alarma Activada 0 y Desactivada 1\n")
        if activarAlarma == '1':
            #El usuario de la habitacion seleccionada se despertara
            habitaciones['habitacion_1'] = '0'
            horaDespertar += 1 ##Calidad de sueño obtenida
            print("Alarma activada en habitacion designada: ")
            print("Incremento en la calidad del sueño: " + str(horaDespertar))
        else:
            print("Activar alarmas de la habitaciones 2 y 3")
            horaDespertar += 1 #Aumento en calidad de sueño por activacion de alarmas
            print("Incremento en la calidad del sueño: " + str(horaDespertar))
            #El usuario de las habitaciones 2 y 3 se despiertan
            habitaciones['habitacion_2'] = '0' #Activacion de alarmas
            habitaciones['habitacion_3'] = '0' #Activacion de alarmas
            horaDespertar += 1 ##Aumento en calidad de sueño obtenida por activacion de alarma
            print("Alarmas activada en las habitaciones 2 y 3: " )
            print("Incremento en la calidad del sueño: " + str(horaDespertar))    
    elif activarAlarma == '0':
            print("En la habitacion_1 el usuario se encuentra despierto")
            if complemento_activoAlarma == '1':
                print("En las habitaciones 2 y 3 se encuetra desactivada la alarma")
                horaDespertar += 1 #Aumento en la calidad de sueño por activar alarma
                print("Incremento en la calidad del sueño: " + str(horaDespertar))
                #Activacion de alarma, se marca el usuario despierto
                habitaciones['habitacion_2'] = '0'
                habitaciones['habitacion_3']= '0'
                horaDespertar += 1 #Aumento en calidad de sueño obtenida por activacion de alarma
                print("Alarma activa y usuarios depiertos")
                print("Incremento en la calidad del sueño: " + str(horaDespertar))          
            else:
                print("No se activa la alarma: " + str(horaDespertar))
                print(horaDespertar)
                #Usuario de cada habitacion despierto
                print("Alarmas habitacion 2 y 3 activas")
    elif activarAlarma == '1':
        print("La alarma desactivada en la habitacion 2")
        habitaciones['habitacion_2'] = '0'
        horaDespertar += 1 #Aumento en calidad de sueño obtenida por activacion de alarma
        print("Incremento en la calidad del sueño: " + str(horaDespertar))    
        print("Alarma de habitacion 2 activada")

        if complemento_activoAlarma == '1':#Si las alarmas de las habitaciones 1 y 3 esan desactivadas
            print("Alarma desactivada en las habitaciones 1 y 3")
            horaDespertar += 1 #Aumento en calidad de sueño obtenida por activacion de alarma
            print("Incremento en la calidad del sueño: " + str(horaDespertar))  
            habitaciones['habitacion_1'] = '0'
            habitaciones['habitacion_3'] = '0'
            horaDespertar += 1 #Aumento en calidad de sueño obtenida por activacion de alarma
            print("Incremento en la calidad del sueño: " + str(horaDespertar))
        elif complemento_activoAlarma == '1':
            print("La alarma desactivada en la habitacion 3")
            habitaciones['habitacion_3'] = '0'
            horaDespertar += 1 #Aumento en calidad de sueño obtenida por activacion de alarma
            print("Incremento en la calidad del sueño: " + str(horaDespertar))    
            print("Alarma de habitacion 3 activada")
            print(horaDespertar)
            
    #Alarma activa en las habitaciones
    print("Estado del usuario en cada habitacion:")
    print(habitaciones)
    print("Calidad de sueño: " + str(horaDespertar))
    
RelojDesp()