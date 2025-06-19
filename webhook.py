from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', '')
    
    if message.lower() == 'hola':
        respuesta = 'Hello World!'
    else:
        respuesta = 'Message unfound.'

    return jsonify({'request': respuesta})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
