from flask import make_response, redirect, request
from src.db import get_db
from src.users import user


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