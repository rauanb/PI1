from models.orcamentos import Orcamentos
from flask import request
from flask_restful import Resource, reqparse
from datetime import datetime
import json

class OrcamentoController(Resource):
    def get(self):
        lista_orcamento = []
        lorcamento=Orcamentos.buscar()
        for orcamento in lorcamento:
            jsn = {
                "ORC_ID": orcamento.ORC_ID,
                "ORC_NOME": orcamento.ORC_NOME,
                "ORC_CEP": orcamento.ORC_CEP,
                "ORC_EMISSAO": str(orcamento.ORC_EMISSAO),
                "ORC_EMAIL": orcamento.ORC_EMAIL,
                "ORC_TELEFONE": orcamento.ORC_TELEFONE,
                "ORC_LATITUDE": orcamento.ORC_LATITUDE,
                "ORC_LONGITUDE": orcamento.ORC_LONGITUDE,
                "ORC_LOGRADOURO": orcamento.ORC_LOGRADOURO,
                "ORC_BAIRRO": orcamento.ORC_BAIRRO,
                "ORC_NUMERO": orcamento.ORC_NUMERO,
                "ORC_CIDADE": orcamento.ORC_CIDADE,
                "ORC_ESTADO": orcamento.ORC_ESTADO,
                "ORC_TE": orcamento.ORC_TE,
                "ORC_TUSD": orcamento.ORC_TUSD,
                "ORC_CONSUMO": orcamento.ORC_CONSUMO
            }
            lista_orcamento.append(jsn)
        return lista_orcamento, 200
    def put(self):
        lorcamentos = json.loads(request.data)
        try:
            for vorcamento in lorcamentos:
                now = datetime.now()
                orcamento = Orcamentos(
                    vorcamento['ORC_ID'],
                    vorcamento['ORC_NOME'],
                    vorcamento['ORC_CEP'],
                    now.strftime("%d/%m/%Y %H:%M:%S"),
                    vorcamento['ORC_EMAIL'],
                    vorcamento['ORC_TELEFONE'],
                    vorcamento['ORC_LAGITUDE'],
                    vorcamento['ORC_LONGITUDE'],
                    vorcamento['ORC_LOGRADOURO'],
                    vorcamento['ORC_BAIRRO'],
                    vorcamento['ORC_NUMERO'],
                    vorcamento['ORC_CIDADE'],
                    vorcamento['ORC_ESTADO'],
                    vorcamento['ORC_TE'],
                    vorcamento['ORC_TUSD'],
                    vorcamento['ORC_CONSUMO']
                )
                orcamento.update()
            return {"message": "O dado foi inserido no banco de dados"}
        except Exception as e:
            jsn_resposta = {
            "status": 0,
            "motivo": str(e)
            }
            return jsn_resposta