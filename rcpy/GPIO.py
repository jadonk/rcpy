import rc.gpio as GPIO

# definitions

# direction
IN  = 0
OUT = 1

# edge
EDGE_NONE    = 0
EDGE_RISING  = 1
EDGE_FALLING = 2
EDGE_BOTH    = 3

# input pins
PAUSE_BTN         = 69 	# gpio2.5 P8.9
MODE_BTN          = 68	# gpio2.4 P8.10
IMU_INTERRUPT_PIN = 117 # gpio3.21 P9.25

# gpio output pins 
RED_LED     = 66 # gpio2.2  P8.7
GRN_LED     = 67 # gpio2.3  P8.8
MDIR1A      = 60 # gpio1.28 P9.12
MDIR1A_BLUE = 64 # gpio2.0 pin T13
MDIR1B      = 31 # gpio0.31 P9.13
MDIR2A      = 48 # gpio1.16 P9.15
MDIR2B      = 81 # gpio2.17 P8.34
MDIR2B_BLUE = 10 # gpio0.10 P8_31
MDIR4A      = 70 # gpio2.6  P8.45
MDIR4B      = 71 # gpio2.7  P8.46
MDIR3B      = 72 # gpio2.8  P8.43
MDIR3A      = 73 # gpio2.9  P8.44
MOT_STBY    = 20 # gpio0.20 P9.41
DSM_PIN     = 30 # gpio0.30 P9.11
SERVO_PWR   = 80 # gpio2.16 P8.36

SPI1_SS1_GPIO_PIN = 113 # gpio3.17	P9.28 
SPI1_SS2_GPIO_PIN = 49  # gpio1.17	P9.23 

# BB Blue GPIO OUT
BLUE_GP0_PIN_4 = 49 #  gpio 1_17 pin P9.23

# Battery Indicator LEDs
BATT_LED_1 = 27      #  P8.17
BATT_LED_2 = 65      #  P8.18
BATT_LED_2_BLUE = 11 #  different on BB Blue
BATT_LED_3 = 61      #  P8.26
BATT_LED_4 = 26      #  P8.14
