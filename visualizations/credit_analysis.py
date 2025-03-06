import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_credit_rural(df):
    """ Cria o gráfico de barras para volume de crédito rural anual """
    st.write("### 💰 Qual o volume de crédito rural anual?")
    
    df_credito_rural = df[['ANO', 'CD_CPF_CNPJ', 'CD_PROGRAMA', 'VL_PARC_CREDITO']]
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data=df_credito_rural, x='ANO', y='VL_PARC_CREDITO', estimator=sum, errorbar=None, color='#4C72B0')
    
    plt.title('Qual o volume de crédito rural anual?', fontsize=14, color='darkgray', weight='bold')
    plt.xlabel('Ano', fontsize=12, color='darkgray')
    plt.ylabel(None)
    
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_yticks([])

    for p in ax.patches:
        height = p.get_height() / 1e9
        ax.annotate(f'{height:.1f}B', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=11, color='darkgray')

    plt.xticks(rotation=45, fontsize=11, color='darkgray')
    st.pyplot(plt)

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_credit_pronaf_total(df):
    """Cria o gráfico comparando o crédito total e o crédito do PRONAF."""
    st.write("### 📊 Quanto o PRONAF representa do crédito total?")

    # Criar agregação do total de crédito por ano 
    df_credito_rural = df[['ANO', 'CD_CPF_CNPJ', 'CD_PROGRAMA', 'VL_PARC_CREDITO']]
    credito_total = df_credito_rural.groupby('ANO')['VL_PARC_CREDITO'].sum().reset_index()

    # Filtrar os dados para o programa específico (CD_PROGRAMA = '0001')
    df_programa_0001 = df_credito_rural[df_credito_rural['CD_PROGRAMA'] == '0001']
    credito_programa_0001 = df_programa_0001.groupby('ANO')['VL_PARC_CREDITO'].sum().reset_index()

    # Criar gráfico
    plt.figure(figsize=(12, 6))
    
    # Criando barras para o crédito total
    sns.barplot(data=credito_total, x='ANO', y='VL_PARC_CREDITO', color='#4C72B0', label='Crédito Total')
    
    # Criando barras para o crédito do programa 0001
    sns.barplot(data=credito_programa_0001, x='ANO', y='VL_PARC_CREDITO', color='#55A868', label='Crédito Programa 0001')
    
    # Ajustando título
    plt.title('Quanto o PRONAF representa do crédito total?', fontsize=16, color='darkgray', weight='bold')

    # Ajustando rótulos dos eixos
    plt.xlabel('Ano', fontsize=12, color='darkgray')
    plt.ylabel(None)  # Remove nome do eixo Y

    # Removendo a barra e os números do eixo Y
    ax = plt.gca()
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_yticks([])

    # Adicionando valores no topo das barras (convertendo para bilhões)
    for p in ax.patches:
        height = p.get_height() / 1e9  # Convertendo para bilhões
        if height > 0:  # Evitar anotações em valores zerados
            ax.annotate(f'{height:.1f}B',
                        (p.get_x() + p.get_width() / 2, p.get_height()),
                        ha='center', va='bottom', fontsize=10, color='darkgray')

    # Ajustando rótulos do eixo X
    plt.xticks(rotation=45, fontsize=11, color='darkgray')

    # Exibir o gráfico no Streamlit
    st.pyplot(plt)
