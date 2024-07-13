import random
from format_resources import *
from constants import *
#import time
#import pyautogui
# MANHATAN - TERRENO -
    

### JUGADOR associated functions
def mover_personaje(personaje,mov,juego):
    from granja import Coordenada
    coord_jugador = Coordenada(personaje.posicion.fila,personaje.posicion.columna)
    
    if ARRIBA ==  mov and coord_jugador.fila - 1 in range(TAMAÑO_MATRIZ):
        coord_jugador.fila = coord_jugador.fila-1
    elif ABAJO == mov and (coord_jugador.fila + 1) in range(TAMAÑO_MATRIZ):
        coord_jugador.fila = coord_jugador.fila + 1
    elif IZQUIERDA == mov and (coord_jugador.columna - 1) in range(TAMAÑO_MATRIZ):
        coord_jugador.columna = coord_jugador.columna -1
    elif DERECHA == mov and (coord_jugador.columna + 1) in range(TAMAÑO_MATRIZ):
        coord_jugador.columna = coord_jugador.columna + 1
    else:
        return False, None
    return True, coord_jugador
def set_jugador(juego):
    from granja import Juego
    es_repetida = True
    while es_repetida:
        coord_personaje = get_coord_random()
        es_repetida = es_coord_repetida(coord_personaje,BLANCANIEVES,3,juego)
    juego.jugador.posicion = coord_personaje
    juego.jugador.cant_monedas = MONEDAS_INICIAL   
###
### JUEGO FUNCTIONS 
def actualizar_movimiento(juego):
    juego.cant_movimiento +=1
def refresh_money(amount, juego):    
    msg_fail = "- SALDO INSUFICIENTE - "
    msg_success = get_only_center_text(" - TRANSACCIÓN EXITOSA - ")    
    msg_saldo = " - SALDO ACTUAL $" +str(juego.jugador.cant_moneda)+ " -"
    #msg_saldo = get_only_center_text(msg_saldo)
    if juego.jugador.cant_moneda + amount >= 0:
        juego.jugador.cant_moneda += amount
        msg_saldo = " - SALDO ACTUAL $" +str(juego.jugador.cant_moneda) + " -"
        return True, get_center_text(msg_success) + "\n" + get_center_text(msg_saldo) + "\n"
    else:
        return False,get_center_text(msg_fail)+"\n"+get_center_text(msg_saldo) 
###
### TERRENO functions    
def cargar_tamaño_terreno():
    while True:
        try:
            size = int(input("Ingrese el tamaño de la matriz: "))
            while size not in range(8,16):
                size = int(input("TAMAÑO FUERA DE RANGO\nIngrese el tamaño de la matriz (8 a 15): "))
            return size
        except ValueError:
            print("Error en input")     
def menu_terreno():
    print_empty_bar()
    mov = (input("\t¡Muévase por el terreno -> W: arriba - S: abajo - D: derecha - A: izquierda!: ")).upper()
    print_empty_bar()    
    while mov not in [ARRIBA,ABAJO,IZQUIERDA,DERECHA]:
        print_bar()
        print_empty_bar()        
        mov = (input("\tError: ¡Muévase por el terreno -> W: arriba - S: abajo - D: derecha - A: izquierda!: ")).upper()
        print_empty_bar()
    return mov   
def sobre_objeto(coord,juego):
    """
    Args: game, and coord (where plant or character is standing on)
    It returns the specific object (espina,fert, etc) where coord is the same. If is in a ubication without object, it send NONE
    Only send objects but not garder_objects
    """
    for objeto in juego.objetos:
        if objeto.posicion.es_igual(coord):
            return objeto
    return None
def distancia_manhatan(juego):
    return False
def identificar_ubicacion(juego):
    from granja import Coordenada
    coord_jugador = Coordenada(juego.jugador.posicion.fila,juego.jugador.posicion.columna)
    
    sobreHuerta, cultivo = sobre_huerta(coord_jugador,juego)
    if sobreHuerta:
        return HUERTA, cultivo
    
    resultado,objeto = ocupadoXobjeto(coord_jugador,juego)
    if resultado:
        return objeto.tipo, objeto
    
    return TERRENO, None
def get_coord_random():
    from granja import Coordenada
    return Coordenada(random.randint(0,TAMAÑO_MATRIZ-1),random.randint(0,TAMAÑO_MATRIZ-1))
def es_coord_repetida(coord_consultada,elemento,indice_huerta,juego):
    from granja import Juego
    check_all = False
    iguales = False
    if elemento in [ESPINA,OBSTACULO,DEPOSITO,BLANCANIEVES,HERRAMIENTA,PLAGA,FERTILIZANTE]:
        check_all = True
    #CHECK DEPOSIT        
    #CHECK PARA CENTROS HUERTAS
    if iguales != True and elemento == CENTRO_HUERTA:
        for indice_h in range(len(juego.huertas)):
            if indice_h != indice_huerta and coord_consultada.es_igual(juego.huertas[indice_h].cultivos[COORD_CENTRO].posicion) == True:
                return True
    #CHECK CULTIVOS
    if iguales != True and (elemento == CULTIVO or check_all):
        for indice_h in range(indice_huerta):
            for indice_c in range(MAX_CULTIVOS):
                if coord_consultada.es_igual(juego.huertas[indice_h].cultivos[indice_c].posicion):
                    return True
    #CHECK OBJETOS
    if check_all and iguales != True:
        for objeto in juego.objetos:
            if objeto.posicion.es_igual(coord_consultada):
                return True
    return iguales
