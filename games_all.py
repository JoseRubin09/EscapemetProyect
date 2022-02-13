from api import *
import random
from frases import *
import sympy as sy
import math
from jugador import Jugador
from main import menu_juego
from matrix import Matrix
from juego import Juegos

def adivinanzas(name_game, right_game, new_game, instanteInicial):
    
    pregunta = random.randint(0,2)
    nombre = right_game.get('name')
    reglas = right_game.get('rules')
    lista_preguntas = right_game.get('questions')
    juego = lista_preguntas[pregunta]
    question_random = juego.get('question')
    game = Juegos(nombre,reglas,question_random)
    print(game.mostrar_todo())
    correcto = juego.get('answers')
    # print(correcto)

    continuar = 1
    pista = 1
    while continuar == 1:

        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")
        
        if respuesta == 'pista':
                
            if new_game.quito_pista(1) == True and pista < 3:
    
                if pista == 1:
    
                    print(juego.get('clue_1'))
                    buen_continue()

                if pista == 2:
    
                    print(juego.get('clue_2'))
                    buen_continue()

                if pista == 3:

                    print(juego.get('clue_3'))
                    buen_continue()

                pista = pista + 1
            
            elif new_game.quito_pista(1) == False or pista > 3:
    
                print('No + pistas en este juego')
                buen_continue()
                
            
        else:

            for x in range(len(correcto)):
            
                if respuesta == correcto[x]:
                        
                    print(win)
                    print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
                    continuar = 0
                    new_game.agrego_objeto(right_game.get('award'))
                    time.sleep(3)
                    break

                elif x == (len(correcto)-1):
                    
                    print(lose)
                    new_game.quito_vida(1/2)
                    if new_game.game_over() == True:
        
                        se_acabo(new_game,instanteInicial)
                        menu_juego()

                    continuar = try_again()                

