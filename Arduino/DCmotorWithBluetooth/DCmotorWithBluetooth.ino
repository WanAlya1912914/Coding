byte IN1 = 6;
byte IN2 = 7;
byte EN1 = 3;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(EN1, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() == 1)
  {
    byte ctrlPins = Serial.read();
    switch(ctrlPins)
    {
      case 0:
          digitalWrite(IN1, HIGH);
          digitalWrite(IN2, LOW);
          break;

      case 1:
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        break;

      case 2:
          digitalWrite(IN1, LOW);
          digitalWrite(IN2, HIGH);
          break;
    }
  }

  if(Serial.available() == 2)
  {
    int lowerByte = Serial.read();
    int higherByte = Serial.read();
    int value = (higherByte * 256) + lowerByte;
    byte pwmVal = map(value, 1000, 1255, 0, 255);
    analogWrite(EN1, pwmVal);
  }

  delay(50);

}
