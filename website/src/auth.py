from flask import Blueprint, render_template, request, flash, redirect, url_for

from website.src.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from flask_login import login_required, login_user, logout_user, current_user


auth = Blueprint('auth', __name__)
PASSWORD_SALT = 'asdfgh'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        passwordSalted = password + PASSWORD_SALT

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, passwordSalted):
                flash('Logged in succesfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Email or password incorrect.', category='error')
        else:
            flash('Email or password incorrect.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User has been logout successfully', category='success')
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('first-name')
        password = request.form.get('password')
        passwordConfirmation = request.form.get('password-confirmation')

        user = User.query.filter_by(email=email).first()

        hasErrors = False
        if len(email) < 4:
            hasErrors = True
            flash('Email must be greater than 3 characters.', category='error')
        if len(firstName) < 2:
            hasErrors = True
            flash('First name must be greater than 1 character.', category='error')
        if password != passwordConfirmation:
            hasErrors = True
            flash('Passwords do not match.', category='error')
        if len(password) < 7:
            hasErrors = True
            flash('Password must be greater than 6 characters.', category='error')
        if user:
            hasErrors = True
            flash('Email already taken.', category='error')

        if hasErrors == False:
            passwordSalted = password + PASSWORD_SALT
            new_user = User(email=email, first_name=firstName,
                            password=generate_password_hash(passwordSalted, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created for email:' + email + '!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)
