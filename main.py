from api import *
from closeup_dibujos import *
from cuartos import Cuartos
import datetime
from dibujos_cuartos import *
from frases import *
from instrucciones import *
from jugador import Jugador
from objetos import Objetos
from partida import Partida
from games_all import *
import time

def records():

    print(record)
    print('Elige una de estas opciones')
    opciones = input('''
    1. Top 5
    ''')
    
    if opciones == '1':
        print('Top 5: ')
        with open("Database.txt") as db:
            datos = db.readlines()
        # print(datos)
        cantidad = 0
        for i,x in enumerate(datos):
            leaderboard = x[:-1].split(',')
            datos[i] = leaderboard
            for j in leaderboard[5:]:

                cantidad = cantidad + 1        

        # print(cantidad)
        # print(datos)
        y = 0
        while y < cantidad:
            # print(scores)
            for i,usuario in enumerate(datos):

                scores = usuario[5:]
                if i == 0:
                    maximo = 0
                    top = 30
                for score in scores:
                    if int(score) < top:
                        top = int(score)
                        maximo = i
            y = y + 1
            # print(maximo)
            # print(top)      
            usuarios = datos[maximo]
                # tiempos = usuarios[5:]
            usuarios.remove(str(top))
            # print(usuarios)
            print(f"--------{y}-------\nUsername:{usuarios[0]}\nTiempo:{top}")
            if y == 5:
                break
        
        buen_continue()
    
def partida_nueva():

    print(nueva)
    opcion = input('''
    Eliga la dificultad de su partida: 
    1. Facil
    2. Media
    3. Dificil
    4. Menu\n >> ''')

    while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        opcion = input("Ingreso invalido, ingrese una opcion valida: ")        

    if opcion == '1':

        print(easy)
        dificultad = 'Facil'
        vidas = float(5)
        pistas = 5
        tiempo = 30
        
    elif opcion == '2':

        print(medio)
        dificultad = 'Media'
        vidas = float(3)
        pistas = 3
        tiempo = 20 
        
    elif opcion == '3':

        print(hard)
        dificultad = 'Dificil'
        vidas = float(1)
        pistas = 2
        tiempo = 10
       
    elif opcion == '4':

        print('Adios')
        menu_juego()
    else:
        return 0

    try:

        with open("Database.txt","a+") as db:
            datos = db.readlines()

    except FileNotFoundError:
        pass
    
    username = input('Username: ')
    attempt = 0
    no_existe = 0
    for i,dato in enumerate(datos):

        user = dato[:-1].split(",") # aquí, con el "dato[:-1]" tomo toda la información de la línea sin el salto de línea. Con .split(",") separo el string cada vez que haya una coma y almaceno los strings resultantes en la variable persona (que será una lista)
        # print(user)

        sigue_pregunta = 1
        while sigue_pregunta == 1:

            if username == user[0]:

                print(user[i])
                old_password = input(f'Bienvenido {username} introduce tu contrasena: ')

                if old_password == user[1]:
            
                    print('Welcome back suerte esta vez')
                    time.sleep(2)
                    dificultad = dificultad
                    vidas = vidas
                    pistas = pistas
                    tiempo = tiempo
                    username = user[0]
                    contrasena = old_password
                    edad = user[2]
                    avatar = user[3]
                    inventario = ''
                    tiempo_partidas = ''
                    
                    new_game = Jugador(dificultad, vidas, pistas, tiempo, username, contrasena, edad, avatar,  inventario, tiempo_partidas)
                    # print(nuevo_jugador.mostrar())
                    no_existe = 1
                    sigue_pregunta = 0
                    return new_game
                
                elif attempt == 2:

                    print('Lo siento vuelve a crear la partida')
                    time.sleep(3)
                    menu_juego()

                elif attempt < 2:

                    print(f'Wrong! De verdad eres {username}?')
                    attempt = attempt + 1
                    time.sleep(2)
                    sigue_pregunta = 1
            
            else:

                sigue_pregunta = 0 

    if no_existe == 0: 

        while True:
            try:

                contrasena = input('Contrasena: ')
                edad = int(input('Edad: '))
                break

            except:
                print('Ingresaste un dato invalido')

            
            
        avatar = input('''Elige el Avatar de tu jugador: 
        1. Scharifker
        2. Eugenio Mendoza
        3. Pelusa
        4. Gandhi
        5. Ghost
        6. Richtofen
        7. Robert D.jr\n >>''')
        while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 7): 
            opcion = input("Ingreso invalido, ingrese una opcion valida: ") 
        if avatar == '1':

            avatar = 'Sharifker'

        elif avatar == '2':
        
            avatar = 'Eugenio Mendoza'

        elif avatar == '3':

            avatar = 'Pelusa'

        elif avatar == '4':

            avatar = 'Gandhi'

        elif avatar == '5':

            avatar = 'Ghost'

        elif avatar == '6':

            avatar = 'Richtofen'

        elif avatar == '7':

            avatar = 'Robert D.jr'
            
        #agrego al inventario objetos que no tengo hecho los juegos de una vez para probar el juego
        inventario = ''
        tiempo_partidas = ''

        new_game = Jugador(dificultad, vidas, pistas, tiempo, username, contrasena, edad, avatar,  inventario, tiempo_partidas)
        # print(nuevo_jugador.mostrar())
        return new_game

