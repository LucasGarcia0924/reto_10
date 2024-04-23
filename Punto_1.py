# Se define la funcion promedio
def promedio (arreglo: list) -> float:
    suma: float = 0
    for num in arreglo:
        suma += num
    media = suma/len(arreglo)
    return media # Se retorna un valor flotante
# Se declaran las variables
dato: float
bandera : bool = True
arreglo: list = []
media: float
if __name__ == "__main__": # Función main para indicar el inicio del código
    while bandera == True:
        try: # Permite añadir n elementos al arreglo
            dato = float(input("Ingresa los números que desees, para finalizar digita una \"y\" "))
        except(ValueError): # Finaliza al ingresar un valor diferente a un número
            break
        arreglo.append(dato) 
    media = promedio(arreglo)
    print(f"El valor del promedio de los datos ingresados es {media}")