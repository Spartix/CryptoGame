from time import *
from flask import *
from src.route.main import *
from src.db import get_db
from src.users import user
from src.utility.crypto import get_crypto_data
from src.money import Argent
# conn = sqlite3.connect('DB_CryptoGame.db')


app = Flask(__name__)



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
    return enregistrement()

@app.route("/register")
def register_page():
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return render_template("register.html")
    else:
        return redirect('/profil')


@app.route("/async-login",methods=['POST'])
def log():
    return connexion()

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


@app.route('/data')
def get_data():
    timestamps, prices_btc, prices_ltc, prices_sol = get_crypto_data()
    return jsonify(timestamps=timestamps, prices_btc=prices_btc, prices_ltc=prices_ltc, prices_sol=prices_sol)

@app.route('/chart')
def GetChart():
    return render_template("chart.html")

@app.route('/roue')
def GetRoue():
    return render_template("roue2.html")

@app.route("/send")
def send():
    if not (user.IsLogin(request.cookies.get('access_token'),get_db().cursor())):
        return redirect("/login")
    else:
        return render_template('send.html')

@app.route("/async-search",methods=["POST"])
def Search():
    return {"exist":Argent.Existe(request.get_json()["pseudo"],get_db().cursor())}

@app.route("/async-send",methods=["POST"])
def Send():
    print()
    return Argent.Envoyer(request.cookies.get("access_token"),request.form["Pseudo"],request.form["actifs"],conn=get_db(),montant=request.form["Montant"])
# @app.route("/exemple")
# def exemple():
#     # Get_Inuput_User = request.form["utilisateur"]
#     reponsse_sql = cursor.execute("SELECT * from Users")
#     conn.commit()
#     print(reponsse_sql)
#     return str(reponsse_sql)
@app.route("/async-roue")
def Roue():
    return tourne()
if __name__ == '__main__':
    app.run(debug=True,port=3000,host='0.0.0.0')