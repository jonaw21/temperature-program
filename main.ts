//  Function to convert Celsius to Fahrenheit.
function temp_F(C: number): number {
    //  Formula for Celsius to Fahrenheit is F = C * 1.8 + 32.
    return 32 + C * 1.8
}

//  Function when button A is pressed to read out the highest temperature recorded.
//  Display the highest temperature.
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    //  Check of the current temperature is higher than the recorded highest temperature.
    if (temp_F(input.temperature()) >= highest_temp) {
        highest_temp = temp_F(input.temperature())
    }
    
    //  Update the highest temperature.
    basic.showNumber(highest_temp)
})
//  Function when button B is pressed to read out the lowest temperature recorded.
//  Display the lowest temperature.
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    //  Check if the current temperature is lower that the recorded lowest temperature.
    if (temp_F(input.temperature()) <= lowest_temp) {
        lowest_temp = temp_F(input.temperature())
    }
    
    //  Update the lowest temperature.
    basic.showNumber(lowest_temp)
})
//  Initialize the lowest and highest temperatures with current temperature.
let lowest_temp = 0
let highest_temp = 0
highest_temp = temp_F(input.temperature())
lowest_temp = temp_F(input.temperature())
//  Function to display the current temperature at regular intervals.
//  Repeat the function to be called every 1 minute.
//  Repeat the function to be called every 1 minute.
loops.everyInterval(60000, function on_every_interval() {
    //  Show the current temperature in Fahrenheit.
    basic.showNumber(temp_F(input.temperature()))
})
