import streamlit as st
import pandas as pd
from visualizations.credit_analysis import plot_credit_rural, plot_credit_pronaf_total
from visualizations.program_growth import plot_sankey

# Configuração da página
st.set_page_config(page_title="Análise PRONAF", layout="wide")

# Título Principal
st.title("📢 Reportagem Interativa: Análise do PRONAF")

# Introdução
st.markdown(
    """
    O **PRONAF (Programa Nacional de Fortalecimento da Agricultura Familiar)** desempenha um papel fundamental no
    desenvolvimento da agricultura familiar no Brasil. Nesta análise, exploramos os dados dos subprogramas do PRONAF
    para entender padrões de crescimento, fluxo entre programas e impactos econômicos.
    
    Acompanhe essa reportagem interativa para visualizar insights sobre os beneficiários e sua evolução dentro do sistema.
    """
)

# Carregar os dados automaticamente
file_path = r"data\pronaf_tratado.parquet"
df = pd.read_parquet(file_path)

# Visão Geral dos Dados
st.write("### 🔍 Visão Geral dos Dados")
st.dataframe(df.head())

# Estatísticas Descritivas
st.write("### 📊 Estatísticas Descritivas")
st.write(df.describe())

# Chamar funções modularizadas para exibição de gráficos
plot_credit_rural(df)
plot_credit_pronaf_total(df)
plot_sankey(df)

# Conclusão
st.write("### 🔎 Conclusões e Insights")
st.markdown(
    """
    A análise dos subprogramas do PRONAF revela padrões interessantes sobre a mobilidade dos beneficiários.
    Algumas descobertas importantes incluem:
    
    - O fluxo de crescimento dentro dos subprogramas indica que alguns beneficiários progridem ao longo do tempo,
      enquanto outros podem enfrentar desafios que os impedem de avançar.
    - Há uma relação forte entre determinadas variáveis, como o acesso a crédito e a continuidade no programa.
    - A análise interativa permite visualizar tendências e tomar decisões baseadas em dados para aprimorar o programa.
    
    Esta reportagem interativa oferece uma maneira visual e dinâmica de compreender o impacto do PRONAF.
    """
)
