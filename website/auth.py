from sre_constants import SUCCESS
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Patient_data, User
from werkzeug.security import generate_password_hash, check_password_hash
from .import db
from flask_login import login_user, login_required, logout_user, current_user,login_manager
import pickle
import numpy as np
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect('/homepage')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email=request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(first_name) < 2:
            flash('first Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not the same', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user= User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')
            return redirect('/homepage')

            #return redirect(url_for('/prediction'))
    return render_template("sign_up.html")

model = pickle.load(open('website/ml_1model.pkl', 'rb'))

@auth.route('/result',methods=['POST'])
def getprediction():    

    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)

    if (prediction == 1):
        output = 'Breast Cancer is Malignant'
    else:
        output = 'Breast Cancer is Benign'

    return render_template('result.html', output=output)
    #return render_template('result.html', output='Predicted Outcome :{}'.format(prediction))