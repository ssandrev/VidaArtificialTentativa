import pygame, random
import Criaturas
import numpy as np


def verificaLado(pos, campo):
    if (pos[1] + 1) != 60 and (pos[1] - 1) != -1 and (pos[0] + 1) != 60 and (pos[0] - 1) != -1:
        c = pos[0], (pos[1] + 1)
        b = pos[0], (pos[1] - 1)
        e = (pos[0] + 1), pos[1]
        d = (pos[0] - 1), pos[1]
        cont = 0
        tentando = True
        up = down = left = right = True
        while (tentando):
            y = random.randint(0, 3)
            if y == 0 and up:
                up = False
                cont += 1
                if campo[c] == 0 and pos[1] != 60:
                    return True
            if y == 1 and down:
                down = False
                cont += 1
                if campo[b] == 0 and pos[1] != 0:
                    return True
            if y == 2 and left:
                left = False
                cont += 1
                if campo[e] == 0 and pos[0] != 60:
                    return True
            if y == 3 and right:
                right = False
                cont += 1
                if campo[d] == 0 and pos[0] != 0:
                    return True
            if cont == 4:
                return False
    else:
        return False


def verificaPosInic(pos, campo):
    if (campo[pos] == 0):
        return True
    else:
        return False


def main():
    black = 0, 0, 0
    white = 255, 255, 255
    green = 124, 252, 0
    red = 255, 0, 0
    x1 = 300 / 30
    y1 = 300 / 30

    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.mixer.__PYGAMEinit__
    pygame.init()
    relogio = pygame.time.Clock()

    c = np.zeros((60, 60))
    plantas = []
    planta_skin = pygame.Surface((5, 5))
    planta_skin.fill(green)
    initpos = 0, 0
    adao = Criaturas.planta(False, initpos, c, green)
    herbivoros = []
    plantas.append(adao)
    c[adao.pos] = 1
    sol = True

    campo = 300, 300
    screen = pygame.display.set_mode(campo)
    pygame.display.set_caption("Fauna e Flora")
    cont = 0
    while (plantas):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plantas.clear()

        for planta in plantas:
            planta.fotossintese(sol)
            if verificaLado(planta.pos, c):
                if planta.reproducao():
                    filho = Criaturas.planta(True, planta.pos, c, planta.cor)
                    c[filho.pos] = 1
                    plantas.append(filho)
            if random.randint(0, 1000) == 10:
                planta.morte()
            if planta.die:
                c[planta.pos] = 0
                plantas.remove(planta)

        '''for herbivoro in herbivoros:
            pos_ant = herbivoro.movimentacao(c)
            c[herbivoro.pos] = 2
            if herbivoro.reproducao():
                filho_h = Criaturas.Herbivoro(True, pos_ant, c, herbivoro.cor)
                c[filho_h.pos] = 2
                herbivoros.append(filho_h)
            else: c[pos_ant] = 0
            if random.randint(0, 10000) == 100:
                herbivoro.morte()
            if herbivoro.die:
                c[herbivoro.pos] = 0
                herbivoros.remove(herbivoro)

        for planta in plantas:
            if c[planta.pos] == 2:
                planta.morte()
            if planta.die:
                c[planta.pos] = 0
                plantas.remove(planta)'''


        if cont < 10:
            cont += 1
        if cont == 10:
            tent = True
            while tent:
                initpos = random.randint(0, 59), random.randint(0, 59)
                if verificaPosInic(initpos, c):
                    eva = Criaturas.Herbivoro(False, initpos, c, red)
                    c[eva.pos] = 2
                    herbivoros.append(eva)
                    cont += 1
                    tent = False
        screen.fill(black)
        for planta in plantas:
            # pygame.draw.circle(screen, planta.cor, planta.rect, 2)
            screen.blit(planta.skin, planta.rect)
        '''for herbivoro in herbivoros:
            #pygame.draw.circle(screen, herbivoro.cor, herbivoro.rect, 2)
            screen.blit(herbivoro.skin, herbivoro.rect)'''
        pygame.display.flip()
        relogio.tick(5)




main()
