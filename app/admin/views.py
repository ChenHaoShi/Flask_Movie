from . import admin
from flask import render_template, url_for, redirect, flash, session, request
from app.admin.forms import LoginForm, TagForm
from app.models import Admin, Tag
from functools import wraps
from app import db

@admin.route("/")
def index():
    return render_template('admin/index.html')

# 管理员登录
@admin.route('/login/', methods=["GET", "POST"])
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
def logout():
    session.pop("admin", None)
    return redirect(url_for('admin.login'))

@admin.route('/pwd/')
def pwd():
    return render_template('admin/pwd.html')

@admin.route('/tag/add/', methods=["GET", "POST"])
def tag_add():
    form = TagForm()
    if form.validate_on_submit():
        data = form.data
        tag = Tag.query.filter_by(name=data["tag"]).count()
        if tag == 1:
            flash("标签已经存在!", "err")
            return redirect(url_for("admin.tag_add"))
        tag = Tag(
            name = data["tag"]
        )
        db.session.add(tag)
        db.session.commit()
        flash("标签添加成功!", "ok")
        return redirect(url_for("admin.tag_add"))
    return render_template('admin/tag_add.html', form=form)

@admin.route('/tag/list/<int:page>/', methods=["GET"])
def tag_list(page=None):
    if page is None:
        page = 1
    page_data = Tag.query.order_by(
        Tag.addtime.desc()
    ).paginate(page=page, per_page=1)
    return render_template('admin/tag_list.html', page_data=page_data)

@admin.route('/movie/add/')
def movie_add():
    return render_template('admin/movie_add.html')

@admin.route('/movie/list/')
def movie_list():
    return render_template('admin/movie_list.html')

@admin.route('/preview/add/')
def preview_add():
    return render_template('admin/preview_add.html')

@admin.route('/preview/list/')
def preview_list():
    return render_template('admin/preview_list.html')

@admin.route('/user/list/')
def user_list():
    return render_template('admin/user_list.html')

@admin.route('/user/view/')
def user_view():
    return render_template('admin/user_view.html')

@admin.route('/comment/list/')
def comment_list():
    return render_template('admin/comment_list.html')

@admin.route('/moviecol/list/')
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