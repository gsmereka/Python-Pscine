from sys import argv


def main():
    try:
        if len(argv) != 2:
            if len(argv) > 2:
                raise AssertionError("more than one argument is provided")
            else:
                raise AssertionError("no argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    try:
        num = int(argv[1])

        if num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")
        return


if __name__ == "__main__":
    main()
