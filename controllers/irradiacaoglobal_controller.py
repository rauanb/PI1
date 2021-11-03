from models.irradiacao_global import IrradiacaoGlobal
from flask import request
from flask_restful import Resource, reqparse
import json

class IrradiacaoGlobalController(Resource):
    def get(self):
        lista_irradiacao = []
        lirradiacao=IrradiacaoGlobal.buscar()
        for irradiacao in lirradiacao:
            jsn = {
                "IG_ID": irradiacao.IG_ID,
                "IG_LATITUDE": irradiacao.IG_LATITUDE,
                "IG_LONGITUDE": irradiacao.IG_LONGITUDE,
                "IG_CIDADE": irradiacao.IG_CIDADE,
                "IG_UF": irradiacao.IG_UF,
                "IG_IRRADIACAO": irradiacao.IG_IRRADIACAO
            }
            lista_irradiacao.append(jsn)
        return lista_irradiacao, 200
    def put(self):
        lirradiacao = json.loads(request.data)
        try:
            for virradiacao in lirradiacao:
                irradiacao = IrradiacaoGlobal(
                    virradiacao["IG_ID"],
                    virradiacao["IG_LATITUDE"],
                    virradiacao["IG_LONGITUDE"],
                    virradiacao["IG_CIDADE"],
                    virradiacao["IG_UF"],
                    virradiacao["IG_IRRADIACAO"]
                )
                irradiacao.update()
            return {"message": "O dado foi inserido no banco de dados"}
        except Exception as e:
            jsn_resposta = {
            "status": 0,
            "motivo": str(e)
            }
            return jsn_resposta 