def sobre_deposito(coord,deposito):
    return (coord.es_igual(deposito) == True )

def ocupadoXobjeto(coord,juego):
    for objeto in juego.objetos:
        if objeto.posicion.es_igual(coord):
            return True,objeto
    return False,None
    # para poblar terreno sin ocupar posicion de DEPOSITO y OBJETOS            
    if sobre_deposito(coord,juego.deposito):
        return True
    for objeto in juego.objetos:
        if objeto.posicion.es_igual(coord):
            return True
    return False
#####################
### OBJECTS functions
def get_espinas(juego):
    from granja import Juego, Objeto
    for i in range(5):
        es_repetida = True
        while es_repetida:
            coord_espina =  get_coord_random()
            es_repetida = es_coord_repetida(coord_espina,ESPINA,3,juego)
        juego.objetos.append(Objeto(coord_espina,ESPINA))   
def load_objeto(juego, tipo_obj):
    from granja import Objeto
    es_repetida = True
    while es_repetida:
        coord_obj = get_coord_random()
        es_repetida = es_coord_repetida(coord_obj,tipo_obj,3,juego)
    juego.objetos.append(Objeto(coord_obj,tipo_obj))  
def get_obstaculos(juego):
    from granja import Juego, Objeto
    es_repetida = True
    for i in range(CANT_OBSTACULOS):    
        while es_repetida:
            coord_obs = get_coord_random()
            es_repetida = es_coord_repetida(coord_obs,OBSTACULO,3,juego)
        juego.objetos.append(Objeto(coord_obs,OBSTACULO))
        es_repetida = True
def pudrir_plaga(juego,obj_plaga):
    juego.objetos.remove(obj_plaga)
###################
###HUERTA functions
def crear_semillas(SEMILLAS):
    from granja import Semilla
    #(tipo=VACIO,compra=0,venta=0,vida=0,cosecha_mov=0):
    SEMILLAS.append(Semilla(TOMATE,5,30,3,2))
    SEMILLAS.append(Semilla(ZANAHORIA,10,50,25,15))
    SEMILLAS.append(Semilla(BROCOLI,15,70,20,10))
    SEMILLAS.append(Semilla(LECHUGA,20,80,15,10)) 
    # title_game = f"<<{'JUEGO':_^90}>>"
    #return f"<<{leyenda}:{char:^100}>>" 
def get_nombre_planta(inicial):
    if inicial == TOMATE:
        return "Tomate"
    elif inicial == LECHUGA:
        return "Lechuga"
    elif inicial == BROCOLI:
        return "Brocoli"
    elif inicial == ZANAHORIA:
        return "Zanahoria"
    else:
        return "Vacío"   
def sobre_huerta(coord_jugador,juego):
    for huerta in juego.huertas:
        for cultivo in huerta.cultivos:
            if cultivo.posicion.es_igual(coord_jugador):
                return True, cultivo
    return False, None
def plantar(juego,cultivo):
    msj_plantar = f"\tEliga la semilla a sembrar o muévase (a,w,s,d) ->\n\t[Z - zanahoria $10][T - tomate $5][L - lechuga $20][B - brocoli $15]: "
    msj_exito = f"\n\tFELICITACIONES! Ha plantado "
    print_bar()
    print_empty_bar()
    semilla_elegida = (input(msj_plantar)).upper()
    print_empty_bar()
    while semilla_elegida not in MOVIMIENTOS and semilla_elegida not in PLANTAS:
        print_bar()
        
        semilla_elegida = (input("\tInválido - " + msj_plantar)).upper()        
    if semilla_elegida in MOVIMIENTOS:
        return semilla_elegida
    else:
        semilla = get_datos_semilla(semilla_elegida)
        result_buy, msg = refresh_money(semilla.compra*-1, juego)
        if result_buy:
            cultivo.tipo = semilla.tipo
            cultivo.ocupado = True
            cultivo.mov_plantado = juego.cant_movimiento
            return msg + msj_exito + f"{(get_nombre_planta(cultivo.tipo)).upper()} por un valor de {semilla.compra} monedas"
        else:
            return msg
def get_datos_semilla(semilla_elegida):
    for semilla in SEMILLAS:
        if semilla.tipo == semilla_elegida:
            return semilla
    print("semilla no encontrada")
    return None  
