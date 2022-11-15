#include <Servo.h>


#define END_ANGLE    90 
#define START_ANGLE  0 
#define ENTRY_PIN    9

Servo myservo;
int action;
int pos;

char Action = "d";

typedef enum 
{
  Up_State,
  Down_State,
}Servo_State;

Servo_State State = Down_State;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
myservo.attach(ENTRY_PIN);
}

void loop() {
  // put your main code here, to run repeatedly:

  switch ( State )
  {
    case Down_State:
    {
      for (pos = END_ANGLE; pos >= START_ANGLE; pos -= 1) 
      { 
        myservo.write(pos);             
        delay(15);  
      } 

      while (1)
      {
        Action = Serial.read();
        if (  Action == "0" )
        {
          State = Up_State;
          break;
        }
          
      }
      
    }break;

    case Up_State:
    {

      for (pos = START_ANGLE; pos >= END_ANGLE; pos += 1) 
      { 
        myservo.write(pos);             
        delay(15);  
      } 

      while ( 1 )
      {
        Action = Serial.read();
        if ( Action == "1" )
        {
          State = Down_State;
          break;
        }
          
      }
      
    }break;

    default: 
    {
      // nothing to do
    }
    
  }

}
