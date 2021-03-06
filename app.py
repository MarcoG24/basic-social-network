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
        url = f'http://127.0.0.1:4000/get-user?email={username}&password={password}'
        res = requests.get(url)
        response = json.loads(res.text)
        msg=''
        if response:
            session['loggedin'] = True
            session['data'] = response[0]
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
        return render_template('update-user.html', user='')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/delete-user', methods=['GET', 'POST'])
def delete_user():
    if session['loggedin']:
        return render_template('delete-user.html', user='')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    if session['loggedin']:
        return render_template('new-post.html')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/update-post', methods=['GET', 'POST'])
def update_post():
    if session['loggedin']:
        return render_template('update-post.html', post='')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/delete-post', methods=['GET', 'POST'])
def delete_post():
    if session['loggedin']:
        return render_template('delete-post.html', post='')
    else:
        return render_template('login.html', msg='🛑 No olvides iniciar sesión ⛔')

@app.route('/register-user', methods=['GET', 'POST'])
def register_user():
    if (request.method == 'POST'):
        response = _pscale_connect_users(request.form, 'register-user')
        if int(response) > 0:
            return render_template('new-user.html', msg='✅ El usuario se registró con éxito!. ✅')
        return render_template('new-user.html', msg='⛔ Hubo un error, intente de nuevo. ⛔')

@app.route('/find-user', methods=['GET', 'POST'])
def find_user():
    if (request.method == 'POST'
        and 'email' in request.form
        ):
        email = request.form['email']
        url = f'http://127.0.0.1:4000/find-user?email={email}'
        res = requests.get(url)
        response = json.loads(res.text)
        data_user = response
        if response:
            data_user = response[0]
            data_user['email'] = email
            data_user['msg'] = '✅  Usuario encontrado con éxito ✅ '
            data_user['msg_find'] = ''
            return render_template('update-user.html', user=data_user)
        else:
            data_user = {
                'name': '',
                'type_user':'',
                'password':'',
                'msg': '',
                'msg_find': '⛔  Usuario no encontrado ⛔ '
            }
            return render_template('update-user.html', user=data_user)

@app.route('/find-post', methods=['GET', 'POST'])
def find_post():
    if (request.method == 'POST'
        and 'id' in request.form
        ):
        id_post = request.form['id']
        url = f'http://127.0.0.1:4000/find-post?id={id_post}'
        res = requests.get(url)
        response = json.loads(res.text)
        data_post = response
        if response:
            data_post = response[0]
            data_post['msg'] = ''
            data_post['msg_find'] = '✅  Publicacion encontrada con éxito ✅ '
            return render_template('update-post.html', post=data_post)
        else:
            data_post = {
                'title_post': '',
                'subtitle':'',
                'note':'',
                'user': '',
                'msg': '',
                'msg_find': '⛔  Usuario no encontrado ⛔ '
            }
            return render_template('update-post.html', post=data_post)

@app.route('/update-data-user', methods=['GET', 'POST'])
def update_data_user():
    if (request.method == 'POST'):
        data = request.form
        response = _pscale_connect_users(data, 'update-data-user')
        data_user = {
                'name': data['name'],
                'type_user': data['type_user'],
                'password': data['password'],
                'email': data['email'],
                'msg': '⛔ Hubo un error, intente de nuevo. ⛔',
                'msg_find': ''
        }
        if int(response) > 0:
            data_user['msg'] = '✅ El usuario se actualizó con éxito!. ✅'
        return render_template('update-user.html', user=data_user)

@app.route('/delete-data-user', methods=['GET', 'POST'])
def delete_data_user():
    if (request.method == 'POST'):
        data = request.form
        response = _pscale_connect_users(data, 'delete-data-user')
        data_user = {
                'email': data['email'],
                'msg': '⛔ Hubo un error, intente de nuevo. ⛔'
        }
        if int(response) > 0:
            data_user['msg'] = '✅ El usuario se borró con éxito!. ✅'
        return render_template('delete-user.html', user=data_user)

@app.route('/get-post', methods=['GET', 'POST'])
def get_post():
    url = f'http://127.0.0.1:4000/get-posts'
    res = requests.get(url)
    response = json.loads(res.text)
    if response:
        return {"data": response}
    return {"data": ""}

@app.route('/create-post', methods=['GET', 'POST'])
def create_post():
    if (request.method == 'POST'):
        data_to_send = request.form.to_dict()
        data_to_send['user'] = session['data']['name']
        response = _pscale_connect_post(data_to_send, 'create-post')
        if int(response) > 0:
            return render_template('new-post.html', msg='✅ Publicado con éxito!. ✅')
        return render_template('new-post.html', msg='⛔ Hubo un error, intente de nuevo. ⛔')
        

@app.route('/update-data-post', methods=['GET', 'POST'])
def update_data_post():
    if (request.method == 'POST'):
        data = request.form
        response = _pscale_connect_post(data, 'update-data-post')
        data_post = {
                'title_post': data['title_post'],
                'subtitle': data['subtitle'],
                'note': data['note'],
                'user': session['data']['name'],
                'msg': '⛔ Hubo un error, intente de nuevo. ⛔',
                'msg_find': ''
        }
        if int(response) > 0:
            data_post['msg'] = '✅ La publicación se actualizó con éxito!. ✅'
        return render_template('update-post.html', post=data_post)

@app.route('/delete-data-post', methods=['GET', 'POST'])
def delete_data_post():
    if (request.method == 'POST'):
        data = request.form
        response = _pscale_connect_post(data, 'delete-data-post')
        data_post = {
                'id': data['id'],
                'msg_delete': '⛔ Hubo un error, intente de nuevo. ⛔'
        }
        if int(response) > 0:
            data_post['msg_delete'] = '✅ El post se elimino con éxito!. ✅'
        return render_template('delete-post.html', post=data_post)

@app.route('/update-hits', methods=['GET', 'POST'])
def update_hits():
    if (request.method == 'POST'):
        data = request.form
        response = _pscale_connect_post(data, 'update-data-post')
        data_post = {
                'id': data['id'],
                'hits': data['hits'],
                'msg': '⛔ Hubo un error, intente de nuevo. ⛔',
                'msg_find': ''
        }
        if int(response) > 0:
            data_post['msg'] = '✅ El usuario se actualizó con éxito!. ✅'
        return render_template('index.html', user=session['data'])

def _pscale_connect_users(data, api_name):
    if ('name' in data
        and 'email' in data
        and 'type_user' in data
        and 'password' in data
        or api_name == 'delete-data-user'
    ):
        # Create variables for easy access
        data_to_send = '?'
        for element in data:
            data_to_send = f'{data_to_send}{element}={data[element]}&'
        url = f'http://127.0.0.1:4000/{api_name}{data_to_send[:-1]}'
        res = requests.get(url)
        response = json.loads(res.text)
        return response

def _pscale_connect_post(data, api_name):
    if ('title_post' in data
        and 'subtitle' in data
        and 'note' in data
        or api_name == 'delete-data-post'
        or 'id' in data
    ):
        # Create variables for easy access
        data_to_send = '?'
        for element in data:
            data_to_send = f'{data_to_send}{element}={data[element]}&'
        url = f'http://127.0.0.1:4000/{api_name}{data_to_send[:-1]}'
        res = requests.get(url)
        response = json.loads(res.text)
        return response

