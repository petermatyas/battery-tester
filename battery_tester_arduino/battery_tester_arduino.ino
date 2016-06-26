float R = 3.3;
float Ut = 4.68;
#define bata1 A2
#define batd1 2
#define bata2 A3
#define batd2 3

void setup() {
  Serial.begin(9600);
  pinMode(batd1, OUTPUT);
  pinMode(batd2, OUTPUT);
  digitalWrite(batd1, LOW);
  digitalWrite(batd2, LOW);
  //analogReference(INTERNAL);
  
}

void loop() {
  while (Serial.available() > 0) {
    String str = Serial.readStringUntil('\n');
      if (str == "ibat1") {
        ibat1();
      } else if (str == "ibat2") {
        ibat2();     
      } else if (str == "ubat1") {
        ubat1();
      } else if (str == "ubat2") {
        ubat2() ;
      } else if (str == "r1") {
        r1();
      } else if (str == "r2") {
        r2();        
      } else if (str == "loadon1") {
        digitalWrite(batd1, HIGH);
      } else if (str == "loadon2") {
        digitalWrite(batd2, HIGH);  
      } else if (str == "loadonall") {
        digitalWrite(batd1, HIGH);      
        digitalWrite(batd2, HIGH);   
      } else if (str == "loadoff1") {
        digitalWrite(batd1, LOW);
      } else if (str == "loadoff2") {
        digitalWrite(batd2, LOW);
      } else if (str == "loadoffall") {
        digitalWrite(batd1, LOW);
        digitalWrite(batd2, LOW);
      } else if (str == "status") {
        Serial.print("OK");          
      }
      str = "";
    }
}

void ibat1() {
    digitalWrite(batd1, HIGH);
    delay(100);
    int adcout = analogRead(bata1); 
    //delay(100);
    digitalWrite(batd1, LOW);
    float u = Ut * adcout / 1024;
    float i = u / R;
    //Serial.print("current [A]: ");
    Serial.println(i,5);  
  }

void ibat2() {
    digitalWrite(batd2, HIGH);
    delay(100);
    int adcout = analogRead(bata2); 
    delay(100);
    //digitalWrite(batd2, LOW);
    float u = Ut * adcout / 1024;
    float i = u / R;
    //Serial.print("current [A]: ");
    Serial.println(i,5);   
  
  }

void ubat1() {
      digitalWrite(batd1, LOW);
      delay(100);
      int adcout = analogRead(bata1); 
      float u = Ut * adcout / 1024;
      //Serial.print("adcout [V]: ");
      Serial.println(u,5);
  }

 void ubat2() {
      digitalWrite(batd2, LOW);
      delay(100);
      int adcout = analogRead(bata2); 
      float u = Ut * adcout / 1024;
      //Serial.print("adcout [V]: ");
      Serial.println(u,5);  
  }

void r1() {
      digitalWrite(batd1, LOW);
      delay(100);
      int adcout = analogRead(bata1); 
      float ue = Ut * adcout / 1024;
      digitalWrite(batd1, HIGH);
      delay(100);
      adcout = analogRead(bata1); 
      delay(100);
      float ub = Ut * adcout / 1024;
      digitalWrite(batd1, LOW);
      float r = R * ((ue / ub) - 1);
      if (ub == 0) {
        r = 0;
        }
      Serial.println(r,5); 
  }

void r2() {
      digitalWrite(batd2, LOW);
      delay(100);
      int adcout = analogRead(bata2); 
      float ue = Ut * adcout / 1024;
      digitalWrite(batd2, HIGH);
      delay(100);
      adcout = analogRead(bata2); 
      delay(100);
      float ub = Ut * adcout / 1024;
      digitalWrite(batd2, LOW);
      float r = R * ((ue / ub) - 1);
      Serial.println(r,5);
  }
  
