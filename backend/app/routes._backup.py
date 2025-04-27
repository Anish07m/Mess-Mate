from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import db, User, Feedback, Complaint
from flask_bcrypt import Bcrypt
from . import app

bcrypt = Bcrypt()

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

# Home page
@main.route('/')
def index():
    return render_template('index.html')

# Feedback Page
@main.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        feedback_entry = Feedback(name=name, message=message)
        db.session.add(feedback_entry)
        db.session.commit()
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('main.feedback'))
    return render_template('feedback.html')

# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html')

# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('main.index'))
        flash("Login failed. Check username and/or password.", "danger")
    return render_template('login.html')

# Logout
@auth.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('main.index'))
