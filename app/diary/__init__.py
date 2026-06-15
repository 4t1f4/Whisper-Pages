from flask import Blueprint

diary_bp = Blueprint(
  "diary",
  __name__,
  url_prefix="/diary"
)


from app.diary import routes
