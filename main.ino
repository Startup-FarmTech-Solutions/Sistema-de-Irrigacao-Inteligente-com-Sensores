#include <Arduino.h>
#include "controller/sensor_controller.h"

void setup() {
  Serial.begin(115200);
  initAllSensors();
}

void loop() {
  readAllSensors();
  delay(2000);
}
