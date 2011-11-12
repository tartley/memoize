
def memoize(wrapped):

    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = wrapped(*args, **kwargs)
        return cache[key]

    return wrapper

