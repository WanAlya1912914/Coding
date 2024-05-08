#include <Servo.h>

int servoPin = 10;
float servoAngle;
//int servoAngle2 = 0;
int Pin = A0;

Servo microservo;

void setup() {
  // put your setup code here, to run once:
  pinMode(Pin, A0);
Serial.begin(9600);
microservo.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  servoAngle = 165./1023. * analogRead(Pin);
  microservo.write(servoAngle);
  delay(100);

}
