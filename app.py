from flask import (Flask, render_template, request) # IMPORTA O FLASK

app = Flask (__name__) #CRIA UMA INSTÂNCIA

@app.route("/", methods=('GET',)) #ASSINA UMA ROTA
 
def index(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    nome = request.args.get ('nome')
    # HTML RETORNADO
    
    return f"""<h1>Página Inicial</h1>
        <p>Olá {nome}, que nome 🔑
        <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """


@app.route("/galeria", methods=('GET',)) #ASSINA UMA ROTA
def galeria(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return """<h1>Página Secundária</h1> <p>GALERIA</p>
    <ul><h3>MENU</h3>
            <li><a href="/">INDEX</a></li>
            <li><a href="/galeria">GALERIA</a></li>
            <li><a href="/contato">CONTATO</a></li>
            <li><a href="/sobre">SOBRE</a></li>
            <li><a href="/tabuada">TABUADA</a></li>
            <li><a href="/nsb">NOME E SOBRENOME</a></li>
            <li><a href="/nmr">IMPAR E PAR</a></li>
            <li><a href="/area/10.0/5.0">AREA</a></li>
            <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
            <li><a href="/teste">TESTE</a></li>
            <li><a href="/juros">JUROS</a></li>
            <li><a href="/login">LOGIN</a></li>
            <li><a href="/imc">IMC</a></li>
    </ul>
"""


@app.route("/contato", methods=('GET',)) #ASSINA UMA ROTA
def contato(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return """<h1>Página Terceiária</h1> <p>CONTATO</p>
    <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """

@app.route("/sobre", methods=('GET',)) #ASSINA UMA ROTA
def sobre(): # FUNÇÃO RESPONSÁVEL PELA PÁGINA
    return """<h1>Página Quaternária</h1> <p>SOBRE</p>
    <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>        
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """


@app.route("/teste", methods=('GET',)) #ASSINA UMA ROTA
def teste():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    p1 = request.args.get('p1')
    p2 = request.args.get('p2')
    p3 = request.args.get('p3')
    return f"""<h1>PASTEL</h1>
        <ul><li>{p1}</ul></li><ul><li>{p2}</ul></li><ul><li>{p3}</ul></li>

        <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """

@app.route("/nmr", methods=('GET',)) #ASSINA UMA ROTA
def nmr():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    nmr = request.args.get('n', type= int)
    
    if nmr is None:
        return """<p>Digite um número válido</p>
        <ul><h3>MENU</h3>
            <li><a href="/">INDEX</a></li>
            <li><a href="/galeria">GALERIA</a></li>
            <li><a href="/contato">CONTATO</a></li>
            <li><a href="/sobre">SOBRE</a></li>
            <li><a href="/tabuada">TABUADA</a></li>
            <li><a href="/nsb">NOME E SOBRENOME</a></li>
            <li><a href="/nmr">IMPAR E PAR</a></li>
            <li><a href="/area/10.0/5.0">AREA</a></li>
            <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
            <li><a href="/teste">TESTE</a></li>
            <li><a href="/juros">JUROS</a></li>
            <li><a href="/login">LOGIN</a></li>
            <li><a href="/imc">IMC</a></li>
        </ul>
        """
    
    if nmr % 2 == 0:
        return """<p>O número é par</p>
        <ul><h3>MENU</h3>
            <li><a href="/">INDEX</a></li>
            <li><a href="/galeria">GALERIA</a></li>
            <li><a href="/contato">CONTATO</a></li>
            <li><a href="/sobre">SOBRE</a></li>
            <li><a href="/tabuada">TABUADA</a></li>
            <li><a href="/nsb">NOME E SOBRENOME</a></li>
            <li><a href="/nmr">IMPAR E PAR</a></li>
            <li><a href="/area/10.0/5.0">AREA</a></li>
            <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
            <li><a href="/teste">TESTE</a></li>
            <li><a href="/juros">JUROS</a></li>
            <li><a href="/login">LOGIN</a></li>
            <li><a href="/imc">IMC</a></li>
        </ul>
    """

    else:
        return """<p>O número é ímpar</p> 
        <ul><h3>MENU</h3>
            <li><a href="/">INDEX</a></li>
            <li><a href="/galeria">GALERIA</a></li>
            <li><a href="/contato">CONTATO</a></li>
            <li><a href="/sobre">SOBRE</a></li>
            <li><a href="/tabuada">TABUADA</a></li>
            <li><a href="/nsb">NOME E SOBRENOME</a></li>
            <li><a href="/nmr">IMPAR E PAR</a></li>
            <li><a href="/area/10.0/5.0">AREA</a></li>
            <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
            <li><a href="/teste">TESTE</a></li>
            <li><a href="/juros">JUROS</a></li>
            <li><a href="/login">LOGIN</a></li>
            <li><a href="/imc">IMC</a></li>
        </ul>
    """

@app.route("/nsb", methods=('GET',)) #ASSINA UMA ROTA
def nsb():# FUNÇÃO RESPONSÁVEL PELA PÁGINA
    p1 = request.args.get('n')
    p2 = request.args.get('sb')

    return f"""<p>{p2}, {p1}</p>
    <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>"""

@app.route("/area/<float:largura>/<float:comprimento>", methods=('GET',)) #ASSINA UMA ROTA
def area(largura, comprimento):# FUNÇÃO RESPONSÁVEL PELA PÁGINA
   
    return f"""<h1>A área informada: {largura*comprimento}</h1>
    <ul><li><p>LARGURA: {largura}</p></ul></li><ul><li><p>COMPRIMENTO: {comprimento}</p></ul></li>
    
    <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """

@app.route("/potencia/<float:p1>/<float:p2>", methods=('GET',)) #ASSINA UMA ROTA
def potencia(p1, p2):# FUNÇÃO RESPONSÁVEL PELA PÁGINA
   
    return f"""<h1>A POTÊNCIA informada: {p1**p2}</h1>
    <ul><li><p>VALOR 1: {p1}</p></ul></li><ul><li><p>VALOR 2: {p2}</p></ul></li>
    
    <ul><h3>MENU</h3>
        <li><a href="/">INDEX</a></li>
        <li><a href="/galeria">GALERIA</a></li>
        <li><a href="/contato">CONTATO</a></li>
        <li><a href="/sobre">SOBRE</a></li>
        <li><a href="/tabuada">TABUADA</a></li>
        <li><a href="/nsb">NOME E SOBRENOME</a></li>
        <li><a href="/nmr">IMPAR E PAR</a></li>
        <li><a href="/area/10.0/5.0">AREA</a></li>
        <li><a href="/potencia/10.0/5.0">POTENCIA</a></li>
        <li><a href="/teste">TESTE</a></li>
        <li><a href="/juros">JUROS</a></li>
        <li><a href="/login">LOGIN</a></li>
        <li><a href="/imc">IMC</a></li>
    </ul>
    """


@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET",)) #ASSINA UMA ROTA
def tabuada(numero= None ):# FUNÇÃO RESPONSÁVEL PELA PÁGINA

    if 'numero' in request.args:
        numero = request.args.get('numero')
        numero = int(request.args.get('numero'))
    
    return render_template('tabuada.html', numero=numero)

@app.route("/juros")
@app.route("/juros/<nmr>/<tp>/<pct>/<apt>", methods=("GET",)) #ASSINA UMA ROTA
def juros(nmr = None, tp = None, pct = None, apt= None ):# FUNÇÃO RESPONSÁVEL PELA PÁGINA

    if 'nmr' in request.args:
        nmr = request.args.get('nmr')
        nmr = float (request.args.get('nmr'))

    if 'tp' in request.args:
        tp = request.args.get('tp')
        tp= float (request.args.get('tp'))

    if 'pct' in request.args:
        pct = request.args.get('pct')
        pct= float (request.args.get('pct'))

    if 'apt' in request.args:
        apt = request.args.get('apt')
        apt = float (request.args.get('apt'))
    
    return render_template('juros.html', pct=pct, nmr=nmr, tp=tp, apt=apt)

@app.route("/login")
def login(em = None, snh = None ):# FUNÇÃO RESPONSÁVEL PELA PÁGINA

    if 'em' and 'snh' in request.args:
        em = request.args.get('em')
        snh = request.args.get ('snh')
    
    return render_template('login.html', em=em, snh=snh)

@app.route("/imc")
def imc(peso = None, alt = None ):# FUNÇÃO RESPONSÁVEL PELA PÁGINA

    if 'peso' and 'alt' in request.args:
        peso = float (request.args.get('peso'))
        alt = float (request.args.get ('alt'))
    
    return render_template('IMC.html', peso=peso, alt=alt)