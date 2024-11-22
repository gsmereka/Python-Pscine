import sys
import string

def analyze_text(text):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0
    punctuation_count = 0

    if not isinstance(text, str):
        printf("TEXT")
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        elif char in string.punctuation:
            punctuation_count += 1

    print(f"O texto contém {len(text)} caracteres:")
    print(f"- {upper_count} letras maiúsculas")
    print(f"- {lower_count} letras minúsculas")
    print(f"- {punctuation_count} caracteres de pontuação")
    print(f"- {space_count} espaços")
    print(f"- {digit_count} dígitos")

def main():
    if len(sys.argv) > 2:
        print("Erro: Apenas um argumento é permitido.")
        return
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("Digite o texto a ser analisado:\n")

    analyze_text(text)

if __name__ == "__main__":
    main()
