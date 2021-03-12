import app
import fichier

appr1 = app.Appr(1)

app.Appr.base.modifBase("""ALTER TABLE apprenants
ADD email varchar(255)""")

fm = fichier.Fichier(r"apprenantmail.txt")
lm = fm.listeF()
lm.sort()

for i in range(1, 21):
    app.Appr(i)

for collegue in app.Appr.table:
    for mail in lm:
        print('mail =', mail)
        print('pseudo_email =', (collegue.prenom.lower() + '.' + collegue.nom.lower() + '@isen-ouest.yncrea.fr'))
        if((collegue.prenom.lower() + '.' + collegue.nom.lower() + '@isen-ouest.yncrea.fr') == mail):
            collegue.mail = mail
            collegue.save()