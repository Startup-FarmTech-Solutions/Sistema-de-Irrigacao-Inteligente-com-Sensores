import requests

# --- CONFIGURAÇÕES ---
API_KEY = "c33c7debc53ff32bdee3d24a1188e27e"
CIDADE = "São Paulo"
UNITS = "metric"  # Celsius
LANG = "pt_br"

# --- URL e PARÂMETROS ---
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": CIDADE,
    "appid": API_KEY,
    "units": UNITS,
    "lang": LANG
}

# --- REQUISIÇÃO ---
try:
    resposta = requests.get(url, params=params)
    resposta.raise_for_status()
    dados = resposta.json()

    # --- DADOS CLIMÁTICOS ---
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    chuva = dados.get("rain", {}).get("1h", 0)

    # --- EXIBIÇÃO ---
    print(f"Temperatura: {temperatura:.1f}°C")
    print(f"Condição: {descricao}")
    print(f"Chuva (última hora): {chuva} mm")

    # --- LÓGICA DE IRRIGAÇÃO ---
    if chuva > 0 or "chuva" in descricao.lower():
        print("→ Não irrigar: previsão ou ocorrência de chuva.")
    elif temperatura > 30:
        print("→ Irrigar: está quente e seco.")
    else:
        print("→ Irrigar: condições normais, sem chuva detectada.")

except requests.exceptions.RequestException as erro:
    print("Erro na requisição:", erro)
except KeyError as erro:
    print("Erro ao processar os dados:", erro)

