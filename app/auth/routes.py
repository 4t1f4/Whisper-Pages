from app.auth import auth_bp



@auth_bp.route("/test")
def test():
  return "Auth Blueprint Working"