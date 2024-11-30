def ft_filter(fun_to_apply, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    try:
        iter(iterable)
    except TypeError:
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")

    if (fun_to_apply is None):
        return (item for item in iterable if item)
    return (item for item in iterable if fun_to_apply(item))
