unsigned long time_now = 0;
char comando;
const int SensorPin = A0 , RefPin = A2;
const int Rshunt = 33 ;
double rawSquaredSum = 0;
double Iant = 0;
double freq = 50 ;
double n_trafo = 1000;
double Irms = 0;
int count_integral = 0;
unsigned long time_ant = 0, difTime = 0, act_time = 0;
const int sampleDuration = 500;
double n_turns = 4;


// Configure the relay digital pin, and the serial port interface
void setup() 
{
  // Initialize the relay digital pin as an output. If the student doesn't have the Smart Plug, use the LED_BUILTIN = 13
  pinMode(13, OUTPUT);
  
  // Start serial port at a baudrate of 9600 bps
  Serial.begin(9600);
}

// Loop function
void loop()
{

    // First: check if there is any command from the computer to control the relay
    if (Serial.available() > 0)
    {
        // Read the message from the serial port
        comando = Serial.read();
        // If the message, correspond to the command 'H' or 'L', change the state of the output pin
        if (comando == 'H') {
            digitalWrite(13, HIGH);     // Turn the relay on       
        }
        else if (comando == 'L') {
            digitalWrite(13, LOW);      // Turn the relay off
        }
    }

    act_time = micros();
    difTime = act_time - time_ant;
    int RawValue = 0;

    if (difTime >= 1000) {
      time_ant = act_time + (difTime - 1000);
    
      double ADC_sensor = analogRead(A0);
      double ADC_ref = analogRead(A2);
      double V_sens = ADC_sensor*5/1023;
      double V_ref = ADC_ref*5.0/1023;
      double Iinst =  n_trafo * (V_sens - V_ref) / Rshunt;
      rawSquaredSum += Iinst * Iinst * 0.001;
      count_integral++;
      }
      if (count_integral >= sampleDuration) {
        Irms = sqrt(freq * rawSquaredSum);
        Serial.println(Irms/n_turns);
        count_integral = 0;
        rawSquaredSum = 0;

      }
   
    }  
