// Definindo o pino do botão
#define PINO_POTASSIO 18

// Variável para armazenar a leitura do botão
int potassioPresente = 0;

void setup() {
  // Inicializa a comunicação serial
  Serial.begin(115200);

  // Define o pino como entrada com resistor pull-up interno
  pinMode(PINO_POTASSIO, INPUT_PULLUP);
}

void loop() {
  // Lê o estado do botão
  int leituraBotao = digitalRead(PINO_POTASSIO);

  // Como usamos INPUT_PULLUP: pressionado = LOW, solto = HIGH
  // Vamos inverter a lógica para facilitar
  potassioPresente = (leituraBotao == LOW) ? 1 : 0;

  // Mostra no Serial Monitor
  if (potassioPresente) {
    Serial.println("Potassio Detectado!");
  } else {
    Serial.println("Sem Potassio.");
  }

  // Pequena pausa para não inundar o serial
  delay(500);
}
