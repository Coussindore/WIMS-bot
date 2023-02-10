from ExerciceClass import *

link = input("Lien de l'exercice : ")

exercice = Exercice1Reponse(link)

exercice.actualiser()

nombre1 = int(exercice.enonce[0].split(" %")[-2:])
nombre2 = int(exercice.enonce[1].split(" %")[-2:])

resultat = (nombre1/100) * (nombre2/100) * 100

exercice.repondre(resultat)
