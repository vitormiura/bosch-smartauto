int counter = 0;

void setup(){
  pinMode(13, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  Serial.println(digitalRead(13));

  int toggle = digitalRead(13);
  
  if (toggle == 1){
    digitalWrite(11, HIGH);
    counter = counter + 1;
  }
  
}
