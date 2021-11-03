from db import db
from datetime import datetime
from sqlalchemy.sql.expression import func

class Orcamentos(db.Model):
  __tablename__ = 'ORCAMENTOS'

  ORC_ID = db.Column(db.Integer, nullable=False, primary_key=True)
  ORC_NOME = db.Column(db.String(80), nullable=False)
  ORC_CEP = db.Column(db.String(9), nullable=False)
  ORC_EMISSAO = db.Column(db.DateTime, nullable=False, default=datetime.now().strftime("%Y-%m-%d %H:%M:&S"))
  ORC_EMAIL = db.Column(db.String(80), nullable=False)
  ORC_TELEFONE = db.Column(db.String(20), nullable=False)
  ORC_LATITUDE = db.Column(db.Float, default = 0.00, nullable=False)
  ORC_LONGITUDE = db.Column(db.Float, default = 0.00, nullable=False)
  ORC_LOGRADOURO = db.Column(db.String(80), nullable=False)
  ORC_BAIRRO = db.Column(db.String(60), nullable=False)
  ORC_NUMERO = db.Column(db.String(10), nullable=False)
  ORC_CIDADE = db.Column(db.String(80), nullable=False)
  ORC_ESTADO = db.Column(db.String(2), nullable=False)
  ORC_TE = db.Column(db.Float, default = 0.00, nullable=False)
  ORC_TUSD = db.Column(db.Float, default = 0.00, nullable=False)
  ORC_CONSUMO = db.Column(db.Float, default = 0.00, nullable=False)

  #IG_ID = db.Column(db.Integer, db.ForeignKey('irradiacao_global.IG_ID'))
  #CC_ID = db.Column(db.Integer, db.ForeignKey('concessionaria.CC_ID'))
  #irradiaca_global = db.relationship('IrradiacaoGlobal')
  #concessionaria = db.relationship('Concessionaria')

  def __init__(self, id_orc, nome, cep , emissao, email, telefone, latitude, longitude, logradouro, bairro, numero, cidade, estado, te , tusd, consumo):
    self.ORC_ID = id_orc
    self.ORC_NOME = nome
    self.ORC_CEP = cep
    self.ORC_EMISSAO = emissao
    self.ORC_EMAIL = email
    self.ORC_TELEFONE = telefone
    self.ORC_LATITUDE = latitude
    self.ORC_LONGITUDE = longitude
    self.ORC_LOGRADOURO = logradouro
    self.ORC_BAIRRO = bairro
    self.ORC_NUMERO = numero
    self.ORC_CIDADE = cidade
    self.ORC_ESTADO = estado
    self.ORC_TE = te
    self.ORC_TUSD = tusd
    self.ORC_CONSUMO = consumo
  @classmethod
  def buscar(cls):
    return db.session.query(Orcamentos).filter(Orcamentos.ORC_ID>0).order_by(Orcamentos.ORC_ID).all()
  @classmethod
  def maiorid(cls):
    lista = db.session.query(func.max(Orcamentos.ORC_ID)).first()
    if lista is not None:
      return lista[0] if lista[0] is not None else 0
    else:
      return 0
  def save(self):
    db.session.add(self)
    db.session.commit()
  def update(self):
    db.session.merge(self)
    db.session.commit()