int readPin = A0;
//float v2 = 0;
int readvalue;

void setup() 
{
  pinMode(readPin, INPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

void loop() 
{
  readvalue = analogRead(readPin);

  if(readvalue<512)
  {
    digitalWrite(10, LOW);
    digitalWrite(11, HIGH);
    Serial.print(readvalue);
    Serial.println("lEFT");
  }

  else
  {
    digitalWrite(10, HIGH);
    digitalWrite(11, LOW);
    Serial.print(readvalue);
    Serial.println("RIGHT");
  }

  delay(500);



}
