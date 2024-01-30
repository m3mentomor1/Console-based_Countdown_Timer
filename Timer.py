import time

print("\n========= Countdown Timer =========\n")

while True:
    try:
        time_input = int(input("Enter time in seconds: "))
        if time_input < 0:                                                  
            print("Input must be a positive integer!\n")              
        else:                                                         
            break 
    except:
        print("Invalid input! Try again.\n")


def timer(time_input):

    while time_input:
        minutes = int(time_input / 60) # Calculates the number of minutes
        hours = int(minutes / 60)      # Calculates the number of hours
        seconds = time_input % 60      # Calculates the number of seconds

        time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds) # Time display format
        print(time_format, end='\r')
        
        time_input -= 1     # Decrements the inputted time until it reaches 1
        time.sleep(1)       # 1 second countdown lag
    print("Timer ended!")

timer(time_input)

print("\n===================================\n")

