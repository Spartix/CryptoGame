import sqlite3

from flask import redirect, render_template
from src.users import user

class Argent:
    def peux_payer(token,argent,types,cursor) -> bool:
        # avec son token savoir si il a assez d'argent ( PeutPayer(token,argent) -> Bool )
        resultat = cursor.execute(f"select BTC,LTC,SOL from Argent JOIN Users on Argent.ID_User = Users.ID_User where Users.Token = ?",(token,))   
        rez = resultat.fetchone()
        d = {"BTC":rez[0],"LTC":rez[1],"SOL":rez[2]}
        if float(argent) <= d[types]:
            return True
        else:
            return False
        
    # exemple : peux_payer("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbi5zcGFydGl4NjY3QGdtYWlsLmNvbSIsIklEIjoxfQ.21SmngKsDncN37JjH95v2qRVmhkkboCFEYBC4I-sLbI",10,"BTC","Akabinks")

        
    def Existe(receveur_username,cursor):
        # verifier si la personne a payer exist ( Existe(receveur_username) -> ID_user & bool )
        res = cursor.execute(f"select id_User from Users Where Username = ?",(receveur_username,))
        user = res.fetchone()
        if user:
            d ={"id":user[0]}
            return (True , d["id"])
        else:
            return (False)
        
    # exemple : Existe("Akabinks") / Existe("Aka")
        
    def Rajouter_Argent(receveur_id,types,montant,conn:sqlite3.Connection):
        cursor = conn.cursor()
        # rajouter de l'argent a qqun ( Rajouter_Argent(receveur_id , type, montant) -> None)
        cursor.execute(f"UPDATE Argent SET {types} = ? WHERE id_User = ?", (montant, receveur_id))
        conn.commit()
 
    def Retire_argent(token,types,montant,conn:sqlite3.Connection):
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Argent SET {types} = (SELECT {types} FROM Argent JOIN Users ON Argent.ID_User = Users.ID_User WHERE Users.Token = ?) - {montant} WHERE ID_User = (SELECT ID_User FROM Users WHERE Token = ?)",(token,token))
        conn.commit()
        
    #exemple : Retire_argent('Akabinks','BTC',7)
        
    def Envoyer(token,receveur_username,types,montant,conn:sqlite3.Connection):

        # Envoyer a qqqun ( Envoyer(token,receveur_username,types,motant) -> None)
        if Argent.peux_payer(token,montant,types,conn.cursor()):
            existe = Argent.Existe(receveur_username,conn.cursor())
            if existe[0]:
                receveur_id = existe[1]
                Argent.Rajouter_Argent(receveur_id,types,montant,conn)
                Argent.Retire_argent(token,types,montant,conn)
                conn.commit()
                return redirect('/send?success=true')
            else:
                return render_template('send.html')
        else:
            return redirect('/send?error=true&message=Pas_Assez_Argent')
   


# Envoyer a qqqun ( Envoyer(token,receveur_username,type,motant) -> None)

    