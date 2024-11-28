def count_in_list(lst, to_find) -> int:
    """Count the number of times to_find is in lst"""
    count = 0
    for item in lst:
        if item == to_find:
            count += 1
    return count
