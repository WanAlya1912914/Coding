int buzzer = 11;

void setup() 
{
  pinMode(buzzer, OUTPUT);
}

void loop() 
{
  tone(buzzer, 2000);
  delay(100);
  noTone(buzzer);
  delay(500);
}
