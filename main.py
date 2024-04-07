from flask import Flask, redirect, render_template, request,g,url_for,make_response
import sqlite3
from src.route.main import *
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

@app.route('/disconnect')
def deco():
    response = make_response(redirect("/"))
    response.delete_cookie('access_token')
    return response

@app.route('/profil')
def index():
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return render_template("./login.html")
    else:
        return render_template('profil.html')

@app.route('/')
def acceuil():
    return home()

@app.route("/login")
def login_page():
    if user.IsLogin(request.cookies.get('access_token'),get_db().cursor()):
        return redirect("/profil")
    return render_template("login.html")

@app.route("/async-register",methods=["POST"])
def register():
    name = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    age = request.form["age"]
    mdp = request.form['password']
    username = request.form["username"]
    confirm_mdp = request.form["confirm password"]
    print(name,prenom,email,age,mdp,confirm_mdp)
    if confirm_mdp != mdp:
        return render_template("register.html")
    # try:
    token = user.inscrire(name,prenom,int(age),email,mdp,username,get_db())
    if(type(token) == str):
        if("le compte existe déjà" in token):
            return redirect("/register?error=true&message=Le_Compte_Existe_Deja")
    token = user.GetToken(email,mdp,get_db())
    print(token)
    response = make_response(render_template('profil.html'))
    response.set_cookie('access_token', token)
    return response
    # except Exception as e:
    return redirect("/register?error=true&message=erreur_d_inscription")

@app.route("/register")
def register_page():
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return render_template("register.html")
    else:
        return redirect('/profil')


@app.route("/async-login",methods=['POST'])
def connexion():
    with get_db() as conn:
        cursor = conn.cursor()
        if user.IsValid(request.form["username"],request.form["password"],cursor):
            token = user.GetToken(request.form["username"],request.form["password"],get_db())
            response = make_response(redirect('profil'))
            response.set_cookie('access_token', token)
            return response
        else:
            return redirect("/login?error=true")
@app.route("/Balance")
def GetBalance():
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return redirect("./login")
    return str(user.GetBalance(get_db(),request.cookies.get('access_token')))

@app.route("/@Me")
def GetMe():
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return redirect("./login")
    return str(user.Me(get_db(),request.cookies.get('access_token')))
# @app.route("/exemple")
# def exemple():
#     # Get_Inuput_User = request.form["utilisateur"]
#     reponsse_sql = cursor.execute("SELECT * from Users")
#     conn.commit()
#     print(reponsse_sql)
#     return str(reponsse_sql)


if __name__ == '__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')