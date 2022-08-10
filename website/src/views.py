import json

from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from website.src.models import Note
from .. import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':

        # note = request.form.get('note')
        data = json.loads(request.data)
        note = data['note']
        if len(note) < 1:
            flash('Note is too short!', category='error')

        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Form sent succesfully!', category='success')

        return redirect(url_for('views.home'))

    return render_template('home.html', user=current_user)

@views.route("/delete-note", methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({"message":"Note has been deleted", "result":1})
        else:
            return jsonify({"message": "Wrong user", "result":0})
    else:
        return jsonify({"message": "Note not found", "result":0})
