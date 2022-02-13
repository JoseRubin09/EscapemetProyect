class Juegos:
     
    '''
    nombre: str saco el nombre de la API como str
    reglas: str de las reglas del juego de la API
    juego: str del juego que saca random una pregunta 
    hago esta herencia para poder nombrar a esos 
    juegos que tienen mas de una posibilidad de jugar  
    '''
    def __init__(self, nombre, reglas,question_random):
        self.nombre = nombre
        self.reglas = reglas
        self.question_random = question_random

    def mostrar_todo(self):
        
        return(f"Nombre del juego: {self.nombre}\nReglas: {self.reglas}\nPregunta: {self.question_random}\n")

    def mostrar(self):
        
        return(f"Nombre del juego: {self.nombre}\nReglas: {self.reglas}\n")