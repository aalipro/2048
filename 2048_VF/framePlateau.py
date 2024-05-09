import telnetlib
from tkinter import*
import random
import time
from tkinter.font import Font

import IA


class FramePlateau(Frame):
    LIGNES=4
    COLONES=4
    plateau = [[0] * 4] + [[0] * 4] + [[0] * 4] + [[0] * 4]

    lesLabels = []
    height = 85
    width = 85
    color = {0: "#CDC0B4",
             2: "#EEE4DA",
             4: "#EDE0C8",
             8: "#F2B179",
             16: "#F59563",
             32: "#F67C5F",
             64: "#F65E3B",
             128: "#EDCC61",
             256: "#EDCC61",
             512: "#EDC850",
             1024: "#EDC53F",
             2048: '#EDC22E'}


    fg = {
        0: "#CDC0B4",
        2: "black",
        4: "black",
        8: "white",
        16: "white",
        32: "white",
        64: "white",
        128: "white",
        256: "white",
        512:"white",
        1024: "white",
        2048: "white"
    }

    fontsize = {
        0: 38,
        2: 38,
        4: 38,
        8: 38,
        16: 34,
        32: 34,
        64: 34,
        128: 32,
        256: 32,
        512: 32,
        1024: 28,
        2048: 28
    }

    bg = "#BBADA0"
    mouvementEffectue = False
    score = 0

    # VARIABLES ANIMATION
    bool_anim = [[False] * 4] + [[False] * 4] + [[False] * 4] + [[False] * 4]
    mettreA = [[0] * 4] + [[0] * 4] + [[0] * 4] + [[0] * 4]
    anime = {}
    velocity = 40
    time = 0.0000000001
    lesLabelsAnime = []
    add_anime = []
    #  VARIABLES BUTTON
    plateauUndo = [[0] * 4] + [[0] * 4] + [[0] * 4] + [[0] * 4]

    def change_plateau_undo(self):
        for l in range(self.LIGNES):
            for c in range(self.COLONES):
                n = self.plateau[l][c]
                self.plateauUndo[l][c] = n

    def undo(self):
        for l in range(self.LIGNES):
            for c in range(self.COLONES):
                n = self.plateauUndo[l][c]
                print(n)
                self.modifieCase(l, c, n)
        self.update()
    #GAUCHE
    def addLeft(self, ligne):
        for colone in range(self.COLONES-1):
            if (self.plateau[ligne][colone] == 0):
                break
            if self.plateau[ligne][colone] == self.plateau[ligne][colone + 1]:
                self.modifieCase(ligne, colone, 2 * self.plateau[ligne][colone])
                self.modifieCase(ligne, colone + 1, 0)
                self.score += self.plateau[ligne][colone]
                self.add_anime.append([ligne, colone])
                #self.anime_add(ligne, colone)
                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True
                self.left(ligne)
                self.drawLabelAnime()
                self.animeLeft()
    def animation_genereCase(self, l, c):
        x = int(self.lesLabels[l][c].place_info().get('x'))
        y = int(self.lesLabels[l][c].place_info().get('y'))
        side = 75
        self.lesLabels[l][c].place_configure(x=x + 5, width=side, height=side)
        self.update()
        time.sleep(0.01)
        side += 5
        self.lesLabels[l][c].place_configure(x=x + 3, width=side, height=side)
        self.update()
        time.sleep(0.01)
        self.lesLabels[l][c].place_configure(x=x, width=self.width, height=self.height)
        self.lesLabels[l][c].configure(font=('Courrier', 43))
        self.update()
        time.sleep(0.01)


    def animation_add(self):
        side = 95
        for i in range(len(self.add_anime)):
            l, c = self.add_anime[i][0], self.add_anime[i][1]
            x = int(self.lesLabels[l][c].place_info().get('x'))
            y = int(self.lesLabels[l][c].place_info().get('y'))
            self.lesLabels[l][c].place_configure(x=x - 5, width=side, height=side)
            self.lesLabels[l][c].configure(font=('Courrier', 45))
        self.update()
        time.sleep(self.time)
        side -= 5
        for i in range(len(self.add_anime)):
            l, c = self.add_anime[i][0], self.add_anime[i][1]
            x = int(self.lesLabels[l][c].place_info().get('x'))
            y = int(self.lesLabels[l][c].place_info().get('y'))
            self.lesLabels[l][c].place_configure(x=x - 3, width=side, height=side)
            self.lesLabels[l][c].configure(font=('Courrier', 43))
        self.update()
        time.sleep(self.time)
        for i in range(len(self.add_anime)):
            l, c = self.add_anime[i][0], self.add_anime[i][1]
            x = int(self.lesLabels[l][c].place_info().get('x'))
            y = int(self.lesLabels[l][c].place_info().get('y'))
            '''print('coucou2')
            print(x)'''
            self.lesLabels[l][c].place_configure(x=x+8, y=y, width=self.width, height=self.height)
            self.lesLabels[l][c].configure(font=('Courrier', 40))
        self.update()
        time.sleep(self.time)
        self.add_anime.clear()


    def anime_add(self, l, c):
        x = int(self.lesLabels[l][c].place_info().get('x'))
        y = int(self.lesLabels[l][c].place_info().get('y'))

        side = 95
        self.lesLabels[l][c].place_configure( x=x-5,width=side, height=side)
        self.lesLabels[l][c].configure(font=('Courrier', 45))
        self.lesLabels[l][c].update()
        time.sleep(self.time)
        side -= 5
        self.lesLabels[l][c].place_configure(x=x-3, width=side, height=side)
        self.lesLabels[l][c].configure(font=('Courrier', 43))
        self.lesLabels[l][c].update()
        time.sleep(self.time)
        self.lesLabels[l][c].place_configure(x=x, width=self.width, height=self.height)
        self.lesLabels[l][c].configure(font=('Courrier', 40))
        self.lesLabels[l][c].update()

    def drawLabelAnime(self):
        if len(self.anime) != 0:
            for i in range(len(self.anime)):
                if self.anime.get(i) is not None:
                    ligne_cr = self.anime.get(i)[0][0]
                    colone_cr =  self.anime.get(i)[0][1]
                    ligne_cv  = self.anime.get(i)[1][0]
                    colone_cv = self.anime.get(i)[1][1]
                    n = self.plateau[ligne_cv][colone_cv]
                    unLabel = Label(self, text=str(n), font=("Courrier,", 40), bg=self.color.get(n), fg=self.fg.get(n))
                    self.lesLabelsAnime.append(unLabel)
                    x = self.lesLabels[ligne_cr][colone_cr].place_info().get('x')
                    y = self.lesLabels[ligne_cr][colone_cr].place_info().get('y')
                    self.lesLabelsAnime[i].place(x=x, y=y, width=self.width, height=self.height)


    def animeLeft(self):
        while not self.animeFini():
            for i in range(len(self.anime)):
                if self.anime.get(i) is not None:
                    ligne_cr = self.anime.get(i)[0][0]
                    colone_cr = self.anime.get(i)[0][1]
                    ligne_cv = self.anime.get(i)[1][0]
                    colone_cv = self.anime.get(i)[1][1]
                    if self.bool_anim[ligne_cr][colone_cr]:
                        x = int(self.lesLabelsAnime[i].place_info().get('x'))
                        y = int(self.lesLabelsAnime[i].place_info().get('y'))
                        if int(self.lesLabels[ligne_cv][colone_cv].place_info().get('x')) + self.velocity < x:
                            self.lesLabelsAnime[i].place(x=x-self.velocity)
                        else:
                            self.bool_anim[ligne_cr][colone_cr] = False
                            self.lesLabelsAnime[i].destroy()
                            self.modifieCase1(ligne_cv, colone_cv)
            self.update()
            time.sleep(self.time)
        self.end_animation()

    def end_animation(self):
        '''''
        for i in range(len(self.lesLabelsAnime)):
            self.lesLabelsAnime[i].destroy()
        '''
        self.lesLabelsAnime.clear()
        self.anime.clear()
    def animeFini(self):
        for i in range(self.LIGNES):
            for j in range(self.COLONES):
                if self.bool_anim[i][j] is True:
                    return False
        return True

    def left(self, ligne):
        caseVide = 0
        caseRemplie = 0
        while caseVide < self.COLONES and caseRemplie < self.COLONES:
            if self.plateau[ligne][caseVide] == 0:
                caseRemplie = caseVide + 1
                while caseRemplie < self.COLONES:
                    if self.plateau[ligne][caseRemplie] != 0:
                        self.plateau[ligne][caseVide] = self.plateau[ligne][caseRemplie]
                        self.anime[len(self.anime)] = [[ligne, caseRemplie], [ligne, caseVide]]
                        #self.anime[str(len(self.anime))] = [[ligne][caseRemplie], [ligne][caseVide]]
                        self.bool_anim[ligne][caseRemplie] = True
                        self.modifieCase(ligne, caseRemplie, 0)
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue = True
                        caseVide += 1

                        break
                    caseRemplie += 1
            else:
                caseVide += 1

    def allLeft(self):
        self.change_plateau_undo()
        for ligne in range(self.LIGNES):
            self.left(ligne)
        self.drawLabelAnime()
        self.animeLeft()
        for ligne in range(self.LIGNES):
            self.addLeft(ligne)
        '''
        for i in range(len(self.add_anime)):
            self.anime_add(self.add_anime[i][0], self.add_anime[i][1])
        self.add_anime.clear()
        '''
        self.animation_add()
        if self.mouvementEffectue:
            self.genereCase()
        self.print_plateau()

    def right(self, ligne):
        caseVide=self.COLONES-1
        caseRemplie=self.COLONES-1
        while caseVide >=0 and caseRemplie>=0:
            if self.plateau[ligne][caseVide] == 0:
                caseRemplie= caseVide-1
                while caseRemplie >= 0:
                    if self.plateau[ligne][caseRemplie] !=0 :
                        self.plateau[ligne][caseVide] = self.plateau[ligne][caseRemplie]
                        self.anime[len(self.anime)] = [[ligne, caseRemplie], [ligne, caseVide]]
                        # self.anime[str(len(self.anime))] = [[ligne][caseRemplie], [ligne][caseVide]]
                        self.bool_anim[ligne][caseRemplie] = True
                        self.modifieCase(ligne, caseRemplie, 0)
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue = True
                        caseVide -= 1
                        break
                    caseRemplie -= 1
            else:
                caseVide -= 1

    def addRight(self, ligne):
        for colone in range(self.COLONES-1, 0, -1):
            if self.plateau[ligne][colone] == 0:
                break
            if self.plateau[ligne][colone] == self.plateau[ligne][colone-1]:
                self.modifieCase(ligne, colone , 2* self.plateau[ligne][colone])
                self.modifieCase(ligne, colone-1, 0)
                self.score += self.plateau[ligne][colone]
                self.anime_add(ligne, colone)
                self.right(ligne)
                self.drawLabelAnime()
                self.animeRight()
                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True

    def animeRight(self):
        while not self.animeFini():
            for i in range(len(self.anime)):
                if self.anime.get(i) is not None:
                    ligne_cr = self.anime.get(i)[0][0]
                    colone_cr = self.anime.get(i)[0][1]
                    ligne_cv = self.anime.get(i)[1][0]
                    colone_cv = self.anime.get(i)[1][1]
                    if self.bool_anim[ligne_cr][colone_cr]:
                        x = int(self.lesLabelsAnime[i].place_info().get('x'))
                        y = int(self.lesLabelsAnime[i].place_info().get('y'))
                        if int(self.lesLabels[ligne_cv][colone_cv].place_info().get('x')) - self.velocity > x:
                            self.lesLabelsAnime[i].place(x=x+self.velocity)
                        else:
                            self.bool_anim[ligne_cr][colone_cr] = False
                            self.lesLabelsAnime[i].destroy()
                            self.modifieCase1(ligne_cv, colone_cv)
            self.update()
            time.sleep(self.time)
        self.end_animation()

    def allRight(self):
        self.change_plateau_undo()
        for ligne in range(self.LIGNES):
            self.right(ligne)
        self.drawLabelAnime()
        self.animeRight()
        for ligne in range(self.LIGNES):
            self.addRight(ligne)
        '''
        for i in range(len(self.add_anime)):
            self.anime_add(self.add_anime[i][0], self.add_anime[i][1])
        self.add_anime.clear()
        '''
        self.animation_add()
        if self.mouvementEffectue:
            self.genereCase()
        self.print_plateau()


    # DOWN
    def down(self, colone):
        caseVide = self.COLONES - 1
        caseRemplie = self.COLONES - 1
        while caseVide >= 0  and caseRemplie >=0:
            if self.plateau[caseVide][colone] == 0:
                caseRemplie= caseVide-1
                while caseRemplie >= 0:
                    if self.plateau[caseRemplie][colone] != 0:
                        self.plateau[caseVide][colone] = self.plateau[caseRemplie][colone]
                        self.anime[len(self.anime)] = [[caseRemplie, colone], [caseVide, colone]]
                        # self.anime[str(len(self.anime))] = [[ligne][caseRemplie], [ligne][caseVide]]
                        self.bool_anim[caseRemplie][colone] = True
                        self.modifieCase(caseRemplie, colone, 0)
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue= True
                        caseVide -= 1
                        break
                    caseRemplie -= 1
            else:
                caseVide-=1

    def addDown(self, colone):
        for ligne in range(self.LIGNES-1, 0, -1):
            if self.plateau[ligne][colone] ==0:
                break
            if self.plateau[ligne][colone] == self.plateau[ligne-1][colone] :
                self.modifieCase(ligne, colone, 2 * self.plateau[ligne][colone])
                self.modifieCase(ligne-1, colone, 0)
                self.score += self.plateau[ligne][colone]
                self.add_anime.append([ligne, colone])
                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True
                self.down(colone)
                self.drawLabelAnime()
                self.animeDown()
    def animeDown(self):
        while not self.animeFini():
            for i in range(len(self.anime)):
                if self.anime.get(i) is not None:
                    ligne_cr = self.anime.get(i)[0][0]
                    colone_cr = self.anime.get(i)[0][1]
                    ligne_cv = self.anime.get(i)[1][0]
                    colone_cv = self.anime.get(i)[1][1]
                    if self.bool_anim[ligne_cr][colone_cr]:
                        x = int(self.lesLabelsAnime[i].place_info().get('x'))
                        y = int(self.lesLabelsAnime[i].place_info().get('y'))
                        if int(self.lesLabels[ligne_cv][colone_cv].place_info().get('y')) - self.velocity > y:
                            self.lesLabelsAnime[i].place(y=y + self.velocity)
                        else:
                            self.bool_anim[ligne_cr][colone_cr] = False
                            self.lesLabelsAnime[i].destroy()
                            self.modifieCase1(ligne_cv, colone_cv)
            self.update()
            time.sleep(self.time)
        self.end_animation()

    def allDown(self):
        self.change_plateau_undo()
        for colone in range(self.COLONES):
            self.down(colone)
        self.drawLabelAnime()
        self.animeDown()
        for colone in range(self.COLONES):
            self.addDown(colone)
        '''
        for i in range(len(self.add_anime)):
            self.anime_add(self.add_anime[i][0], self.add_anime[i][1])
        self.add_anime.clear()
        '''
        self.animation_add()
        if self.mouvementEffectue:
            self.genereCase()
        self.print_plateau()

    #UP
    def up(self, colone):
        caseVide=0
        caseRemplie=0
        while caseVide< self.LIGNES and caseRemplie < self.LIGNES:
            if self.plateau[caseVide][colone] == 0:
                caseRemplie= caseVide+1
                while caseRemplie<self.LIGNES:
                    if self.plateau[caseRemplie][colone] !=0:
                        self.plateau[caseVide][colone] = self.plateau[caseRemplie][colone]
                        self.anime[len(self.anime)] = [[caseRemplie, colone], [caseVide, colone]]
                        # self.anime[str(len(self.anime))] = [[ligne][caseRemplie], [ligne][caseVide]]
                        self.bool_anim[caseRemplie][colone] = True
                        self.modifieCase(caseRemplie, colone, 0)
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue = True
                        caseVide += 1
                        break
                    caseRemplie+=1
            else:
                caseVide+=1

    def addUp(self, colone):
        for ligne in range(self.LIGNES-1):
            if self.plateau[ligne][colone] == 0:
                break
            if self.plateau[ligne][colone] == self.plateau[ligne+1][colone]:
                self.modifieCase(ligne, colone, 2 * self.plateau[ligne][colone])
                self.modifieCase(ligne +1, colone, 0)
                self.score += self.plateau[ligne][colone]
                self.add_anime.append([ligne, colone])
                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True
                self.up(colone)
                self.drawLabelAnime()
                self.animeUp()

    def allUp(self):
        self.change_plateau_undo()
        for colone in range(self.COLONES):
            self.up(colone)
        self.drawLabelAnime()
        self.animeUp()
        for colone in range(self.COLONES):
            self.addUp(colone)
        '''
        for i in range(len(self.add_anime)):
            self.anime_add(self.add_anime[i][0], self.add_anime[i][1])
        self.add_anime.clear()
        '''
        self.animation_add()
        if self.mouvementEffectue:
            self.genereCase()
        self.print_plateau()


    def animeUp(self):
        while not self.animeFini():
            for i in range(len(self.anime)):
                if self.anime.get(i) is not None:
                    ligne_cr = self.anime.get(i)[0][0]
                    colone_cr = self.anime.get(i)[0][1]
                    ligne_cv = self.anime.get(i)[1][0]
                    colone_cv = self.anime.get(i)[1][1]
                    if self.bool_anim[ligne_cr][colone_cr]:
                        x = int(self.lesLabelsAnime[i].place_info().get('x'))
                        y = int(self.lesLabelsAnime[i].place_info().get('y'))
                        if int(self.lesLabels[ligne_cv][colone_cv].place_info().get('y')) + self.velocity < y:
                            self.lesLabelsAnime[i].place(y=y - self.velocity)
                        else:
                            self.bool_anim[ligne_cr][colone_cr] = False
                            self.lesLabelsAnime[i].destroy()
                            self.modifieCase1(ligne_cv, colone_cv)
            self.update()
            time.sleep(self.time)
        self.end_animation()

    def genereCase(self):
        n = random.randint(0, 9)
        caseVide = False
        while (not caseVide):
            # nombre= random.randint(0)
            ligne = random.randint(0, 3)
            colone = random.randint(0, 3)
            caseVide = self.plateau[ligne][colone] == 0
            hasard = {0: 2,
                      1: 2,
                      2: 2,
                      3: 2,
                      4: 2,
                      5: 2,
                      6: 2,
                      7: 2,
                      8: 2,
                      9: 4}
            if caseVide:
                self.modifieCase(ligne, colone, hasard.get(n))
                self.animation_genereCase(ligne, colone)
                self.mouvementEffectue = False
                break
            self.mouvementEffectue = False

    # CONSTRUCTEUR
    def __init__(self, master):
        super(FramePlateau, self).__init__(master=master, bg=self.bg)
        X=10
        Y=10
        #c11er les labeles et les placer
        for i in range(self.LIGNES):
            self.lesLabels.append([])
            for j in range(self.COLONES):
                unLabel = Label(self, text=str(0), font=("Courrier,", 40), bg=self.color.get(0), fg=self.fg.get(0))
                self.lesLabels[i].append(unLabel)
                self.lesLabels[i][j].place(x=X+j*100, y=Y+i*(self.width+Y), width= self.width, height= self.height)
        self.place(height=397, width=405, x=100, y=170)

        #generer 2 cases
        self.genereCase()
        self.genereCase()

    #MODIFIER UNE CASE
    def modifieCase(self, ligne, colone, nombre):
        self.plateau[ligne][colone] = nombre
        self.lesLabels[ligne][colone].config(text=str(nombre),bg=self.color.get(nombre), fg=self.fg.get(nombre), font=('Courrier',self.fontsize.get(nombre)))

    def modifieCase1(self, ligne , colone):
        nombre = self.plateau[ligne][colone]
        self.lesLabels[ligne][colone].config(text=str(nombre),bg=self.color.get(nombre), fg=self.fg.get(nombre), font=('Courrier',self.fontsize.get(nombre)))

    def print_plateau(self):
        '''for ligne in range(self.LIGNES):
            print(self.plateau[ligne])
        print('---------+++---------')'''

    def moovePossible(self):
        for ligne in range(self.LIGNES):
            for colone in range(self.COLONES):
                if self.plateau[ligne][colone] == 0:
                    return True

    def uneCaseEstVide(self):
        for i in range(self.LIGNES):
            for j in range(self.COLONES):
                if self.plateau[i][j] == 0:
                    return True
        return False

    def addHorizontalPossible(self):
        for i in range(self.LIGNES):
            for j in range(self.COLONES-1):
                if self.plateau[i][j] == self.plateau[i][j+1]:
                    return True
        return False

    def addVerticalePossible(self):
        for colone in range(self.COLONES):
            for ligne in range(self.LIGNES-1):
                if self.plateau[ligne][colone] == 0:
                    break
                if self.plateau[ligne][colone] == self.plateau[ligne+1][colone]:
                    return True

    def mouvementPossible(self):
        if self.uneCaseEstVide() or self.addHorizontalPossible() or self.addVerticalePossible() :
            return True
        else:
            return False

    def win(self):
        for i in range(self.COLONES):
            for j in range(self.LIGNES):
                if self.plateau[i][j] == 2048:
                    return True
        return False


