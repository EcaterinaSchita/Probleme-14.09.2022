def creare_lista():
    n=int(input('Nr.de elemente'))
    lista_locala = []
    for i in range(n):
        elem=int(input('Elementul '+str(i)+' este:'))
        if isinstance(elem,int)== True:
            lista_locala.append(int(elem))
        else:
            print(elem+'scrieti inca o data un numar real')
    return  lista_locala
    
lista1 = creare_lista()
print(lista1)
    
    