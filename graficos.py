import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

# grafico_map_estado = px.scatter_geo(
#     df_rec_estado,
#     lat='lat',
#     lon='lon',
#     scope='south america',
#     size= 'Preço',
#     template='plotly_white',
#     hover_name='Local da compra',
#     hover_data={'lat': False, 'lon': False},
#     title='Receita por estado'
# )

grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    color='Preço',
    color_continuous_scale='Tealgrn',
    template='plotly_white',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False, 'Preço': ':,.0f'},
    title='Receita por estado'
)

grafico_map_estado.update_geos(
    visible=False,      # esconde linhas de grade e eixos
    resolution=50,
    showcountries=True,
    lataxis_range=[-35, 5],   # latitude mínima e máxima
    lonaxis_range=[-75, -30], # longitude mínima e máxima
    fitbounds="locations"     # ajusta automaticamente a visão para os pontos
)


grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='mes_formatado',
    y='Preço',
    markers=True,
    range_y=(0, df_rec_mensal.max()),
    title= 'Receita mensal'
)

grafico_rec_mensal.update_layout(
    xaxis_title = 'Meses',
    yaxis_title = 'Receita'
)

grafico_rec_estado = px.bar(
    df_rec_estado.sort_values('Preço').head(5),
    x = 'Preço',
    y = 'Local da compra',
    orientation='h',
    title = 'Top 5 estados com maior receita',
    text_auto=True
)

grafico_rec_categoria = px.bar(
    df_rec_categoria,
    x = 'Preço',
    y = 'Categoria do Produto',
    orientation= 'h',
    title = 'Top 5 categorias com maior receita',
    text_auto=True
)

grafico_rec_vendedores = px.bar(
    df_vendedores.sort_values('sum', ascending=True).head(10),
    x = 'sum',
    y = 'Vendedor',
    orientation= 'h',
    title = 'Top 10 vendedores com maior receita',
    text_auto=True
)

grafico_vendas_vendedores = px.bar(
    df_vendedores.sort_values('count', ascending=True).head(10),
    x = 'count',
    y = 'Vendedor',
    orientation= 'h',
    title = 'Top 10 vendedores com maior volume de vendas',
    text_auto=True
)