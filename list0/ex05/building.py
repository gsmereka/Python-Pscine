import sys
import string


def analyze_text(text):
    """Analyze the text and count different types of characters."""
    counts = {
        "uppercase": 0,
        "lowercase": 0,
        "digits": 0,
        "spaces": 0,
        "punctuation": 0
    }

    for char in text:
        if char.isupper():
            counts["uppercase"] += 1
        elif char.islower():
            counts["lowercase"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            counts["spaces"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['uppercase']} uppercase letters")
    print(f"{counts['lowercase']} lowercase letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


def main():
    """Main function to process input and analyze the text."""
    try:
        assert len(sys.argv) <= 2, "Too many arguments provided"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        sys.exit()

    if len(sys.argv) == 1:
        text = input("Enter the text to analyze:\n")
        text += '\n'
    else:
        text = sys.argv[1]

    analyze_text(text)


if __name__ == "__main__":
    main()
