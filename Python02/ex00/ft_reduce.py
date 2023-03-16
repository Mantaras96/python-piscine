
from _collections_abc import Iterable

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    if not isinstance(iterable, Iterable):
        return None

    for i, elem in enumerate(iterable):
        if i:
            result = function_to_apply(result, elem)
        else:
            result = elem
    return result
