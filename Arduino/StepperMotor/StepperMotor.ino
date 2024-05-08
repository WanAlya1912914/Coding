int s1 = 8;
int s2 = 9;
int s3 = 10;
int s4 = 11;
int count =0;
int num = 0;

void setup() 
{
  pinMode (s1, OUTPUT);
  pinMode (s2, OUTPUT);
  pinMode (s3, OUTPUT);
  pinMode (s4, OUTPUT);

  Serial.begin(9600);
}

void loop() 
{
  switch(num)
  {
   case 0:
   digitalWrite(s1,HIGH);
   digitalWrite(s2,LOW);
   digitalWrite(s3,LOW);
   digitalWrite(s4,LOW);
   break; 

   case 1:
   digitalWrite(s1,LOW);
   digitalWrite(s2,HIGH);
   digitalWrite(s3,LOW);
   digitalWrite(s4,LOW);
   break;

   case 2:
   digitalWrite(s1,LOW);
   digitalWrite(s2,LOW);
   digitalWrite(s3,HIGH);
   digitalWrite(s4,LOW);
   break;

   case 3:
   digitalWrite(s1,LOW);
   digitalWrite(s2,LOW);
   digitalWrite(s3,LOW);
   digitalWrite(s4,HIGH);
   break;
  }

  num++;

  if(num > 3)
  {
   num = 0;
   count++;
   Serial.println(count); 
  }

  delay(2);
}
