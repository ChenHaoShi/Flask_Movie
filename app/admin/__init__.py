from flask import Blueprint, session, request, redirect, url_for

admin = Blueprint("admin", __name__)

@admin.before_request
def auth_control():
    if session.get("admin"):
        return None
    if request.path == "/admin/login/":
        return None
    return redirect(url_for("admin.login"))

import app.admin.views