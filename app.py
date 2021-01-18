import bdd

class Appr:
    base = bdd.BDD('kusanagi', 'root', '', 'localhost')
    #base = bdd.BDD('kusanagi', 'root', 'root', 'localhost', port=8081)
    table = []
    def __init__(self, id):
        colonnes = Appr.base.select("SHOW COLUMNS FROM apprenants")
        valeurs = Appr.base.select("SELECT * FROM `apprenants` WHERE id_apprenant = %s ORDER BY prenom, nom", id)
        for i, valeur in enumerate(valeurs):
            for attr_value in valeur:
                setattr(self, colonnes[i][0], attr_value)
        Appr.table.insert(id, self)
    
    def save(self):
        Appr.base.update(self, "UPDATE `apprenants` SET `prenom`=%s, `nom`=%s, `pseudo`=%s, `email`=%s WHERE `id_apprenant`=%s", self.prenom, self.nom, self.pseudo, self.email, self.id)