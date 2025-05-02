# 🌱 FarmTech Solutions - Sistema de Irrigação Inteligente

## 📌 Descrição Rápida

Este projeto simula um sistema de irrigação inteligente com sensores físicos implementados na plataforma Wokwi, 
utilizando um microcontrolador ESP32. O sistema coleta dados simulados de umidade do solo, nutrientes (fósforo e potássio) e pH,
controlando uma bomba de irrigação automaticamente e armazenando os dados em um banco de dados SQL via script Python.
Também há funcionalidades extras de visualização via dashboard e integração com dados climáticos reais por meio de uma API pública.

---
## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/Sistema-de-Irrigacao-Inteligente-com-Sensores.git
cd Sistema-de-Irrigacao-Inteligente-com-Sensores

---

## 🔧 Tecnologias Utilizadas

- ESP32 com PlatformIO (VS Code)
- Simulador Wokwi.com
- C/C++ (para o firmware do ESP32)
- Python 3
- SQLite (banco de dados local)
- Bibliotecas Python: `sqlite3`, `matplotlib`, `streamlit`, `requests`
- API Pública: OpenWeather (https://openweathermap.org/api)

---

## 🧠 Lógica do Projeto

### Sensores Simulados

| Sensor       | Componente Simulado | Tipo de Valor    | Descrição                                         |
|--------------|---------------------|------------------|---------------------------------------------------|
| Umidade      | DHT22               | Analógico        | Mede a umidade do solo                            |
| Fósforo (P)  | Botão físico        | Booleano (ON/OFF)| Simula presença/ausência de fósforo               |
| Potássio (K) | Botão físico        | Booleano (ON/OFF)| Simula presença/ausência de potássio              |
| pH           | LDR (sensor de luz) | Analógico        | Representa variação contínua do pH do solo        |

### Atuação

- Um relé é usado para simular a bomba de irrigação.
- O LED embutido no relé indica o status da bomba:
  - 💡 **Ligado** = irrigação ativa
  - ❌ **Desligado** = irrigação inativa

---

## 🧾 Critérios para Acionamento da Bomba

A bomba de irrigação será ligada automaticamente quando:

- A umidade estiver abaixo de um limite mínimo (ex: 40%);
- E houver presença de pelo menos um nutriente (P ou K);
- E o valor de pH estiver dentro de uma faixa considerada ideal (simulado via LDR).

---

## 💻 Estrutura dos Arquivos

/FarmTech-Solutions
│
├── src/
│ └── main.cpp # Código C++ para ESP32
│
├── python/
│ ├── banco_dados.py # Script Python para banco SQL (CRUD)
│ ├── dashboard.py # Dashboard em Streamlit
│ └── clima_api.py # Integração com API do clima
│
├── imagens/
│ └── circuito_wokwi.png # Imagem do circuito montado
│
└── README.md # Documentação do projeto


---

## 🗃️ Banco de Dados (SQL)

- Tabela: `leituras_sensor`
- Campos: `id`, `timestamp`, `umidade`, `fosforo`, `potassio`, `ph`, `estado_rele`

### Operações CRUD:

- **Create:** Inserção de novas leituras
- **Read:** Consulta por data, intervalo ou status da bomba
- **Update:** Correção de dados simulados
- **Delete:** Remoção de registros antigos/teste

---

## 📊 Dashboard Interativo (Ir Além 1)

- Desenvolvido com **Streamlit**
- Mostra:
  - Gráfico de umidade ao longo do tempo
  - Indicadores de pH e nutrientes
  - Status da bomba
- Permite simulação e atualização dos dados manualmente

---

## ☁️ Integração com API do Clima (Ir Além 2)

- API utilizada: **OpenWeather**
- Requisições feitas via Python
- Exemplo de uso:
  - Se a previsão for de chuva nas próximas horas, o sistema evita acionar a bomba de irrigação
- Dados utilizados:
  - Previsão de chuva, temperatura e umidade externa

---

## 📝 Instruções de Execução

### 1. Montagem e Testes no Wokwi

- Acesse: [https://wokwi.com](https://wokwi.com)
- Importe o circuito do projeto (`.png` incluído)
- Suba o código C++ pelo PlatformIO no VS Code

### 2. Execução do Script Python

```bash
cd python
python3 banco_dados.py
python3 dashboard.py
python3 clima_api.py

📸 Circuito (Wokwi)

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.

📄 Licença
Este projeto está sob a licença MIT.
