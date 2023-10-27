from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# simulando um banco de dados por meio de uma lista
itens = []


@app.route('/')
def index():
    return render_template('lista_itens.html', itens=itens)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        categoria = request.form.get('categoria')
        itens.append({'nome': nome, 'descricao': descricao, 'categoria': categoria})
        return redirect(url_for('index'))
    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)