from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('first-name')
        password = request.form.get('password')
        passwordConfirmation = request.form.get('password-confirmation')

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

        if hasErrors == False:
            flash('Account created!', category='success')
    return render_template("signup.html")
