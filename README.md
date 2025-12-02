# Análise Exploratória Interativa com Streamlit

Este projeto consiste em um aplicativo web desenvolvido em Python utilizando Streamlit e Pandas para realizar uma Análise Exploratória de Dados (EDA) de forma simples e interativa. O usuário pode carregar um arquivo CSV e visualizar estatísticas, tabelas e gráficos gerados automaticamente.

---

## Objetivo

O objetivo desta aplicação é permitir:

- O upload de um dataset em formato CSV.
- A conversão automática dos dados em um DataFrame do Pandas.
- A visualização das primeiras linhas da base.
- A exibição de estatísticas descritivas.
- A geração de gráficos interativos baseados nas colunas numéricas do dataset.

---

## Funcionalidades

1. **Upload de arquivo CSV**  
   O usuário seleciona um arquivo `.csv` para análise.

2. **Estruturação dos dados**  
   O arquivo enviado é automaticamente convertido em DataFrame.

3. **Visualização inicial**  
   Exibição das cinco primeiras linhas do dataset.

4. **Estatísticas descritivas**  
   Cálculo e apresentação de médias, máximos, mínimos, contagens e outros dados descritivos.

5. **Gráficos interativos**  
   A aplicação permite a escolha entre:
   - Histograma
   - Gráfico de dispersão
   - Gráfico de linha

   As opções dependem das colunas numéricas presentes no arquivo enviado.

---

## Tecnologias Utilizadas

- Python 3.11  
- Streamlit  
- Pandas  
- Altair (visualização gráfica)

---

## Como Executar

### Instale as dependências:

```bash
pip install streamlit pandas altair
