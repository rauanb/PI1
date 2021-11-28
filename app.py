from flask import Flask
from flask_restful import Api
from db import db
from flask_cors import CORS, cross_origin
import os
from controllers.concessionarias_controller import ConcessionariaController
from controllers.placasolar_controller import PlacaSolarController
from controllers.orcamentos_controller import OrcamentoController
from controllers.irradiacaoglobal_controller import IrradiacaoGlobalController
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type,Access-Control-Allow-Origin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mumlvibqtpxipl:e089c79323642bc6c261807c6cbdf3c6286542d3b92d7e213ff3273a801ad26a@ec2-3-222-24-200.compute-1.amazonaws.com:5432/d3utkbcu4mb99v'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_PROPAGATE_EXCEPTIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("HEROKU_POSTGRESQL_OLIVE_URL")
api = Api(app)
@app.before_first_request
def create_tables():
  db.create_all()
@app.after_request
def apply_caching(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response
api.add_resource(ConcessionariaController, '/concessionarias')
api.add_resource(PlacaSolarController, '/placasolar')
api.add_resource(OrcamentoController, '/orcamentos')
api.add_resource(IrradiacaoGlobalController, '/irradiacao')
if __name__ == '__main__':
    db.init_app(app)
    app.run(host='localhost', debug=True)