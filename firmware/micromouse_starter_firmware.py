#include <Arduino.h>
#include <Wire.h>

#define LSM6DS3_ADDR 0x6B

#define M_L_PWM PA11
#define M_R_PWM PA12

#define M_L_IN1 PB12
#define M_L_IN2 PB13
#define M_R_IN1 PB14
#define M_R_IN2 PB15

#define M_STBY  PA_10

#define IR_1 PA_0
#define IR_2 PA_1
#define IR_3 PA_2
#define IR_4 PA3
#define IR_5 PA4
#define IR_6 PA5

#define LED_MOSFET_1 PA6
#define LED_MOSFET_2 PA7
#define LED_MOSFET_3 PB_0
#define LED_MOSFET_4 PB_1
#define LED_MOSFET_5 PB_2
#define LED_MOSFET_6 PB10

const int FRONT_THRESHOLD = 600;
const int SIDE_THRESHOLD  = 400;

int16_t gyroZ_raw = 0;
float gyroZ_offset = 0;
float current_angle = 0;
unsigned long prev_time = 0;

int ir_val[6];

void setMotors(int left_pwm, int right_pwm) {
  if (left_pwm >= 0) {
    digitalWrite(M_L_IN1, HIGH);
    digitalWrite(M_L_IN2, LOW);
    analogWrite(M_L_PWM, constrain(left_pwm, 0, 255));
  } else {
    digitalWrite(M_L_IN1, LOW);
    digitalWrite(M_L_IN2, HIGH);
    analogWrite(M_L_PWM, constrain(-left_pwm, 0, 255));
  }

  if (right_pwm >= 0) {
    digitalWrite(M_R_IN1, HIGH);
    digitalWrite(M_R_IN2, LOW);
    analogWrite(M_R_PWM, constrain(right_pwm, 0, 255));
  } else {
    digitalWrite(M_R_IN1, LOW);
    digitalWrite(M_R_IN2, HIGH);
    analogWrite(M_R_PWM, constrain(-right_pwm, 0, 255));
  }
}

void stopMotors() {
  analogWrite(M_L_PWM, 0);
  analogWrite(M_R_PWM, 0);
  digitalWrite(M_L_IN1, LOW);
  digitalWrite(M_L_IN2, LOW);
  digitalWrite(M_R_IN1, LOW);
  digitalWrite(M_R_IN2, LOW);
}

void readGyro() {
  Wire.beginTransmission(LSM6DS3_ADDR);
  Wire.write(0x22);
  Wire.endTransmission(false);
  Wire.requestFrom((uint8_t)LSM6DS3_ADDR, (size_t)2, true);

  if (Wire.available() >= 2) {
    uint8_t lsb = Wire.read();
    uint8_t msb = Wire.read();
    gyroZ_raw = (int16_t)((msb << 8) | lsb);
  }

  unsigned long now = micros();
  float dt = (now - prev_time) / 1000000.0;
  prev_time = now;

  float gyroZ_dps = (gyroZ_raw - gyroZ_offset) * 0.070;
  
  if (abs(gyroZ_dps) > 0.5) { 
    current_angle += gyroZ_dps * dt;
  }
}

void calibrateGyro() {
  long sum = 0;
  int valid_samples = 0;
  
  for (int i = 0; i < 500; i++) {
    Wire.beginTransmission(LSM6DS3_ADDR);
    Wire.write(0x22);
    Wire.endTransmission(false);
    Wire.requestFrom((uint8_t)LSM6DS3_ADDR, (size_t)2, true);
    if (Wire.available() >= 2) {
      uint8_t lsb = Wire.read();
      uint8_t msb = Wire.read();
      sum += (int16_t)((msb << 8) | lsb);
      valid_samples++;
    }
    delay(2);
  }
  if (valid_samples > 0) {
    gyroZ_offset = (float)sum / valid_samples;
  }
}

void turnDegrees(float target_deg, int speed) {
  current_angle = 0;
  prev_time = micros();

  if (target_deg > 0) {
    setMotors(speed, -speed);
    while (current_angle < target_deg) {
      readGyro();
      delayMicroseconds(500);
    }
  } else {
    setMotors(-speed, speed);
    while (current_angle > target_deg) {
      readGyro();
      delayMicroseconds(500);
    }
  }
  stopMotors();
}

void turnLeft90(int speed) {
  turnDegrees(-90.0, speed);
}

void turnRight90(int speed) {
  turnDegrees(90.0, speed);
}

void turn180(int speed) {
  turnDegrees(180.0, speed);
}

void readSensors() {
  ir_val[0] = analogRead(IR_1);
  ir_val[1] = analogRead(IR_2);
  ir_val[2] = analogRead(IR_3);
  ir_val[3] = analogRead(IR_4);
  ir_val[4] = analogRead(IR_5);
  ir_val[5] = analogRead(IR_6);
}

void setup() {
  pinMode(M_L_PWM, OUTPUT);
  pinMode(M_R_PWM, OUTPUT);
  pinMode(M_L_IN1, OUTPUT);
  pinMode(M_L_IN2, OUTPUT);
  pinMode(M_R_IN1, OUTPUT);
  pinMode(M_R_IN2, OUTPUT);
  pinMode(M_STBY, OUTPUT);

  digitalWrite(M_STBY, HIGH);

  pinMode(LED_MOSFET_1, OUTPUT);
  pinMode(LED_MOSFET_2, OUTPUT);
  pinMode(LED_MOSFET_3, OUTPUT);
  pinMode(LED_MOSFET_4, OUTPUT);
  pinMode(LED_MOSFET_5, OUTPUT);
  pinMode(LED_MOSFET_6, OUTPUT);

  digitalWrite(LED_MOSFET_1, HIGH);
  digitalWrite(LED_MOSFET_2, HIGH);
  digitalWrite(LED_MOSFET_3, HIGH);
  digitalWrite(LED_MOSFET_4, HIGH);
  digitalWrite(LED_MOSFET_5, HIGH);
  digitalWrite(LED_MOSFET_6, HIGH);

  pinMode(IR_1, INPUT);
  pinMode(IR_2, INPUT);
  pinMode(IR_3, INPUT);
  pinMode(IR_4, INPUT);
  pinMode(IR_5, INPUT);
  pinMode(IR_6, INPUT);

  Wire.setSCL(PB6);
  Wire.setSDA(PB7);
  Wire.begin();
  delay(100); 

  Wire.beginTransmission(LSM6DS3_ADDR);
  Wire.write(0x11);
  Wire.write(0x8C); 
  Wire.endTransmission(true);

  calibrateGyro();
  prev_time = micros();
}

void loop() {
  readSensors();
  readGyro();

  if (ir_val[2] > FRONT_THRESHOLD || ir_val[3] > FRONT_THRESHOLD) {
    if (ir_val[0] < SIDE_THRESHOLD && ir_val[1] < SIDE_THRESHOLD) {
      turnLeft90(120);
    } else if (ir_val[4] < SIDE_THRESHOLD && ir_val[5] < SIDE_THRESHOLD) {
      turnRight90(120);
    } else {
      turn180(120);
    }
  } else {
    setMotors(120, 120);
  }

  delay(5);
}
