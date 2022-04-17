import json
import requests
from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for
)

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
            return redirect(url_for('home'))
            
        else:
            msg = 'Email/Contraseña incorrecta!\n😔'

    return render_template('login.html', msg=msg)

@app.route('/home')
def home():  
    if session['loggedin']:
        return render_template('index.html', user=session['data'])
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/data-user', methods=['GET', 'POST'])
def get_data_user():
    if session['loggedin']:
        return session['data']
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if session['loggedin']:
        return render_template('new-user.html', msg='')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/update-user', methods=['GET', 'POST'])
def update_user():
    if session['loggedin']:
        return render_template('update-user.html', user=session['data'])
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/register-user', methods=['GET', 'POST'])
def register_user():
    if (request.method == 'POST'
        and 'name' in request.form
        and 'email' in request.form
        and 'type_user' in request.form
        and 'password' in request.form
    ):
        # Create variables for easy access
        data_to_send = '?'
        for element in request.form:
            data_to_send = f'{data_to_send}{element}={request.form[element]}&'
        url = f'http://127.0.0.1:4000/register-user{data_to_send[:-1]}'
        res = requests.get(url)
        response = json.loads(res.text)
        if int(response) > 0:
            return render_template('new-user.html', msg='✅ El usuario se registró con éxito!. ✅')
        return render_template('new-user.html', msg='⛔ Hubo un error, intente de nuevo. ⛔')
