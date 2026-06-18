from app.profile import profile_bp


from flask import render_template

from flask_login import (
    login_required,
    current_user
)


@profile_bp.route("/test")
def test():
  return "Profile Blueprint Working"

@profile_bp.route("/")
@login_required
def profile():
    return render_template(
        "profile/profile.html"
    )