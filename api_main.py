import os
from flask import Flask, jsonify, request


app = Flask(__name__) 


@app.route('/', methods=['GET', 'POST'])  # DEFAULT É SÓ GET
def minha_funcao():
    print(request.args.get('Valor'))
    my_params = request.args
    if(request.method == 'POST'):
        return ("Usuário sem permissão")
    return jsonify({"message": "Sorria você está sendo filmado!"})

@app.route('/novorecurso', methods=['GET', 'POST'])  # DEFAULT É SÓ GET
def novo_recurso():
    print(request.args.get('Valor'))
    my_params = request.args
    if(my_params.get('Valor', type=int) == 42):
        return jsonify({"Valor": "O valor recebido foi: "
        +str(my_params.get('Valor', type=int))})
    else:
        return 'bad request!', 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
