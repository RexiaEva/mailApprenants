import app
import fichier

appr1 = app.Appr(1)

app.Appr.base.modifBase("""ALTER TABLE apprenants
ADD email varchar(255)""")

fm = fichier.Fichier(r"mail.txt")
lm = fm.listeF()
lm.sort()

for i in range(25):
    app.Appr(i)

for collegue in app.Appr.table:
    for mail in lm:
        if((collegue.prenom + '.' + collegue.nom + '@isen-ouest.yncrea.fr') == mail):
            collegue.mail = mail
            collegue.save()