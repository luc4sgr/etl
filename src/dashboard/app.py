# Importing necessary libraries
# Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
import sqlite3

# Connecting to SQLite database
# Conectando ao banco de dados SQLite
conn = sqlite3.connect('data/mercadolivre.db')

# Reading data from the "notebook" table into a DataFrame
# Lendo dados da tabela "notebook" para um DataFrame
df = pd.read_sql_query("SELECT * FROM notebook", conn)

# Closing the database connection
# Fechando a conexão com o banco de dados
conn.close()

# Streamlit page title
# Título da página Streamlit
st.title('📊 Pesquisa de Mercado - Notebooks no Mercado Livre')

# Section for main KPIs
# Seção para KPIs principais
st.subheader('💡 KPIs principais')
col1, col2, col3 = st.columns(3)

# Total number of notebook entries
# Total de registros de notebooks
total_itens = df.shape[0]
col1.metric(label="🖥️ Total de Notebooks", value=total_itens)

# Count of unique brands
# Contagem de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="🏷️ Marcas Únicas", value=unique_brands)

# Average new price across all items
# Preço médio dos produtos novos
average_new_price = df['new_price'].mean()
col3.metric(label="💰 Preço Médio (R$)", value=f"{average_new_price:.2f}")

# Section for most frequent brands
# Seção para marcas mais frequentes
st.subheader('🏆 Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)  # Visual bar chart
col2.write(top_brands)      # Display table of brand frequencies

# Section for average price by brand
# Seção para preço médio por marca
st.subheader('💵 Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_price'] > 0]  # Filter out zero prices
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)  # Bar chart of prices
col2.write(average_price_by_brand)      # Price data in table format

# Section for satisfaction ratings by brand
# Seção para avaliação média por marca
st.subheader('⭐ Satisfação média por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]  # Filter out zero ratings
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)  # Bar chart of satisfaction scores
col2.write(satisfaction_by_brand)      # Satisfaction data in table format
