from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.route('/sumar/',methods=['POST'])
def sumar():
	numeros = request.json['numeros']
	num= numeros.split(":")
	sum= 0
	for temp in num:
		sum = int(sum) + int(temp)
	dat = {
	'operacion': 'suma',
	'resultado': sum
	}
	return jsonify(dat)

	
@app.route('/restar/',methods=['POST'])
def restar():
	numero1 = request.json['numero1']
	numero2 = request.json['numero2']
	res = int(numero1) - int(numero2)
	dat = {
	'operacion': 'resta',
	'resultado': res
	}
	return jsonify(dat)
	
@app.route('/multiplicar/',methods=['POST'])
def multiplicar():
	numeros = request.json['numeros']
	num= numeros.split(":")
	sum= 1
	for temp in num:
		sum = int(sum) * int(temp)
	dat = {
	'operacion': 'multiplicar',
	'resultado': sum
	}
	return jsonify(dat)

@app.route('/dividir/',methods=['POST'])
def dividir():
	numero1 = request.json['numero1']
	numero2 = request.json['numero2']
	res = int(numero1) / int(numero2)
	dat = {
	'operacion': 'dividir',
	'resultado': res
	}
	return jsonify(dat)
	
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)