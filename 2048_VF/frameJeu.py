from tkinter import *
import time
import threading
from tkinter import messagebox

from framePlateau import FramePlateau
class FrameJeu(Frame):

    def __init__(self, master):
        self.master= master
        self.framePlateau = FramePlateau(self)


class Window(Tk):
    # touche gauche
    def allLeft(self, event):
        if self.isRunning:
            self.upPossible = False
            self.rightPossible = False
            self.downPossible = False
            self.firstMoove = True
            if self.autoPlay is False and self.leftPossible:
                self.framePlateau.allLeft()
                self.lblScore.configure(text='Score:\n' +str(self.framePlateau.score))
            self.upPossible = True
            self.rightPossible = True
            self.downPossible = True
            self.win()
            self.gameOver()

    # touche droit
    def allRight(self, event):
        if self.isRunning:
            self.upPossible = False
            self.leftPossible = False
            self.downPossible = False
            self.firstMoove = True
            if self.autoPlay is False and self.rightPossible:
                self.framePlateau.allRight()
                self.lblScore.configure(text='Score:\n' +str(self.framePlateau.score))
            self.upPossible = True
            self.leftPossible = True
            self.downPossible = True
            self.win()
            self.gameOver()

    # touche haut
    def allUp(self, event):
        if self.isRunning:
            self.rightPossible = False
            self.leftPossible = False
            self.downPossible = False
            self.firstMoove = True
            if self.autoPlay is False and self.upPossible:
                self.framePlateau.allUp()
                self.lblScore.configure(text='Score:\n' +str(self.framePlateau.score))
            self.rightPossible = True
            self.leftPossible = True
            self.downPossible = True
            self.win()

    # touche bas
    def allDown(self, event):
        if self.isRunning:
            self.rightPossible = False
            self.leftPossible = False
            self.upPossible = False
            self.firstMoove = True
            if self.autoPlay is False and self.downPossible:
                self.framePlateau.allDown()
                self.lblScore.configure(text='Score:\n' +str(self.framePlateau.score))
            self.rightPossible = True
            self.leftPossible = True
            self.upPossible = True
            self.win()

    # revenir en arrière
    def undo(self):
        if self.firstMoove and self.autoPlay is False:
            self.framePlateau.undo()
            self.lblMsg.place_forget()
            self.lblMsg = Label(self, text='Joignez les tuiles pour faire 2048.', fg=self.framePlateau.bg,
                                font=('Courrier', 15))
            self.lblMsg.place(x=100, y=125, width=407, h=40)
            self.win()
            if self.isRunning == False:
                self.isRunning = True


    def __init__(self):
        super(Window, self).__init__()
        self.iconbitmap('Icone2048.ico')
        self.isRunning = True
        self.title("2048")
        self.geometry("600x720")
        # framePlateau
        self.framePlateau = FramePlateau(self)
        self.bind("<KeyRelease-Left>", self.allLeft)
        self.bind("<KeyRelease-Right>", self.allRight)
        self.bind("<KeyRelease-Up>", self.allUp)
        self.bind("<KeyRelease-Down>", self.allDown)

        self.firstMoove = False
        # score
        self.lblScore = Label(self, text='Score:\n' +str(self.framePlateau.score), bg='black',fg='white', font =('Courrier', 15))
        self.lblScore.place(height=50, width=135, x=230, y=10)

        # Button Undo
        self.buttonUndo = Button(self, text='UNDO', command=self.undo, bg='red', font=('Courrier',20), fg='white')
        self.buttonUndo.place(x=370, y=70, width=135, height=50)

        # Button Restart
        self.btnRestart = Button(self, text='RESTART', command=self.restart, bg='red', font=('Courrier',20), fg='white')
        self.btnRestart.place(x=230, y=70, width=135, height=50)


        #lblIcone
        self.lblIcone = Label(self,
                              text='2048',
                              bg=self.framePlateau.color.get(2048),
                              fg=self.framePlateau.fg.get(2048),
                              font=('Courrier', 40)
                              )
        self.lblIcone.place(x=100, y=10, width=110, height=110)

        self.lblMsg = Label(self, text='Joignez les tuiles pour faire 2048.', fg=self.framePlateau.bg, font=('Courrier', 15))
        self.lblMsg.place(x=100, y=125, width=407, h=40)

        ######### Variable pour le bot

        # Button Auto
        self.buttonAuto = Button(self, text='AUTO', command=self.auto, bg='red', font=('Courrier', 20), fg='white')
        self.buttonAuto.place(x=370, y=10, width=135, height=50)
        self.autoPlay = False

        # Button Stop
        self.buttonStop = Button(self, text='STOP', command=self.stop, bg='red', font=('Courrier', 20), fg='white')

        # les threads
        self.threadAuto = threading.Thread(target=self.auto)
        self.threadStop = threading.Thread(target=self.stop)

        ######### Fin des variables pour le bot

        # mainloop
        self.mainloop()

    # activer le jeu auto
    def auto(self):
        self.buttonAuto.place_forget()
        self.buttonStop.place(x=370, y=10, width=135, height=50)
        self.update()
        self.autoPlay = True
        i = 0
        while self.autoPlay:
            if self.isRunning:
                self.framePlateau.algoIA()
                self.lblScore.configure(text='Score:\n' + str(self.framePlateau.score))
                self.win()
                self.gameOver()
                i += 1
                self.update()
            else:
                self.stop()
                #time.sleep(1)
        self.update()

    # desactiver le jeu auto
    def stop(self):
        self.autoPlay = False
        self.buttonStop.place_forget()
        self.buttonAuto.place(x=370, y=10, width=135, height=50)
        self.update()

    def restart(self):
        reponse = messagebox.askyesno('Recommencer?', "Voulez vous vraiment recommencer?")
        if reponse == 1:
            self.framePlateau.restart()
            self.lblScore.configure(text='Score:\n' + str(self.framePlateau.score))
            self.stop()
            self.lblMsg.place_forget()
            self.lblMsg = Label(self, text='Joignez les tuiles pour faire 2048.', fg=self.framePlateau.bg, font=('Courrier', 15))
            self.lblMsg.place(x=100, y=125, width=407, h=40)
            self.isRunning = True

    def win(self):
        if self.framePlateau.win():
            self.lblMsg.configure(text='You Won!', bg='red', fg='white', font=('Courrier', 25))
            self.update()
            return True

    # Variables pour éviter de lancer 2 déplacements a la fois(bug)
    leftPossible = True
    upPossible = True
    rightPossible = True
    downPossible = True

    def gameOver(self):
        if not self.framePlateau.moovePossible():
            self.lblMsg.place_forget()
            self.lblMsg = Label(self, text='Game Over! Plus Aucun Mouvement Possible.', fg='red',
                                font=('Courrier', 15))
            self.lblMsg.place(x=100, y=125, width=407, h=40)
            self.isRunning = False


