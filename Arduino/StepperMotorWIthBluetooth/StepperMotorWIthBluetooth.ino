#include <Stepper.h>
const int spr = 40;
Stepper stepper (spr, 8, 9, 10, 11);

String text = "";

void setup() 
{
  // put your setup code here, to run once:
  stepper.setSpeed(10);
  Serial.begin(9600);

}

void loop() 
{
  while (Serial.available())
  {
    delay(10);
    char c = Serial.read();
    text +=c;
  }

  if (text.length () > 0)
  {
    Serial.println(text);
    if (text == "clockwise")
    {stepper.step(spr);}
    if (text == "reverse")
    {stepper.step(-spr);}
    if (text == "stop")
    {stepper.setSpeed(0);}
   
   text="";
  }

}
