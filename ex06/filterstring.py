from ft_filter import ft_filter
import sys

def main():
    # Validate that there are exactly two arguments
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    # Validate that the first argument is a string and the second is an integer
    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    if not isinstance(S, str) or not isinstance(N, int):
        print("AssertionError: the arguments are bad")
        return

    # List comprehension with lambda to filter words by length
    result = ft_filter(lambda word: len(word) > N, S.split())
    # result = ft_filter(len, S.split())
    # result = [word for word in S.split() if len(word) > N]

    print(result)

if __name__ == "__main__":
    main()