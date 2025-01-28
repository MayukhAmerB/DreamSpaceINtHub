from flask import Blueprint, render_template

# Update Blueprint to include template_folder parameter
main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/admin')
def admin():
    return render_template('admin.html')


@main.route('/cheff')
def cheff():
    return render_template('cheff.html')

@main.route('/invoice')
def invoice():
    return render_template('invoice.html')

@main.route('/menu')
def menu():
    return render_template('menu.html')

@main.route('/terms')
def terms():
    return render_template('terms&cond.html')
