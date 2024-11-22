import sys

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        return
    
    arg = sys.argv[1]
    
    assert isinstance(arg, int), "argument is not an integer"
    number = int(arg)
    
    # Check if the number is odd or even and print the result
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
