from flask import Flask, redirect, render_template, request,g,url_for,make_response
import sqlite3
from src.users import user
conn = sqlite3.connect('DB_CryptoGame.db')


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
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return render_template("./login.html")
    else:
        return render_template('index.html')

@app.route("/login")
def login_page():
    if user.IsLogin(request.cookies.get('access_token'),get_db().cursor()):
        return render_template("./index.html")
    return render_template("login.html")

@app.route("/async-register",methods=["POST"])
def register():
    name = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    age = request.form["age"]
    mdp = request.form['password']
    confirm_mdp = request.form["confirm password"]
    print(name,prenom,email,age,mdp,confirm_mdp)
    if confirm_mdp != mdp:
        return render_template("register.html")
    try:
        token = user.inscrire(name,prenom,int(age),email,mdp,get_db())
        if("le compte existe déjà" in token):
            return redirect("/register?error=true&message=Le_Compte_Existe_Deja")
        token = user.GetToken(email,mdp,get_db().cursor())
        print(token)
        response = make_response(render_template('index.html'))
        response.set_cookie('access_token', token)
        return response
    except Exception as e:
        return redirect("/register?error=true&message=erreur_d_inscription")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/async-login",methods=['POST'])
def connexion():
    with get_db() as conn:
        cursor = conn.cursor()
        if user.IsValid(request.form["username"],request.form["password"],cursor):
            token = user.GetToken(request.form["username"],request.form["password"],get_db())
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