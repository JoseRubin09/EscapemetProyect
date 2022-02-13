from frases import instruccion

def instrucciones():
    print(instruccion)
    print('''Un escape room, sala de escape o cuarto de escape es un juego de 
    aventura físico y mental que consiste en encerrarte a ti en una habitación, 
    donde deberán solucionar enigmas y rompecabezas de todo tipo
    para ir desenlazando una historia y conseguir escapar antes de que 
    finalice el tiempo disponible.''')
    while True:

        try:
            opcion = int(input('Presione 1 para ver las teclas y 2 para salir al menu'))
            if opcion > 2:
                pass
            elif opcion < 2:    
                break
        
        except:
            ('Ingreso invalido\n')

    if opcion == 1:

        print('''
        ████████╗███████╗ █████╗ ██╗      █████╗  ██████╗
        ╚══██╔══╝██╔════╝██╔══██╗██║     ██╔══██╗██╔════╝
           ██║   █████╗  ██║  ╚═╝██║     ███████║╚█████╗    
           ██║   ██╔══╝  ██║  ██╗██║     ██╔══██║ ╚═══██╗   
           ██║   ███████╗╚█████╔╝███████╗██║  ██║██████╔╝
           ╚═╝   ╚══════╝ ╚════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ 
    W ---> Para elegir el objeto que esta en el medio
    A ---> Para elegir el objeto que esta a la izquierda
    D ---> Para elegir el objeto que esta a la derecha
    S ---> Para ir al cuarto que hay antes de ese 
    SPACE ---> Para ir al siguiente cuarto
    M ---> Para ver este mismo menu de juego
    I ---> Para ver tu inventario
    OJO: Cuidado! 
    Completando cuartos obtendras objetos para seguir adelante...
    Dependiendo de la dificultad vas a tener una cierta cantidad de vidas y pistas, tambien
    un determinado tiempo para completar el juego
                            Buena suerte!''')

    elif opcion == 2:
        pass

    
