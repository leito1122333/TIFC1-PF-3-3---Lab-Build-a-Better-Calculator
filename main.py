
def addmultiplenumbers(numeros):
    # Recibe una lista de numeros y retorna la suma de todos ellos.
    return sum(numeros)


def multiplymultiplenumbers(numeros):
    # Recibe una lista de numeros y multiplica sus elementos en secuencia.
    resultado = 1

    for n in numeros:
        # Multiplicamos el resultado acumulado por el numero actual.
        resultado *= n

    return resultado


def isiteven(numero):
    # Comprueba si el numero es entero y si es divisible entre 2.
    return numero % 1 == 0 and numero % 2 == 0


def isitaninteger(numero):
    # Comprueba si el numero es entero.
    return numero % 1 == 0


def main():
    print("Hello learners!")   
    # Ciclo que mantiene activo el menu hasta que el usuario decida salir.
    while True:
        print("\n CALCULADORA")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Comprobar si un número es par")
        print("4. Comprobar si un número es entero")
        print("5. Salir")
        

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Solicita varios numeros separados por espacios.
            numeros = input("Ingresa los números separados por espacios: ")
            lista = [float(n) for n in numeros.split()]

            print("Resultado:", addmultiplenumbers(lista))

        elif opcion == "2":
            # Solicita varios numeros para multiplicarlos.
            numeros = input("Ingresa los números separados por espacios: ")
            lista = [float(n) for n in numeros.split()]

            print("Resultado:", multiplymultiplenumbers(lista))

        elif opcion == "3":
            # Comprueba si el numero ingresado es par.
            numero = float(input("Ingresa un número: "))

            print("¿Es par?", isiteven(numero))

        elif opcion == "4":
            # Comprueba si el numero ingresado es entero.
            numero = float(input("Ingresa un número: "))

            print("¿Es entero?", isitaninteger(numero))

        elif opcion == "5":
            # Finaliza el programa.
            print("Gracias por utilizar la calculadora.")
            break

        else:
            print("Aprenda a escribir")


if __name__ == "__main__":
    main()
