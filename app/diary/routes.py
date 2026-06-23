from app.diary import diary_bp
from flask import render_template, request, redirect, url_for
from app.utils import (
  encrypt_text,
  decrypt_text
)

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
    content = encrypt_text(
        request.form.get("content")
    )

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

    for entry in entries:
        entry.decrypted_content = decrypt_text(entry.content)

    return render_template(
        "diary/history.html",
        entries=entries
    )



@diary_bp.route("/<int:id>")
@login_required
def entry_detail(id):

    entry = Entry.query.get_or_404(id)

    if entry.user_id != current_user.id:
        return "Access Denied"
    
    entry.decrypted_content = decrypt_text(entry.content)

    return render_template(
        "diary/entry_detail.html",
        entry=entry
    )



@diary_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete_entry(id):

    entry = Entry.query.get_or_404(id)

    if entry.user_id != current_user.id:
        return "Access Denied"

    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for("diary.history"))


@diary_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "diary/dashboard.html"
    )


@diary_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit_entry(id):
    entry = Entry.query.get_or_404(id)

    if entry.user_id != current_user.id:
        return "Access Denied"

    if request.method == "POST":
        entry.title = request.form.get("title")
        entry.content = encrypt_text(
            request.form.get("content")
        )
        db.session.commit()
        return redirect(url_for("diary.entry_detail", id=entry.id))

    # Reuses your beautiful entry form layout style, just pre-filled!

    entry.content = decrypt_text(entry.content)
    return render_template("diary/new_entry.html", entry=entry)