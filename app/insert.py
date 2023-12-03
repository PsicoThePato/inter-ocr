from datetime import datetime
from ocr.ocr import get_pages
from parse.parser import filter_fatura, parse_line
from models.transacao import Transacao

pages = get_pages('/home/dev-machine/pessoal/inter-ocr/input/fat_nov.pdf')
compras = []
for page in pages:
    compras += filter_fatura(page)

for compra in compras:
    data, recebedor, preco = parse_line(compra)
    trans = Transacao.create(
        data=datetime(
            day=data[0], month=data[1], year=data[2]
            ), 
        recebedor=recebedor, 
        preco=preco
        )
    print(trans.preco)
    Transacao.insert(trans)