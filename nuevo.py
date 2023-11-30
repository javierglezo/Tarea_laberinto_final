# Dimensiones del laberinto (5x5)
filas = 5
columnas = 5

# Lista de listas del laberinto con espacios ' '
laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

# Definir coordenadas de las casillas con muro
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

# Colocar 'X' en las casillas con muro
for i, j in muro:
    laberinto[i][j] = 'X'

# Colocar inicio (S) y final (E) en laberinto directamente
laberinto[4][4] = 'E'
laberinto[0][0] = 'S'

#Función menú del juego:
def menú():
    print("Bienvenido:")
    print("-Introduzca 1 para visualizar el laberinto")
    print("-Introduzca 2 si quiere salir del programa")


# Posición incial jugador
posicion_jugador = [0, 0]

# Función para mostrar el laberinto
def imprimir_laberinto():
    for fila in laberinto:
        print(' '.join(fila))

#Función llamada desde el launcher para iniciar el juego:
def jugar():
    while True:
        menú()
        opcion = input("Tu elección: ")

        if opcion == '1':
            # Inicializar lista movimientos correctos
            posiciones_correctas = []
            # Bucle para moverse por el laberinto
            while True:
                imprimir_laberinto()
                print("Teclas de movimiento: W (arriba), A (izquierda), S (abajo), D (derecha)")
                movimiento = input("Tu movimiento: ").upper()
                # Actualizar posición del jugador según la tecla ingresada y borrar la anterior posición
                if movimiento == 'W' and posicion_jugador[0] > 0 and laberinto[posicion_jugador[0] - 1][posicion_jugador[1]] != 'X':
                    laberinto[posicion_jugador[0]][posicion_jugador[1]] = ' '
                    posicion_jugador[0] -= 1
                    posiciones_correctas.append('Arriba')
                elif movimiento == 'A' and posicion_jugador[1] > 0 and laberinto[posicion_jugador[0]][posicion_jugador[1] - 1] != 'X':
                    laberinto[posicion_jugador[0]][posicion_jugador[1]] = ' '
                    posicion_jugador[1] -= 1
                    posiciones_correctas.append('Izquierda')
                elif movimiento == 'S' and posicion_jugador[0] < filas - 1 and laberinto[posicion_jugador[0] + 1][posicion_jugador[1]] != 'X':
                    laberinto[posicion_jugador[0]][posicion_jugador[1]] = ' '
                    posicion_jugador[0] += 1
                    posiciones_correctas.append('Abajo')
                elif movimiento == 'D' and posicion_jugador[1] < columnas - 1 and laberinto[posicion_jugador[0]][posicion_jugador[1] + 1] != 'X':
                    laberinto[posicion_jugador[0]][posicion_jugador[1]] = ' '
                    posicion_jugador[1] += 1
                    posiciones_correctas.append('Derecha')
                # Verificar si llega a la salida
                if laberinto[posicion_jugador[0]][posicion_jugador[1]] == 'E':
                    print("¡Has llegado a la salida!")
                    print(posiciones_correctas)
                    quit()
                else:
                    laberinto[posicion_jugador[0]][posicion_jugador[1]] = '.'
        elif opcion == '2':
            break
