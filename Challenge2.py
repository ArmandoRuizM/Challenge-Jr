#Se recibe un arreglo con numeros en orden ascendente y se debe retornar un arreglo con los cuadrados de dichos numeros en orden ascendente.
#En caso que un cuadrado sea mayor a SS, en este caso 88, no se incluira en el nuevo arreglo
def challenge2(list):
    aux = []
    #Se rellena un arreglo auxiliar con los cuadrados:
    for i in list:
        if(i*i <= 88):
            aux.append(i*i)
    #Una vez se tiene el arreglo con todos los cuadrados menores a 88, se ordena y se retorna
    insertion(aux)
    return aux

#Metodo auxiliar de ordenamiento, pues se pedia no usar los proporcionados por python
def insertion(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >=0 and key < list[j] :
                list[j+1] = list[j]
                j -= 1
        list[j+1] = key

print(challenge2([1, 2, 3, 5, 6, 8, 9]))
print(challenge2([-2, -1]))
print(challenge2([-6, -5, 0, 5, 6]))
print(challenge2([-10, 10]))