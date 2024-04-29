from datetime import datetime
from src.app import db

payment_table = db.Table(
    'payments', db.metadata,
    db.Column('id',
              db.Integer,
              unique=True, nullable=False, primary_key=True, autoincrement=True),
    db.Column('name', db.String, nullable=False),
    db.Column('governmentId', db.String, nullable=False),
    db.Column('email', db.String, nullable=False),
    db.Column('debtAmount',  db.Float(asdecimal=True), nullable=False),
    db.Column('debtDueDate', db.DateTime, nullable=False),
    db.Column('debtID', db.String, nullable=False)
)
