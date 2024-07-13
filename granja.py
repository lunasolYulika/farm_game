from funciones import *#NOQA
from format_resources import *#NOQA
from constants import * #NOQA
import os #NOQA
###
###CONSTANTES
CANT_COIN_WIN = 30
RAND_MOV_PLAGA = 4
RAND_MOV_FERT = 2

def clear_screen_windows():
    os.system('cls')

###CLASES
class Coordenada:
    def __init__(self,fila=-1,columna=-1):
        self.fila = fila
        self.columna = columna
    def __str__(self):
        return f"({self.fila};{self.columna})"
    def es_igual(self,c2):
        return self.fila == c2.fila and self.columna == c2.columna
class Cultivo:
    def __init__(self,posicion=Coordenada(),tipo=VACIO,ocupado=False,mov_plantado=0):      
        self.posicion=posicion
        self.tipo=tipo
        self.ocupado=ocupado
        self.mov_plantado=mov_plantado
    def __str__(self):
        return f"\t{self.posicion.__str__()}\t\t{self.tipo}\t{self.ocupado}\t\t{self.mov_plantado}"
class Huerta:
    def __init__(self,movimientos_plagado=0,plagado=False,cultivos=None,tope_cultivos=0):
        self.movimientos_plagado=movimientos_plagado
        self.plagado=plagado
        self.cultivos=cultivos
        self.tope_cultivos=tope_cultivos
    def get_cultivos(self):
        encabezado_cultivos = f"\n{'*******************************CULTIVOS**********************************':^90}\n\tN° Cultivo\tPosición\tTipo\tOcupado\t\tMov_plantado"
        datos_cultivos = ""
        for index_c in range(len(self.cultivos)):
            datos_cultivos = datos_cultivos + f"\n\t{index_c}\t{self.cultivos[index_c].__str__()}"
        return encabezado_cultivos + datos_cultivos
    def __str__(self):
        cadena_cultivos = self.get_cultivos()
        cadena_huerta = f"\n\tMov_plagados: {self.movimientos_plagado}\t\tPlagado: {self.plagado}\t\t\tTope_cultivos: {self.tope_cultivos}"
        return cadena_huerta + cadena_cultivos         
class Objeto:
    def __init__(self,posicion,tipo):
        self.posicion=posicion
        self.tipo=tipo
    def __str__(self):
        return ""       #return f"Posicion: {self.posicion} Tipo: {self.tipo}\n"
class Personaje:
    def __init__(self,posicion=Coordenada(),tiene_fertilizante=False,cant_insecticida=CANT_INSECTICIDA,cant_moneda=MONEDAS_INICIAL,canasta=[]):
        self.posicion = posicion
        self.tiene_fertilizante = tiene_fertilizante
        self.cant_insecticida = cant_insecticida
        self.cant_moneda = cant_moneda
        self.canasta = canasta
    def take_fert(self):
        if not self.fertilizante:
            self.fertilizante=True
            return True
        else:
            return False
    def use_fert(self):
        if self.fertilizante:
            self.fertilizante=False
            return True
        else:
            return False
    def pinchar(self,objeto):
        self.vida-=1
        self.posicion = objeto.posicion

    def __str__(self):
        canasta_cosechada = ""
        for c in self.canasta:
            canasta_cosechada += f"[{c.tipo}]"
        return f"[[Personaje: {self.posicion.__str__()}][Fertilizantes: {self.tiene_fertilizante}][Insecticida: {self.cant_insecticida}][Monedas: {self.cant_moneda}][Canasta: {canasta_cosechada}]"
class Semilla:
    def __init__(self,tipo=VACIO,compra=0,venta=0,vida=0,cosecha_mov=0):
        self.tipo=tipo
        self.compra=compra
        self.venta=venta
        self.vida = vida
        self.cosecha_mov = cosecha_mov
    def __str__(self):
        return f"[Tipo {self.tipo}][compra ${self.compra}][venta: ${self.venta}][vida={self.vida}][cosecha={self.cosecha_mov}]"
class Juego:
    def __init__(self,cant_movimiento=0,objetos=[],tope_obj=0,huertas=[],deposito=Coordenada(),jugador=Personaje()):
        self.cant_movimiento = cant_movimiento
        self.objetos = objetos
        self.tope_obj = tope_obj
        self.huertas = huertas
        self.deposito = deposito
        self.jugador = jugador
    def get_huertas_data(self):
        gardens_data = ""
        for index_h in range(len(self.huertas)):
            garden_title = f"\nHUERTA NRO.{index_h}"
            gardens_data = gardens_data + garden_title + self.huertas[index_h].__str__()
        return gardens_data
    
    def print_screen_game(self):
        corner_line = get_corners_line()
        empty_bar = get_empty_bar()
        title = get_title(GAME_NAME)
        subt = f"[Cant_Mov: {self.cant_movimiento}]"
        obj_data = ""
        for o in self.objetos:
            obj_data = obj_data + o.__str__()            
        player_data = self.jugador.__str__()        
        print(f"{corner_line+empty_bar+title+empty_bar+get_center_text(subt+obj_data+player_data)}")
        print_empty_bar()
        print_bar()
        
    def __str__(self):
        #title_game = f"|{'LA GRANJA DE RUPELTINSKI':=^120}|\n\n"
        line = get_line()
        title_game = get_title("LA GRANJA DE RUPELTINSKI")
        empty_line = get_empty_bar()
