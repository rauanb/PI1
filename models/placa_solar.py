from db import db

class PlacaSolar(db.Model):
  __tablename__ = 'PLACA_SOLAR'

  PS_ID = db.Column(db.Integer, nullable=False, primary_key=True)
  PS_NOME = db.Column(db.String(80), nullable=False)
  PS_POTENCIA = db.Column(db.Float, default = 0.00, nullable=False)
  PS_ALTURA = db.Column(db.Float, default = 0.00, nullable=False)
  PS_LARGURA = db.Column(db.Float, default = 0.00, nullable=False)
  PS_PESO = db.Column(db.Float, default = 0.00, nullable=True)
  PS_EFICIENCIA = db.Column(db.Float, default = 0.00, nullable=False)
  PS_PRECO = db.Column(db.Float, default = 0.00, nullable=False)

  def __init__(self, id_ps, nome, potencia , altura, largura , peso, eficiencia, preco):
    self.PS_ID = id_ps
    self.PS_NOME = nome
    self.PS_POTENCIA = potencia
    self.PS_ALTURA = altura
    self.PS_LARGURA = largura
    self.PS_PESO = peso
    self.PS_EFICIENCIA = eficiencia
    self.PS_PRECO = preco
  @classmethod
  def buscar(cls):
    return db.session.query(PlacaSolar).filter(PlacaSolar.PS_ID>0).order_by(PlacaSolar.PS_ID).all()
  def save(self):
    db.session.add(self)
    db.session.commit()
  def update(self):
    db.session.merge(self)
    db.session.commit()

