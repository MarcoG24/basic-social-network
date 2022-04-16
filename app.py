from crypt import methods
import json
import requests
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = 'PruebaMarcoGomez'


@app.route('/', methods=['GET', 'POST'])
def login():
    session['loggedin'] = False
    msg = ''
    if (request.method == 'POST'
        and 'username' in request.form
        and 'password' in request.form
        ):
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        url = f'http://127.0.0.1:4000/get-data?email={username}'
        res = requests.get(url)
        response = json.loads(res.text)
        data_user = response[0]
        if response:
            session['loggedin'] = True
            session['email'] = data_user['email']
            session['pass'] = data_user['password']
            session['data'] = data_user
            # Redirect to home page
            return render_template('index.html', user=data_user)
            
        else:
            msg = 'Email/Contraseña incorrecta!\n😔'

    return render_template('login.html', msg=msg)

@app.route('/data-user', methods=['GET', 'POST'])
def get_data_user():
    if session['loggedin']:
        return session['data']
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if session['loggedin']:
        return render_template('new-user.html', msg='probando weee')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')
