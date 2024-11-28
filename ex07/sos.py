import sys


def encode_to_morse(input_string):
    """
    Encodes the input string into Morse code,\
raising an error for invalid characters.
    """
    encoded_message = []
    for char in input_string.upper():
        if char in NESTED_MORSE:
            encoded_message.append(NESTED_MORSE[char])
        else:
            raise AssertionError("the arguments are bad")
    return " ".join(encoded_message)


def main():
    """
    Processes command-line input and prints the\
encoded Morse code or an error message.
    """
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()

    input_string = sys.argv[1]
    try:
        result = encode_to_morse(input_string)
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


if __name__ == "__main__":
    main()
