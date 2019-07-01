from flask import Blueprint, request, session, redirect, url_for

home = Blueprint("home", __name__)

@home.before_request
def auth_control():
    if request.path == "/1/":
        return None
    if request.path == "/animation/":
        return None
    if request.path == "/register/":
        return None
    if request.path == "/login/":
        return None
    if session.get("user"):
        return None
    return redirect(url_for("home.login"))

import app.home.views