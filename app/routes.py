from flask import render_template
from app import app, db
from app.models import Afiliado

@app.route('/')
def index():
    return "Bem-vindo ao Painel de Afiliados!"

@app.route('/afiliados')
def listar_afiliados():
    afiliados = Afiliado.query.all()
    return render_template('list_afiliados.html', afiliados=afiliados)

@app.route('/afiliado/<int:afiliado_id>')
def detalhes_afiliado(afiliado_id):
    afiliado = Afiliado.query.get_or_404(afiliado_id)
    return render_template('detalhes_afiliado.html', afiliado=afiliado)
