#test files
def pruebasCargaPrint():
    j1 =  Personaje(Coordenada(1,1),False,1,100,[],6)
    c1 = Cultivo(Coordenada(1,1),TOMATE,True,10)    
    c2 = Cultivo(Coordenada(2,5),LECHUGA,True,4)
    cultivos = []
    cultivos.append(c1)
    cultivos.append(c2)
    
    huerta2 = Huerta(8,True,cultivos,9)
    huerta3 = Huerta(10,False,cultivos,1)
    huertas = []
    huertas.append(huerta2)
    huertas.append(huerta3)
    o1 = Objeto(Coordenada(3,3),'F')
    o2 = Objeto(Coordenada(3,3),'F')
    objetos = []
    objetos.append(o1)
    objetos.append(o2)
    juego1 = Juego(10,objetos,4,huertas,Coordenada(1,1),j1)
    juego1.__str__()
