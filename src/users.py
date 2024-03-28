import sqlite3
import jwt

SECRET_KEY = '"PasTresSecretLaCleSecrete"'
class user:

    def IsValid(mail,mdp,cursor) -> bool:
        # print("je me connecte")
        assert type(mail) == str, "l'e-mail est invalide"
        assert '@' and '.' in mail,"l'e-mail est invalide"    
        assert type(mdp) == str, "le mot de passe est invalide"
        assert len(mdp) <= 12, "le mot de passe déâsse la limite"
        #FAIRE LA REQUEST
        cursor.execute(f"select ID_User FROM users where email = '{mail}' and pass = '{mdp}'")
        response = cursor.fetchall()
        print(response) # Le reponse contient donc tous les utilisateurs
        return response != []

    def IsLogin(token,cursor) -> bool:
        cursor.execute(f"select ID_User FROM users where Token = '{token}'")
        response = cursor.fetchall()
        return response != []

    def GetToken(email,pas,cursor) -> str:
        cursor.execute(f"select ID_User FROM users where email = '{email}' and pass = '{pas}'")
        response = cursor.fetchall()
        if(user.IsValid(email,pas,cursor)):
            print(response[0])
            # encoded_jwt = JWT.encode({"username": email,"ID":response[0][0]}, "PasTresSecretLaCleSecrete", algorithm="HS256")
            accesstoken = user.encode_token({"username": email,"ID":response[0][0]})
            #need to add the access token to database
            cursor.execute(f"UPDATE users set Token = '{accesstoken}' WHERE email = '{email}'")
        return accesstoken

    def inscrire(nom,prenom,age,mail,mdp,conn):
        cursor = conn.cursor()
        cursor.execute(f"select * FROM users where email = '{mail}'")
        response = cursor.fetchall()
        #print(response) # La reponse contient donc tous les utilisateurs
        if response == []:
            pass
        else:
            return 'le compte existe déjà'     
        # print("je m'inscris")
        assert age >= 18,"vous n'avez pas l'age requis"
        # print(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
        cursor.execute(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
        conn.commit()
    
    def GetId(type,value,cursor):
        cursor.execute(f"select * FROM users where {type} = '{value}'")
        response = cursor.fetchall()
        return response

    # Secret key for encoding and decoding JWT tokens
    
    # def Session_Alive(token,cursor):
    #     cursor.execute(f"select ID_User FROM users where Token = '{token}'")
    #     response = cursor.fetchall()
    #     print(response) # Le reponse contient donc tous les utilisateurs
    #     return response != []


    def encode_token(payload) -> str:
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token  # Convert bytes to string

    def decode_token(token) -> str:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    
    def addmoney(userID,money:int,actif:str,conn):
        cursor = conn.cursor()
        cursor.execute(f"select * FROM users where email = '{mail}'")
        response = cursor.fetchall()
        #print(response) # La reponse contient donc tous les utilisateurs
        if response == []:
            pass
        else:
            return 'le compte existe déjà'     
        print("je m'inscris")
        assert age >= 18,"vous n'avez pas l'age requis"
        print(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
        cursor.execute(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
        conn.commit()