# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP" width="40%">
  </a>
</p>


<br>

# 🌱 FarmTech Solutions - Sistema de Irrigação Inteligente
## 👨‍🎓 Integrantes: 
- Vitor Eiji Fernandes Teruia
- Beatriz Pilecarte de Melo 
- Francismar Alves Martins Junior  
- Antônio Ancelmo Neto barros  
- Matheus Soares Bento da Silva 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusc">ANDRÉ GODOI CHIOVATO</a>


## 📜 Descrição

Este projeto simula um sistema de irrigação inteligente com sensores físicos implementados na plataforma Wokwi, 
utilizando um microcontrolador ESP32. O sistema coleta dados simulados de umidade do solo, nutrientes (fósforo e potássio) e pH,
controlando uma bomba de irrigação automaticamente e armazenando os dados em um banco de dados SQL via script Python.
Também há funcionalidades extras de visualização via dashboard e integração com dados climáticos reais por meio de uma API pública.

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

## imagens dos circuitos

### Sensor de Umidade
<img src="assets/imagens_dos_circuitos/imagens/captura-umidade.png" alt="Sensor de umidade" width="300">

### Sensor de Fósforo
<img src="assets/imagens_dos_circuitos/imagens/sensor_fosforo.png" alt="Sensor de fósforo" width="300">

### Sensor de pH
<img src="assets/imagens_dos_circuitos/imagens/sensor_ph.png" alt="Sensor de pH" width="300">

### Sensor de Potássio
<img src="assets/imagens_dos_circuitos/imagens/sensor_potassio.png" alt="Sensor de potássio" width="300">

### sensor solo
<img src="assets/imagens_dos_circuitos/imagens/sensor_solo.png" alt="Sensor solo" width="300">


---


## 📁 Estrutura de pastas
```
Sistema-de-Irrigacao-Inteligente-com-Sensores
├── pycache/ # Arquivos compilados automaticamente pelo Python
├── .vscode/ # Configurações do Visual Studio Code
├── imagens_dos_circuitos/ # Imagens utilizadas na documentação ou no projeto
├── sensor_fosforo/ # Código relacionado ao sensor de fósforo
├── sensor_ph/ # Código relacionado ao sensor de pH
├── sensor_potassio/ # Código relacionado ao sensor de potássio
├── sensor_umidade/ # Código relacionado ao sensor de umidade do solo
├── main.py # Script principal do sistema
└── README.md # Documentação do projeto
```
## 🔧 Como executar o código

1. clone o repositório
```bash
git clone https://github.com/seuusuario/Sistema-de-Irrigacao-Inteligente-com-Sensores.git
cd Sistema-de-Irrigacao-Inteligente-com-Sensores
```

2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install fastapi uvicorn
```
4. Execute o servidor FastAPI:
```bash
uvicorn main:app --reload
```
5. Teste a API no navegador ou com uma ferramenta como Postman
```
Após rodar o comando:


uvicorn main:app --reload

A aplicação estará disponível localmente em:

arduino
Copiar código
http://localhost:8000
Você pode testá-la de duas formas:

🔹 No navegador:
Acesse http://localhost:8000/docs
Essa é uma documentação interativa gerada automaticamente, onde você pode testar o endpoint POST /sensor enviando um dado como:

json
Copiar código
{
  "presenca": true
}
🔹 Com o Postman ou curl:
Envie uma requisição POST para:

bash
Copiar código
http://localhost:8000/sensor
Com o corpo da requisição (JSON):

json
Copiar código
{
  "presenca": true
}
```
## 🗃 Histórico de lançamentos

* 0.1.0 - 14/05/2025
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

