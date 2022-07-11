// Declarando os pinos
const int PINO_LED_R = 11;  // Vermelho
const int PINO_LED_G = 10;  // Verde
const int PINO_LED_B = 9; // Azul

void setup() {
  // Configurando os pinos como saida
  pinMode(PINO_LED_R, OUTPUT); // LED vermelho
  pinMode(PINO_LED_G, OUTPUT); // LED verde
  pinMode(PINO_LED_B, OUTPUT); // LED azul
}

void loop() {
  digitalWrite(PINO_LED_R, HIGH); 
  digitalWrite(PINO_LED_G, LOW); 
  digitalWrite(PINO_LED_B, LOW);  
  delay(2000);                    
  digitalWrite(PINO_LED_R, LOW);  
  delay(2000);                    

  digitalWrite(PINO_LED_R, LOW);  
  digitalWrite(PINO_LED_G, HIGH); 
  digitalWrite(PINO_LED_B, LOW);  
  delay(2000);                    
  digitalWrite(PINO_LED_G, LOW);  
  delay(2000);                    

  digitalWrite(PINO_LED_R, LOW);  // Desliga LED vermelho
  digitalWrite(PINO_LED_G, LOW);  // Desliga LED verde
  digitalWrite(PINO_LED_B, HIGH); // Liga LED azul
  delay(2000);                    // Deixando 2 segundos para ligar proximo LED
  digitalWrite(PINO_LED_B, LOW);  // Desliga LED azul
  delay(2000);                    // Espera 2 segundos para voltar ao  LED vermelho

  digitalWrite(PINO_LED_R, HIGH); // Liga LED vermelho
  digitalWrite(PINO_LED_G, LOW);  // Desliga LED verde
  digitalWrite(PINO_LED_B, HIGH); // Liga LED azul
  delay(2000);                    // Deixando 2 segundos para ligar proximo LED
  digitalWrite(PINO_LED_R, LOW);  // Desliga LED vermelho
  digitalWrite(PINO_LED_B, LOW);  // Desliga LED azul
  delay(2000);                    // Espera dois segundos para voltar ao vermelho
}
