morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
              'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--','4': '....-','5': '.....',
              '6': '-....','7': '--...','8': '---..','9': '----.','0': '-----',
              }

# Get input from user
string_to_morse = input("Please write here to convert it to Morse code: ")
string_to_morse = string_to_morse.upper()
morse_string = ''
for letter in string_to_morse:
    if letter == " ":
        morse_string += "  "
    else:
        morse_letter = morse_code[letter]
        morse_string += f"{morse_letter} "
print(f"The morse code of the string: {morse_string}")
