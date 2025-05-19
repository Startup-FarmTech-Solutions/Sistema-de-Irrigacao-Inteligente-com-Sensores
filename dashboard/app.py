"""
Dashboard Sensorial para Visualização de Dados de Sensores

Este aplicativo Dash lê dados de sensores de um arquivo JSON e exibe:
- Gráficos de linha para temperatura, umidade, pH e luminosidade (LDR)
- Histograma para a presença de fósforo e potássio
- Quadro de status da máquina (irrigação ativa/inativa)

Autor: francismaralvesmartinsjunior
"""

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import json


def load_json_data(filepath):
    """
    Carrega os dados JSON a partir de um arquivo.

    Args:
        filepath (str): Caminho para o arquivo JSON.

    Returns:
        dict: Conteúdo do JSON carregado.
    """
    with open(filepath, "r") as f:
        return json.load(f)


def create_temperature_figure(df):
    """
    Cria gráfico de linha para a temperatura do solo.

    Args:
        df (pd.DataFrame): DataFrame com os dados.

    Returns:
        plotly.graph_objs._figure.Figure: Gráfico de linha.
    """
    return px.line(df, y="temperatura", title="Temperatura do Solo", markers=True)


def create_humidity_figure(df):
    """
    Cria gráfico de linha para a umidade do solo.

    Args:
        df (pd.DataFrame): DataFrame com os dados.

    Returns:
        plotly.graph_objs._figure.Figure: Gráfico de linha.
    """
    return px.line(df, y="umidade", title="Umidade do Solo", markers=True)


def create_ph_figure(df):
    """
    Cria gráfico de linha para o pH do solo.

    Args:
        df (pd.DataFrame): DataFrame com os dados.

    Returns:
        plotly.graph_objs._figure.Figure: Gráfico de linha.
    """
    return px.line(df, y="ph", title="pH do Solo", markers=True)


def create_ldr_figure(df):
    """
    Cria gráfico de linha para a leitura de luminosidade (LDR).

    Args:
        df (pd.DataFrame): DataFrame com os dados.

    Returns:
        plotly.graph_objs._figure.Figure: Gráfico de linha.
    """
    return px.line(df, y="leitura_ldr", title="Luminosidade (LDR)", markers=True)


def create_fosforo_potassio_figure(df):
    """
    Cria histograma para a presença de fósforo e potássio.

    Args:
        df (pd.DataFrame): DataFrame com os dados.

    Returns:
        plotly.graph_objs._figure.Figure: Histograma.
    """
    df_bool = df[["potassio", "fosforo"]].apply(lambda col: col.map({True: "Presente", False: "Ausente"}))
    df_bool = df_bool.melt(var_name="Elemento", value_name="Estado")

    return px.histogram(
        df_bool,
        x="Elemento",
        color="Estado",
        barmode="group",
        title="Fósforo e Potássio"
    )


def create_status_component(status):
    """
    Cria componente visual de status da irrigação.

    Args:
        status (str): Status atual da irrigação ("ATIVA" ou "INATIVA").

    Returns:
        dash.html.Div: Elemento HTML do status.
    """
    cor = "red" if status == "ATIVA" else "green"
    texto = "Máquina Ligada" if status == "ATIVA" else "Máquina Desligada"

    return html.Div(
        children=[
            html.Span("🛠️", style={"fontSize": "32px", "marginRight": "10px"}),
            html.Span(texto, style={"fontSize": "20px", "color": cor}),
        ],
        style={
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "flex-start",
            "border": "2px solid #ccc",
            "padding": "10px",
            "borderRadius": "8px",
            "marginBottom": "20px",
            "width": "300px",
            "backgroundColor": "#f9f9f9"
        }
    )


def two_column_row(graph1, graph2):
    """
    Cria uma linha com até dois gráficos lado a lado.

    Args:
        graph1: Primeiro gráfico.
        graph2: Segundo gráfico ou None.

    Returns:
        dash.html.Div: Linha com os gráficos organizados.
    """
    col1 = html.Div(dcc.Graph(figure=graph1), style={"width": "48%", "display": "inline-block", "padding": "1%"})
    col2 = html.Div(dcc.Graph(figure=graph2), style={"width": "48%", "display": "inline-block", "padding": "1%"}) if graph2 else None

    return html.Div(children=[col for col in [col1, col2] if col is not None])


def main():
    """
    Função principal que inicializa e executa o aplicativo Dash.
    """
    app = Dash(__name__)

    # Carrega os dados
    json_data = load_json_data("sensor_solo/data/console_print.json")
    df = pd.DataFrame(json_data["data"])
    status_irrigacao = df.iloc[-1]["irrigacao"]

    # Cria os gráficos
    fig_ldr = create_ldr_figure(df)
    fig_humidity = create_humidity_figure(df)
    fig_ph = create_ph_figure(df)
    fig_temperature = create_temperature_figure(df)
    fig_fos_pot = create_fosforo_potassio_figure(df)

    # Layout do app
    app.layout = html.Div([
        html.H1("Dashboard Sensorial"),
        html.P("Visualização dos dados coletados de sensores do solo e irrigação."),
        create_status_component(status_irrigacao),

        two_column_row(fig_ldr, fig_fos_pot),
        two_column_row(fig_humidity, fig_ph),
        two_column_row(fig_temperature, None)
    ], style={"padding": "20px"})

    app.run(debug=True)


#    if __name__ == '__main__':
#        main()
