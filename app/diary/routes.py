from app.diary import diary_bp



@diary_bp.route("/test")
def test():
  return "Diary Blueprint Working"