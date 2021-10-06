'''sample code decorator is useful for debugging some part of code'''

import functools

def debug(function):
    @functools.wraps(function)
    def debug_(*args, **kwargs):
        res = function(*args, **kwargs)
        print('%s(%r, %r): %r' % \
                (function.__name__, args, kwargs, res))
        return res
    return debug_
