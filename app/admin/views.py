from . import admin
from flask import render_template, url_for, redirect, flash, session, request
from app.admin.forms import LoginForm
from app.models import Admin
from functools import wraps

def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@admin.route("/")
@admin_login_req
def index():
    return render_template('admin/index.html')

# 管理员登录
@admin.route('/login/', methods=["GET", "POST"])
@admin_login_req
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data["account"]).first()
        if not admin.check_pwd(data["pwd"]):
            flash("密码错误")
            return redirect(url_for("admin.login"))
        session["admin"] = data["account"]
        return redirect(request.args.get("next") or url_for("admin.index"))
    return render_template('admin/login.html', form=form)

@admin.route('/logout/')
@admin_login_req
def logout():
    session.pop("admin", None)
    return redirect(url_for('amdin.login'))

@admin.route('/pwd/')
@admin_login_req
def pwd():
    return render_template('admin/pwd.html')

@admin.route('/tag/add/')
@admin_login_req
def tag_add():
    return render_template('admin/tag_add.html')

@admin.route('/tag/list/')
@admin_login_req
def tag_list():
    return render_template('admin/tag_list.html')

@admin.route('/movie/add/')
@admin_login_req
def movie_add():
    return render_template('admin/movie_add.html')

@admin.route('/movie/list/')
@admin_login_req
def movie_list():
    return render_template('admin/movie_list.html')

@admin.route('/preview/add/')
@admin_login_req
def preview_add():
    return render_template('admin/preview_add.html')

@admin.route('/preview/list/')
@admin_login_req
def preview_list():
    return render_template('admin/preview_list.html')

@admin.route('/user/list/')
@admin_login_req
def user_list():
    return render_template('admin/user_list.html')

@admin.route('/user/view/')
@admin_login_req
def user_view():
    return render_template('admin/user_view.html')

@admin.route('/comment/list/')
@admin_login_req
def comment_list():
    return render_template('admin/comment_list.html')

@admin.route('/moviecol/list/')
@admin_login_req
def moviecol_list():
    return render_template('admin/moviecol_list.html')

@admin.route('/oplog/list/')
def oplog_list():
    return render_template('admin/oplog_list.html')

@admin.route('/adminloginlog/list/')
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')

@admin.route('/userloginlog/list/')
def userloginlog_list():
    return render_template('admin/userloginlog_list.html')

@admin.route('/role/add/')
def role_add():
    return render_template('admin/role_add.html')

@admin.route('/role/list/')
def role_list():
    return render_template('admin/role_list.html')

@admin.route('/auth/add/')
def auth_add():
    return render_template('admin/auth_add.html')

@admin.route('/auth/list/')
def auth_list():
    return render_template('admin/auth_list.html')

@admin.route('/admin/add/')
def admin_add():
    return render_template('admin/admin_add.html')

@admin.route('/admin/list/')
def admin_list():
    return render_template('admin/admin_list.html')