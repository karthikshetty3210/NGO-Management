from flask import Blueprint, render_template, redirect, url_for

user_module = Blueprint('user_module', __name__, template_folder='templates/user')


@user_module.route('/')
@user_module.route('/home')
def home():
    return redirect(url_for('user_module.login'))


@user_module.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


@user_module.route('/register', methods=['GET','POST'])
def register():
    return render_template('register.html')
