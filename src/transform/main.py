# Importing necessary libraries
# Importando bibliotecas necessárias
import pandas as pd
from datetime import datetime
import sqlite3

# Reading the JSON Lines data into a DataFrame
# Lendo dados do arquivo JSON Lines para um DataFrame
df = pd.read_json("data/data.jsonl", lines=True)

# Displaying the full DataFrame for inspection
# Exibindo o DataFrame completo para inspeção
print(df)
pd.options.display.max_columns = None  # Show all columns in the output
                                      # Mostrar todas as colunas na saída

# Adding metadata columns
# Adicionando colunas de metadados
df["_source"] = "https://lista.mercadolivre.com.br/notebook"  # Data source
                                                              # Fonte dos dados
df["_datetime"] = datetime.now()  # Timestamp of data processing
                                 # Momento do processamento dos dados

# NULL HANDLING
# TRATATIVAS DE NULOS
df['old_price'] = df['old_price'].fillna('0')                     # Fill missing prices with 0
df['new_price'] = df['new_price'].fillna('0')                     # Preencher preços ausentes com 0
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')  # Fill missing ratings
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')         # Fill missing review amounts

# STRING CLEANING
# LIMPEZA DE STRINGS

# Remove thousands separators (e.g., "2.000" -> "2000")
# Remove os separadores de milhar (ex: "2.000" -> "2000")
df["old_price"] = df["old_price"].astype(str).str.replace(".", "", regex=False)

# Copy the cleaned price into 'new_price'
# Copia o preço limpo para a coluna 'new_price'
df["new_price"] = df["old_price"].astype(str).str.replace(".", "", regex=False)

# Remove parentheses from review count strings
# Remove os parênteses das quantidades de avaliações
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

# TYPE CONVERSION
# CONVERSÃO DE TIPOS

# Convert monetary values and review numbers to appropriate types
# Converte valores monetários e avaliações para os tipos apropriados
df['old_price'] = df['old_price'].astype(float)
df['new_price'] = df['new_price'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)

# PRICE RANGE FILTERING
# FILTRAGEM POR FAIXA DE PREÇO

# Only keep products priced between 1000 and 10000 BRL
# Mantém apenas os produtos com preços entre R$1000 e R$10000
minPrice = 1000
maxPrice = 10000
df = df[
    (df["old_price"] >= minPrice) & (df["old_price"] <= maxPrice) &
    (df["new_price"] >= minPrice) & (df["new_price"] <= maxPrice)
]

# DATABASE EXPORT
# EXPORTAÇÃO PARA BANCO DE DADOS

# Connect to SQLite database
# Conecta ao banco de dados SQLite
conn = sqlite3.connect('data/mercadolivre.db')

# Export DataFrame to the 'notebook' table, replacing existing data
# Exporta o DataFrame para a tabela 'notebook', substituindo os dados existentes
df.to_sql('notebook', conn, if_exists='replace', index=False)

# Close the database connection
# Fecha a conexão com o banco de dados
conn.close()