def comienza_partida(new_game):
    print(new_game.mostrar())
    primer_discurso(new_game)
    print(ready)
    time.sleep(3)
    segundo_discurso(new_game)
    time.sleep(3)
    # x posicion en donde se encuentra el jugador
    x = 1
    #funcion para llamar la api
    api = api_call()  

    continuar = 1
    #tiempo en el que comienza el jugador
    instanteInicial = datetime.datetime.now().minute  
    #conteo de cuartos
    lab = 0
    biblio = 0
    plaza = 0
    pasillo = 0
    servers = 0

    #Variables para verificar si ganaron o no ciertos juegos
    boolean_count = 0
    pizarra_count = 0
    math_count = 0
    cripto_count = 0
    random_count = 0

    while continuar == 1:
        
        #Comienza a correr el tiempo
        instanteFinal = datetime.datetime.now().minute
        end = instanteFinal - instanteInicial


        if end == new_game.ded_time():

            se_acabo(new_game,instanteInicial)
            print('Se te acabo el tiempo lo siento....................')
            time.sleep(5)
            menu_juego()


        dic = api[x]
        name = dic.get('name')
        cosas = dic.get('objects')
        room = Cuartos(name)
        
        print(dibujos_rooms[x])
        print(room.mostrar())
        print('Puedes ver el Menu apretando la letra (M)')
        

        movimiento = input('Hacia donde te diriges?\n>> ')      

        if movimiento.lower() == 'w':

            center_obj = cosas[0]
            name = center_obj.get('name')
            position = center_obj.get('position')    
            objeto_center = Objetos(name,position)
            print(objeto_center.mostrar())

            center_game = center_obj.get('game')
            name_game = center_game.get('name')
            # juego = Juegos(name_game)
            # print(juego.mostrar())

            if x == 2:

                print('NOOOOO, pisaste el saman perdiste una vida cuidado!!')
                new_game.quito_vida(1)
                if new_game.game_over() == True:
    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()
             
            if center_game.get('message_requirement') != None:
    
                print(f'Bienvenido a ',center_game.get('name'),center_game.get('message_requirement'))
                time.sleep(3)

            valido_premio = new_game.check_inventario(center_game.get('award'))
            valido_requirement = new_game.check_inventario(center_game.get('requirement'))
            # print(valido_requirement)
        
            if valido_premio == True:

                print(dibujos_closeup[x][0])
                print('Ya pasaste por aqui y ganaste, tienes en tu INVENTARIO -->',center_game.get('award'))
                time.sleep(2)
                    
            elif valido_requirement == True or center_game.get('requirement') == False or x == 0 or x == 2:
                    
                print(dibujos_closeup[x][0])

                if x == 0:

                    #SOUP HARD
                    if pizarra_count == 0:
                        logrado = sopa_letras(name_game,center_game,new_game, instanteInicial)
                        if logrado == 1:

                            pizarra_count == 1
                        
                        else:

                            print('Buu')
                            x = 0

                        
                    elif pizarra_count == 1:
                        print('No puedes volver a jugar, ya ganaste este juego tienes talento')
                        time.sleep(2)
                        x = 0


                elif x == 1:

                    #AHORCADO HARD
                    ahorcado(name_game, center_game, new_game, instanteInicial)
                    pass

                elif x == 2:

                    list_awards = center_game.get('requirement')
                    # print(list_awards)
                    first_award = list_awards[0]
                    # print(first_award)
                    second_award = list_awards[1]
                    print(second_award)
                    valido_1 = new_game.check_inventario(first_award)
                    valido_2 = new_game.check_inventario(second_award)

                    if valido_1 == True and valido_2 == True:

                        #Solve logic
                        solve_logic(name_game,center_game,new_game, instanteInicial)
                        pass

                    else:

                        print('No puedes entrar a jugar el juego del saman pero ya te quite 1 vida r.i.p')
                        time.sleep(2)

                elif x == 3:

                    #LOGICA BOOLEANA 
                    if boolean_count == 0:
                        logrado = logic_bool(name_game,center_game,new_game, instanteInicial)

                        if logrado == 1:

                            boolean_count = 1    
                            print('Adelante tu puedes')
                            time.sleep(2)
                            x = 0

                        elif logrado == 0:
        
                            print('Lo siento tienes que completar el juego para pasar')
                            time.sleep(2)
                            pass
                    
                    elif boolean_count == 1:
                        print('Adelante ya habias destruido el candado y completado el juego')
                        time.sleep(2)
                        x = 0


                else:

                    pass  

            elif valido_requirement == False and x != 4:

                print(f'Lo siento no puedes pasar, necesitas -->', center_game.get('requirement'))
                buen_continue()     
                
            if x == 4:
                
                list_awards = center_game.get('requirement')
                first_award = list_awards[0]
                second_award = list_awards[1]

                valido_1 = new_game.check_inventario(first_award)
                valido_2 = new_game.check_inventario(second_award)

                if valido_1 == True and valido_2 == True:
            
                    refranes(new_game, instanteInicial)

                else:

                    print('Todavia te falta algo, sigue buscando buena suerte')
                    time.sleep(2)
                    pass        
                
        elif movimiento.lower() == 'a':

            left_obj = cosas[1]
            name = left_obj.get('name')
            position = left_obj.get('position')

            objeto_izq = Objetos(name,position)
            left_game = left_obj.get('game')
            name_game = left_game.get('name')
            print(objeto_izq.mostrar())
            
            if left_game.get('message_requirement') != None:
    
                print(f'Bienvenido a ',left_game.get('name'),left_game.get('message_requirement'))
                time.sleep(3)
    
            valido_requirement = new_game.check_inventario(left_game.get('requirement'))
            valido_premio = new_game.check_inventario(left_game.get('award'))

            if valido_premio == True:

                print(dibujos_closeup[x][1])
                print('Ya pasaste por aqui y ganaste, tienes en tu INVENTARIO -->',left_game.get('award'))
                buen_continue()
                pass

            elif valido_requirement == True or left_game.get('requirement') == False:

                print(dibujos_closeup[x][1])
                if x == 0:

                    python_game(name_game,left_game,new_game, instanteInicial)
                    pass

                elif x == 1:

                    #preguntas matematica
                    if math_count == 0:
                        logrado = preguntas_mate(name_game,left_game,new_game, instanteInicial)
                        if logrado == 1:

                            math_count = 1
                        
                        else:
                            print('Aprende a derivar vale')
                            time.sleep(2)
                            x = 1
                            
                    else:
                        
                        print('No te dejare volver a derivar que sufrimiento chao')
                        time.sleep(2)
                
                elif x == 2:

                    #QUIZZIS
                    millonario(name_game,left_game,new_game, instanteInicial)
                    pass

                elif x == 4:

                    #Palabras mezcladas
                    p_mezcladas(name_game,left_game,new_game, instanteInicial)
                    pass

            else:

                print(f'Lo siento no puedes pasar, necesitas -->', left_game.get('requirement'))
                buen_continue()

        elif movimiento.lower() == 'd':

            right_obj = cosas[2]
            name = right_obj.get('name')
            position = right_obj.get('position')
            objeto_right = Objetos(name,position)
            right_game = right_obj.get('game')
            name_game = right_game.get('name')

            print(objeto_right.mostrar())
            if right_game.get('message_requirement') != None:

                print(f'Bienvenido a ',right_game.get('name'),right_game.get('message_requirement'))
                time.sleep(3)

            valido_requirement = new_game.check_inventario(right_game.get('requirement'))
            valido_premio = new_game.check_inventario(right_game.get('award'))

            if valido_premio == True:

                print(dibujos_closeup[x][2])
                print('Ya pasaste por aqui y ganaste, ya obtuviste -->',right_game.get('award'))
                
                time.sleep(5)
                pass
                
            
            elif valido_requirement == True or right_game.get('requirement') == False:

                print(dibujos_closeup[x][2])

                if x == 0:

                    contra = input('Contraseña: ')

                    while not ("".join(contra.split(" "))).isalpha():
                        contra = input("Ingreso invalido, ingrese el contra :\n >> ")

                    if contra == 'escapandoando':

                        adivinanzas(name_game,right_game,new_game, instanteInicial)
                        pass

                    else:

                        print('Contraseña invalida, fuera de aqui')
                        time.sleep(2)
                        pass

                elif x == 1:

                    
                    #Criptograma 
                    if cripto_count == 0:
                        logrado = criptograma(name_game, right_game,new_game, instanteInicial)

                        if logrado == 1:

                            cripto_count = 1
                        
                        else:

                            print('Codigo Cesar, no es tan hard buscalo en google')
                            time.sleep(2)
                    
                    else:

                        print('Ya pasaste por aqui revisa tu inventario dude')
                        time.sleep(2)
                        
                elif x == 2:

                    #MEmoria con EMOJIS should be easy
                    memoria(name_game, right_game,new_game, instanteInicial)
                    pass

                elif x == 4:

                    #RAndom number generator
                    if random_count == 0:
                        
                        logrado = random_number(name_game, right_game,new_game, instanteInicial)
                        if logrado == 1:

                            random_count = 1
                        
                        else:

                            print('Este juego es muy dificil confirmo')

                    elif random_count == 1:

                        print('Para que vas a volver a entrar aqui alo')
                        time.sleep(2)


            else:

                print(f'Lo siento no puedes pasar, necesitas -->', right_game.get('requirement'))
                time.sleep(3)  
                
        
        elif movimiento == ' ':

            if x == 0:
                lab = lab + 1
                x = 4
            
            elif x == 1:

                biblio = biblio + 1
                x = 3

            elif x == 2:
                
                plaza = plaza + 1 
                x = 1
            
            elif x == 3:

                pasillo = pasillo + 1
                if boolean_count == 1:
    
                    # print('Felicidades por desbloquear un nuevo cuarto atento con lo que obtienes aqui!')
                    x = 0

                else:

                    print('Lo siento tienes que completar el juego para pasar')
                    time.sleep(3)
                    x = 3

            elif x == 4:

                servers = servers + 1
                print('Pa onde vas tu? ')
                time.sleep(2)
                x = 4
    
        elif movimiento.lower() == 's':

            if x == 0:
                lab = lab + 1
                x = 3
            

            elif x == 1:
    
                biblio = biblio + 1
                x = 2

            elif x == 2:

                plaza = plaza + 1 
                print('Pa onde vas tu? ')
                buen_continue()
                x = 2
            
            elif x == 3:

                pasillo = pasillo + 1
                x = 1

            elif x == 4:

                x = 0
                servers = servers + 1
                
        elif movimiento.lower() == 'm':
    
            print(new_game.mostrar())
            print(f'''
            <-------   (S)      Te devuelves de cuarto       (S)    <-------
            -------> (SPACE) Avanzas al siguiente cuarto   (SPACE) ------->
    Para los objetos:  (W)               Centro              (W) 
                       (A)              Izquierda            (A)
                       (D)               Derecha             (D)
                       (I)       Para ver tu inventario      (I)

            Acuerdate que puedes usar la palabra (pista) en algunos juegos!\n''')

            sigue_partida = input('''

                    Este es el menu lee cuidadosamente y para salirte del juego 
                        utiliza la letra (N) para seguir en el juego (Y)''')

            while not ("".join(sigue_partida.split(" "))).isalpha():   
                sigue_partida = input("Ingreso invalido:\n >> ")
                    
            if sigue_partida == 'y':
                
                pass

            elif sigue_partida == 'n':

                menu_juego()
        
        elif movimiento.lower()== 'i':

            new_game.veo_inventario()

        else:

            ('No te moviste pa ningun lado')
            time.sleep(3)
            continuar = 1

def menu_juego():

    while True:
        opcion = input("""
        Elige una opcion: 
        1. Nueva Partida
        2. Instrucciones
        3. Records
        4. Para salir \n >> """)

        while (not opcion.isnumeric()) or (int(opcion) < 1): 
          opcion = input("Ingreso invalido, ingrese una opcion valida: ") 

        if opcion == '1':

            new_game = partida_nueva()
           
            comienza_partida(new_game)

        elif opcion == '2':

            instrucciones()

        elif opcion == '3':

            records()

        elif opcion == '4':

            break

        else:

            print('Opcion invalida')

def main():

    print(bienvenido)
    menu_juego()


if __name__ == '__main__':
    main()

