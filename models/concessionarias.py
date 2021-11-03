from db import db

class Concessionarias(db.Model):
  __tablename__ = 'CONCESSIONARIAS'

  CC_ID = db.Column(db.Integer, nullable=False, primary_key=True)
  CC_NOME = db.Column(db.String(80), nullable=False)

  def __init__(self, id_cc, nome):
    self. CC_ID = id_cc
    self. CC_NOME = nome

  @classmethod
  def buscar(cls):
    return db.session.query(Concessionarias).filter(Concessionarias.CC_ID>0).order_by(Concessionarias.CC_NOME)
  def save(self):
    db.session.add(self)
    db.session.commit()
  def update(self):
    db.session.merge(self)
    db.session.commit()