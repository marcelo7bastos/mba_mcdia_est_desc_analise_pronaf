import plotly.graph_objects as go
import streamlit as st

def plot_sankey(df):
    """ Cria um diagrama de Sankey para visualizar a escalada de crescimento dos programas do PRONAF """
    st.write("### 📈 Existe uma Escada de Crescimento nos Subprogramas do PRONAF?")

    if "subprograma_origem" in df.columns and "subprograma_destino" in df.columns and "fluxo" in df.columns:
        fig_sankey = go.Figure(go.Sankey(
            node=dict(
                pad=15, thickness=20, line=dict(color="black", width=0.5),
                label=list(set(df["subprograma_origem"]).union(set(df["subprograma_destino"])))
            ),
            link=dict(
                source=df["subprograma_origem"].astype(str),
                target=df["subprograma_destino"].astype(str),
                value=df["fluxo"]
            )
        ))
        fig_sankey.update_layout(title_text="Fluxo entre Subprogramas", font_size=10)
        st.plotly_chart(fig_sankey)
    else:
        st.warning("Os dados não contêm as colunas necessárias para o gráfico de Sankey.")
