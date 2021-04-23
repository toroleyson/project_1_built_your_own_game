# I. PREVIO

# 1.1. Objetivo del juego:
    #Sacar una carta cuyo valor sea mayor al valor de la carta que saque el dealer.

# 1.2 Reglas del juego:
    # - El jugador que tenga la carta más alta gana. La carta más alta es el A, luego el K,Q,J,10,9,8,7,6,5,4,3,2. El valor es el mismo para los diferentes palos. Es decir: el A de corazones = el A de diamantes.
    # - Antes de iniciar el juego, el jugador selecciona el importe a apostar.
    # - Se hace la repartición de las cartas: Una carta para el jugador y una carta para el dealer.
    # - Si la carta del jugador es MAYOR a la del dealer, el jugador GANA la partida y el jugador gana lo apostado.
    # - Si la carta del jugador es MENOR a la del dealer, el jugador PIERDE la partida y el jugador pierde lo apostado.
    # - Si la carta del jugador es IGUAL a la del dealer, se tienen 2 opciones:
        # Opción 1:
            # Termina en empate

        # Opción 2: Se elige entre:
            # El jugador elige retirarse y pierde la mitad de lo apostado.
            # El jugador elige continuar y apuesta nuevamente lo apostado para obtener una carta de desempate.


# II. CÓDIGO DEL JUEGO

# 2.1 Importamos las librerías que vamos a utilizar:
import random

# 2.2 Creamos la baraja con la que se va a jugar.

# Opción 1:

baraja_1 = sum(list(map( lambda carta: ['2'+str(carta),'3'+str(carta),'4'+str(carta),'5'+str(carta),'6'+str(carta),'7'+str(carta),'8'+str(carta),'9'+str(carta),'10'+str(carta),'J'+str(carta),'Q'+str(carta),'K'+str(carta),'A'+str(carta)], ['♥','♦','♣','♠'])),[])
print(baraja_1)

# Con el map creamos una lista de listas de cada uno de los elementos de las cartas de la baraja, del 2 al A, para cada uno de los 4 palos.
# Con el sum hacemos que esta lista de listas quede en una lista sola.

print('- - - ')

# Opción 2:

creacion_baraja_2 = list(map (lambda carta: ['2'+str(carta),'3'+str(carta),'4'+str(carta),'5'+str(carta),'6'+str(carta),'7'+str(carta),'8'+str(carta),'9'+str(carta),'10'+str(carta),'J'+str(carta),'Q'+str(carta),'K'+str(carta),'A'+str(carta)], ['♥','♦','♣','♠']))
baraja_2 = []
for i in creacion_baraja_2:
    for j in i:
        baraja_2.append(j)

print(baraja_2)

# Si queremos hacerla con un for, iteramos para que se cree un elemento de cada palo de la baraja en todos los números de la baraja.


# 2.3 Le asignamos un valor númerico a cada carta para poder compararlas en el juego.

# Creamos una lista de los valores que vamos a asignarle a cada carta
valores_baraja = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14]

# Creamos un diccionario con las cartas y los valores
baraja= dict(zip(baraja_1,valores_baraja))

# Convertimos el diccionario en una lista para poder seleccionar elemenos random más adelante
baraja_mix = list(baraja.items())
print(baraja_mix)


# 2.4 Definimos los parámetros con los que se realizará el juego.

# Le pedimos el nombre al jugador.
jugador = input('Indique el nombre del jugador: ')
dealer = 'dealer'
# Le pedimos indique el importe que va a querer jugar
bank_inicial = int(input('Indique el importe de fichas que quiere comprar: $'))


# 2.5 Iniciamos el juego.

# Pasamos el saldo comprado en bank_inical a la variable bank
bank = bank_inicial

print('El saldo actual de '+jugador+' es: $'+ str(bank))

# Comprobamos que el jugador tenga dinero para apostar lo deseado:

apuesta = int(input('Indique el importe a apostar en esta partida: $'))
print('- - - - -')

if apuesta <= bank:
    print('No van más apuestas.')
    print('- - - - -')
    print('Iniciamos partida')
else:
    print('Saldo insuficiente, regrese otro día')

print('- - - - -')

# Desarrollo del juego:

# Actulizamos el saldo del jugador:
bank = bank - apuesta

# Seleccionamos la carta del jugador:
carta_jugador = random.choice(baraja_mix)
print('Carta de ' + jugador + ':')
print(carta_jugador[0])

print('- - - - -')

# Seleccionamos la carta del dealer:
carta_dealer = random.choice(baraja_mix)
print('Carta de Dealer:')
print(carta_dealer[0])

# Hacemos la comparación de ambas cartas para ver quien gana

if carta_jugador[1] > carta_dealer[1]:
    print(jugador + ' gana la partida.')
    bank = bank + apuesta * 2
    print('Su nuevo saldo es: $' + str(bank))

if carta_jugador[1] < carta_dealer[1]:
    print(jugador + ' pierde la partida.')
    bank = bank
    print('Su nuevo saldo es: $' + str(bank))

if carta_jugador[1] == carta_dealer[1]:
    print('Empate')
    bank = bank + apuesta
    print('Su saldo se mantiene igual: $' + str(bank))