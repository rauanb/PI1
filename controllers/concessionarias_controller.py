from models.concessionarias import Concessionarias
from flask import request
from flask_restful import Resource, reqparse
import json

class ConcessionariaController(Resource):
    def get(self):
        lista_conessionaria = []
        lconcessionarias=Concessionarias.buscar()
        for concessionaria in lconcessionarias:
            jsn = {
                "CC_ID": concessionaria.CC_ID,
                "CC_NOME": concessionaria.CC_NOME
            }
            lista_conessionaria.append(jsn)
        return lista_conessionaria, 200
    def put(self):
        lconcessionarias = json.loads(request.data)
        try:
            for vconcessionaria in lconcessionarias:
                id=vconcessionaria['CC_ID']
                nome=vconcessionaria['CC_NOME']
                concessionaria = Concessionarias(id,nome)
                concessionaria.update()
            return {"message": "O dado foi inserido no banco de dados"}
        except Exception as e:
            jsn_resposta = {
            "status": 0,
            "motivo": str(e)
            }
            jsn_resposta.headers.add('Access-Control-Allow-Origin', '*')
            return jsn_resposta 