from flask import Flask, redirect, render_template, request,g,url_for,make_response
import sqlite3
from src.users import user
conn = sqlite3.connect('DB_CryptoGame.db')
cursor = conn.cursor()

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('DB_CryptoGame.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    print(request.headers.get('x-Access-Token'))
    return render_template('index.html')

@app.route("/login")
def login_page():
    return render_template("login.html")

# @app.route("/aysnc-register")
# def register_page():
#     name = request.form['nom']
#     prenom = resquest.form['prenom']
#     email = request.form['email']
#     mdp = request.form['password']
#     confirm_mdp = request.form[confirm password]
#     return render_template("register.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/async-login",methods=['POST'])
def connexion():
    with get_db() as conn:
        cursor = conn.cursor()
        if user.IsValid(request.form["username"],request.form["password"],cursor):
            token = user.GetToken(request.form["username"],request.form["password"],cursor)
            response = make_response(render_template('index.html'))
            response.set_cookie('access_token', token)
            return response
        else:
            return redirect("/login?error=true")

# @app.route("/exemple")
# def exemple():
#     # Get_Inuput_User = request.form["utilisateur"]
#     reponsse_sql = cursor.execute("SELECT * from Users")
#     conn.commit()
#     print(reponsse_sql)
#     return str(reponsse_sql)


if __name__ == '__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')