def criptograma(name_game, right_game, new_game, instanteInicial):
    
    nombre = (right_game.get('name'))
    reglas = (right_game.get('rules'))
    pregunta = random.randint(0,2)
    lista_preguntas = right_game.get('questions')
    juego = lista_preguntas[pregunta]
    question_random = juego
    game = Juegos(nombre,reglas,question_random)
    print(game.mostrar())

    #abecedario
    abc = ['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

    #lista del abecedario con sus desplacamientos el primer termino 0 es desplazamiento 2 el segundo 4 y el tercero 5

    new_abc = [['y','z','a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
    ['w','x','y','z','a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'],
    ['v','w','x','y','z','a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']]

    correcto = 'si te graduas pisas el saman'

    mensaje = ('si te graduas pisas el saman')
   
    print(abc)
    print(' \n')
    print(new_abc[pregunta])
    j = 0
    for i in range(len(abc)):
        if i == j:

            cambiando_mensaje = mensaje.replace(abc[i],new_abc[pregunta][j])
            j = j + 1

            if mensaje != cambiando_mensaje:
                
                mensaje = cambiando_mensaje
    
    continuar = 1
    while continuar == 1:
        
        print(mensaje)
        respuesta = input('Que dice aqui?:\n>>')
        while not ("".join(respuesta.split(" "))).isalpha():
                respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")

    
        if respuesta == correcto:

            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            continuar = 0
            mensaje_mod = right_game.get('award')
            #Lo que necesito es solo la palabra Mensaje
            mensaje_solo = mensaje_mod[0:7]
            new_game.agrego_objeto(mensaje_solo)
            time.sleep(3) 
            # print(mensaje_solo)
            return 1

        elif respuesta == 'pista':

            print('No hay pistas en este juego')
            time.sleep(2)
        
        else:
        
            print(lose)
            new_game.quito_vida(1/2)
            if new_game.game_over() == True:

                se_acabo(new_game,instanteInicial)
                menu_juego()

            continuar = try_again() 
            if continuar == 0:

                return 0    

def memoria(name_game, right_game, new_game, instanteInicial):
    
    nombre = right_game.get('name')
    rules = right_game.get('rules')
    question_random = right_game.get('questions')
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar())
    # lista_preguntas = right_game.get('questions')
    # juego = lista_preguntas[0]

    memory_table=[]
    temp_table = []
    dataset = [
        ['😀', '🙄', '🐧', '🥵'],                                                   
        ['🐧', '😨', '🤓', '😷'],                                                 
        ['😨', '🤓', '🥵', '😷'],                                                  
        ['🤑', '🤑', '🙄', '😀'], 
    ]

    # print('Juego de memoria bla bla bla instrucciones')

    #Contruccion de la tabla de referencia
    cont = 0
    for row in dataset:
        aux_row = []
        for column in row:
            cont = cont + 1
            aux_row.append(cont)
        memory_table.append(aux_row)

    # Funcion encargada de buscar el emoji correspondiente en el dataset
    def get_emoji(num):
        cont = 0
        for row in dataset:
            for column in row:
                cont = cont + 1
                if(cont == option):
                    return column

    # Funcion encargada de imprimir la tabla de juego
    def print_table(table):
        for row in table:

            print('')
            print('|', end='')

            for column in row:

                print(' ', column, end='')

                if(isinstance(column, int) and column < 10):
                    print(' ', end='')
                    
                print(' |', end='')

            print('')

    # Funcion encargada de asignar un emoji a la tabla de juego
    def set_emoji(table,option,emoji):
        cont = 0
        for x in range(len(table)):
            for y in range(len(table[x])):
                cont = cont + 1
                if(cont == option):
                    table[x][y] = emoji
    continuar = 1
    while continuar == 1:

        # Se copia la tabla en cada iteracion para mostrar los nuevo emojis volteados
        temp_table = [list(row) for row in memory_table]

        print_table(memory_table)

        # Se le pide al usuario voltear el primer emoji
        print('')
        while True:
            try: 
                option = int(input('Ingrese la casilla a voltear: '))
                break
            except:
                print("Ingreso Invalido.")
                
        if option == 123456789:
            #Para los admins
            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            continuar = 0
            new_game.agrego_objeto(right_game.get('award'))
            time.sleep(3)
            break

        firts_emoji = get_emoji(option)
        set_emoji(temp_table,option,firts_emoji)
        print_table(temp_table)
        print('')

        # Se le pide al usuario voltear el el segundo emoji
        print('')

        while True:
            try: 
                option = int(input('Ingrese la casilla a voltear: '))
                break
            except:
                print("Ingreso Invalido.")
                
        second_emoji = get_emoji(option)
        set_emoji(temp_table,option,second_emoji)
        print_table(temp_table)

        print('')


        # Si los dos emojis coinciden te actualiza la tabla
        if(firts_emoji == second_emoji):

            print('Los emojis iguales')
            memory_table = [list(row) for row in temp_table]
        else:

            new_game.quito_vida(1/4)
            if new_game.game_over() == True:
        
                se_acabo(new_game,instanteInicial)
                menu_juego()

            print('Wrong!!!')
            time.sleep(3)
            print('Los emojis no son iguales')
            continuar = 1
        # Verifica cuando se han encontrados todas las parejas de emoji y termina el juego
        if(memory_table == dataset):
            
            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            continuar = 0
            new_game.agrego_objeto(right_game.get('award'))
            time.sleep(4)
            break
                                        
def random_number(name_game, right_game, new_game, instanteInicial):

    nombre = right_game.get('name')
    reglas = right_game.get('rules')
    lista_preguntas = right_game.get('questions')
    juego = lista_preguntas[0]

    question_random = juego.get('question')
    game = Juegos(nombre,reglas,question_random)
    print(game.mostrar_todo())

    correcto = random.randint(1,15)

    continuar = 1
    attempts = 0
    while continuar == 1:
    
        while True:

            try: 

                respuesta = int(input("Ingrese un  posicion: "))
                break

            except:

                print("Ingreso Invalido.")

        if respuesta == correcto:

            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            titulo_mod = right_game.get('award').replace('í','i').title()
            # print(titulo_mod)
            # print(type(titulo_mod))
            new_game.agrego_objeto(titulo_mod)

            to_be_continue()
            continuar = 0
            return 1

        elif respuesta != correcto:

            print('Equivocado, sigue intentando\n')
            attempts = attempts + 1
            

        if attempts == 3:

            print(lose)
            new_game.quito_vida(1/4)
            print('         Perdiste -____-')

            if new_game.game_over() == True:
    
                se_acabo(new_game,instanteInicial)
                menu_juego()

            #quitarle cuantas vidas sean 
            continuar = try_again()
            if continuar == 0:
                
                return 0
        
            
def python_game(name_game, left_game, new_game, instanteInicial):
    
    nombre = left_game.get('name')
    rules = left_game.get('rules')
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,1)

    juego = lista_preguntas[pregunta]

    frase = 'tengo en mi cuenta 50,00 $'
    random_question = juego.get('question')
    game = Juegos(nombre, rules, random_question)

    print(game.mostrar_todo())
    
    if pregunta == 1:

        continuar = 1
        pista = 1
        while continuar == 1: 

            print("Invierte este string con python en un línea  para poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\"")
            codigo = input('\nCodigo: \n>>')
            frase = 'oidutse ne al ortem aireinegni ed sametsis'
            a = frase.split(' ')

            if codigo == 'frase[::-1]':

                for i in range(len(a)):
            
                    a[i] = a[i][::-1]

                print(" ".join(a))

                logrado = input('Cual era la frase: \n>>')
                while not ("".join(logrado.split(" "))).isalpha():
                    logrado = input("Ingreso invalido :\n >> ")

                if logrado == 'estudio en la metro ingenieria de sistemas':

                    print(win)
                    print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                    new_game.agrego_objeto(left_game.get('award'))
                    # print(new_game.mostrar())
                    continuar = 0
                    to_be_continue()
                    break

                else:

                    print(lose)
                    new_game.quito_vida(1/2)

                    if new_game.game_over() == True:

                        se_acabo(new_game,instanteInicial)
                        menu_juego()

                    continuar = try_again()
                
            elif codigo.lower() == 'pista':

                if new_game.quito_pista(1) == True and pista <= 1:

                    pista = pista + 1
                    print(juego.get('clue_1'))
                    buen_continue()
                
                elif new_game.quito_pista(1) == False or pista > 1:

                    print('No + pistas en este juego')
                    buen_continue()

            else:

                print(lose)
                new_game.quito_vida(1/2)
                if new_game.game_over() == True:
    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()
                
                continuar = try_again()

    else:
          
        frase = 'tengo en mi cuenta 50,00 $'
        respuesta = '''[int(float(x)) for x in frase.replace(",",".").split(' ') if x.replace('.','',1).isdigit()][0]'''
        correcto = input('Indique su codigo en una sola linea:\n>>')
        pista = 1
        continuar = 1

        while continuar == 1:

            if correcto == respuesta:

                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                new_game.agrego_objeto(left_game.get('award'))
                # print(new_game.mostrar())
                to_be_continue()
                continuar = 0
                break

            elif correcto == """int(float(x)) for x in frase.replace(",",".").split(' ') if x.replace('.','',1).isdigit()""":
                
                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                new_game.agrego_objeto(left_game.get('award'))
                # print(new_game.mostrar())
                continuar = 0
                to_be_continue()
                break
            
            elif correcto == 'soyadmin':

                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                new_game.agrego_objeto(left_game.get('award'))
                # print(new_game.mostrar())
                continuar = 0
                to_be_continue()
                break
            
            elif correcto == 'pista':
                
                if new_game.quito_pista(1) == True and pista < 3:

                    if pista == 1:
        
                        print(juego.get('clue_1'))
                        buen_continue()

                    if pista == 2:
        
                        print(juego.get('clue_2'))
                        buen_continue()

                    if pista == 3:

                        print(juego.get('clue_3'))
                        buen_continue()

                    pista = pista + 1

                elif new_game.quito_pista(1) == False or pista > 3:

                    print('No + pistas')
                    buen_continue()
                
            else:
    
                print(lose)
                new_game.quito_vida(1/2)

                if new_game.game_over() == True:

                    se_acabo(new_game,instanteInicial)
                    menu_juego()

                continuar = try_again()
        
