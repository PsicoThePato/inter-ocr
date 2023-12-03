import re
from .meses import standardize_mes

def filter_fatura(text: str):
    lines = text.splitlines()
    pattern = '^\d{2} \w{3} \d{4}.*\$ \d*,\d{2}'
    compras = filter(lambda texto: re.findall(pattern, texto), lines)
    return [*compras]


def parse_line(text: str) -> tuple[tuple[str, str, str], str, str]:
    pattern = '(\d{4})'
    line =  ' '.join(re.split(pattern, text)).split()
    dia = int(line[0])
    mes = int(standardize_mes(line[1]))
    year = int(line[2])
    recebedor = ' '.join(line[3:-2])
    preco = line[-1].replace(",", "")

    return((dia, mes, year), recebedor, preco)