from flask import Flask # IMPORTA O FLASK

app = Flask (__name__) #CRIA UMA INSTÂNCIA

@app.route("/", methods=('GET',)) #ASSINA UMA ROTA
 
def index(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Inicial</h1> <p>Eu sou fulano</p>"


@app.route("/galeria", methods=('GET',)) #ASSINA UMA ROTA
def galeria(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Secundária</h1> <p>GALERIA</p>"


@app.route("/contato", methods=('GET',)) #ASSINA UMA ROTA
def contato(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Terceiária</h1> <p>CONTATO</p>"

@app.route("/sobre", methods=('GET',)) #ASSINA UMA ROTA
def sobre(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return "<h1>Página Quaternária</h1> <p>SOBRE</p>"

