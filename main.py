from utlidades import mayor_menor, mayor_menor_tres_opciones, contar_vocales, suma_acumulada
# print("Ingrese su nombre")
# nombre= input()


# print("Bienvenido ", nombre)

# print("Ingrese la temperatura que desea convertir")
# Temp= input()
# Temp= float(Temp)
# TempF= (Temp * 9/5)+32

# print("La temperatura convertida en Fahrenheit es: ",TempF)

# numero1= input("Ingrese el primer numero:  ")
# numero2=input("Ingrese el segundo numero:  ")
# numero1= int(numero1)
# numero2= int(numero2)
# operacion= input("Mecione la operacion(Suma, resta, division, multiplicacion)").lower()

# if operacion == "suma" or operacion== "+"  :
#     print("El resultado de la suma es: ", numero1+numero2)


# elif operacion == "resta" or operacion== "-"  :
#         print("El resultado de la resta es: ", numero1-numero2)


# elif operacion == "division" or operacion== "/"  :
#             print("El resultado de la division es: ", numero1/numero2)

# elif operacion == "multiplicacion" or operacion== "*"  :
#                 print("El resultado de la multiplicacion es: ", numero1*numero2)
# else  : print("Operacion invalida")

# print("Columna          Resultado")
# for i in range(1,11):
#     print(i,"          ",numero1*i)




# print(mayor_menor(numero1, numero2))


opcion= ""

while opcion != "salir":
        print("=== Menú ===")
        print("1. Saludar")
        print("2. Ver tabla de multiplicar")
        print("3. Calcular mayor")
        print("4. Calcular mayor entre 3 opciones")
        print("5. Selector de Vocales")
        print("6. Suma acumulada")
        print("10. Salir")

        opcion= input("Elegi una opcion: ").lower()

        if opcion== "1":

            nombre= input("Ingrese su nombre: ")


            print("Bienvenido ", nombre)

        elif opcion=="2":
            numero1= input("Ingrese el primer numero:  ")
            numero2=input("Ingrese el segundo numero:  ")
            numero1= int(numero1)
            numero2= int(numero2)
            print("Columna          Resultado")
            for i in range(1,numero2+1):
                print(i,"          ",numero1*i)

        elif opcion=="3":
            numero1= input("Ingrese el primer numero:  ")
            numero2=input("Ingrese el segundo numero:  ")
            numero1= int(numero1)
            numero2= int(numero2)
            print("El numero mayor entre los 2 ingresados es: ", mayor_menor(numero1,numero2))
        elif opcion=="4":
            numero1= input("Ingrese el primer numero:  ")
            numero2=input("Ingrese el segundo numero:  ")
            numero3=input("Ingrese el tercer  numero:  ")
            numero1= int(numero1)
            numero2= int(numero2)
            numero3= int(numero3)
            print("El numero mayor entre los 2 ingresados es: ", mayor_menor_tres_opciones(numero1,numero2,numero3))
        elif opcion=="5" :
           contar_vocales()
        elif opcion=="6" :
            suma_acumulada()

        elif opcion=="10" or opcion =="salir":
            opcion= "salir"
            print("Hazta luego!")
        else:
            print("Opcion invalida")



           


