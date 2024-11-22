import sys

# Define the Morse Code dictionary
NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def encode_to_morse(input_string):
    """Encodes a string into Morse code."""
    encoded_message = []
    for char in input_string.upper():
        if char in NESTED_MORSE:
            encoded_message.append(NESTED_MORSE[char])
        else:
            raise AssertionError("the arguments are bad")
    return " ".join(encoded_message)

if __name__ == "__main__":
    # Ensure exactly one argument is passed (besides the script name)
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    
    # Process the input string
    input_string = sys.argv[1]
    try:
        result = encode_to_morse(input_string)
        print(result)
    except AssertionError as e:
        print(e)
