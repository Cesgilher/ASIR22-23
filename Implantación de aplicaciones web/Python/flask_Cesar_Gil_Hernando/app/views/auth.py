
from flask import  render_template, Blueprint, flash, g, request, redirect, session, url_for
from app.models.user import User
from app import db
from os import error
import functools
auth = Blueprint('auth', __name__, url_prefix='/')



#redirecciona al login si no ha iniciado sesion
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
#Registrar usuario
@auth.route('/register', methods=['GET','POST'])
@login_required
def register():
    users = User.query.all()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username, email, password)
    
        user_name= User.query.filter_by(username=username).first()
        if user_name==None:
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado correctamente')
            return redirect(url_for('auth.register'))
        else:
            error = f'El usuario {username} ya existe'
            flash(error)
    if g.user.username != 'profesor':
        flash('No tienes permiso para acceder a esta URL.',category='error')        
        return redirect(url_for('web.index'))
    else:
        return render_template('register.html', users=users)
        

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user= User.query.filter_by(username=username,password=password).first()

        if user==None:
            error = 'Credenciales incorrectas'
            flash(error)
        if error is None:
            session.clear()
            session['user_id'] = user.id
            
            if user.username=='profesor':
                return redirect(url_for('web.add_mark'))
            else:
                return redirect(url_for('web.index'))
    if g.user:
        return redirect(url_for('web.index'))
    else:
        return render_template('login.html')
#verifica si el usuario ha iniciado sesion
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

#cierra la sesion actual
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

