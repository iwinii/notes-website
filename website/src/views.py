from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from website.src.models import Note
from .. import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':

        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')

        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Form sent succesfully!', category='success')

        return redirect(url_for('views.home'))

    return render_template('home.html', user=current_user)
