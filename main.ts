//  Function to convert Celsius to Fahrenheit.
function temp_F(C: number): number {
    //  Formula for Celsius to Fahrenheit is F = C * 1.8 + 32.
    return 32 + C * 1.8
}

//  Function when button A is pressed to read out the highest temperature recorded.
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    current_temp_F = temp_F(input.temperature())
    //  Check of the current temperature is higher than the recorded highest temperature.
    if (current_temp_F > highest_temp) {
        //  Update the highest temperature.
        highest_temp = current_temp_F
    }
    
    //  Display the highest temperature.
    basic.showNumber(highest_temp)
})
//  Function when button B is pressed to read out the lowest temperature recorded.
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    current_temp_F = temp_F(input.temperature())
    //  Check if the current temperature is lower that the recorded lowest temperature.
    if (current_temp_F < lowest_temp) {
        //  Update the lowest temperature.
        lowest_temp = current_temp_F
    }
    
    //  Display the lowest temperature.
    basic.showNumber(lowest_temp)
})
//  Initialize the lowest and highest temperature to the current temperature.
let lowest_temp = 0
let highest_temp = 0
let current_temp_F = 0
current_temp_F = temp_F(input.temperature())
highest_temp = current_temp_F
lowest_temp = current_temp_F
//  Function to display the current temperature at 1 minute intervals.
loops.everyInterval(60000, function on_every_interval() {
    basic.showNumber(current_temp_F)
})
