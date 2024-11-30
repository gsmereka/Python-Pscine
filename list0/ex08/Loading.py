import sys


def ft_tqdm(lst: range):
    """
    Displays a progress bar in the terminal while iterating over a sequence.

    Acts as a generator that yields elements from the input sequence (`lst`)
    and updates a progress bar in the terminal.

    Args:
        lst (range): The sequence to iterate over.

    Yields:
        The next element in the sequence.

    Example:
        for elem in ft_tqdm(range(100)):
            # Perform some operation
            pass
    """
    total = len(lst)

    for i, elem in enumerate(lst):
        progress = (i + 1) / total
        bar_length = 50
        bar_filled = int(progress * bar_length)
        bar = "█" * bar_filled + "" + " " * (bar_length - bar_filled)
        sys.stdout.write(f"\r{int(progress * 100)}%|{bar}| {i + 1}/{total}")
        yield elem
    print()
