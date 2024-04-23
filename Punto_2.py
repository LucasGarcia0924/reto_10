# Se define la función producto punto
def producto_dot (arreglo_1: list, arreglo_2: list) -> int:
    producto: int = 0
    for num, num2 in zip(arreglo_1, arreglo_2):
        producto += num*num2
    return producto # Retorna el valor entero
# Se declaran las variables
dato: int
bandera : bool = True
arreglo_1: list = []
arreglo_2: list = []
producto_punto: int
if __name__ == "__main__": # Función main para indicar el inicio del código
    while bandera == True:
        try: # Permite ingresar n elementos al arreglo
            dato = int(input("Ingresa los números que desees, para finalizar digita una \"y\" "))
        except(ValueError): # Termina al ingresar un valor no numérico
            break
        arreglo_1.append(dato)
    print(f"Ya que el arreglo anterior tiene {len(arreglo_1)} elementos,")
    # Va a aceptar valores hasta llegar a la misma cantidad de los que tiene el arreglo 1
    while bandera == True or len(arreglo_2) < len(arreglo_1): 
        bandera = False
        dato = int(input("Ahora ingresa la misma cantidad para el arreglo 2 "))
        arreglo_2.append(dato)
    producto_punto = producto_dot(arreglo_1, arreglo_2) # Se llama a la función
    print(f"El producto punto de los arreglos ingresados es {producto_punto}")