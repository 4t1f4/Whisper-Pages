from app.auth import auth_bp

from flask import (
    request,
    render_template,
    redirect,
    url_for
)

from app.models import User
from app.extensions import db, bcrypt

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)


@auth_bp.route("/test")
def test():
    return "Auth Blueprint Working"


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "GET":
        return render_template("auth/signup.html")

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if password != confirm_password:
        return "Passwords do not match"

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return "Username already exists"

    existing_email = User.query.filter_by(email=email).first()

    if existing_email:
        return "Email already registered"

    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    user = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("auth/login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(
        username=username
    ).first()

    if user and bcrypt.check_password_hash(
        user.password_hash,
        password
    ):
        login_user(user)

        return "Successfully Logged In"

    return "Invalid Username or Password"


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))