from app.auth import auth_bp

from flask import (
    request,
    render_template,
    redirect,
    url_for,
    flash
)

from app.models import User
from app.extensions import db, bcrypt

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

#only for test
@auth_bp.route("/test")
def test():
    return "Auth Blueprint Working"

#sign up page logic
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for("profile.profile"))


    if request.method == "GET":
        return render_template("auth/signup.html")

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if password != confirm_password:
        flash("Passwords do not match", "error")
        return redirect(url_for("auth.signup"))
    
    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        flash("Username already exists", "error")
        return redirect(url_for("auth.signup"))


    existing_email = User.query.filter_by(email=email).first()

    if existing_email:
        flash("Email already registered", "error")
        return redirect(url_for("auth.signup"))

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

    flash("Account created successfully. Please log in.", "success")
    return redirect(url_for("auth.login"))



#login page logic
@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("profile.profile"))


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

        return redirect(url_for("profile.profile"))

    flash("Invalid username or password", "error")
    return redirect(url_for("auth.login"))


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))