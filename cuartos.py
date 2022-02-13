class Cuartos:
    '''
    Nombre: str 
    gracias a esta clase sabremos donde esta el jugador y 
    se ira creando el cuarto donde este
    '''

    def __init__(self,name):
        self.name = name

    def mostrar(self):
        return (f'Nombre del cuarto: {self.name}')