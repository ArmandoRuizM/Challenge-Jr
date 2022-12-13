#Se recibe un arreglo con monedas de diferentes denominaciones, se debe retornar la cantidad minima de dinero que no puede ser devuelta con dichas monedas
def Challenge3(list):
    #Se ordena para que las monedas mas pequeñas queden de primeras
    list.sort()
    limit=0
    #Se llena el arreglo de cambios con la monedas mas pequeña
    changes=[list[0]]
    zeroToLimit=[]
    #Se crean todas las posibles combinaciones hasta llegar al tope maximo de cambio
    for i in list:
        limit = limit + i
    for i in range(1, limit+2, 1):
        zeroToLimit.append(i)
    #Se saca de la lista de monedas la que ya se considero como una posibilidad
    del list[0]
    #Mientras hayan monedas a analizar
    while(len(list)!=0):
        #Se recorre el arreglo de devueltas, y se combina cada una con el valor de la moneda que se analiza
        for i in range(0, len(changes), 1):
            #Si no estaba ya entre la devueltas, se añade
            if(not contained(changes, changes[i]+list[0])):
                changes.append(changes[i]+list[0])
        #Si no estaba aun en las devueltas, se añade la moneda anaizada
        if(not contained(changes, list[0])):
            changes.append(list[0])
        #Se saca la moneda del arreglo para no considerarla mas
        del list[0]
    #Se verifica cual es la devuelta minima que no se puede generar
    for i in range(0, len(zeroToLimit), 1):
        if(not contained(changes, zeroToLimit[i])):
            return zeroToLimit[i]
    

#Metodo auxiliar que recibe una lista y un valor n y determina si el valor n esta contenido en la lista
def contained (list, n):
    contained=False
    for i in range(0, len(list), 1):
        if(list[i]==n):
            contained=True
    return contained
    
print(Challenge3([1,1,1,1,1]))
print(Challenge3([5, 7, 1, 1, 2, 3, 22]))
print(Challenge3([1, 1, 1, 1, 5, 10, 15, 20, 100]))
