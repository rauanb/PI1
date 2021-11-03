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
                if vorcamento['ORC_ID']=='':
                    idorcamento=Orcamentos.maiorid()+1
                else:
                    idorcamento=vorcamento['ORC_ID']
                print(idorcamento)
                now = datetime.now()
                orcamento = Orcamentos(
                    idorcamento,
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
            jsn_resposta = {
                "id": int(idorcamento),
                "motivo": "Orçamento Incluido com sucesso",
                "total": "R$ 3.000,00"
            }
        except Exception as e:
            jsn_resposta = {
            "status": 0,
            "motivo": str(e)
            }
        return jsn_resposta