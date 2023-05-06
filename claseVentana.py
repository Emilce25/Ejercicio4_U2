class Ventana:
    __titulo=""
    __x1=""
    __y1=""
    __x2=""
    __y2=""
    
    def __init__(self, titulo, x1, y1, x2, y2):
        self.titulo = titulo
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def mover_izquierda(self):
        if self.x1 > 0 and self.x2 > 0:
            self.x1 -= 1
            self.x2 -= 1
        
    def mover_derecha(self):
        if self.x1 < 499 and self.x2 < 499:
            self.x1 += 1
            self.x2 += 1
        
    def mover_arriba(self):
        if self.y1 > 0 and self.y2 > 0:
            self.y1 -= 1
            self.y2 -= 1
        
    def mover_abajo(self):
        if self.y1 < 499 and self.y2 < 499:
            self.y1 += 1
            self.y2 += 1
            
    def __str__(self):
        return f"{self.titulo}: ({self.x1}, {self.y1}), ({self.x2}, {self.y2})"
