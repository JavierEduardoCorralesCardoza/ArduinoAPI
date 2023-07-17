//define pin numbers
int trigPin = D7;
int echoPin = D6;
int RLED = D4;
int GLED = D3;
int YLED = D2;
int BLED = D1;

 //define variables
 long duration1, duration2, distance1, distance2, dif;

void setup() {
  long duration1, duration2, distance1, distance2, dif;
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(RLED, OUTPUT);
  pinMode(GLED, OUTPUT);
  pinMode(YLED, OUTPUT);
  pinMode(BLED, OUTPUT);
  digitalWrite(RLED, LOW);
  digitalWrite(GLED, LOW);
  digitalWrite(YLED, LOW);
  digitalWrite(BLED, LOW);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    digitalWrite(RLED, HIGH);
    delay(500);
    digitalWrite(RLED, LOW);
    delay(500);
    digitalWrite(RLED, HIGH);
    delay(500);
    digitalWrite(RLED, LOW);
    delay(500);
    digitalWrite(GLED, HIGH);
    delay(1000);
    digitalWrite(GLED, LOW);
    delay(500);
    digitalWrite(YLED, HIGH);
    delay(2000);
    
    digitalWrite(trigPin, LOW);        // Nos aseguramos de que el trigger está desactivado
    delayMicroseconds(2);              // Para asegurarnos de que el trigger está LOW
    digitalWrite(trigPin, HIGH);       // Activamos el pulso de salida
    delayMicroseconds(100);             // Esperamos 10µs. El pulso sigue active este tiempo
    digitalWrite(trigPin, LOW);        // Cortamos el pulso y a esperar el ECHO

    duration1 = pulseIn(echoPin, HIGH);

    distance1 = (duration1/2)/29.1;
    Serial.print(distance1);
    Serial.print("cm\n");
    delay(100);

    Serial.print("Distance Sensor 1: ");
    Serial.print(distance1);
    Serial.print("\n\n");

    delay(3000);
    digitalWrite(YLED, LOW);

    
    digitalWrite(RLED, HIGH);
    delay(500);
    digitalWrite(RLED, LOW);
    delay(500);
    digitalWrite(RLED, HIGH);
    delay(500);
    digitalWrite(RLED, LOW);
    delay(500);
    digitalWrite(GLED, HIGH);
    delay(1000);
    digitalWrite(GLED, LOW);
    delay(500);
    digitalWrite(BLED, HIGH);
    delay(2000);

    digitalWrite(trigPin, LOW);        // Nos aseguramos de que el trigger está desactivado
    delayMicroseconds(2);              // Para asegurarnos de que el trigger está LOW
    digitalWrite(trigPin, HIGH);       // Activamos el pulso de salida
    delayMicroseconds(100);             // Esperamos 10µs. El pulso sigue active este tiempo
    digitalWrite(trigPin, LOW);        // Cortamos el pulso y a esperar el ECHO

    duration2 = pulseIn(echoPin, HIGH);

    distance2 = (duration2/2)/29.1;
    Serial.print(distance2);
    Serial.print("cm\n");
    delay(100);

    Serial.print("Distance Sensor 2: ");
    Serial.print(distance2);
    Serial.print("\n\n");

    delay(3000);
    digitalWrite(BLED, LOW);

    //xd
    dif = abs(distance1-distance2);
    Serial.print(dif);
    Serial.print("cm\n");
    delay(100);

    Serial.print("Distance difference: ");
    Serial.print(dif);
    Serial.print("\n\n");
    
    if (dif > 5){
      digitalWrite (RLED , HIGH);     //Si el sensor detecta una distancia menor a 20 cm enciende el LED Rojo
      digitalWrite (GLED , LOW);      // y apaga los demás
      digitalWrite (YLED , LOW);  
      digitalWrite (BLED , LOW);
      delay(5000);  
    }
    else{       // de lo contrario
      digitalWrite (GLED , HIGH);     //Enciende el LED Verde
      digitalWrite (RLED , LOW);      // y apaga los demás
      digitalWrite (YLED , LOW);  
      digitalWrite (BLED , LOW);
      delay(5000);
    }

    digitalWrite(RLED, LOW);
    digitalWrite(GLED, LOW);
    digitalWrite(YLED, LOW);
    digitalWrite(BLED, LOW);
    delay(6000);
}
