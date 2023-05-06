import random
continuar=1
print("Usted ha ingresado a nuestra plataforma, por favor indique los siguientes datos: ")
celular= input("Ingrese el número de su celular: ")
contraseña= input("Ingrese su contraseña: ")
if (len(celular)==10 and len(contraseña)==4):
    print("¡Usted ha ingresado exitosamente!")
    valorI=4500
    while continuar==1:
        proceso= int(input("Que quieres hacer, escoje una de las siguientes opcionés menú: \n 1. Saca \n 2. Envia \n 3. Recarga \n 4. Salir\n"))
        if proceso==1:
            puntodeRetiro=int(input("Ingresa \n 1.Punto fisico \n 2. Cajero\n"))
            if puntodeRetiro==1 and valorI>2000:
                codigodeRetiro= random.randint(000000,999999)
                print("Usted escogio punto fisico como forma de retiro y su codigo para retirar es ",codigodeRetiro)
                valorR=int(input("Ingrese el valor a retirar"))
                valorI=valorI-valorR
                print("Usted retito ",valorR," el saldo que le queda en la cuenta es de ",valorI)
            elif puntodeRetiro==2 and valorI>2000:
                codigodeRetiro= random.randint(000000,999999)
                print("Usted escogio cajero como forma de retiro y su codigo para retirar es ",codigodeRetiro)
                valorR=int(input("Ingrese el valor a retirar"))
                valorI=valorI-valorR
                print("¡Retiro exitoso! Usted retito ",valorR," el saldo que le queda en la cuenta es de ",valorI)
            elif (puntodeRetiro==1 or puntodeRetiro==2) and valorI<2000:
                print("¡No te alcanza!")
            else:
                print("¡Transacción invalida!")
        elif proceso==2:
            numEnvio= input("Ingrese por favor el número al que va a realizar el envio")
            valorE=int(input("Ingrese el valor que va a enviar"))
            if valorE<valorI:
                valorI=valorI-valorE
                print("Usted envío ",valorE,"el saldo que le queda en la cuenta es de ",valorI)  
            elif valorE>valorI:
                print("Proceso invalido, saldo insuficiente")
        elif proceso==3:
            valorRec=int(input("Ingrese el valor que va a recargar a su cuenta: \n"))
            print("Usted va a recargar ",valorRec)
            seguro=int(input("¿Esta seguro? Ingrese el número correspondiente\n 1.Si \n 2.No \n"))
            if seguro==1:
                valorI=valorI+valorRec
                print("¡Recarga exitosa! Usted recargo ",valorRec,"el saldo disponible en la cuenta es de ",valorI)
            elif seguro==2:
                print("¡Transacción cancelada!")
            else:
                print("¡Transacción invalida!")
        elif proceso==4:
            print("Usted esta por salir del sistema")
            continuar=int(input("Ingresa 1.Para continuar realizando transacciones o 2. Para salir \n") )
elif (len(celular)!=10 and len(contraseña)!=4):
    print("¡Upps! Tus datos son incorrectos, tienes 3 intentos más.")
    contadorIntentos=1
    while contadorIntentos<4:
        contadorIntentos=contadorIntentos+1
        celular= input("Ingrese su número de celular: ")
        contraseña= input("Ingrese su contraseña: ")
        if len(celular)==10 and len(contraseña)==4:
          print("¡Usted ha ingresado exitosamente!")
        elif (len(celular)!=10 and len(contraseña)!=4):
          print("¡Upps! Tus datos son incorrectos intenta nuevamente.")