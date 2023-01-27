void setup() {
  for(int i = 2; i <= 8; i++)
    pinMode(i, OUTPUT);
}

void loop() {
  // CODIGUIM
   for(int i = 2; i <= 8; i++){
    setOn(i);
  }
  for(int i = 8; i >= 2; i--){
    setOn(i);
  }
}

void setOn(int pin){
  digitalWrite(pin, HIGH);
  delay(50);
  digitalWrite(pin, LOW);
  delay(50);
}
