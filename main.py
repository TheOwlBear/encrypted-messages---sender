from microbit import *
import radio

radio.on()
radio.config(channel=7) # Make sure you are using the same channel number as the receiver!

def get_letter() -> str:
    current_letter = 'A'
    choosing = True
    while choosing:
        sleep(300)
        display.show(current_letter)

        button_a_pressed = button_a.was_pressed()
        button_b_pressed = button_b.was_pressed()

        if button_a_pressed and button_b_pressed:
            choosing = False
        elif button_a_pressed:
            current_letter = shift_letter(current_letter, -1)
        elif button_b_pressed:
            current_letter = shift_letter(current_letter, 1)

    return current_letter

def shift_letter(letter: str, amount: str) -> str:
    letter_num = ord(letter) - ord('A')
    shifted_letter_num = (letter_num + amount) % 26
    return chr(ord('A') + shifted_letter_num)

display.scroll("Choose shift")
shift_amount = 0
choosing_shift = True

while choosing_shift:
    sleep(300)
    display.show(str(shift_amount))

    button_a_pressed = button_a.was_pressed()
    button_b_pressed = button_b.was_pressed()

    if button_a_pressed and button_b_pressed:
        choosing_shift = False
    elif button_a_pressed:
        shift_amount -= 1
    elif button_b_pressed:
        shift_amount += 1

while True:
    chosen_letter = get_letter()
    display.show(chosen_letter)
    radio.send(shift_letter(chosen_letter, shift_amount))
    sleep(2000)
