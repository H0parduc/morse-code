import pygame
import os
from gtts import gTTS
from time import sleep

# Define the Morse code dictionary.
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

pygame.mixer.init()


def play_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            pygame.mixer.Sound('audio/dot.wav').play()
        elif symbol == '-':
            pygame.mixer.Sound('audio/dash.wav').play()
        elif symbol == ' ':
            sleep(1)


def play_message_to_sound(message):
    language = 'en'
    audio_path = "audio/test.mp3"
    if os.path.exists(audio_path):
        os.remove(audio_path)

    audio = gTTS(text=message, lang=language, slow=False)
    audio.save(audio_path)



    if os.name == 'nt':  # Check if the operating system is Windows
        os.system(f"start {audio_path}")
    elif os.name == 'posix':  # Check if the operating system is Linux or macOS
        os.system(f"xdg-open {audio_path}")


# Convert a message to Morse code.
def to_morse_code(message):
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
        else:
            morse_code = f'This character {char} is not exist in morse code!'
            break
    return morse_code


# Convert a Morse code sequence to a message.
def from_morse_code(morse_code):
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message


# User interface
def main():
    while True:
        choice = input(
            "Choose an option:\nPress 1 to convert text to Morse code\nPress 2 to convert Morse code to text"
            "\nPress 3 to use text to speech \nPress 4 to quit \n")
        if choice == '1':
            message = input("Enter a message to convert to Morse code: ")
            morse_code = to_morse_code(message)
            print(morse_code)
            play_morse_code(morse_code)

        elif choice == '2':
            morse_code = input("Enter a Morse code sequence to convert to text: ")
            message = from_morse_code(morse_code)
            print(message)

        elif choice == '4':
            print("Quited1 successfully")
            break
        elif choice == '3':
            message = input("Enter a message to play back \n3")
            play_message_to_sound(message)
        else:
            print("Invalid choice, please choose from the available options.")


if __name__ == "__main__":
    main()
