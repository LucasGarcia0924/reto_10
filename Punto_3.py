# Se declaran las variables
arreglo: list = []
dato: int
if __name__ == "__main__": # Función main para indicar el inicio del código
    while True:
        try: # Permite ingresar n datos a los arreglos
            dato = int(input("Ingresa los números que desees, para finalizar digita una \"y\" "))
        except(ValueError): # Se termina al ingresar un dato no numérico
            break
        arreglo.append(dato)
    # Se imprime la cuenta de la cantidad de veces que el valor "0" se encuentra en el arreglo
    print(f"El número de veces que se encuentra el 0 en la lista es de {arreglo.count(0)}")