from flask import  render_template, Blueprint, flash, g, request, redirect, url_for
from werkzeug.exceptions import abort
from app.models.user import User
from app.models.mark import Mark
from app import db
from app.views.auth import login_required

web = Blueprint('web', __name__, url_prefix='/')

def get_user(id):
    user = User.query.get(id)
    if user is None:
        abort(404, f"El usuario con el id {id} no existe")
    return user

@web.route('/')
@login_required
def index():
    marks = Mark.query.filter_by(alumno=g.user.username).order_by('asignatura').all()
    db.session.commit()
    if g.user.username != 'profesor':
        return render_template('index.html', marks=marks) 
    else:
        return redirect(url_for('web.add_mark'))

#añadir notas
@web.route('/mark', methods=['GET','POST'])
@login_required
def add_mark():
    marks = Mark.query.order_by('alumno').all()
    users = User.query.all()
    if request.method == 'POST':
        asignatura = request.form['asignatura']
        puntuacion = request.form['puntuacion']
        alumno = request.form['alumno']
        mark = Mark(asignatura, puntuacion, alumno)
        user=User.query.filter_by(username=alumno).first()
        user_mark= Mark.query.filter_by(asignatura=asignatura,alumno=alumno).first()
        if user!=None:
            if user_mark==None:
                db.session.add(mark)
                db.session.commit()
                flash('Nota añadida con exito',category='success')
                return redirect(url_for('web.add_mark'))
            else:
                flash('El alumno ya tiene una nota en esta asignatura',category='error')
        else:
            flash('El alumno no esta registrado',category='error')
        
    if g.user.username != 'profesor':
        flash('No tienes permiso para acceder a esta URL.',category='error')        
        return redirect(url_for('web.index'))
    else:
        return render_template('add_mark.html', marks=marks, users=users)

#eliminar notas
@web.route('/mark/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete_mark(id):
    mark = Mark.query.get_or_404(id)
    if g.user.username != 'profesor':
        flash('No tienes permiso para acceder a esta URL.',category='error')        
        return redirect(url_for('web.index'))
    else:
        db.session.delete(mark)
        db.session.commit()
        flash('Nota eliminada con exito',category='success')
        return redirect(url_for('web.add_mark'))

#editar notas
@web.route('/mark/<int:id>/edit', methods=['GET','POST'])
@login_required

def edit_mark(id):
    mark = Mark.query.get_or_404(id)
    if request.method == 'POST':
        puntuacion = request.form['puntuacion']
        mark.puntuacion = puntuacion
        db.session.commit()
        flash('Nota editada con exito',category='success')
        return redirect(url_for('web.add_mark'))
    if g.user.username != 'profesor':
        flash('No tienes permiso para acceder a esta URL.',category='error')        
        return redirect(url_for('web.index'))
    else:

        return render_template('edit_mark.html', mark=mark)

#eliminar usuario
@web.route('/delete/<int:id>', methods=['GET','POST'])
@login_required
def delete_user(id):
    user = User.query.get_or_404(id)
    if g.user.username != 'profesor':
        flash('No tienes permiso para acceder a esta URL.',category='error')        
        return redirect(url_for('web.index'))
    else:
        db.session.delete(user)
        db.session.commit()
        flash('Usuario eliminado con exito',category='success')
        return redirect(url_for('auth.register'))
