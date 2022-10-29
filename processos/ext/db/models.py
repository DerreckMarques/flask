
#from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Student {self.firstname}>'