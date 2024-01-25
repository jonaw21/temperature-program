# Function to convert Celsius to Fahrenheit.
def temp_F(C: number):
    # Formula for Celsius to Fahrenheit is F = C * 1.8 + 32.
    return 32 + C * 1.8

# Function when button A is pressed to read out the highest temperature recorded.
def on_button_pressed_a():
    global highest_temp
    # Check of the current temperature is higher than the recorded highest temperature.
    if temp_F(input.temperature()) >= highest_temp:
        highest_temp = temp_F(input.temperature())  # Update the highest temperature.
    basic.show_number(highest_temp) # Display the highest temperature.
input.on_button_pressed(Button.A, on_button_pressed_a)

# Function when button B is pressed to read out the lowest temperature recorded.
def on_button_pressed_b():
    global lowest_temp
    # Check if the current temperature is lower that the recorded lowest temperature.
    if temp_F(input.temperature()) <= lowest_temp:
        lowest_temp = temp_F(input.temperature())   # Update the lowest temperature.
    basic.show_number(lowest_temp)  # Display the lowest temperature.
input.on_button_pressed(Button.B, on_button_pressed_b)



# Initialize the lowest and highest temperatures with current temperature.
lowest_temp = 0
highest_temp = 0
highest_temp = temp_F(input.temperature())
lowest_temp = temp_F(input.temperature())
# Function to display the current temperature at regular intervals.

# Repeat the function to be called every 1 minute.
def on_every_interval():
    # Show the current temperature in Fahrenheit.
    basic.show_number(temp_F(input.temperature()))
# Repeat the function to be called every 1 minute.
loops.every_interval(60000, on_every_interval)