#       subtitle_game = f"[Terreno: {TAMAÑO_MATRIZ}x{TAMAÑO_MATRIZ}][Cant_Mov: {self.cant_movimiento}][Tope_Obj: {self.tope_obj}][Deposito:{self.deposito.__str__()}]"
        subtitle_game = f"|\t[Cant_Mov: {self.cant_movimiento}]"
        player_data = self.jugador.__str__()
        gardens_data = "\n"+ self.get_huertas_data()
        objects_title = ""
        #f"\n{'OBJETOS'}\n"
        objects_data = ""
        for o in self.objetos:
            objects_data = objects_data + o.__str__()
        #return f"{title_game+subtitle_game+player_data+gardens_data+objects_title+objects_data}"
        #return f"{title_game+subtitlegame+player_data+objects_title+objects_data}"
        return f"{line+empty_line+title_game+empty_line+subtitle_game+objects_data+player_data+objects_data}\n{empty_line}\n"
###
### INICIO y JUEGO
def print_matriz(matriz):
    tab = 3
    print_empty_bar()
    col_names = [i for i in range(TAMAÑO_MATRIZ)]
    line_col_names = ""
    for col_name in col_names:
        if len(str(col_name)) == 1:
            line_col_names += f"{col_name}{SEPARACION_TERRENO*3}"
        else:
            line_col_names += f"{col_name}{SEPARACION_TERRENO*2}"
    print(get_center_text(line_col_names))
    print_empty_bar()
    for f in range(TAMAÑO_MATRIZ):     
        line = ""
        if len(str(f)) == 1:
            line += f"{f}{SEPARACION_TERRENO*3}"
        else:
            line += f"{f}{SEPARACION_TERRENO*2}"
        for c in range(TAMAÑO_MATRIZ):
            if len(matriz[f][c]) == 1:
                line += f"{matriz[f][c]}{SEPARACION_TERRENO*3}"
            else:
                line += f"{matriz[f][c]}{SEPARACION_TERRENO*2}"
        print(get_center_text(line))
    print_empty_bar()

def imprimir_terreno(juego):
    land = []
    for row in range(TAMAÑO_MATRIZ):
        land.append([CHAR_TERRENO]*TAMAÑO_MATRIZ)        
    #FILL LAND
    land[juego.deposito.fila][juego.deposito.columna] = DEPOSITO
    coord_none = Coordenada(-1,-1)
    for index_huerta in range(len(juego.huertas)):
        for index_cultivo in range(len(juego.huertas[index_huerta].cultivos)):
            c = juego.huertas[index_huerta].cultivos[index_cultivo]            
            #print(f"TEST IMPRTERR: {coord_index} de [{index_huerta}][{index_cultivo}]")
            if not c.posicion.es_igual(coord_none):
                if c.tipo != SIMBOLO_HUERTA:
                    land[c.posicion.fila][c.posicion.columna] = c.tipo + str(juego.cant_movimiento-c.mov_plantado)
                else:
                    land[c.posicion.fila][c.posicion.columna] = c.tipo
    for objeto in juego.objetos:
        land[objeto.posicion.fila][objeto.posicion.columna] = objeto.tipo
    land[juego.jugador.posicion.fila][juego.jugador.posicion.columna] = BLANCANIEVES    
    print_matriz(land)
    print_empty_bar()
    print_bar()
        
def refresh_objects(juego):
    mensaje = ""
    cant_movimientos = juego.cant_movimiento
    #LOAD RAND OBJECTS
    if cant_movimientos == RAND_MOV_PLAGA:
        load_objeto(juego,PLAGA)
        mensaje += f" Apareció una nueva plaga en el terreno"
    if cant_movimientos == RAND_MOV_FERT:
        load_objeto(juego,FERTILIZANTE)
        if (len(mensaje)>0): mensaje += "\n";
        mensaje += f" Apareció un fertilizante en el terreno"
    for huerta in juego.huertas:
        for c in huerta.cultivos:
            if c.tipo != VACIO:
                semilla = get_datos_semilla(c.tipo)
                mov_pasados = cant_movimientos - c.mov_plantado
                mov_vida = semilla.vida - mov_pasados
                if mov_vida < 1:
                    if (len(mensaje)>0): mensaje += "\n";
                    mensaje += f" Se pudrió 1 {get_nombre_planta(c.tipo).upper()}"
                    c.tipo = VACIO
    if mensaje:
        return get_center_text(mensaje)
    else:
        return mensaje
    
