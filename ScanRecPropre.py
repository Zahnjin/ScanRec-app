from tkinter import *
from tkinter import tix
from tkinter.constants import *
from NewRecept import *




#Définition de la fenetre principale

menuPrincipal = Tk()

#Définition des boutons du menu principal


bouttonNewRecept = Button(menuPrincipal,text="Nouvelle réception", command=fenetreNewRecept)
bouttonConsulterBase = Button(menuPrincipal, text="Consulter Base de données")


#Placement des éléments

bouttonNewRecept.pack(fill=X, ipady=15, padx=10, pady=10)
bouttonConsulterBase.pack(fill=X, ipady=15, padx=10, pady=10)

#Boucle de la fenetre

menuPrincipal.mainloop()