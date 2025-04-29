#include <HTTPClient.h>

const char* serverName = "http://192.168.0.123:8000/sensor";  // Substitua com o IP real

#define buttonPin 22  // Pino conectado ao botão (sensor)

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);  // Configura o botão como entrada com pull-up interno

  Serial.println("Iniciando...");
}

void loop() {
  int buttonState = digitalRead(buttonPin);  // Lê o estado do botão

  bool presenca = (buttonState == LOW);  // Pressionado = presença detectada
  Serial.print("Presença detectada: ");
  Serial.println(presenca ? "Sim" : "Não");

  HTTPClient http;
  http.begin(serverName);  // Inicia a requisição HTTP

  http.addHeader("Content-Type", "application/json");

  // Criando o corpo JSON para enviar ao servidor
  String json = "{\"presenca\": " + String(presenca ? "true" : "false") + "}";

  // Envia os dados via POST
  int httpResponseCode = http.POST(json);

  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println("Resposta do servidor: " + response);
  } else {
    Serial.print("Erro na requisição: ");
    Serial.println(httpResponseCode);
  }

  http.end();  // Finaliza a requisição HTTP

  delay(10000);  // Aguarda 10 segundos antes da próxima leitura
}
