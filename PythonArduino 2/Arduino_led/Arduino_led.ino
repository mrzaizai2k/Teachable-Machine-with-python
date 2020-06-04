int datafromUser=0;
int led = 12;
void setup() {
  // put your setup code here, to run once:
  pinMode(led , OUTPUT );
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)
  {
    datafromUser=Serial.read();
  }
  if(datafromUser == '1')
  {
    digitalWrite(led , HIGH );
  }
}
