import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Análise Exploratória Interativa",
    layout="wide"
)

st.title("📊 Análise Exploratória Interativa com Streamlit")

st.write("""
Aplicativo simples para realizar uma **Análise Exploratória de Dados (EDA)**.
Envie um arquivo CSV para visualizar tabelas, estatísticas e gráficos interativos.
""")

uploaded_file = st.file_uploader("Envie seu arquivo .csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🧾 Primeiras linhas do DataFrame")
    st.dataframe(df.head())

    st.subheader("📈 Estatísticas Descritivas")
    st.write(df.describe(include="all"))

    st.subheader("📊 Visualização Interativa")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) < 1:
        st.warning("Não há colunas numéricas suficientes para gerar gráficos.")
    else:
        chart_type = st.selectbox(
            "Escolha o tipo de gráfico:",
            ["Histograma", "Dispersão", "Linha"]
        )

        if chart_type == "Histograma":
            coluna = st.selectbox("Selecione a coluna:", numeric_cols)
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X(coluna, bin=True),
                y='count()'
            ).properties(width=700, height=400)
            st.altair_chart(chart, use_container_width=True)

        elif chart_type == "Dispersão":
            x = st.selectbox("Eixo X:", numeric_cols)
            y = st.selectbox("Eixo Y:", numeric_cols)

            chart = alt.Chart(df).mark_circle(size=60).encode(
                x=x,
                y=y,
                tooltip=[x, y]
            ).properties(width=700, height=400)

            st.altair_chart(chart, use_container_width=True)

        elif chart_type == "Linha":
            coluna = st.selectbox("Selecione a coluna:", numeric_cols)
            df_reset = df.reset_index().rename(columns={"index": "Índice"})

            chart = alt.Chart(df_reset).mark_line().encode(
                x='Índice',
                y=coluna
            ).properties(width=700, height=400)

            st.altair_chart(chart, use_container_width=True)

else:
    st.info("👆 Envie um CSV para iniciar.")
