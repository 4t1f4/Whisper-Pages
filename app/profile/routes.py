from app.profile import profile_bp



@profile_bp.route("/test")
def test():
  return "Profile Blueprint Working"