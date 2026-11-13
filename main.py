
def SumarMultiplesNumeros(numeros):# Hacemos la funcion SumarMultiplesNumeros que recibe como parametro una lista de numeros y retorna la suma de esos numeros
    return sum(numeros) # le decimos que retorne la suma de los numeros que recibe como parametro


def MultiplicarMultiplesNumeros(numeros):# la funcion MultiplicarMultiplesNumeros recibe como parametro una lista de numeros y retorna la multiplicacion de esos numeros en secuencia, es decir, multiplica el primer numero por el segundo, el resultado por el tercero y asi sucesivamente hasta que se acaben los numeros de la lista
    resultado = 1

    for n in numeros:# hacemos un ciclo for que recorra la lista de numeros y multiplique cada numero por el resultado acumulado
        resultado *= n # multiplicamos el resultado acumulado por el numero actual de la lista 
    return resultado


def EsPar(numero): # usamos la funcion EsPar para comprobar si un numero es par, es decir, si el residuo de la division entre 1 es igual a 0 y el residuo de la division entre 2 es igual a 0
    return numero % 1 == 0 and numero % 2 == 0 


def EsEntero(numero):# usamos la funcion EsEntero para comprobar si un numero es entero, es decir, si el residuo de la division entre 1 es igual a 0
    return numero  % 1 == 0


def main():
    while True:# ciclo while activo hasta que el usuario descida salir del programa con un menu
        print("\n CALCULADORA ")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Comprobar si un número es par")
        print("4. Comprobar si un número es entero")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")# entrada del usuario para seleccionar una opcion del menu

        if opcion == "1":# si el usuario selecciona la opcion 1, se le pedira que ingrese los numeros separados por espacios y se llamara a la funcion SumarMultiplesNumeros con la lista de numeros ingresados como parametro
            numeros = input("Ingresa los números separados por espacios: ")# se le indica que ingrese los numeros separados por espacios y se guardan en la variable numeros establecida en la parte superior del codigo
            lista = [int(n) for n in numeros.split()]# hacemos una lista por comprension que recorra la variable numeros y convierta cada numero en un int y lo guarde en la lista
            print("Resultado:", SumarMultiplesNumeros(lista)) # imprimimos el resultado de la funcion SumarMultiplesNumeros con la lista de numeros ingresados como parametro

        elif opcion == "2": #si el usuario selecciona la opcion 2, se le pedira que ingrese los numeros separados por espacios y se llamara a la funcion MultiplicarMultiplesNumeros con la lista de numeros ingresados como parametro
            numeros = input("Ingresa los números separados por espacios: ") # se le indica que ingrese los numeros separados por espacios y se guardan en la variable numeros establecida en la parte superior del codigo
            lista = [int(n) for n in numeros.split()]# hacemos una lista por comprension que recorra la variable numeros y convierta cada numero en un int y lo guarde en la lista
            print("Resultado:", MultiplicarMultiplesNumeros(lista)) # imprimimos el resultado de la funcion MultiplicarMultiplesNumeros con la lista de numeros ingresados como parametro

        elif opcion == "3": # si el usuario selecciona la opcion 3, se le pedira que ingrese un numero y se llamara a la funcion EsPar con el numero ingresado como parametro
            numero = int(input("Ingresa un número: ")) # se le indica que ingrese un numero y se guarda en la variable numero establecida en la parte superior del codigo
            print("¿Es par?", EsPar(numero))# imprimimos el resultado de la funcion EsPar con el numero ingresado como parametro

        elif opcion == "4": # si el usuario selecciona la opcion 4, se le pedira que ingrese un numero y se llamara a la funcion EsEntero con el numero ingresado como parametro
            numero = float(input("Ingresa un número: ")) # se le indica que ingrese un numero y se guarda en la variable numero establecida en la parte superior del codigo
            print("¿Es entero?", EsEntero   (numero))# imprimimos el resultado de la funcion EsEntero con el numero ingresado como parametro

        elif opcion == "5":# opcion para salir del programa, se imprime un mensaje de despedida y se rompe el ciclo while
            print("Gracias por utilizar la calculadora.")
            break

        else:
            print("Aprenda a escribir.")# mensaje de error si el usuario ingresa una opcion que no esta en el menu


if __name__ == "__main__":# si el archivo es ejecutado directamente, se llama a la funcion main para iniciar el programa
    main()
