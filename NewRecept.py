from tkinter import *
from tkinter import tix
from tkinter.constants import *
from Combo import *

fen=NONE

def fenetreNewRecept():


    Norme = "ASME BPE"

    #Définition de la nouvelle fenetre

    fen = Toplevel()
    fen.title("Nouvelle récéption")

    #Définition des différents labels

        #Titre

    titre = Label(fen, text="Nouvelle réception")

        #Nom des champs

    com = Label(fen, text="N° de commande : ")
    fournisseur = Label(fen, text="Fournisseur : ")  # Mettre un menu déroulant
    designation = Label(fen, text="Designation : ")
    norme = Label(fen, text="Norme : ")
    diametre = Label(fen, text="Diamètre :")
    diametreun = Label(fen, text="ø1")
    diametredeux = Label(fen, text="ø2")
    diametretrois = Label(fen, text="ø3")
    rugosite = Label(fen, text="Rugosité : ")
    heatnumber = Label(fen, text="Numéro de coulée : ")

    #Définition des différents champs :

        #Champs de saisie

    champcom = Entry(fen, width=150)
    champfournisseur = Entry(fen, width=150)
    champdesignation = Entry(fen, width=150)
    champnorme = Entry(fen, width=150)
    champdiametreun = Entry(fen)
    champdiametredeux = Entry(fen)
    champdiametretrois = Entry(fen)
    champrugosite = Entry(fen, width=150)
    champheatnumber = Entry(fen, width=150)



        #Champs de menu déroulant

    comboDiamUn = NewCombo(fen, valnorme)
    comboDiamDeux = NewCombo(fen, valnorme)
    comboDiamTrois = NewCombo(fen, valnorme)


        #Bouttons

    bttest = Button(fen, text="tester", command = ImportComboDiam)#(fen, valnorme))



    #Placement des éléments dans la fenetre

        #Placement des Labels

            #Placement du titre

    titre.grid(row=1, column=1, columnspan=7)

            #Placement du nom des champs

    com.grid(row=2, column=1)
    fournisseur.grid(row=3, column=1)
    designation.grid(row=4, column=1)
    norme.grid(row=5, column=1)
    diametre.grid(row=6, column=1)
    diametreun.grid(row=6, column=2)
    diametredeux.grid(row=6, column=4)
    diametretrois.grid(row=6, column=6)
    rugosite.grid(row=7, column=1)
    heatnumber.grid(row=8, column=1)

        #Placement des champs

            #Placement des Entry

    champcom.grid(row=2, column=2, columnspan=6, padx=10, pady=10)
    champfournisseur.grid(row=3, column=2, columnspan=6, padx=10, pady=10)
    champdesignation.grid(row=4, column=2, columnspan=6, padx=10, pady=10)
    champnorme.grid(row=5, column=2, columnspan=6, padx=10, pady=10)
    champrugosite.grid(row=7, column=2, columnspan=6, padx=10, pady=10)
    champheatnumber.grid(row=8, column=2, columnspan=6, padx=10, pady=10)

            #Placement des ComboBox

    comboDiamUn.grid(row=6, column=3, padx=10, pady=10)
    comboDiamDeux.grid(row=6, column=5, padx=10, pady=10)
    comboDiamTrois.grid(row=6, column=7, padx=10, pady=10)



            #Bouton test

    bttest.grid(row=9)

