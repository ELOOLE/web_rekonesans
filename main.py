from flask import Flask, url_for, request, render_template, redirect, request, session
import os

app = Flask(__name__, static_folder='./static')
app.secret_key = "secretKEYranDoM2022"
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/")
def index():
    return render_template('index.html', page='index')
    #return "<p>index page</p>"


@app.route("/about")
def about():
    return render_template('about.html', page='about')


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # tutaj odpytanie bazy danych czy istnieje
        # na razie tak ubogo - prowizorka
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('panel'))
    return render_template('login.html', error=error)


@app.route('/panel')
def panel(name=None):
    if session.get("username"):
        return render_template('panel.html', name=session.get("username"))
    return "Please login"


@app.route('/logout') # define logout path
def logout(): #define the logout function
    session.clear()
    return redirect(url_for('index'))

def projekty():
    return os.walk('.')

@app.route('/create_projekt')
def create_projekt(dirname):
    os.makedirs(dirname)
    return 'Utworzony'

#with app.test_request_context():
#    print(url_for)
#    print(url_for('index'))
#    print(url_for('about'))
#    print(url_for('login'))
#    print(url_for('login', next='/'))
#    print(url_for('hello'))