def refresh_game_status(juego):
    #START GAME
    while True:
        try:
            while juego.jugador.cant_monedas in range(CANT_COIN_WIN):
                msg_obj,msg_plantar,msg_mov,msg_fer,msg_efecto_personaje = "","","","",""            
                mensaje_refresh_objetos = refresh_objects(juego)    
                
                if distancia_manhatan(juego):
                    #vaciar_canasta()
                    pass                
                ubicacion, objeto = identificar_ubicacion(juego)
                
                if ubicacion == TERRENO:
                    mov = menu_terreno()
                    print_bar()
                    mov_valido, nueva_posicion = mover_personaje(juego.jugador,mov,juego)
                    if mov_valido == False or sobre_deposito(nueva_posicion,juego.deposito):          
                        msg_mov = " Movimiento fuera de terreno / Posición ocupada"
                    else:
                        juego.jugador.posicion = nueva_posicion
                        actualizar_movimiento(juego)                        
                elif ubicacion == HUERTA: #obj = cultivo
                    mov = menu_huerta(objeto)
                    if mov in MOVIMIENTOS:
                        mov_valido, nueva_posicion = mover_personaje(juego.jugador,mov,juego)
                        if mov_valido == False or sobre_deposito(nueva_posicion,juego.deposito):          
                            msg_mov = " Movimiento fuera de terreno / Posición ocupada"
                        else:
                            juego.jugador.posicion = nueva_posicion
                            actualizar_movimiento(juego)
                    else:
                        cultivo = objeto #renombro                
                        if mov == PLANTAR:
                            result = plantar(juego,cultivo)            
                            if result in MOVIMIENTOS:
                                mov_valido, nueva_posicion = mover_personaje(juego.jugador,result,juego)
                                if mov_valido == False or sobre_deposito(nueva_posicion,juego.deposito):          
                                    msg_mov = " Movimiento fuera de terreno / Posición ocupada"
                                else:
                                    juego.jugador.posicion = nueva_posicion
                                    actualizar_movimiento(juego)
                            else:
                                msg_plantar = result
                        elif mov == COSECHAR:
                            msg_plantar = cosechar_planta(juego,cultivo)
                        elif mov == INFO:
                            msg_plantar = get_info_planta(cultivo, juego.cant_movimiento)
                elif ubicacion in OBJETOS:
                    objeto = ubicacion
                    if objeto == FERTILIZANTE:
                        if juego.jugador.take_fert():
                            msg_efecto_personaje= MSJ_RECOGE_FERT
                        else:
                            msg_efecto_personaje = MSJ_NO_ENTRA_FERT
                    elif objeto.tipo == ESPINA:
                        juego.jugador.pinchar(objeto)
                        msg_efecto_personaje = MSJ_SE_PINCHO                                        
                else:   
                    pass
                
                clear_screen_windows()  
                juego.print_screen_game()       
                imprimir_terreno(juego)
                if msg_plantar != "":
                    print(msg_plantar)
                    print_bar()   
                if mensaje_refresh_objetos != "":
                    print(mensaje_refresh_objetos)
                    print_bar()
                if msg_mov != "":
                    print(get_center_text(msg_mov))
                    print_bar()
                if msg_efecto_personaje !="":
                    print(get_center_text(msg_efecto_personaje))
                    print_bar()             
                
            print(f"FIN DEL JUEGO, monedas: {juego.jugador.cant_monedas}")
            
        except KeyboardInterrupt:
            print()
            print_empty_bar()
            print_bar()       
            print_empty_bar()
            salir = input("\t¿DESEA SALIR DEL PROGRAMA? PERDERA SU PROGRESO. CONFIRME SI o NO: ").upper()
            print_empty_bar()
            print_bar()
            while salir not in ["SI","NO"]:
                print_empty_bar()
                salir = input("\tERROR\n\t¿DESEA SALIR DEL PROGRAMA? PERDERÁ SU PROGRESO. CONFIRME SI o NO: ").upper()
                print_empty_bar()
                print_bar()
            
            if salir == "SI":
                print_empty_bar()
                print(get_center_text("- FIN DEL PROGRAMA -"))
                break
            else:
                refresh_game_status(juego)  
    
def inicializar_juego(juego):
###########DATA SETTING##################
    crear_semillas(SEMILLAS)
    #1 - SET HUERTAS
    get_huertas(juego)
    #2 - SET OBSTACULOS
    get_espinas(juego)
    get_obstaculos(juego)
    #3 - SET HERRAMIENTAS
    pass
    #4 - SET BLANCANIEVES
    set_jugador(juego)
    #5 - SET DEPOSITO
    es_repetida=True
    #6 - CREO SEMILLAS
    while es_repetida:
        coord_deposito = get_coord_random()
        es_repetida = es_coord_repetida(coord_deposito,DEPOSITO,3,juego)
    juego.deposito = coord_deposito
    #TEST
    juego.print_screen_game()
###
        