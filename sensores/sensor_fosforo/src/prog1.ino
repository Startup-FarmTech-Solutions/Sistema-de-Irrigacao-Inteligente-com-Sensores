#include <SPI.h>
#include <SD.h>

File dataFile;

void setup() {
  // Inicializa a comunicação serial com o computador
  Serial.begin(115200);

  // Inicializa o cartão SD. O pino CS do cartão SD está no pino 5
  if (!SD.begin(5)) {
    Serial.println("Falha ao inicializar o cartão SD.");
    return;
  }

  // Tenta abrir o arquivo "data.txt" no cartão SD para escrita
  dataFile = SD.open("data.txt", FILE_WRITE);
  
  if (dataFile) {
    // Se o arquivo foi aberto com sucesso, escreve "Hello, World!" nele
    dataFile.println("Hello, World!");
    dataFile.close();  // Fecha o arquivo após a escrita
    Serial.println("Escrita bem-sucedida no cartão SD.");
  } else {
    Serial.println("Falha ao abrir o arquivo.");
  }
}

void loop() {
  // Nada necessário aqui, pois o código de gravação acontece apenas uma vez no setup
}