def preguntas_mate(name_game, left_game, new_game , instanteInicial):

    nombre = left_game.get('name')
    rules = left_game.get('rules')
    lista_preguntas = left_game.get('questions')

    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    question_random = juego.get('question')
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar_todo())
    # si gana  ensenarselo en pantalla etc. new_game.agrego_vida(1)

    continuar = 1
    x = sy.symbols('x')

    while continuar == 1:

        if pregunta == 0:
            

            f_1 = (sy.sin(x))/2
            c_1 = sy.Derivative(f_1)
            a_1 = c_1.doit()
            d_1 = a_1.evalf(subs={x: math.pi})
    
            correcto = round(d_1,2)
            # print(type(correcto))
            # print(float(correcto))
            while True:

                try:

                    respuesta = float(input('Indique su respuesta:\n >>'))
                    break

                except:
                
                    print('Ingreso invalido')

          
            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste:',left_game.get('award'))
                new_game.agrego_vida(1)
                continuar = 0
                time.sleep(2)
                return 1

            else:

                print(lose)
                new_game.quito_vida(1/4)

                if new_game.game_over() == True:
                    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()

                continuar = try_again()
                if continuar == 0:

                    return 0
        
        elif pregunta == 1:

            f_2 = (sy.cos(x/2))/2 - (sy.tan(x))/5
            c_2 = sy.Derivative(f_2)
            a_2 = c_2.doit()
            d_2 = a_2.evalf(subs={x: math.pi})

            correcto = round(d_2,1)
            correcto = float(correcto)
            correcto = round(correcto,1)
            # print(type(correcto))
            # print(correcto)
            
            while True:

                try:

                    respuesta = float(input('Indique su respuesta:\n >>'))
                    break

                except:

                    print('Ingreso invalido')

            respuesta = round(respuesta,1)
            # print(type(respuesta))
            # print(respuesta)
            if respuesta == float(correcto):

                print(win)
                print(f'Felicidades obtuviste:',left_game.get('award'))
                new_game.agrego_vida(1)
                continuar = 0
                time.sleep(3)
                return 1
            
            else:

                print(lose)
                new_game.quito_vida(1/4)

                if new_game.game_over() == True:
                    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()

                continuar = try_again()
                if continuar == 0:

                    return 0
        
        elif pregunta == 2:

            f_3 = (sy.sin(x))/5 -(sy.tan(x))
            a = math.pi
            c_3 = sy.Derivative(f_3)
            a_3 = c_3.doit()
            d_3 = a_3.evalf(subs={x: a/3})

            correcto = round(d_3,1)
            correcto = float(correcto)
            correcto = round(correcto,1)
            # print(type(correcto))
            # print(correcto)

            while True:

                try:

                    respuesta = float(input('Indique su respuesta:\n >>'))
                    break

                except:

                    print('Ingreso invalido')

            # print(type(respuesta))
            # print(respuesta)
            respuesta = round(respuesta,1)
            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste:',left_game.get('award'))
                new_game.agrego_vida(1)
                continuar = 0
                time.sleep(3)
                return 1

            else:

                print(lose)
                new_game.quito_vida(1/4)
                if new_game.game_over() == True:
                    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()

                continuar = try_again()
                if continuar == 0:

                    return 0

