from flask import (Flask, request) # IMPORTA O FLASK

app = Flask (__name__) #CRIA UMA INSTÂNCIA

@app.route("/", methods=('GET',)) #ASSINA UMA ROTA
 
def index(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    nome = request.args.get ('nome')
    # HTML RETORNADO
    return f"""<h1>Página Inicial</h1>
        <p>Olá {nome}, que nome 🔑"""


@app.route("/galeria", methods=('GET',)) #ASSINA UMA ROTA
def galeria(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Secundária</h1> <p>GALERIA</p>"


@app.route("/contato", methods=('GET',)) #ASSINA UMA ROTA
def contato(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Terceiária</h1> <p>CONTATO</p>"

@app.route("/sobre", methods=('GET',)) #ASSINA UMA ROTA
def sobre(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Quaternária</h1> <p>SOBRE</p>"


@app.route("/teste", methods=('GET',)) #ASSINA UMA ROTA
def teste():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    p3 = request.args.get('p3')
    return f"""<h1>Rodolfinho do grau</h1>
        <ul><li>{p1}</ul></li><ul><li>{p2}</ul></li><ul><li>{p3}</ul></li>
    """

@app.route("/area", methods=('GET',)) #ASSINA UMA ROTA
def area():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    p1 = float (request.args.get('a'))
    p2 = float (request.args.get('l'))
    return f"""<h1>A área informada: {p1*p2}</h1>
    <ul><li><p>Altura: {p1}</p></ul></li><ul><li><p>Largura: {p2}</p></ul></li>
    """

@app.route("/nmr", methods=('GET',)) #ASSINA UMA ROTA
def nmr():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    p1 = int (request.args.get('n'))
    
    if p1 is None:
        return "<p>Digite um número válido</p>"
    
    if p1 % 2 == 0:
        return "<p>O número é par</p>"

    else:
        return "<p>O número é ímpar</p>"

@app.route("/nsb", methods=('GET',)) #ASSINA UMA ROTA
def nsb():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    p1 = request.args.get('n')
    p2 = request.args.get('sb')

    return f"""<p>{p2}, {p1}</p>"""