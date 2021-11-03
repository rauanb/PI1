from db import db

class IrradiacaoGlobal(db.Model):
  __tablename__ = 'IRRADIACAO_GLOBAL'

  IG_ID = db.Column(db.Integer, nullable=False, primary_key=True)
  IG_LATITUDE = db.Column(db.Float, default = 0.00, nullable=True)
  IG_LONGITUDE = db.Column(db.Float, default = 0.00, nullable=True)
  IG_CIDADE = db.Column(db.String(80), nullable=False)
  IG_UF = db.Column(db.String(2), nullable=False)
  IG_IRRADIACAO = db.Column(db.Float, default = 0.00, nullable=False)

  def __init__(self, id_ig, latitude, longitude, cidade, uf, irradiacao):
    self.IG_ID = id_ig
    self.IG_LATITUDE = latitude
    self.IG_LONGITUDE = longitude
    self.IG_CIDADE = cidade
    self.IG_UF = uf
    self.IG_IRRADIACAO = irradiacao
  @classmethod
  def buscar(cls):
    return db.session.query(IrradiacaoGlobal).filter(IrradiacaoGlobal.IG_ID>0).order_by(IrradiacaoGlobal.IG_ID)
  def save(self):
    db.session.add(self)
    db.session.commit()
  def update(self):
    db.session.merge(self)
    db.session.commit()