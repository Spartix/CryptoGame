import json
import sqlite3
import jwt

SECRET_KEY = '"PasTresSecretLaCleSecrete"'
class user:

    def IsValid(mail,mdp,cursor:sqlite3.Cursor) -> bool:
        try:
            cursor.execute("SELECT ID_User FROM users WHERE email = ? AND pass = ?", (mail, mdp))
            response = cursor.fetchone()
            print(response)
            return bool(response)
        except Exception as e:
            print(f"Erreur lors de la validation des informations d'identification : {e}")
            return False

    def IsLogin(token,cursor) -> bool:
        try:
            cursor.execute("SELECT ID_User FROM users WHERE Token = ?", (token,))
            response = cursor.fetchone()
            return bool(response)
        except Exception as e:
            print(f"Erreur lors de la vérification de la connexion: {e}")
            return False

    def GetToken(email,pas,conn) -> str:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT ID_User FROM users WHERE email = ? AND pass = ?", (email, pas))
            response = cursor.fetchone()
            if response:
                user_id = response[0]
                accesstoken = user.encode_token({"username": email, "ID": user_id})
                cursor.execute("UPDATE users SET Token = ? WHERE email = ?", (accesstoken, email))
                conn.commit()
                return accesstoken
            else:
                return 'Informations d\'identification invalides'
        except Exception as e:
            # Gérer l'exception, par exemple, journaliser l'erreur ou renvoyer un message d'erreur approprié
            print(f"Erreur lors de la récupération du jeton: {e}")
            return 'Une erreur est survenue lors de la récupération du jeton'
        finally:
            cursor.close()


    def inscrire(nom,prenom,age,mail,mdp,username,conn):
        cursor = conn.cursor()
        if age < 18:
            return "Vous n'avez pas l'age requis"
        try:
            cursor.execute("SELECT * FROM users WHERE email = ?", (mail,))
            response = cursor.fetchall()
            cursor.execute("SELECT * FROM users WHERE Username = ?", (username,))
            rez2 = cursor.fetchall()
            if "@" not in mail:
                return 'invalid email type'
            if not response and not rez2:
                cursor.execute("INSERT INTO Users(Nom, Prenom, Age, email, pass, Username) VALUES (?, ?, ?, ?, ?, ?)",
                            (nom, prenom, int(age), mail, mdp, username))
                conn.commit()
            else:
                return 'Le compte existe déjà'
        finally:
            cursor.close()   


    
    def GetId(type,value,cursor):
        cursor.execute(f"SELECT * FROM users WHERE {type} = ?", (value,))
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
        cursor.execute("SELECT Argent.* FROM Argent JOIN Users ON Users.ID_User = Argent.ID_User WHERE Users.Token = ?", (token,))
        response = cursor.fetchone()
        if response:
            columns = [col[0] for col in cursor.description]
            balance_dict = dict(zip(columns, response))
            return json.dumps(balance_dict)
        else:
            return json.dumps({})
        
    # def Infos(conn:sqlite3.Connection,token):
    #     with conn.cursor() as cursor:
    #         cursor.execute("SELECT Argent.* FROM Argent JOIN Users ON Users.ID_User = Argent.ID_User WHERE Users.Token = ?", (token,))
    #         response = cursor.fetchone()
    #         if response:
    #             columns = [col[0] for col in cursor.description]
    #             balance_dict = dict(zip(columns, response))
    #             return json.dumps(balance_dict)
    #         else:
    #             return json.dumps({})
        
    def Me(conn:sqlite3.Connection,token):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE Token = ?", (token,))
        response = cursor.fetchone()
        if response:
            columns = [col[0] for col in cursor.description]
            balance_dict = dict(zip(columns, response))
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