def millonario(name_game,left_game, new_game, instanteInicial):

    nombre = left_game.get('name')
    rules = left_game.get('rules')
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)

    juego = lista_preguntas[pregunta]
    continuar = 1
    correcto = 'b'
    question_random = juego.get('question')
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar_todo())
    while continuar == 1:

        print(f'''
            A --> {juego.get('answer_2')}      B --> {juego.get('correct_answer')}

            C --> {juego.get('answer_3')}      D --> {juego.get('answer_4')}
        ''')

        opcion = input('Elige una opcion:\n>>').lower()
            # while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        #     opcion = input("Ingreso invalido, ingrese una opcion:\n>>")
        pista = 0
        if opcion.lower() == correcto:

            print(win)
            print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
            new_game.agrego_objeto(left_game.get('award'))
            # print(new_game.mostrar())
            continuar = 0
            to_be_continue()

            break

        elif opcion.lower() == 'pista':
            
            if new_game.quito_pista(1) == True and pista == 0:

                pista = pista + 1
                print(juego.get('clue_1'))
                buen_continue()
            
            elif new_game.quito_pista(1) == False:

                buen_continue()

        else:

            print(lose)
            new_game.quito_vida(1/2)

            if new_game.game_over() == True:

                se_acabo(new_game,instanteInicial)
                menu_juego()

            continuar = try_again()
    
