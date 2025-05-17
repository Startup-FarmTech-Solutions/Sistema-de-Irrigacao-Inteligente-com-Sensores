#include <WiFi.h>
#include <WiFiClient.h>
#include <ArduinoJson.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

// Definições dos pinos
#define DHTPIN 13
#define DHTTYPE DHT22
#define PINO_POTASSIO 18
#define LIGHT_SENSOR_PIN 36
#define PINO_FOSFORO 22
#define RELE_PIN 4
#define IRRIGACAO_ATIVA HIGH
#define IRRIGACAO_INATIVA LOW

// Configurações da rede Wi-Fi (Wokwi)
const char *ssid = "Wokwi-GUEST";     // Nome da rede Wi-Fi do Wokwi
const char *password = "";           // Senha da rede Wi-Fi do Wokwi

// Configurações do servidor Python
const char *serverHost = "127.0.0.1"; // Endereço IP do servidor (no Wokwi)
const int serverPort = 12345;         // Porta do servidor Python

// Variáveis globais
WiFiClient client;
LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHTTYPE);
int potassioPresente = 0;
int fosforoPresente = 0;
int leituraLDR_inicial = 0;
float pH = 7.0;
float pH_display = 7.0;
float temperatura_display = 0.0;
float humidity_display = 0.0;
bool leituraRealizada = false;
unsigned long lastReadTime = 0;
const unsigned long readInterval = 2000;

// Calibração do sensor de pH (LDR) - Ajuste esses valores conforme seu LDR no Wokwi
const int ldrMin = 100; // Valor LDR em alta luminosidade (pH alto/baixo) - Ajuste!
const int ldrMax = 900; // Valor LDR em baixa luminosidade (pH baixo/alto) - Ajuste!

// Funções auxiliares
float mapearPH(int ldrValue) {
  return map(ldrValue, ldrMax, ldrMin, 0, 14);
}

String categorizarPH(float phValue) {
  if (phValue < 6.5) {
    return "Acido";
  } else if (phValue > 7.5) {
    return "Alcalino";
  } else {
    return "Neutro";
  }
}

void setup() {
  // Inicializa a serial
  Serial.begin(115200);
  delay(1000);

  // Inicializa o LCD
  dht.begin();
  lcd.init();
  lcd.backlight();
  lcd.setCursor(2, 0);
  lcd.print("HELLO EVERYONE!");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Medidor de");
  lcd.setCursor(0, 1);
  lcd.print("Parametros Solo");
  delay(2000);
  lcd.clear();

  // Inicializa o gerador de números aleatórios
  randomSeed(micros());

  // Configura os pinos dos botões e do relé
  pinMode(PINO_POTASSIO, INPUT_PULLUP);
  pinMode(PINO_FOSFORO, INPUT_PULLUP);
  pinMode(RELE_PIN, OUTPUT);
  digitalWrite(RELE_PIN, IRRIGACAO_INATIVA);
  lastReadTime = millis();

  // Conecta ao Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("Conectado ao Wi-Fi");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());

  // Conecta ao servidor Python
  Serial.print("Conectando ao servidor Python em ");
  Serial.print(serverHost);
  Serial.print(":");
  Serial.println(serverPort);
  if (client.connect(serverHost, serverPort)) {
    Serial.println("Conectado ao servidor Python");
  } else {
    Serial.print("Falha ao conectar ao servidor Python. Status do WiFi: ");
    Serial.println(WiFi.status());
    lcd.clear();
    lcd.print("Erro de conexao");
    while (1); // Aguarda aqui
  }

    // Lê os dados dos sensores
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    // Adiciona uma pequena variação aos valores
    float humidity_variation = random(-10, 10) / 10.0;
    float temperature_variation = random(-5, 5) / 10.0;
    float temperature_display = temperature + temperature_variation;
    float humidity_display = humidity + humidity_variation;

    // Lê o valor de pH
    leituraLDR_inicial = analogRead(LIGHT_SENSOR_PIN);
    pH = mapearPH(leituraLDR_inicial);
    float pH_variation = random(-20, 20) / 10.0;
    pH_display = constrain(pH + pH_variation, 0.0, 14.0);
    String categoriaPH_atual = categorizarPH(pH_display);

    // Atualiza o estado dos nutrientes
    potassioPresente = (digitalRead(PINO_POTASSIO) == LOW) ? 1 : 0;
    fosforoPresente = (digitalRead(PINO_FOSFORO) == LOW) ? 1 : 0;

    // Cria um objeto JSON para enviar os dados
    StaticJsonDocument<256> doc;  // Ajuste o tamanho conforme necessário
    doc["temperatura"] = temperature_display;
    doc["umidade"] = humidity_display;
    doc["pH"] = pH_display;
    doc["categoria_pH"] = categoriaPH_atual;
    doc["potassio"] = potassioPresente;
    doc["fosforo"] = fosforoPresente;
    doc["irrigacao"] = false; // A irrigação começa desligada, certo?
    
    // Envia os dados JSON para o servidor Python
    char jsonBuffer[256];
    serializeJson(doc, jsonBuffer);
    client.println(jsonBuffer);
    Serial.println("Dados JSON enviados:");
    Serial.println(jsonBuffer);

    // Exibe os dados no LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(temperature_display, 1);
    lcd.print("C U:");
    lcd.print(humidity_display, 1);
    lcd.print("%");
    lcd.setCursor(0, 1);
    lcd.print("pH:");
    lcd.print(pH_display, 1);
    lcd.print(" OFF"); //Começa com a irrigação OFF
}

