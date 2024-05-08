int trigPin = 5;
int echoPin = 6;
int pingTravelTime;
float distance;

void setup() 
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  Serial.begin(9600);
}

void loop() 
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  pingTravelTime = pulseIn(echoPin, HIGH);
  distance = pingTravelTime * 343.0/2/1000;

  Serial.print(pingTravelTime);
  Serial.print(" ");
  Serial.println(distance);

  delay(500);

  

}
