# CETTE PARTI CE TROUVE TT EN HAUT DE MAIN.PY
import sqlite3
conn = sqlite3.connect('DB_CryptoGame.db')
cursor = conn.cursor()


#FAIRE LA REQUEST
cursor.execute("SELECT * from Users")
response = cursor.fetchall()
print(response) # Le reponse contient donc tous les utilisateurs
