from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# simulando um banco de dados por meio de uma lista
itens = []
current_id = 0  # para gerar IDs únicos para cada item


@app.route('/')
def index():
    return render_template('lista_itens.html', itens=itens)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    global current_id
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        categoria = request.form.get('categoria')

        # atribuindo um ID único para cada novo item e incrementando o current_id
        current_id += 1
        itens.append({'id': current_id, 'nome': nome, 'descricao': descricao, 'categoria': categoria})

        return redirect(url_for('index'))
    return render_template('cadastro.html')


@app.route('/atualizar/<int:item_id>', methods=['PATCH'])
def atualizar(item_id):
    item = next((item for item in itens if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item não encontrado'}), 404

    data = request.json
    item['nome'] = data.get('nome', item['nome'])
    item['descricao'] = data.get('descricao', item['descricao'])
    item['categoria'] = data.get('categoria', item['categoria'])
    return jsonify(item)


@app.route('/deletar/<int:item_id>', methods=['DELETE'])
def deletar(item_id):
    global itens
    itens = [item for item in itens if item['id'] != item_id]
    return jsonify({'status': 'sucesso'})


if __name__ == '__main__':
    app.run(debug=True)