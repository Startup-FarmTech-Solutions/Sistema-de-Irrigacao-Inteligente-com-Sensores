#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN 13
#define DHTTYPE DHT22

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  dht.begin();
  lcd.init();
  lcd.backlight();

  lcd.setCursor(2, 0);
  lcd.print("HELLO EVERYONE!");
  delay(2000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Medidor de temperatura");
  lcd.setCursor(0, 1);
  lcd.print("e umidade");
  delay(3000);
  lcd.clear();

  // Inicializa o gerador de números aleatórios com um valor diferente toda vez
  randomSeed(micros());


  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Adiciona pequenas variações aleatórias:
  float humidity_variation = random(-10, 10) / 10.0;   // variação de -1.0% a +1.0%
  float temperature_variation = random(-5, 5) / 10.0;  // variação de -0.5°C a +0.5°C

  float humidity_display = humidity + humidity_variation;
  float temperature_display = temperature + temperature_variation;

  lcd.setCursor(0, 0);
  lcd.print(F("Temperatura : "));
  lcd.print(temperature_display, 1); // Mostra com 1 casa decimal
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print(F("Umidade:"));
  lcd.print(humidity_display, 1); // Mostra com 1 casa decimal
  lcd.print("%");

  delay(1000);
}

void loop(){

}
