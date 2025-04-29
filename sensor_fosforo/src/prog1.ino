#include <esp32-hal-gpio.h>
#include <HardwareSerial.h>

#define buttonPin 22  // Pino GPIO conectado ao push button

void setup() {
    pinMode(buttonPin, INPUT_PULLUP);  // Configura o pino do botão como entrada com pull-up interno
    Serial.begin(9600);                // Inicia a comunicação serial
}

void loop() {
    int buttonState = digitalRead(buttonPin);  // Lê o estado do botão

    if (buttonState == LOW) {  // O botão está pressionado (pino conectado ao GND)
        Serial.println("presenca");
    } else {  // O botão não está pressionado (pino em estado HIGH)
        Serial.println("ausencia");
    }

    delay(10000);  // Pequeno atraso para evitar ruído de contato (debounce)
}