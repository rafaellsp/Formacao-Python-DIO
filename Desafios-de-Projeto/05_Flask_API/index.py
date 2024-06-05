# Importar bibliotecas
from flask import Flask, jsonify, request
from pyngrok import ngrok
import json

# Criar dados de exemplo e salvar em um arquivo JSON
data = [
    {'id': 1, 'name': 'John', 'age': 30},
    {'id': 2, 'name': 'Jane', 'age': 25}
]

with open('/content/data.json', 'w') as f:
    json.dump(data, f)

# Criar o aplicativo Flask
app = Flask(__name__)

# Carregar os dados do JSON
with open('/content/data.json') as f:
    data = json.load(f)

# Definir endpoints da API
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data/<int:id>', methods=['GET'])
def get_data_by_id(id):
    item = next((item for item in data if item['id'] == id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/data', methods=['POST'])
def add_data():
    new_item = request.get_json()
    data.append(new_item)
    with open('/content/data.json', 'w') as f:
        json.dump(data, f)
    return jsonify(new_item), 201

# Expor o servidor Flask usando ngrok
public_url = ngrok.connect(port='5000')
print(f'Public URL: {public_url}')

# Executar o aplicativo Flask
app.run()
