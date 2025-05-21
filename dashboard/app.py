from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import json

# Integração com o banco Oracle
from leitura_sensor_repository import LeituraSensorRepository
from leitura_sensor_model import LeituraSensorModel


def load_json_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)


def create_leitura_model(ultima_leitura_dict):
    """Cria o modelo a partir do último registro do JSON"""
    return LeituraSensorModel(
        id_sensor=ultima_leitura_dict["id_sensor"],
        id_area_plantio=ultima_leitura_dict["id_area_plantio"],
        data_hora=ultima_leitura_dict["data_hora"],
        temperatura=ultima_leitura_dict["temperatura"],
        umidade=ultima_leitura_dict["umidade"],
        leitura_ldr=ultima_leitura_dict["leitura_ldr"],
        ph=ultima_leitura_dict["ph"],
        potassio=ultima_leitura_dict["potassio"],
        fosforo=ultima_leitura_dict["fosforo"],
        irrigacao=ultima_leitura_dict["irrigacao"]
    )


def create_status_component(status):
    cor = "red" if status == "ATIVA" else "green"
    texto = "Máquina Ligada" if status == "ATIVA" else "Máquina Desligada"
    return html.Div([
        html.Span("🛠️", style={"fontSize": "32px", "marginRight": "10px"}),
        html.Span(texto, style={"fontSize": "20px", "color": cor}),
    ], style={
        "display": "flex",
        "alignItems": "center",
        "padding": "10px",
        "border": "2px solid #ccc",
        "borderRadius": "8px",
        "backgroundColor": "#f9f9f9",
        "width": "300px",
        "marginBottom": "15px"
    })


def create_leitura_existe_component(existe):
    cor = "green" if existe else "orange"
    texto = "✅ Leitura já registrada no banco" if existe else "🆕 Nova leitura ainda não registrada"
    return html.Div(texto, style={
        "color": cor,
        "fontSize": "18px",
        "padding": "8px",
        "border": f"2px solid {cor}",
        "borderRadius": "6px",
        "width": "fit-content",
        "marginBottom": "20px"
    })


def create_ldr_figure(df):
    return px.line(df, y="leitura_ldr", title="Luminosidade (LDR)", markers=True)


def create_fosforo_potassio_figure(df):
    df_bool = df[["potassio", "fosforo"]].apply(lambda col: col.map({True: "Presente", False: "Ausente"}))
    df_bool = df_bool.melt(var_name="Elemento", value_name="Estado")
    return px.histogram(df_bool, x="Elemento", color="Estado", barmode="group", title="Fósforo e Potássio")


def create_temperature_figure(df):
    return px.line(df, y="temperatura", title="Temperatura do Solo", markers=True)


def create_humidity_figure(df):
    return px.line(df, y="umidade", title="Umidade do Solo", markers=True)


def create_ph_figure(df):
    return px.line(df, y="ph", title="pH do Solo", markers=True)


def two_column_row(graph1, graph2):
    col1 = html.Div(dcc.Graph(figure=graph1), style={"width": "48%", "display": "inline-block", "padding": "1%"})
    col2 = html.Div(dcc.Graph(figure=graph2), style={"width": "48%", "display": "inline-block", "padding": "1%"}) if graph2 else None
    return html.Div(children=[col for col in [col1, col2] if col is not None])


def main():
    app = Dash(__name__)

    # 🔹 Carrega os dados JSON
    json_data = load_json_data("sensor_solo/data/console_print.json")
    df = pd.DataFrame(json_data["data"])

    # 🔹 Cria modelo da última leitura
    ultima_leitura = df.iloc[-1].to_dict()
    leitura_model = create_leitura_model(ultima_leitura)

    # 🔹 Consulta Oracle: a leitura já existe?
    repositorio = LeituraSensorRepository()
    leitura_existe = repositorio.leitura_ja_existe(leitura_model)

    # 🔹 Gráficos
    fig_ldr = create_ldr_figure(df)
    fig_fos_pot = create_fosforo_potassio_figure(df)
    fig_humidity = create_humidity_figure(df)
    fig_ph = create_ph_figure(df)
    fig_temperature = create_temperature_figure(df)

    # 🔹 Layout do Dashboard
    app.layout = html.Div([
        html.H1("Dashboard Sensorial"),
        html.P("Visualização dos dados coletados de sensores do solo."),
        create_status_component(ultima_leitura["irrigacao"]),
        create_leitura_existe_component(leitura_existe),
        two_column_row(fig_ldr, fig_fos_pot),
        two_column_row(fig_humidity, fig_ph),
        two_column_row(fig_temperature, None)
    ], style={"padding": "20px"})

    app.run(debug=True)


if __name__ == '__main__':
    main()