def p_mezcladas(name_game,left_game, new_game, instanteInicial):
    
    nombre = left_game.get('name')
    rules = left_game.get('rules')
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    question_random = juego.get('question')
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar_todo())
    palabras = juego.get('words')

    # print(palabras)
    buena = random.randint(0,4)
    one_word = palabras[buena]
    # print(one_word)
    correcta = list(one_word)
    random.shuffle(correcta)
    list_str = ' '.join([str(elem) for elem in correcta])
    
    continuar = 1
    while continuar == 1:

        print('Categoria:',juego.get('category'))
        print(list_str)

        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")

        for x in range(len(palabras)):
            
            if respuesta == palabras[x]:

                print(win)
                print(f'Felicidades obtuviste una contraseña: escapandoando')
                new_game.agrego_objeto("introducir contraseña de la computadora")
                continuar = 0
                to_be_continue()
                break

            elif x == (len(palabras)-1):

                print(lose)
                new_game.quito_vida(1/2)

                if new_game.game_over() == True:
    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()

                continuar = try_again() 

            elif x == 'pista':

                print('Aqui no hay pistas')
                pass

def sopa_letras(name_game, center_game, new_game, instanteInicial):   
    
    nombre = center_game.get('name')
    rules = center_game.get('rules')
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    question_random = juego.get('question')
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar())
    time.sleep(3)

    DIM = 15

    palabras = [juego.get('answer_1').lower(),juego.get('answer_2').lower(),juego.get('answer_3').lower(),'zxahfyd']
    
    matriz = Matrix(DIM)
    while matriz.libres:
        palabra = palabras[random.randint(0, len(palabras) - 1)]
        largo = len(palabra)
        matriz.put(palabra)

    pista = 1
    continuar = 1
    palabra_menos = 3
    while continuar == 1:
        print(matriz)
        # print(matriz.palabras)  
        respuesta = input('Indique que palabra encuentra\n>>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese la respuesta :\n >>")
        
        if respuesta == juego.get('answer_1').lower() or respuesta == juego.get('answer_2').lower() or respuesta == juego.get('answer_3').lower():

            palabra_menos = palabra_menos - 1
            print('CORRECTO SIGUE ASI!')
            time.sleep(1)

            if palabra_menos == 0:

                print(win)
                new_game.agrego_vida(1)
                print('Obtuviste -->', center_game.get('award'))
                continuar = 0
                return 1
        
        elif respuesta == 'pista':
                
            if new_game.quito_pista(1) == True and pista < 3:
    
                if pista == 1:
    
                    print(juego.get('clue_1'))
                    buen_continue()

                if pista == 2:
    
                    print(juego.get('clue_2'))
                    buen_continue()

                if pista == 3:

                    print(juego.get('clue_3'))
                    buen_continue()

                pista = pista + 1
            
            elif new_game.quito_pista(1) == False or pista > 3:
    
                print('No + pistas en este juego')
                buen_continue()

        else:

            print('Incorrecta tu palabra media vida menos')
            new_game.quito_vida(1/2)

            if new_game.game_over() == True:
            
                se_acabo(new_game,instanteInicial)
                menu_juego()

            continuar = try_again()

            if continuar == 0:

                return 0

def ahorcado(name_game, center_game, new_game, instanteInicial):
    
    nombre = center_game.get('name')
    rules = center_game.get('rules')
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    random_question = juego.get('question')
    game = Juegos(nombre,rules,random_question)

    print(game.mostrar_todo())

    palabra = juego.get('answer')
    # print(palabra)
    print ("Start")

    word = palabra.lower()
    #creates an variable with an empty value
    guesses = ''
    continuar = 1
    pista = 1
    while continuar == 1:         

        failed = 0             

        for char in word:      

            if char in guesses:    
        
                print (char)    

            else:
        
                print ("_")     
        
                failed += 1    

        if failed == 0:   

            print(win)
            print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
            new_game.agrego_objeto(center_game.get('award'))
            to_be_continue()
            continuar = 0
            break 
                

        letra_letra = input("guess a character:") 
        while not ("".join(letra_letra.split(" "))).isalpha():
            letra_letra = input("Ingreso invalido, ingrese una letra:\n >> ")

        guesses += letra_letra

        if letra_letra == 'pista':
                
            if new_game.quito_pista(1) == True and pista < 3:
    
                if pista == 1:
    
                    print(juego.get('clue_1'))
                    buen_continue()

                if pista == 2:
    
                    print(juego.get('clue_2'))
                    buen_continue()

                if pista == 3:

                    print(juego.get('clue_3'))
                    buen_continue()

                pista = pista + 1
            
            elif new_game.quito_pista(1) == False or pista > 3:
    
                print('No + pistas en este juego')
                buen_continue()


        elif letra_letra not in word:     

            print ("Wrong, perdiste 1/4 de vida")
            new_game.quito_vida(1/4)

            if new_game.game_over() == True:
        
                se_acabo(new_game,instanteInicial)
                menu_juego()

            continuar = try_again()
     
def solve_logic(name_game,center_game, new_game, instanteInicial):
    
    nombre = center_game.get('name')
    rules = center_game.get('rules')

    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    question_random = juego
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar())
    print(juego)
    
    continuar = 1
    while continuar == 1:    

        if pregunta == 1:

            correcto = 41

            while True:

                try: 

                    respuesta = int(input('Indique la respuesta:\n>>'))
                    break

                except:

                    print("Ingreso Invalido.")

            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
                new_game.agrego_objeto(center_game.get('award'))
                to_be_continue()
                time.sleep(3)
                continuar = 0
                break

            else:

                print(lose)
                new_game.quito_vida(1)
                if new_game.game_over() == True:
        
                    se_acabo(new_game,instanteInicial)
                    menu_juego()        
                continuar = try_again()
        
        else:

            correcto = 67
            
            while True:

                try: 

                    respuesta = int(input('Indique la respuesta:\n>>'))
                    break

                except:

                    print("Ingreso Invalido.")

            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
                new_game.agrego_objeto(center_game.get('award'))
                to_be_continue()
                continuar = 0
                break

            else:

                print(lose)
                new_game.quito_vida(1)

                if new_game.game_over() == True:
    
                    se_acabo(new_game,instanteInicial)
                    menu_juego()

                continuar = try_again()

        #print(juego.get('questions'))

