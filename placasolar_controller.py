from models.placa_solar import PlacaSolar
from flask import request
from flask_restful import Resource, reqparse
import json

class PlacaSolarController(Resource):
    def get(self):
        listaplaca=[]
        lplacas=PlacaSolar.buscar()
        for placa in lplacas:
            jsn = {
                "PS_ID": placa.PS_ID,
                "PS_NOME": placa.PS_NOME,
                "PS_POTENCIA": placa.PS_POTENCIA,
                "PS_ALTURA": placa.PS_ALTURA,
                "PS_LARGURA": placa.PS_LARGURA,
                "PS_PESO": placa.PS_PESO,
                "PS_EFICIENCIA": placa.PS_EFICIENCIA,
                "PS_PRECO": placa.PS_PRECO
            }
            listaplaca.append(jsn)
        return listaplaca, 200
    def put(self):
        lplaca = json.loads(request.data)
        try:
            for vplacasolar in lplaca:
                print(id)
                placasolar = PlacaSolar(
                vplacasolar['PS_ID'],
                vplacasolar['PS_NOME'],
                vplacasolar['PS_POTENCIA'],
                vplacasolar['PS_ALTURA'],
                vplacasolar['PS_LARGURA'],
                vplacasolar['PS_PESO'],
                vplacasolar['PS_EFICIENCIA'],
                vplacasolar['PS_PRECO'])
                placasolar.update()
            return {"message": "O dado foi inserido no banco de dados"},200
        except Exception as e:
            jsn_resposta = {
            "status": 0,
            "motivo": str(e)
            }
            return jsn_resposta 