void loop() {
  // Lê o estado dos botões
  int leituraBotaoP = digitalRead(PINO_POTASSIO);
  int leituraBotaoF = digitalRead(PINO_FOSFORO);

  // Lógica de controle da irrigação
  bool irrigar = false;
  if (humidity_display < 40.0 || pH_display < 6.0 || pH_display > 8.0 || potassioPresente == 0 || fosforoPresente == 0) {
    irrigar = true;
  } else if (humidity_display > 60.0 && pH_display >= 6.5 && pH_display <= 7.5 && potassioPresente == 1 && fosforoPresente == 1) {
    irrigar = false;
  }

  // Controla o relé
  digitalWrite(RELE_PIN, irrigar ? IRRIGACAO_ATIVA : IRRIGACAO_INATIVA);

  if (leituraBotaoP == LOW || leituraBotaoF == LOW) {
    leituraRealizada = true;
    // Lê os dados dos sensores
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    // Adiciona uma pequena variação aos valores
    float humidity_variation = random(-10, 10) / 10.0;
    float temperature_variation = random(-5, 5) / 10.0;
    float temperature_display = temperature + temperature_variation;
    float humidity_display = humidity + humidity_variation;

    // Lê o valor de pH
    leituraLDR_inicial = analogRead(LIGHT_SENSOR_PIN);
    pH = mapearPH(leituraLDR_inicial);
    float pH_variation = random(-20, 20) / 10.0;
    pH_display = constrain(pH + pH_variation, 0.0, 14.0);
    String categoriaPH_atual = categorizarPH(pH_display);
    
    potassioPresente = (leituraBotaoP == LOW) ? 1 : 0;
    fosforoPresente = (leituraBotaoF == LOW) ? 1 : 0;

    // Cria um objeto JSON para enviar os dados
    StaticJsonDocument<256> doc;  // Ajuste o tamanho conforme necessário
    doc["temperatura"] = temperature_display;
    doc["umidade"] = humidity_display;
    doc["pH"] = pH_display;
    doc["categoria_pH"] = categoriaPH_atual;
    doc["potassio"] = potassioPresente;
    doc["fosforo"] = fosforoPresente;
    doc["irrigacao"] = irrigar;

    // Envia os dados JSON para o servidor Python
    char jsonBuffer[256];
    serializeJson(doc, jsonBuffer);
    client.println(jsonBuffer); // Envia para o servidor Python
    Serial.println("Dados JSON enviados:");
    Serial.println(jsonBuffer);

    Serial.println("\n--- Leitura dos Sensores ---");
    Serial.print("pH: ");
    Serial.print(pH_display, 1);
    Serial.print(" (");
    Serial.print(categorizarPH(pH_display));
    Serial.println(")");
    Serial.print("Potássio Detectado: ");
    Serial.println(potassioPresente ? "Sim" : "Não");
    Serial.print("Fósforo Detectado: ");
    Serial.println(fosforoPresente ? "Sim" : "Não");
    Serial.printf("Irrigacao: %s\n", irrigar ? "ATIVA" : "INATIVA");
    Serial.println("--------------------------");

    // Exibe os dados no LCD
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("T:");
    lcd.print(temperature_display, 1);
    lcd.print("C U:");
    lcd.print(humidity_display, 1);
    lcd.print("%");
    lcd.setCursor(0, 1);
    lcd.print("pH:");
    lcd.print(pH_display, 1);
    lcd.print(irrigar ? " ON" : " OFF"); // Indica o status da irrigação no LCD
    delay(1000);
  } else if (leituraRealizada) {
    // Mantém a última leitura no LCD
    lcd.setCursor(0, 1);
    lcd.print(" (");
    lcd.print(categorizarPH(pH_display));
    lcd.print(")");
    lcd.print(irrigar ? " ON" : " OFF"); // Indica o status da irrigação no LCD
    delay(200);
  } else {
    // Mantém a tela inicial
    delay(200);
  }
}