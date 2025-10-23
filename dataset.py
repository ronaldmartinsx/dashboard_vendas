import json
import pandas as pd

#1 - Importando o dataset JSON
file = open('data/sales.json')
data = json.load(file)

#2 - Transformando em dataframe com o pandas
df = pd.DataFrame.from_dict(data)

#3 - Corrigindo o tipo da coluna "Data da Compra" para datetime
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

#4 - Fechando o arquivo JSON que abrimos na etapa 1
file.close()