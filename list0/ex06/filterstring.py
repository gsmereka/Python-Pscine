from ft_filter import ft_filter
import sys


def main():
    """Main function to filter words from a string by their length."""
    try:
        assert len(sys.argv) == 3, "AssertionError: bad arguments"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        sys.exit()

    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the second argument must be an integer")
        return

    try:
        result = list(ft_filter(lambda word: len(word) > N, S.split()))
    except Exception as e:
        print(f"Error while filtering: {e}")
        return

    print(result)


if __name__ == "__main__":
    main()