#-----------PARTIE IA------------

#plateau virtuel pour faire tourner l'IA
    plateau2 = [[0] * 4] + [[0] * 4] + [[0] * 4] + [[0]*4]
#booleen direction du premier coup de la recherche
    bhaut = False
    bbas = False
    bdroite = False
    bgauche = False
#score total pour chaque direction
    haut = 0
    bas = 0
    droite = 0
    gauche = 0
#compteur pour chaque direction (premier coup de la position initiale)
    chaut = 1
    cbas = 1
    cdroite = 1
    cgauche = 1
#compteur nombre essai
    cpt = 0
#score d'un essai
    score2 = 0
#nombre d'essai total
    ESSAI = 100

    def algoIA(self):
        print(self.score)
        #boucle de n essai
        while(self.cpt<self.ESSAI):

            #initialisation d'un essai
            self.initialisationIA()

            #boucle pour un essai
            while (self.possible_up() or self.possible_down() or self.possible_right() or self.possible_left()):
                self.aleatoire()

            #ajout du score en fonction du premier coup de l'essai
            if self.bhaut:
                self.haut += self.score2
            elif self.bbas:
                self.bas += self.score2
            elif self.bdroite:
                self.droite += self.score2
            elif self.bgauche:
                self.gauche += self.score2

        for i in range(4):
            for j in range(4):
                self.plateau2[i][j] = self.plateau[i][j]

        #trie des scores obtenus
        liste = [[self.haut/self.chaut, 'haut'], [self.bas/self.cbas,'bas'], [self.gauche/self.cgauche, 'gauche'], [self.droite/self.cdroite, 'droite']]
        liste2 = sorted(liste)

        #exécution du coup en fonction du resultat
        if liste2[3][1] == 'haut':
            self.allUp()
        elif liste2[3][1] == 'bas':
            self.allDown()
        elif liste2[3][1] == 'gauche':
            self.allLeft()
        elif liste2[3][1] == 'droite':
            self.allRight()

        self.cpt = 0
        self.haut = 0
        self.bas = 0
        self.droite = 0
        self.gauche = 0
        self.chaut = 1
        self.cbas = 1
        self.cdroite = 1
        self.cgauche = 1

    #decale les cases vers la droite
    def rightIA(self, ligne):
        caseVide = self.COLONES - 1
        caseRemplie = self.COLONES - 1
        while caseVide >= 0 and caseRemplie >= 0:
            if self.plateau2[ligne][caseVide] == 0:
                caseRemplie = caseVide - 1
                while caseRemplie >= 0:
                    if self.plateau2[ligne][caseRemplie] != 0:
                        self.plateau2[ligne][caseVide] = self.plateau2[ligne][caseRemplie]
                        self.plateau2[ligne][caseRemplie] = 0
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue = True
                        caseVide -= 1
                        break
                    caseRemplie -= 1
            else:
                caseVide -= 1

    #additionne les cases vers la droite
    def addRightIA(self, ligne):
        for colone in range(self.COLONES - 1, 0, -1):
            if self.plateau2[ligne][colone] == 0:
                break
            if self.plateau2[ligne][colone] == self.plateau2[ligne][colone - 1]:
                self.plateau2[ligne][colone] = 2 * self.plateau2[ligne][colone]
                self.plateau2[ligne][colone - 1] = 0
                self.score2 += self.plateau2[ligne][colone]
                self.rightIA(ligne)
                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True

    def allRightIA(self):
        #decale les cases vers la droite
        for ligne in range(self.LIGNES):
            self.rightIA(ligne)
        #additionne les cases vers la droite
        for ligne in range(self.LIGNES):
            self.addRightIA(ligne)
        #genere une nouvelle case
        if self.mouvementEffectue:
            self.genereCaseIA()

    #decale les cases vers la gauche
    def leftIA(self, ligne):
        caseVide = 0
        caseRemplie = 0
        while caseVide < self.COLONES and caseRemplie < self.COLONES:
            if self.plateau2[ligne][caseVide] == 0:
                caseRemplie = caseVide + 1
                while caseRemplie < self.COLONES:
                    if self.plateau2[ligne][caseRemplie] != 0:
                        self.plateau2[ligne][caseVide] = self.plateau2[ligne][caseRemplie]
                        self.plateau2[ligne][caseRemplie] = 0
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue = True
                        caseVide += 1
                        break
                    caseRemplie += 1
            else:
                caseVide += 1

    #additionne les cases vers la gauche
    def addLeftIA(self, ligne):
        for colone in range(self.COLONES-1):
            if (self.plateau2[ligne][colone] == 0):
                break
            if self.plateau2[ligne][colone] == self.plateau2[ligne][colone + 1]:
                self.plateau2[ligne][colone] = 2 * self.plateau2[ligne][colone]
                self.plateau2[ligne][colone + 1] = 0
                self.score2 += self.plateau2[ligne][colone]
                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True
                self.leftIA(ligne)

    def allLeftIA(self):
        #decale les cases vers la gauche
        for ligne in range(self.LIGNES):
            self.leftIA(ligne)
        #additionne les cases vers la gauche
        for ligne in range(self.LIGNES):
            self.addLeftIA(ligne)
        #genere une nouvelle case
        if self.mouvementEffectue:
            self.genereCaseIA()

    #decales les cases vers le bas
    def downIA(self, colone):
        caseVide = self.COLONES - 1
        caseRemplie = self.COLONES - 1
        while caseVide >= 0  and caseRemplie >=0:
            if self.plateau2[caseVide][colone] == 0:
                caseRemplie= caseVide-1
                while caseRemplie >= 0:
                    if self.plateau2[caseRemplie][colone] != 0:
                        self.plateau2[caseVide][colone] = self.plateau2[caseRemplie][colone]
                        self.plateau2[caseRemplie][colone] = 0
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue= True
                        caseVide -= 1
                        break
                    caseRemplie -= 1
            else:
                caseVide-=1

    #additionne vers le bas
    def addDownIA(self, colone):
        for ligne in range(self.LIGNES-1, 0, -1):
            if self.plateau2[ligne][colone] == 0:
                break
            if self.plateau2[ligne][colone] == self.plateau2[ligne-1][colone]:
                self.plateau2[ligne][colone] = 2 * self.plateau2[ligne][colone]
                self.plateau2[ligne - 1][colone] = 0
                self.score2 += self.plateau2[ligne][colone]
                if not self.mouvementEffectue:
                    self.mouvementEffectue = True
                self.downIA(colone)

    def allDownIA(self):
        #decale les cases vers le bas
        for colone in range(self.COLONES):
            self.downIA(colone)
        #additionne les cases vers le bas
        for colone in range(self.COLONES):
            self.addDownIA(colone)
        #genere une nouvelle case
        if self.mouvementEffectue:
            self.genereCaseIA()

    #decale les cases vers le haut
    def upIA(self, colone):
        caseVide=0
        caseRemplie=0
        while caseVide< self.LIGNES and caseRemplie < self.LIGNES:
            if self.plateau2[caseVide][colone] == 0:
                caseRemplie= caseVide+1
                while caseRemplie<self.LIGNES:
                    if self.plateau2[caseRemplie][colone] !=0:
                        self.plateau2[caseVide][colone] = self.plateau2[caseRemplie][colone]
                        self.plateau2[caseRemplie][colone] = 0
                        if self.mouvementEffectue == False:
                            self.mouvementEffectue = True
                        caseVide += 1
                        break
                    caseRemplie+=1
            else:
                caseVide+=1

    #additionne les cases vers le haut
    def addUpIA(self, colone):
        for ligne in range(self.LIGNES-1):

            if self.plateau2[ligne][colone] == 0:
                break

            if self.plateau2[ligne][colone] == self.plateau2[ligne+1][colone]:
                self.plateau2[ligne][colone] = 2 * self.plateau2[ligne][colone]
                self.plateau2[ligne + 1][colone] = 0
                self.score2 += self.plateau2[ligne][colone]

                if self.mouvementEffectue == False:
                    self.mouvementEffectue = True
                self.upIA(colone)

    def allUpIA(self):
        #decale les cases vers le haut
        for colone in range(self.COLONES):
            self.upIA(colone)

        #additionne les cases
        for colone in range(self.COLONES):
            self.addUpIA(colone)

        #genere nouvelle case
        if self.mouvementEffectue:
            self.genereCaseIA()


