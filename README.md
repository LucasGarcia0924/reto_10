# Reto_10
Evidencia del cumplimiento de las actividades propuestas en el reto ya mencionado.
## Punto 1
Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
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
```
## Punto 2
Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```python
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
```
## Punto 3
Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
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
```