def logic_bool(name_game,center_game, new_game, instanteInicial):

    nombre = center_game.get('name')
    rules = center_game.get('rules')
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    question_random = juego.get('question')
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar_todo())

    respuesta = input('Indique la respuesta:\n>>')
    while not ("".join(respuesta.split(" "))).isalpha():
        respuesta = input("Ingreso invalido, ingrese una respuesta valida:\n >> ")

    continuar = 1
    while continuar == 1:

        if respuesta.title() == juego.get('answer'):

            print(win)
            print(f'Felicidades obtuviste -->',center_game.get('award'))
            new_game.agrego_vida(1)
            continuar = 0
            return 1
            
        else:

            print(lose)
            new_game.quito_vida(1/2)
            print('Vuelve a intentarlo')
            time.sleep(2)

            if new_game.game_over() == True:
    
                se_acabo(new_game,instanteInicial)
                menu_juego()

            return 0

def refranes(new_game, instanteInicial):
    
    refranes = ['Camaron que se duerme...' , 'Guerra avisada...', 'Tres tristes tigres...', 'De tal palo...']

    answer = ['se lo lleva la corriente', 'no mata soldado', 'comen trigo en un trigal', 'tal astilla']

    # print('')
    pregunta = random.randint(0,3)
    nombre = 'Refranes/Trabalenguas'
    rules = 'Pierdes una vida al equivocarte cuidado no vayas a perder aqui'
    question_random = 'Completa el refran o trabalengua para parar la catastrofe!'
    game = Juegos(nombre,rules,question_random)
    print(game.mostrar_todo())
    print(refranes[pregunta])

    continuar = 1
    while continuar == 1:

        respuesta = input('Indique la respuesta:\n>>')
        while not ("".join(respuesta.split(" "))).isalpha():

            respuesta = input("Ingreso invalido, ingrese una respuesta valida:\n >> ")

        if respuesta == answer[pregunta]:

            print(win)
            ganador(new_game, instanteInicial)
            menu_juego()
            
        else:

            print(lose)
            new_game.quito_vida(1)

            if new_game.game_over() == True:
    
                se_acabo(new_game,instanteInicial)
                menu_juego()

            continuar = try_again()
        


