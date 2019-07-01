from flask import Blueprint, session, request, redirect, url_for, abort
from app.models import Admin, Auth, Role

admin = Blueprint("admin", __name__)

@admin.before_request
def auth_control():
    if request.path == "/admin/login/":
        return None
    if session.get("admin"):
        admin = Admin.query.join(
            Role
        ).filter(
            Role.id == Admin.role_id,
            Admin.id == session["admin_id"]
        ).first()
        auths = admin.role.auths
        auths = list(map(lambda v: int(v), auths.split(",")))
        auth_list = Auth.query.all()
        urls = [v.url for v in auth_list for val in auths if val == v.id]
        rule = request.url_rule
        if str(rule) not in urls:
            abort(404)
        return None
    return redirect(url_for("admin.login"))

import app.admin.views