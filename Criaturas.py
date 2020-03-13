import random
import pygame




class planta():
    def __init__(self, filho, pos, campo, cor):
        self.energia = 10
        self.idade = 0
        self.die = False
        self.pos = self.getPos(filho, pos, campo)
        self.rect = self.pos[0] * 5, self.pos[1] * 5
        self.skin = pygame.Surface((5, 5))
        self.cor =  self.skinColor( cor, filho )#self.skin.fill((124, 252, 0))


    def skinColor( self, cor, filho ):
        if filho:
            x = cor[0] + random.randint(0, 5)
            y = cor[1] + random.randint(0, 5)
            z = cor[2] + random.randint(0, 5)
            if x > 255:
                x -= 256
            if y > 255:
                y -= 256
            if z > 255:
                z -= 256
            cor = x, y, z
            self.skin.fill(cor)
        else: self.skin.fill(cor)
        return cor

    def getPos( self, filho, pos, campo ):
        if filho == False:
            x = random.randint(0, 59), random.randint(0, 59)
        else:
            c = pos[0], (pos[1] + 1)
            b = pos[0], (pos[1] - 1)
            e = (pos[0] + 1), pos[1]
            d = (pos[0] - 1), pos[1]
            cont = 0
            tentando = True
            up = down = left = right = True
            while(tentando):
                y = random.randint(0, 3)
                if y == 0 and up:
                    up = False
                    cont += 1
                    if campo[c] == 0 and pos[1] != 59:
                        x = pos[0], pos[1] + 1
                        tentando = False
                if y == 1 and down:
                    down = False
                    cont += 1
                    if campo[b] == 0 and pos[1] != 0:
                        x = pos[0], pos[1] - 1
                        tentando = False
                if y == 2 and left:
                    left = False
                    cont += 1
                    if campo[e] == 0 and pos[0] != 59:
                        x = pos[0] + 1, pos[1]
                        tentando = False
                if y == 3 and right:
                    right = False
                    cont += 1
                    if campo[d] == 0 and pos[0] != 0:
                        x = pos[0] - 1, pos[1]
                        tentando = False

                #if cont == 4:
                 #   tentando = False
        return x


    def reproducao(self):
        if self.energia >= 50:
            self.energia -= 40
            return True
        else:
            return False

    def fotossintese(self, sol):
        if sol == True:
            self.energia += 20
            self.idade += 3
            if self.idade >= 100:
                self.die = True
        else:
            self.energia -= 10

    def morte(self):
            self.die = True


class Herbivoro():
    def __init__(self, filho, pos, campo, cor):
        self.energia = 10
        self.idade = 0
        self.die = False
        self.pos = pos
        self.rect = self.pos[0] * 5, self.pos[1] * 5
        self.skin = pygame.Surface((5, 5))
        self.cor = self.skinColor(cor)

    def skinColor(self, cor):
        '''if filho:
            x = cor[0] + random.randint(0, 5)
            y = cor[1] + random.randint(0, 5)
            z = cor[2] + random.randint(0, 5)
            if x > 255:
                x -= 256
            if y > 255:
                y -= 256
            if z > 255:
                z -= 256
            cor = x, y, z
            self.skin.fill(cor)
        else:'''
        self.skin.fill(cor)
        return cor

    def reproducao(self):
        if self.energia == 50:
            self.energia -= 40
            return True
        else:
            return False

    def alimentacao(self, new_pos):
        self.energia += 5
        self.pos = new_pos


    def movimentacao(self, campo):
        pos = self.pos
        c = self.pos[0], (self.pos[1] + 1)
        b = self.pos[0], (self.pos[1] - 1)
        e = (self.pos[0] + 1), self.pos[1]
        d = (self.pos[0] - 1), self.pos[1]
        tent_ali = True
        cont = 0
        up = down = left = right = True
        comeu = False
        while tent_ali:
            xy = random.randint(0, 3)
            if xy == 0 and up:
                    cont += 1
                    up = False
                    if self.pos[1] != 59:
                        if campo[c] == 1:
                            self.alimentacao(c)
                            tent_ali = False
                            comeu = True

            if xy == 1 and down:
                    down = False
                    cont += 1
                    if self.pos[1] != 0:
                        if campo[b] == 1:
                            self.alimentacao(b)
                            tent_ali = False
                            comeu = True

            if xy == 2 and left:
                    cont += 1
                    left = False
                    if self.pos[0] != 59:
                        if campo[e] == 1:
                            self.alimentacao(e)
                            tent_ali = False
                            comeu = True

            if xy == 3 and right:
                    cont += 1
                    right = False
                    if self.pos[0] != 0:
                        if campo[d] == 1:
                            self.alimentacao(d)
                            tent_ali = False
                            comeu = True

            if cont == 4:
                tent_ali = False

        if not comeu:
            #cont = 0
            up = down = left = right = True
            tent_andar = True
            while tent_andar:
                xy = random.randint(0, 3)
                if xy == 0 and up:
                    cont += 1
                    up = False
                    if self.pos[1] != 59:
                        if campo[c] == 0:
                            self.pos = c
                            tent_andar = False

                if xy == 1 and down:
                    down = False
                    cont += 1
                    if self.pos[1] != 0:
                        if campo[b] == 0:
                            tent_andar = False
                            self.pos = b

                if xy == 2 and left:
                    cont += 1
                    left = False
                    if self.pos[0] != 59:
                        if campo[e] == 0:
                            self.pos = e
                            tent_andar = False

                if xy == 3 and right:
                    cont += 1
                    right = False
                    if self.pos[0] != 0:
                        if campo[d] == 0:
                            self.pos = d
                            tent_andar = False

                if up == down == left == right == False:
                    tent_andar = False


        self.idade += 1
        if self.idade >= 55:
            self.morte()
        self.rect = self.pos[0] * 5, self.pos[1] * 5

        return pos

    def morte(self):
            self.die = True
