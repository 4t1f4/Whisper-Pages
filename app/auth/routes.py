from app.auth import auth_bp
from flask import request, render_template, redirect, url_for



@auth_bp.route("/test")
def test():
  return "Auth Blueprint Working"

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template("auth/signup.html")
  
  username = request.form.get("username")
  email = request.form.get("email")
  password = request.form.get("password")
  confirm_password = request.form.get("confirm_password")

  print(username)
  print(email)
  print(password)
  print(confirm_password)

  return "Form Submitted Successfully"