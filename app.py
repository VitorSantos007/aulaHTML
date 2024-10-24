from flask import (Flask, render_template, request) # IMPORTA O FLASK

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

@app.route("/area/<float:largura>/<float:comprimento>", methods=('GET',)) #ASSINA UMA ROTA
def area(largura, comprimento):# FUNÇÃO RESPONSÁVEL PELA PÁGINA
   
    return f"""<h1>A área informada: {largura*comprimento}</h1>
    <ul><li><p>Altura: {largura}</p></ul></li><ul><li><p>Largura: {comprimento}</p></ul></li>
    """

@app.route("/potencia/<float:p1>/<float:p2>", methods=('GET',)) #ASSINA UMA ROTA
def potencia(p1, p2):# FUNÇÃO RESPONSÁVEL PELA PÁGINA
   
    return f"""<h1>A POTÊNCIA informada: {p1**p2}</h1>
    <ul><li><p>VALOR 1: {p1}</p></ul></li><ul><li><p>VALOR 2: {p2}</p></ul></li>
    """


@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET",)) #ASSINA UMA ROTA
def tabuada(numero= None ):# FUNÇÃO RESPONSÁVEL PELA PÁGINA

    if 'numero' in request.args:
        numero = request.args.get('numero')
        numero = int(request.args.get('numero'))
    
    return render_template('tabuada.html', numero=numero)