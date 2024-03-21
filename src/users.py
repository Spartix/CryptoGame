import sqlite3
import jwt

conn = sqlite3.connect('DB_CryptoGame.db')
cursor = conn.cursor()

class user:

    def IsValid(mail,mdp):
        print("je me connecte")
        assert type(mail) == str, "l'e-mail est invalide"
        assert '@' and '.' in mail,"l'e-mail est invalide"    
        assert type(mdp) == str, "le mot de passe est invalide"
        assert len(mdp) <= 12, "le mot de passe déâsse la limite"
        #FAIRE LA REQUEST
        cursor.execute(f"select ID_User FROM users where email = '{mail}' and pass = '{mdp}'")
        response = cursor.fetchall()
        print(response) # Le reponse contient donc tous les utilisateurs
        return response == []

    def IsLogin(token):
        cursor.execute(f"select ID_User FROM users where Token = '{token}'")
        response = cursor.fetchall()
        return response == []

    def GetToken(user,pas):
        cursor.execute(f"select ID_User FROM users where email = '{user}' and pass = '{pas}'")
        response = cursor.fetchall()
        if(user.IsValid(user,pas)):
            encoded_jwt = jwt.encode({"username": user,"ID":response[0][0]}, "PasTresSecretLaCleSecrete", algorithm="HS256")
        return response[0][0]