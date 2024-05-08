#include <Servo.h>

int servoPin = 10;
float servoAngle;
int Sensor = A5;
int Pin = A0;
int readvalue;

Servo microservo;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(Pin, INPUT);
  pinMode(Sensor, INPUT);
  Serial.begin(9600);
  microservo.attach(servoPin);
}

void loop() 
{
  // put your main code here, to run repeatedly:
  readvalue = analogRead(A5);
  if(readvalue < 300)
  {
    microservo.write(0);
  }

  else
  {
    microservo.write(90);
  }
  
}
