from flask import Flask, redirect, url_for
from user import user_module


app = Flask(__name__)
app.register_blueprint(user_module, url_prefix='/user')


@app.route('/')
def home():
    return redirect(url_for('user_module.login'))


if __name__ == '__main__':
    app.run(debug=True)
