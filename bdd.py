import mysql.connector

class BDD:
    """classe pour gérer une baseb de données"""
    def __init__(self, base, pseudo, passe, hote, port=None):
        """Se connecter à la base de données"""
        self.nom = base
        self.hote = hote
        self.gerant = pseudo
        if port is not None:
            self.connexion = mysql.connector.connect(host=hote,
                                                 user=pseudo, password=passe,
                                                 database=base, port=port)
        else:
            self.connexion = mysql.connector.connect(host=hote,
                                                 user=pseudo, password=passe,
                                                 database=base)
        self.curseur = self.connexion.cursor()
    def __del__(self):
        """Se déconnecter"""
        self.connexion.close()
    def __repr__(self):
        """Quand on entre l'objet dans l'interpréteur"""
        return "<Base : {} ; serveur : {} ; gerant : {}>".format(self.nom, self.hote, self.gerant)
    def __str__(self):
        """Afficher la base"""
        return "Base {} sur le serveur {} gérer par {}".format(self.nom, self.hote, self.gerant)
    def modifBase(self, requete):
        """Exécute une requête qui modifie le base de données"""
        try:
            self.curseur.execute(requete)
            print("Execution : requète =", requete)
        except:
            print("ERREUR : requète =", requete)
    def inserer(self, requete, *donnees, **nommees):
        """Insérer des données ou ajouter une ligne"""
        try:
            if donnees and not nommees:
                requetec = requete
                i = requete.find('%')
                for donnee in donnees:
                    j = i+1
                    if(requetec[j] == 's'):
                        requetec = requetec.replace('%' + requetec[j], "'" + str(donnee) + "'", 1)
                    elif(requetec[j] == 'd'):
                        requetec = requetec.replace('%' + requetec[j], str(donnee), 1)
                    i = requetec.find('%')
                self.curseur.execute(requete, tuple(donnees))
            elif nommees and not donnees:
                requetec = requete
                i = requete.find('%')
                for nomme in nommees:
                    j = i + 3 + len(nomme)
                    srt1 = '%(' + nomme + ')' + requetec[j]
                    if(requetec[j] == 's'):
                        srt2 = str(nommees[nomme])
                    elif(requetec[j] == 'd'):
                        srt2 = str(nommees[nomme])
                    requetec = requetec.replace(srt1, srt2, 1)
                    i = requetec.find('%')
                #self.curseur.execute(requete, nommees)
                self.curseur.execute(requetec)
            self.connexion.commit()
            print("Execution : requète =", requetec)
        except:
            print("ERREUR : requète =", requetec, "; données =", donnees, "; nommées =", nommees)
            self.connexion.rollback()
    def select(self, requete, *donnees):
        try:
            requetec = requete
            i = requete.find('%')
            for donnee in donnees:
                j = i+1
                if(requetec[j] == 's'):
                    requetec = requetec.replace('%' + requetec[j], "'" + str(donnee) + "'", 1)
                elif(requetec[j] == 'd'):
                    requetec = requetec.replace('%' + requetec[j], str(donnee), 1)
                i = requetec.find('%')
            #self.curseur.execute(requete, tuple(donnees))
            self.curseur.execute(requetec)
            print("Execution : requète =", requetec)
            return self.curseur.fetchall()
        except:
            print("ERREUR : requète =", requetec, "; données =", donnees)
    def update(self, requete, *donnees, **nommees):
        """mettre à jour une ou des lignes"""
        try:
            if donnees and not nommees:
                requetec = requete
                i = requete.find('%')
                for donnee in donnees:
                    j = i+1
                    if(requetec[j] == 's'):
                        requetec = requetec.replace('%' + requetec[j], "'" + str(donnee) + "'", 1)
                    elif(requetec[j] == 'd'):
                        requetec = requetec.replace('%' + requetec[j], str(donnee), 1)
                    i = requetec.find('%')
                self.curseur.execute(requete, tuple(donnees))
            elif nommees and not donnees:
                requetec = requete
                i = requete.find('%')
                for nomme in nommees:
                    j = i + 3 + len(nomme)
                    srt1 = '%(' + nomme + ')' + requetec[j]
                    if(requetec[j] == 's'):
                        srt2 = str(nommees[nomme])
                    elif(requetec[j] == 'd'):
                        srt2 = str(nommees[nomme])
                    requetec = requetec.replace(srt1, srt2, 1)
                    i = requetec.find('%')
                #self.curseur.execute(requete, nommees)
                self.curseur.execute(requetec)
            self.connexion.commit()
            print("Execution : requète =", requetec)
        except:
            print("ERREUR : requète =", requetec, "; données =", donnees, "; nommées =", nommees)
            self.connexion.rollback()

# if __name__ == "__main__":
