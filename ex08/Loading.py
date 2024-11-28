import sys


def ft_tqdm(lst: range):
    total = len(lst)

    for i, elem in enumerate(lst):
        progress = (i + 1) / total
        bar_length = 50
        bar_filled = int(progress * bar_length)
        bar = "█" * bar_filled + "" + " " * (bar_length - bar_filled)
        sys.stdout.write(f"\r{int(progress * 100)}%|{bar}| {i + 1}/{total}")
        yield elem
    print()
