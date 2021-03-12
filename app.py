import bdd

class Appr:
    # base = bdd.BDD('kusanagi', 'root', '', 'localhost')
    base = bdd.BDD('kusanagi', 'root', 'root', 'localhost', port=8081)
    table = []
    def __init__(self, id):
        valeurs = Appr.base.select("SELECT * FROM `apprenants` WHERE id_apprenant = %s ORDER BY prenom, nom", id)
        for valeur in valeurs:
            self.id = valeur[0]
            self.prenom = valeur[1]
            self.nom = valeur[2]
            self.pseudo = valeur[3]
            self.email = valeur[4]
        Appr.table.insert(id, self)
    
    def save(self):
        Appr.base.update(self, "UPDATE `apprenants` SET `prenom`=%s, `nom`=%s, `pseudo`=%s, `email`=%s WHERE `id_apprenant`=%s", self.prenom, self.nom, self.pseudo, self.email, self.id)