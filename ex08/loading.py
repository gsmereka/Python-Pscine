import sys
import time

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    
    for i, elem in enumerate(lst):
        # Progress bar
        progress = (i + 1) / total
        bar_length = 50  # Length of the progress bar
        bar_filled = int(progress * bar_length)
        bar = "=" * bar_filled + ">" + "." * (bar_length - bar_filled)
        
        # Time elapsed
        elapsed_time = time.time() - start_time
        items_per_second = (i + 1) / elapsed_time if elapsed_time > 0 else 0
        
        # Print progress
        sys.stdout.write(f"\r{int(progress * 100)}%|[{bar}]| {i + 1}/{total} [Elapsed: {elapsed_time:.2f}s, {items_per_second:.2f}it/s]")
        sys.stdout.flush()
        
        yield elem

    # Print a new line after completion
    print()
