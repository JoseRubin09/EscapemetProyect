class Partida:

    '''
    vidas: float numero que con un metodo le quitare o agregare vidas
    pistas: int que le quitare a medida que usa las pistas
    tiempo: str idk
    '''
    def __init__(self, dificultad, vidas, pistas, tiempo):

        self.dificultad = dificultad
        self.vidas = vidas
        self.pistas = pistas
        self.tiempo = tiempo

    
    def mostrar(self):
        
        return(f"Vidas: {self.vidas}\nPistas: {self.pistas}\nTiempo: {self.tiempo}\n")

    def mostrar_tiempo(self):

        return(f'{self.tiempo}')

    def quito_vida(self,num):
        
        self.vidas = self.vidas - num 

        return(f'{self.vidas}')
    
    def game_over(self):

        if self.vidas <= 0:

            return True

    def quito_pista(self,num):
        
        self.pistas = int(self.pistas) - num
        if self.pistas == 0:

            ('Lo siento no te quedan mas pistas suerte jeje')
            
            return False

        else:

            print(f'Perdiste una pista te quedan: {self.pistas} en todo el juego')
            return True

    def agrego_vida(self,num):

        self.vidas = self.vidas + num

    def ded_time(self):
    
        return (self.tiempo)

    