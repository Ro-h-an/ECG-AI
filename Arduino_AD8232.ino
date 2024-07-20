void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud rate
  pinMode(A0, INPUT); // AD8232 Output connected to Analog Pin 0
}

void loop() {
  int sensorValue = analogRead(A0); // Read the analog value from AD8232
  Serial.println(sensorValue); // Print the value to the serial monitor
  delay(1); // Small delay for stability
}