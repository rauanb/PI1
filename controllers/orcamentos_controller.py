from models.orcamentos import Orcamentos
from flask import request
from flask_restful import Resource, reqparse
from datetime import datetime
import json
def investimento(consumo):
    return float(consumo)*60.00
def carbono(consumo):
    return float(consumo)*0.086
def temporetorno(consumo,te,tusd,investimento):
    return int(investimento/((float(consumo)*float(te)) + (float(consumo)*float(tusd))))
class OrcamentoController(Resource):
    @classmethod
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
                vinvestimento = investimento(vorcamento['ORC_CONSUMO'])
                vcarbono = carbono(vorcamento['ORC_CONSUMO'])
                vretorno = temporetorno(vorcamento['ORC_CONSUMO'],vorcamento['ORC_TE'],vorcamento['ORC_TUSD'],vinvestimento)
                orcamento = Orcamentos(
                    idorcamento,
                    vorcamento['ORC_NOME'],
                    vorcamento['ORC_CEP'],
                    now.strftime("%m/%d/%Y %H:%M:%S"),
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
            jsn_resposta = [{
                "Investimento": "O valor do investimento será R$ " +str(vinvestimento),
                "Carbono": "Deixarão de ser emitidos "+str(vcarbono) +" Kg de carbono por mês",
                "Retorno": "Serão necessários " +str(vretorno) +" meses para o investimento ter retorno financeiro" 
            }],200
        except Exception as e:
            jsn_resposta = [{
            "status": 0,
            "motivo": str(e)
            }]
        return jsn_resposta