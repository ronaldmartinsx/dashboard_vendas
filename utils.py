import time
from dataset import df
import pandas as pd
import streamlit as st
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

#1 - Funcao para formatacao de numeros
def format_number(value, prefix=''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} mi'

# 2 - Dataframe receita por estado
df_rec_estado = df.groupby('Local da compra')['Preço'].sum()
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat', 'lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

#3 - Dataframe receita mensal
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index().sort_values('Data da Compra', ascending=True)
df_rec_mensal['mes_formatado'] = df_rec_mensal['Data da Compra'].dt.strftime('%b%y')

#4 -  Dataframe receita por categoria
df_rec_categoria = df.groupby('Categoria do Produto')['Preço'].sum().reset_index().sort_values('Preço', ascending=True).head()

#5 - Dataframe vendedores
df_vendedores = df.groupby('Vendedor')['Preço'].agg(['sum', 'count']).reset_index()


#6 - Conversao para arquivo CSV
@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def messagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        icon='✅'
    )
    time.sleep(3)
    success.empty()