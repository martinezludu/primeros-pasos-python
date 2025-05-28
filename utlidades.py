def mayor_menor (numero1,numero2):
    if numero1>numero2:
        return numero1
    else : return numero2

def mayor_menor_tres_opciones(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else :
     return c

def contar_vocales():
    vocales = {"a","e","i","o","u"}
    palabra= input("Dime la palabra para asi yo cuento las silabas: ").lower()
    contador= 0
    
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return print("La cantidad en ", palabra, " es de: ", contador, " vocales")


def suma_acumulada():
    numero=0
    ingreso= ""
    while True:
        print("En caso querer finalizar la suma ingrese 'Fin'")
        ingreso= input("Ingrese su numero para ser sumado: ")
        
        if ingreso.lower() == "fin": break
        try 
            ingreso = int(ingreso)
            numero= numero + ingreso
        except ValueError:
            print("Error solo se pueden agregar numeros o 'Fin'")
    return print("La suma acumulada es: ", numero)
