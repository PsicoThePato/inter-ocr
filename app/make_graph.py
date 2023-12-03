import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from models.transacao import Transacao
from collections import defaultdict


total = 0
gastos = defaultdict(lambda: 0)
for trans in Transacao.select():
    trans: Transacao
    gastos[trans.recebedor.split()[0]] += trans.preco/100
gastos_dict = dict(gastos)
#gastos_dict['total'] = sum(gastos_dict.values())
print(gastos_dict)
gastos_df = pd.DataFrame(list(gastos_dict.items()), columns=['estabelecimento', 'preço'])
gastos_df = gastos_df.sort_values(by='preço', ascending=False)

ax = sns.barplot(x="estabelecimento", y="preço", data=gastos_df)
plt.title('Gastos')
plt.xticks(rotation=45, ha='right')

for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')
plt.show()
print(sum(gastos.values()))