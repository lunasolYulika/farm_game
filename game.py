# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Configuración de la ventana
ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Ejemplo de Movimiento")

# Configuración del jugador
jugador_ancho, jugador_alto = 50, 50
jugador_x, jugador_y = ancho // 2, alto // 2

# Configuración de la velocidad del jugador
velocidad = 5

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener el estado de las teclas
    teclas = pygame.key.get_pressed()

    # Actualizar la posición del jugador según las teclas presionadas
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad
    if teclas[pygame.K_UP]:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_y += velocidad

    # Limpiar la pantalla
    ventana.fill(NEGRO)

    # Dibujar al jugador
    pygame.draw.rect(ventana, BLANCO, (jugador_x, jugador_y, jugador_ancho, jugador_alto))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    reloj.tick(30)