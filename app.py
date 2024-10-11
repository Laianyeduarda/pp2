from flask import Flask, render_template, request, redirect # type: ignore

app = Flask(__name__)

Bolos= [] # No nível zero vamos usar uma lista

@app.route('/') # Rota raiz /
def index():
    return render_template('index.html', Bolos=Bolos)

@app.route('/criar', methods=['POST']) # Rota /criar
def create():
    nome = request.form['nome']
    Bolos.append(nome)
    return redirect('/')

@app.route('/alterar', methods=['POST']) # Rota /alterar
def update():
    old_name = request.form['old_name']
    new_name = request.form['new_name']
    if old_name in Bolos:
        index = Bolos.index(old_name)
        Bolos[index] = new_name
        return redirect('/')

@app.route('/apagar', methods=['POST']) # Rota /apagar
def delete():
    nome = request.form['nome']
    if nome in Bolos:
        Bolos.remove(nome)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)