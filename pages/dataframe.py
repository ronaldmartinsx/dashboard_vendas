import streamlit as st
from dataset import df
from utils import convert_csv, messagem_sucesso

st.title('Dataset de vendas')

with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as colunas',
        list(df.columns),
        list(df.columns)
    )

st.sidebar.title('Filtros')

with st.sidebar.expander('Categoria do produto'):
    categorias = st.multiselect(
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique(),
    )

with st.sidebar.expander('Preco do produto'):
    preco = st.slider(
        'Selecione o preco',
        0, 5000,
        (0, 5000),

    )

with st.sidebar.expander('Data da compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(), df['Data da Compra'].max()),
        format= 'DD/MM/YYYY'
    )

query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <=  @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''

filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)

st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')

st.download_button(
    'Baixar arquivo',
    data=convert_csv(filtro_dados),
    file_name='Dataframe.csv',
    mime='text/csv',
    on_click= messagem_sucesso
)