#generer une nouvelle case
    def genereCaseIA(self):
        n = random.randint(0, 9)
        caseVide = False
        while (not caseVide):
            ligne = random.randint(0, 3)
            colone = random.randint(0, 3)
            caseVide = self.plateau2[ligne][colone] == 0
            hasard = {0: 2,
                      1: 2,
                      2: 2,
                      3: 2,
                      4: 2,
                      5: 2,
                      6: 2,
                      7: 2,
                      8: 2,
                      9: 4}
            if caseVide:
                self.plateau2[ligne][colone] = hasard.get(n)
                self.mouvementEffectue = False
                break
            self.mouvementEffectue = False

#coup aléatoire
    def aleatoire(self):
        n = random.randint(0, 3)

        if n == 0:
            self.allUpIA()
        elif n == 1:
            self.allDownIA()
        elif n == 2:
            self.allLeftIA()
        elif n == 3:
            self.allRightIA()



#initialisation de l'IA avec le premier coup
    def initialisationIA(self):
        #initialisation

        self.bhaut = False
        self.bbas = False
        self.bdroite = False
        self.bgauche = False
        self.score2 = 0
        self.cpt += 1

        #copie de la position actuelle dans le plateau virtuel
        for i in range(4):
            for j in range(4):
                self.plateau2[i][j] = self.plateau[i][j]

        #coup aléatoire
        n = random.randint(0, 3)
        if n == 0:
            self.bhaut = True
            self.allUpIA()
            self.chaut += 1
        elif n == 1:
            self.bbas = True
            self.allDownIA()
            self.cbas += 1
        elif n == 2:
            self.bgauche = True
            self.allLeftIA()
            self.cgauche += 1
        elif n == 3:
            self.bdroite = True
            self.allRightIA()
            self.cdroite += 1










    #self.mouvement()

    def mouvement(self):
        if self.possible_right():
            self.allRight()
        elif self.possible_down():
            self.allDown()
        elif self.possible_up():
            self.allUp()
        elif self.possible_left():
            self.allLeft()
            self.allRight()
        else:
            time.sleep(20)

    def choix_mouvement(self):
        if self.possible_up() and self.possible_right():
            if self.addition_horizontal()>=self.addition_vertical():
                time.sleep(0.1)
                self.allRight()
            elif self.addition_horizontal()<self.addition_vertical():
                time.sleep(0.1)
                self.allUp()
        elif self.possible_up():
            time.sleep(0.1)
            self.allUp()
        elif self.possible_right():
            time.sleep(0.1)
            self.allRight()
        else:
            if self.poids_up()>self.poids_right():
                time.sleep(0.1)
                self.allLeft()
                if self.addition_vertical()>1 and self.plateau2[0][3]!=0:
                    self.allUp()

                time.sleep(0.1)
                for ligne in range(self.LIGNES):
                    print(self.plateau2[ligne])
                print('1----------------------')
                self.allRight()
            else:
                time.sleep(0.1)
                self.allDown()
                if self.addition_horizontal()>1 and self.plateau2[0][3]!=0:
                    self.allRight()

                time.sleep(0.1)
                for ligne in range(self.LIGNES):
                    print(self.plateau2[ligne])
                print('2----------------------')
                self.allUp()

    def poids_up(self):
        nombre = 0
        for i in [0, 1]:
            for j in range(4):
                if self.plateau2[i][j] !=0:
                    nombre = nombre + 1
        return nombre

    def poids_right(self):
        nombre = 0
        for i in range(4):
            for j in [2, 3]:
                if self.plateau2[i][j] != 0:
                    nombre = nombre + 1
        return nombre

    def possible_up(self):
        trouve = False
        for i in [1, 2, 3]:
            for j in range(4):
                if(self.plateau2[i-1][j]==0) & (self.plateau2[i][j]!=0):
                    return True
                elif (self.addition_vertical()>0):
                    return True
        return False

    def possible_down(self):
        trouve = False
        for i in [0, 1, 2]:
            for j in range(4):
                if(self.plateau2[i+1][j]==0) & (self.plateau2[i][j]!=0):
                    return True
                elif (self.addition_vertical()>0):
                    return True
        return False

    def possible_right(self):
        trouve = False
        for j in range(3):
            for i in range(4):
                if(self.plateau2[i][j+1]==0) & (self.plateau2[i][j]!=0):
                    return True
                elif (self.addition_horizontal()>0):
                    return True
        return False

    def possible_left(self):
        trouve = False
        for j in [1, 2, 3]:
            for i in range(4):
                if(self.plateau2[i][j-1]==0) & (self.plateau2[i][j]!=0):
                    return True
                elif (self.addition_horizontal()>0):
                    return True
        return False

    def addition_petit(self, i, j):
        if self.plateau2[i][j]==2 or self.plateau2[i][j]==4:
            return 2
        else:
            return 1

    def addition_vertical(self) :
        nombre = 0
        for i in range(3):
            for j in range(4):
                if (i==0) & (self.plateau2[i][j]!=0) :
                    if (self.plateau2[i][j] == self.plateau2[i+1][j]):
                        nombre = nombre + self.addition_petit(i, j)
                    elif (self.plateau2[i][j] != 0) & (self.plateau2[i+1][j] == 0):
                        if (self.plateau2[i][j] == self.bas_blanc(i, j)):
                            nombre = nombre + self.addition_petit(i, j)
                elif (i==1) & (self.plateau2[i][j]!=0) :
                    if (self.plateau2[i][j] != self.plateau2[i-1][j]):
                        if (self.plateau2[i+1][j] == 0) & (self.plateau2[i+2][j] == self.plateau2[i][j]):
                            nombre = nombre + self.addition_petit(i, j)
                        elif (self.plateau2[i][j] == self.plateau2[i+1][j]) :
                            nombre = nombre + self.addition_petit(i, j)
                elif (i==2) & (self.plateau2[i][j]!=0) :
                    if (self.plateau2[i][j] == self.plateau2[i+1][j]):
                        if (self.plateau2[i-2][j] == self.plateau2[i-1][j]):
                            nombre = nombre + self.addition_petit(i, j)
                        elif (self.plateau2[i][j] != self.plateau2[i-1][j]):
                            nombre = nombre + self.addition_petit(i, j)
                        elif (self.plateau2[i-1][j]==0 & (self.plateau2[i][j] != self.plateau2[i-2][j])):
                            nombre = nombre + self.addition_petit(i, j)
        return nombre

    def bas_blanc(self, y, x):
        trouve = False
        i = 1
        while (i+y < 4) & (not trouve):
            trouve = (self.plateau2[y][x] == self.plateau2[y+i][x])
            i = i + 1
        if trouve:
            return self.plateau2[y][x]
        else:
            return 0

    def addition_horizontal(self):
        nombre = 0
        for j in range(3):
            for i in range(4):
                if (j == 0) & (self.plateau2[i][j] != 0):
                    if (self.plateau2[i][j] == self.plateau2[i][j + 1]):
                        nombre = nombre + self.addition_petit(i, j)
                    elif (self.plateau2[i][j] != 0) & (self.plateau2[i][j + 1] == 0):
                        if (self.plateau2[i][j] == self.droite_blanc(i, j)):
                            nombre = nombre + self.addition_petit(i, j)
                elif (j == 1) & (self.plateau2[i][j] != 0):
                    if (self.plateau2[i][j] != self.plateau2[i][j - 1]):
                        if (self.plateau2[i][j + 1] == 0) & (self.plateau2[i][j + 2] == self.plateau2[i][j]):
                            nombre = nombre + self.addition_petit(i, j)
                        elif (self.plateau2[i][j] == self.plateau2[i][j + 1]):
                            nombre = nombre + self.addition_petit(i, j)
                elif (j == 2) & (self.plateau2[i][j] != 0):
                    if (self.plateau2[i][j] == self.plateau2[i][j + 1]):
                        if (self.plateau2[i][j - 2] == self.plateau2[i][j - 1]):
                            nombre = nombre + self.addition_petit(i, j)
                        elif (self.plateau2[i][j] != self.plateau2[i][j - 1]):
                            nombre = nombre + self.addition_petit(i, j)
                        elif (self.plateau2[i][j - 1] == 0 & (self.plateau2[i][j] != self.plateau2[i][j - 2])):
                            nombre = nombre + self.addition_petit(i, j)
        return nombre

    def droite_blanc(self, x, y):
        trouve = False
        i = 1
        while (i + x < 4) & (not trouve):
            trouve = (self.plateau2[y][x] == self.plateau2[y][x + i])
            i = i + 1
        if trouve:
            return self.plateau2[y][x]
        else:
            return 0

    def restart(self):
        # 1)Changer toutes les case en 0
        for ligne in range(self.LIGNES):
            for colone in range(self.COLONES):
                self.modifieCase(ligne, colone, 0)

        # 2) réinitialiser le score
        self.score = 0

        # 3) Générer 2 cases
        self.genereCase()
        self.genereCase()



"""""
window= Tk()
window.geometry("600x720")

framePlateau= FramePlateau(window)
print(framePlateau.lesLabels[0][0].place_info())
window.bind("<KeyRelease-Left>", framePlateau.allLeft)
window.bind("<KeyRelease-Right>", framePlateau.allRight)
window.bind("<KeyRelease-Down>", framePlateau.allDown)
window.bind("<KeyRelease-Up>", framePlateau.allUp)
framePlateau.modifieCase(0,0,16)
framePlateau.modifieCase(1,0,16)
framePlateau.modifieCase(2,0,16)
framePlateau.modifieCase(3,0,16)
window.mainloop()
"""