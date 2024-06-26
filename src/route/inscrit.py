from flask import make_response, redirect, render_template, request
from src.db import get_db
from src.users import user
import urllib.parse

def enregistrement():
    name = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    age = request.form["age"]
    mdp = request.form['password']
    username = request.form["username"]
    confirm_mdp = request.form["confirm password"]
    print(name,prenom,email,age,mdp,confirm_mdp)
    if confirm_mdp != mdp:
        return redirect("register?error=true&message=Les%20mot%20de%20passe%20doivent%20etre%20identique")

    token = user.inscrire(name,prenom,int(age),email,mdp,username,get_db())
    if(type(token) == str):
        return redirect(f"/register?error=true&message={urllib.parse.quote(token)}")
    token = user.GetToken(email,mdp,get_db())
    print(token)
    response = make_response(render_template('profil.html'))
    response.set_cookie('access_token', token)
    return response

    return redirect("/register?error=true&message=erreur_d_inscription")