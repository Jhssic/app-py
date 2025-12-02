import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análise Exploratória Interativa", layout="wide")

st.title("📊 Análise Exploratória Interativa com Streamlit")

st.write("""
Este aplicativo realiza **Análise Exploratória de Dados (EDA)** de forma simples e interativa.
Faça upload de um arquivo CSV para começar.
""")

# 1. Upload
uploaded_file = st.file_uploader("Envie seu arquivo .csv", type=["csv"])

if uploaded_file:
    # 2. Estruturar DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🧾 Primeiras linhas do DataFrame")
    st.write(df.head())  # 3. Exibir primeiras linhas

    # 4. Estatísticas descritivas
    st.subheader("📈 Estatísticas Descritivas")
    st.write(df.describe(include="all"))

    # 5. Visualização interativa
    st.subheader("📊 Visualização Interativa")

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

    if len(numeric_cols) > 0:
        x = st.selectbox("Selecione a variável para o eixo X:", numeric_cols)
        y = st.selectbox("Selecione a variável para o eixo Y:", numeric_cols)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x, y=y, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("O dataset não possui colunas numéricas suficientes.")
else:
    st.info("Aguardando upload do arquivo...")
