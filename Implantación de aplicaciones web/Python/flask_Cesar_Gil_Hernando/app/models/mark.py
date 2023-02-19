from app import db


class Mark(db.Model):
    __tablename__ = 'notas'
    id = db.Column(db.Integer, primary_key=True)
    asignatura = db.Column(db.String(45))
    puntuacion = db.Column(db.Integer)
    alumno = db.Column(db.String(45), db.ForeignKey("usuarios.username",ondelete='CASCADE'))

    def __init__(self, asignatura, puntuacion, alumno):
        self.asignatura = asignatura
        self.puntuacion = puntuacion
        self.alumno = alumno
    
    def __repr__(self) -> str:
        return f'Nota: {self.puntuacion}'