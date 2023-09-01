from app import db

class Afiliado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    # Adicione mais campos conforme necessário
