from app.diary import diary_bp
from flask import render_template, request, redirect, url_for

from flask_login import (
    login_required,
    current_user
)

from app.models import Entry
from app.extensions import db


@diary_bp.route("/new", methods=["GET", "POST"])
@login_required
def new_entry():

    if request.method == "GET":
        return render_template(
            "diary/new_entry.html"
        )

    title = request.form.get("title")
    content = request.form.get("content")

    entry = Entry(
        title=title,
        content=content,
        user_id=current_user.id
    )

    db.session.add(entry)
    db.session.commit()

    return redirect(
        url_for("diary.dashboard")
    )


@diary_bp.route("/history")
@login_required
def history():

    entries = Entry.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "diary/history.html",
        entries=entries
    )