def menu_huerta(cultivo):
    print_empty_bar()
    nom_planta = get_nombre_planta(cultivo.tipo)
    msj_mov_terreno_huerta = f"\tElija una acción o muévase por el terreno (a,s,w,d) ->\n\t[F - Fertilizar huerta][I - Usar insecticida]"
    msj_cultivo_vacio = f"[P - Plantar]: "
    msj_cultivo_plantado = f"[C - Cosechar {nom_planta}][I - Ver info {nom_planta}]: "
    if cultivo.tipo == VACIO:
        accion = input(f"{msj_mov_terreno_huerta+msj_cultivo_vacio}").upper()
        print_empty_bar()
        while accion not in MOVIMIENTOS and accion not in [FERTILIZANTE,PLANTAR,INSECTICIDA]:
            print_bar()
            accion = input(f"\tINVÁLIDO\n {msj_mov_terreno_huerta+msj_cultivo_vacio}").upper()
    else:
        accion = input(msj_mov_terreno_huerta + msj_cultivo_plantado).upper() 
        print_empty_bar()
        while accion not in MOVIMIENTOS and accion not in [FERTILIZANTE,COSECHAR,INSECTICIDA,INFO]:
            print_bar()
            print_empty_bar()
            accion = (input("\tInválido\n"+ msj_mov_terreno_huerta + msj_cultivo_plantado)).upper()
            print_empty_bar()
    return accion    
def cosechar_planta(juego,cultivo):
    semilla = get_datos_semilla(cultivo.tipo)
    cosecha = (juego.cant_movimiento - cultivo.mov_plantado) - semilla.cosecha_mov
    if cosecha == 0:
        if len(juego.jugador.canasta) < MAX_CANASTA:
            cultivo.tipo = VACIO
            cultivo.ocupado = False
            cultivo.mov_plantado = 0
            juego.jugador.canasta.append(semilla)
            return get_only_center_text(f" FELICIDADES! Planta cosechada: {get_nombre_planta(semilla.tipo).upper()}, vaya al DEPÓSITO para venderla")
        else:
            return f" No hay espacio para seguir cosechando, pase por el depósito para vaciar la CANASTA"
    else:
        return f" Faltan movimientos para cosechar la planta de {get_nombre_planta(semilla.tipo).upper()}"
def get_info_planta(cultivo, mov_juego):
    semilla = get_datos_semilla(cultivo.tipo)
    vida = semilla.vida
    info = get_nombre_planta(semilla.tipo).upper()
    mov_pasados = mov_juego - cultivo.mov_plantado
    mov_cosecha = semilla.cosecha_mov - mov_pasados
    mov_vida = vida - mov_pasados
        
    if mov_cosecha < 0:
        mov_cosecha = 0
    if (mov_cosecha == 0): info = f"Info {info}: LISTO PARA COSECHA! -> Plantado mov nro.: {cultivo.mov_plantado} - Cosecha: {mov_cosecha}/{semilla.cosecha_mov} - Vida: {mov_vida}/{semilla.vida} movimientos"
    else: info = f"Info {info}: Plantado mov nro.: {cultivo.mov_plantado} - Cosecha: {mov_cosecha}/{semilla.cosecha_mov} - Vida: {mov_vida}/{semilla.vida} movimientos"
    return get_center_text(info)   
#################      
###HUERTA creation
def get_huertas(juego):
    """
    Inside of Juego recived, build the 3 HUERTAS with rights coordenates    
    """
    from granja import Huerta, Cultivo, Coordenada, Juego
    es_repetida = True
    for index_h in range(3):
        juego.huertas.append(Huerta())
        juego.huertas[index_h].cultivos = []               
        for index_c in range(MAX_CULTIVOS):
            juego.huertas[index_h].cultivos.append(Cultivo())
            if index_c == 4:
                es_repetida = True
                while es_repetida:
                    coord_centro = get_coord_random()
                    es_repetida = es_coord_repetida(coord_centro,CENTRO_HUERTA,index_h,juego)
                juego.huertas[index_h].cultivos[index_c].posicion = coord_centro
        
        set_coord_superpuestas = auto_gen_coord_cultivos(juego.huertas[index_h])
        for i_c in range(len(set_coord_superpuestas)):
            es_repetida = es_coord_repetida(set_coord_superpuestas[i_c],CULTIVO,index_h,juego)
            #es_coord_repetida(set_coord_superpuestas[i_c],CULTIVO,index_h,juego
            if es_repetida == False and set_coord_superpuestas[i_c].fila in range(TAMAÑO_MATRIZ) and set_coord_superpuestas[i_c].columna in range(TAMAÑO_MATRIZ):
                juego.huertas[index_h].cultivos[i_c].posicion = set_coord_superpuestas[i_c]
def auto_gen_coord_cultivos(huerta):
    """
    Args: Empty huerta with only center position charged
    Return: Array with the eight Coordenadas around HUERTA center position * do not check overwrite position
    """
    from granja import Coordenada, Huerta
    coord_calculadas = []
    center_coord = huerta.cultivos[4].posicion
    index_c = 0
    for factor in range(-1,2,+1):
        for factor2 in range(-1,2,+1):
            if index_c == 4:            
                coord_calculadas.append(center_coord)
            else:
                pos_calculada = Coordenada(center_coord.fila+factor2,center_coord.columna+factor)
                coord_calculadas.append(pos_calculada)
            index_c += 1
    return coord_calculadas
################ 

TAMAÑO_MATRIZ = cargar_tamaño_terreno()