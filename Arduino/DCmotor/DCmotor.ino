int Sensor = A0;
int value;
int var;
void setup() 
{
  pinMode(Sensor, INPUT);
  pinMode(6, OUTPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  value = 255./1025. * analogRead(Sensor);
  var = digitalRead(7);
  analogWrite(6, value);
  Serial.println(var);
}
