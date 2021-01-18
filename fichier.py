import os

class Fichier:
    """Gestion des fichiers"""
    def __init__(self, chemin):
        """ouverture fichier
        utiliser une chaîne brute r\"texte\" """
        self.chemin = chemin
    def afficher(self):
        lien = open(self.chemin, 'r')
        contenu = lien.read()
        print(contenu)
        lien.close()
    def listeF(self):
        lien = open(self.chemin, 'r')
        contenu = lien.read()
        liste = contenu.split('\n')
        lien.close()
        return liste

def cd(chemin):
    """changer de repertoir courant
    utiliser une chaîne brute r"texte" """
    os.chdir(chemin)
def pwd():
    """afficher le repertoir courant
    utiliser une chaîne brute r"texte" """
    print(os.getcwd())

if __name__ == "__main__":
    pwd()