#Se recibe el arreglo y se va pasando cada número a un nuevo arreglo pero en una posicion diferente, el valor de S es 8
def challenge1(list):
    aux = []
    result = []
    #Se crea un arreglo auxiliar pero al reves, asegurando que cada numero termina en una posicion distinta
    for i in range(len(list)-1, -1, -1):
        aux.append(list[i])
    #Se convierte el arreglo en un string para remover los numeros >= a S, es decir, a 8
    strList=str(aux)
    strList1=strList.replace('8','')
    strList2=strList1.replace('9','')
    strList3=strList2.replace('[','')
    strList4=strList3.replace(']','')
    #Se convierte nuevamente en un arreglo
    ultimateStrList = strList4.split(',')
    #Se pasa nuevamente a un arreglo de números
    for i in range(0, len(ultimateStrList), 1):
        if (ultimateStrList[i]!=' ' and ultimateStrList[i]!=''):
            result.append(int(ultimateStrList[i]))
    return result

print(challenge1([1, 2, 3, 4, 5, 8]))
print(challenge1([10, 20, 30, 40]))
print(challenge1([8]))
print(challenge1([88]))
print(challenge1([85]))
print(challenge1([8, 2, 1]))
print(challenge1([80, 8, 5, 4, 3, 2, 9, 9, 29, 1]))