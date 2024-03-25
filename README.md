Overview:
This python script runs on the Raspberry Pi Pico W using the CircuitPython bootloader. The adafruit_ahtx0 library must be installed in the lib folder on the RPi Pico for this to work. 

The script work for both the AHT20 and the AHT10 Temperature & Humidity Sensors
These sensors communicate through I2c.
 
Wiring:
Physical pins 6 and 7 are GP4 and GP5 respectively. These are the default I2c connections. GP4 is SDA and GP5 is SCL. You can modify the script and the change GP pins to match your use case.

RPi Pico	              AHTx0
Pin   GP      name	   Pin   
  6        4        SDA       ->   SDA
  7        5        SCL        ->   SCL
36     N/A    3V3out ->  VCC
38     N/A    GND      -> GND


This project was supported by the Arkansas INBRE program, with a grant from the National Institute of General Medical Sciences, (NIGMS), P20 GM103429 from the National Institutes of Health.

In conjunction with Bob Belford in the IoST lab, Information Science - CSTEM, UA Little Rock.
