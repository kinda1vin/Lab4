import time
from hal import hal_input_switch as switch
from hal import hal_led as led

def main():
    # Initialize the switch and LED
    switch.init()
    led.init()
    
    while True:
        if switch.read_slide_switch():  # Switch is active (left position)
            # Blink LED at 5 Hz
            led.set_output(0, 1)  # Turn LED on
            time.sleep(0.1)       # 5 Hz half-period
            led.set_output(0, 0)  
            time.sleep(0.1)       
        else:
            start_time = time.time()  # Record the start time
            while (time.time() - start_time) < 5:  # Run for 5 seconds
                led.set_output(0, 1)  
                time.sleep(0.05)      
                led.set_output(0, 0) 
                time.sleep(0.05)      
            led.set_output(0, 0)  # Ensure the LED is off after the loop
            time.sleep(5)

if __name__ == "__main__":
    main()