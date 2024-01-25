# Function to convert Celsius to Fahrenheit.
def temp_F(C: number):
    # Formula for Celsius to Fahrenheit is F = C * 1.8 + 32.
    return 32 + C * 1.8

# Function when button A is pressed to read out the highest temperature recorded.
def on_button_pressed_a():
    global current_temp_F, highest_temp
    current_temp_F = temp_F(input.temperature())
    # Check of the current temperature is higher than the recorded highest temperature.
    if current_temp_F > highest_temp:
        # Update the highest temperature.
        highest_temp = current_temp_F
    # Display the highest temperature.
    basic.show_number(highest_temp)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Function when button B is pressed to read out the lowest temperature recorded.
def on_button_pressed_b():
    global current_temp_F, lowest_temp
    current_temp_F = temp_F(input.temperature())
    # Check if the current temperature is lower that the recorded lowest temperature.
    if current_temp_F < lowest_temp:
        # Update the lowest temperature.
        lowest_temp = current_temp_F
    # Display the lowest temperature.
    basic.show_number(lowest_temp)
input.on_button_pressed(Button.B, on_button_pressed_b)



#Initialize the lowest and highest temperature to the current temperature.
lowest_temp = 0
highest_temp = 0
current_temp_F = 0
current_temp_F = temp_F(input.temperature())
highest_temp = current_temp_F
lowest_temp = current_temp_F

# Function to display the current temperature at 1 minute intervals.
def on_every_interval():
    basic.show_number(current_temp_F)
loops.every_interval(60000, on_every_interval)
