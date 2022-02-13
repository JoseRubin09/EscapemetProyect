import random

class Cursor:

    def __init__(self, fila, columna):

        self.fila = fila
        self.columna = columna
        self.avanX = [-1, 0, 1][random.randint(0,2)]
        self.avanY = [-1, 0, 1][random.randint(0,2)]
        if self.avanX == 0 and self.avanY == 0:
            self.avanX = 1

    def next(self, pasos=1):
        self.fila += pasos * self.avanX
        self.columna += pasos * self.avanY

    def es_valido(self, dimension):
        return 0 <= self.fila < dimension and 0 <= self.columna < dimension

    def __str__(self):
        return f"[{self.fila} {self.avanX}, {self.columna} {self.avanY}]"