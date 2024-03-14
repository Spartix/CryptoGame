from flask import Flask, render_template, request
import sqlite3
conn = sqlite3.connect('DB_CryptoGame.db')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    name = request.form['nom']
    prenom = resquest.form['prenom']
    email = request.form['email']
    mdp = request.form['password']
    confirm_mdp = request.form[confirm password]
    return render_template("register.html")

@app.route("/async-register")
def register_page():
    
    return render_template("register.html")

@app.route("/async-login",methods=['POST'])
def connexion():
    username = request.form['username']
    password = request.form['password']



    return f'Username: {username}, Password: {password}'

# @app.route("/exemple")
# def exemple():
#     # Get_Inuput_User = request.form["utilisateur"]
#     reponsse_sql = cursor.execute("SELECT * from Users")
#     conn.commit()
#     print(reponsse_sql)
#     return str(reponsse_sql)


if __name__ == '__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')