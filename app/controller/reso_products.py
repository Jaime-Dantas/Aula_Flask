from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.products import Products

#para adicionar
argumentos = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos.add_argument('name', type=str)
argumentos.add_argument('price', type=float)
argumentos.add_argument('data_despesa', type=str)
argumentos.add_argument('valor', type=float)
argumentos.add_argument('meto_pagamento', type=str)
argumentos.add_argument('descricao', type=str)
argumentos.add_argument('status_despesa', type=str)

class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            Products.save_products(self, datas['name'], datas['price'],datas['data_despesa'],datas['valor'],datas['meto_pagamento'],datas['descricao'],datas['status_despesa'])
            return {"message": 'Survivor create successfully!'}, 201
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500