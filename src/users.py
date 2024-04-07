import json
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

    def GetToken(email,pas,conn) -> str:
        cursor = conn.cursor()
        cursor.execute(f"select ID_User FROM users where email = '{email}' and pass = '{pas}'")
        response = cursor.fetchall()
        if(user.IsValid(email,pas,cursor)):
            print(response[0])
            # encoded_jwt = JWT.encode({"username": email,"ID":response[0][0]}, "PasTresSecretLaCleSecrete", algorithm="HS256")
            accesstoken = user.encode_token({"username": email,"ID":response[0][0]})
            #need to add the access token to database
            cursor.execute(f"UPDATE users set Token = '{accesstoken}' WHERE email = '{email}'")
            conn.commit()
        return accesstoken

    def inscrire(nom,prenom,age,mail,mdp,username,conn):
        cursor = conn.cursor()
        cursor.execute(f"select * FROM users where email = '{mail}'")
        response = cursor.fetchall()
        #print(response) # La reponse contient donc tous les utilisateurs
        if response == []:
            assert age >= 18,"vous n'avez pas l'age requis"
            # print(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
            cursor.execute(f"INSERT into Users(Nom,Prenom,Age,email,pass,Username) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}','{username}')")
            conn.commit()
        else:
            return 'le compte existe déjà'     


    
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
    
    def GetBalance(conn:sqlite3.Connection,token):
        cursor = conn.cursor()
        cursor.execute(f"SELECT Argent.* from Argent JOIN Users on Users.ID_User = Argent.ID_User WHERE Users.Token = '{token}'")
        response = cursor.fetchall()
        if response:
            columns = [col[0] for col in cursor.description]
            balance_dict = dict(zip(columns, response[0]))
            return json.dumps(balance_dict)
        else:
            return json.dumps({})
        
    def Infos(conn:sqlite3.Connection,token):
        cursor = conn.cursor()
        cursor.execute(f"SELECT Argent.* from Argent JOIN Users on Users.ID_User = Argent.ID_User WHERE Users.Token = '{token}'")
        response = cursor.fetchall()
        if response:
            columns = [col[0] for col in cursor.description]
            balance_dict = dict(zip(columns, response[0]))
            return json.dumps(balance_dict)
        else:
            return json.dumps({})
        
    def Me(conn:sqlite3.Connection,token):
        cursor = conn.cursor()
        cursor.execute(f"SELECT * from Users WHERE Token = '{token}'")
        response = cursor.fetchall()
        if response:
            columns = [col[0] for col in cursor.description]
            balance_dict = dict(zip(columns, response[0]))
            return json.dumps(balance_dict)
        else:
            return json.dumps({})

    # def addmoney(userID,money:int,actif:str,conn):
    #     cursor = conn.cursor()
    #     cursor.execute(f"select * FROM users where email = '{mail}'")
    #     response = cursor.fetchall()
    #     #print(response) # La reponse contient donc tous les utilisateurs
    #     if response == []:
    #         pass
    #     else:
    #         return 'le compte existe déjà'     
    #     print("je m'inscris")
    #     assert age >= 18,"vous n'avez pas l'age requis"
    #     print(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
    #     cursor.execute(f"INSERT into Users(Nom,Prenom,Age,email,pass) VALUES('{nom}','{prenom}',{int(age)},'{mail}','{mdp}')")
    #     conn.commit()