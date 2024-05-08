#include <Stepper.h>
const int spr = 2048;
Stepper stepper (spr, 8, 9, 10, 11);

void setup() 
{
  // put your setup code here, to run once:
  stepper.setSpeed(10);
  Serial.begin(9600);

}

void loop() 
{
  // put your main code here, to run repeatedly:
  stepper.step(spr);
  delay(1000);
  stepper.step(-spr);
  delay(1000);

}
