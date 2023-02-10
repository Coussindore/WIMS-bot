import requests
import webbrowser

class Exercice1Reponse:

    def __init__(self, lien) -> None:
        self.lien = lien
        self.enonce = [""]
        self.question = ""

    def actualiser(self):

        page = requests.get(self.lien)

        text = page.text

        text = text.split("oefstatement")[1]

        self.enonce = text.split("<p>")[0].split("<br />")

        for i in range (len(self.enonce)) :
            while not self.enonce[i][1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                self.enonce[i] = self.enonce[i][1:]

        self.question = text.split("<p>")[1].split("</label>")[0].split(">")[1]

        return None

    def repondre(self, reponse):

        session = self.lien.split("session=")[1].split("&")[0]
        langue = self.lien.split("lang=")[1].split("&")[0]
        module = self.lien.split("module=")[1].split("&")[0]
        debut = self.lien.split("?")[0]

        lienReponse = debut + "?session=" + session + "&+lang=" + langue + "&+module=" + module + "&+reply1=" + reponse

        webbrowser.open(lienReponse)
    

