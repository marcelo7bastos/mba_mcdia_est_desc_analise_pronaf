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
#https://drive.google.com/file/d/1whqhmvsWbXpmCaOjASUDmEolMIyMjZIG/view?usp=sharing
#file_path = r"data\pronaf_tratado.parquet"
#df = pd.read_parquet(file_path)
import pandas as pd
import gdown
import os

# Definir o ID do arquivo no Google Drive
file_id = "1whqhmvsWbXpmCaOjASUDmEolMIyMjZIG"

# Criar diretório "data" se não existir
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Definir o caminho do arquivo dentro da pasta "data"
file_path = os.path.join(data_dir, "pronaf_tratado.parquet")

# Baixar o arquivo apenas se ele não existir
if not os.path.exists(file_path):
    try:
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, file_path, quiet=False)
        print(f"Arquivo baixado com sucesso: {file_path}")
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")

# Carregar o arquivo Parquet
try:
    df = pd.read_parquet(file_path)
    print("Arquivo Parquet carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o arquivo Parquet: {e}")
#######

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
