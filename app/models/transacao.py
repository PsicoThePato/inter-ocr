from datetime import datetime
import decimal


from peewee import SqliteDatabase, Model
from peewee import IntegerField, CharField, DateField, AutoField

db = SqliteDatabase('db/transactions.db')

class Transacao(Model):
    preco = IntegerField()
    recebedor = CharField()
    data = DateField()
    id = AutoField(primary_key=True)
    
    class Meta:
        database = db


db.connect()
db.create_tables([Transacao])