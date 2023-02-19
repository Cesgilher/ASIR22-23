from app import db



class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45),unique=True, nullable=False)
    email = db.Column(db.String(45),unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)

    def __init__(self, username,email, password) -> None:
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self) -> str:
        return f'Usuario: {self.username}' 