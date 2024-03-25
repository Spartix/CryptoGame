import sqlite3
import jwt

SECRET_KEY = '"PasTresSecretLaCleSecrete"'
class user:

    def IsValid(mail,mdp,cursor):
        print("je me connecte")
        assert type(mail) == str, "l'e-mail est invalide"
        assert '@' and '.' in mail,"l'e-mail est invalide"    
        assert type(mdp) == str, "le mot de passe est invalide"
        assert len(mdp) <= 12, "le mot de passe déâsse la limite"
        #FAIRE LA REQUEST
        cursor.execute(f"select ID_User FROM users where email = '{mail}' and pass = '{mdp}'")
        response = cursor.fetchall()
        print(response) # Le reponse contient donc tous les utilisateurs
        return response != []

    def IsLogin(token,cursor):
        cursor.execute(f"select ID_User FROM users where Token = '{token}'")
        response = cursor.fetchall()
        return response != []

    def GetToken(email,pas,cursor):
        cursor.execute(f"select ID_User FROM users where email = '{email}' and pass = '{pas}'")
        response = cursor.fetchall()
        if(user.IsValid(email,pas,cursor)):
            print(response[0])
            # encoded_jwt = JWT.encode({"username": email,"ID":response[0][0]}, "PasTresSecretLaCleSecrete", algorithm="HS256")
            accesstoken = user.encode_token({"username": email,"ID":response[0][0]})
            #need to add the access token to database
        return accesstoken

    # Secret key for encoding and decoding JWT tokens
    

    def encode_token(payload):
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token  # Convert bytes to string

    def decode_token(token):
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload