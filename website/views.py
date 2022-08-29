from flask import Blueprint, render_template,request

views = Blueprint('views', __name__)

@views.route('/')
def hello():
    return render_template("base.html")

@views.route('/about')
def about():
    return render_template ('about.html')

@views.route('/homepage')
def home():
    return render_template ('homepage.html')

@views.route('/prediction')
def diagnose():
    return render_template ('prediction.html')

@views.route('/history')
def history():
    return render_template ('history.html')

@views.route('/result')
def result():
    return render_template ('result.html')
