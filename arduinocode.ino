int ledPin=7;
char receivedChar;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
}

void loop() {
 if (Serial.available() > 0) {
    receivedChar = Serial.read();
    if (receivedChar == '1') {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED is ON");
    } else if (receivedChar == '0') {
      digitalWrite(ledPin, LOW);
      Serial.println("LED is OFF");
    }
  }
}
