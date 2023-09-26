
class Point():
    def __init__(self, x , y, colour = "black"):
        self.x = x
        self.y = y
        self.z = 1
        self.colour = colour

class Line():
    def __init__(self, pi, pf, colour = "black"):
        self.xi = pi.x
        self.xf = pf.x
        self.yi = pi.y
        self.yf = pf.y
        self.zi = pi.z
        self.zf = pf.z
        self.colour = colour

class Wireframe():
    def __init__(self, colour = "black"):
        self.pontos = []
        self.colour = colour

    def add_ponto(self, p):
        self.pontos.append(p)


