from app import app, Task
from app.forms import AddNewTask, LoginForm
from flask import render_template, url_for, flash, redirect
from flask_login import current_user, login_user, logout_user, login_required

from app.models import AdminUser


@app.route('/')
@app.route('/index')
@login_required
def index():
    form = AddNewTask()
    
    return render_template("index.html", form=form)


@app.route("/tasks1")
def tasks1():
    tasks = map(str, Task.query.filter(Task.module==1).all())
    return render_template("/pages/tasks1.html", tasks=tasks)

@app.route("/tasks2")
def tasks2():
    tasks = map(str, Task.query.filter(Task.module==2).all())
    return render_template("pages/tasks2.html", tasks=tasks)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    form = LoginForm()
    if form.validate_on_submit():
        au = AdminUser.query.filter_by(login=form.login.data).first()
        if au is None or au.password != form.password.data:
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(au, remember=False)
        return redirect(url_for("index"))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('tasks1'))