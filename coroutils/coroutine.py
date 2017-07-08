from functools import wraps


def coroutine(function):
    """Wraps function to prime it. Thanks L. Ramalho (Fluent Python)"""
    @wraps(function)
    def primer(*args, **kwargs):
        """Creates an instance of the function and primes it"""
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return primer


__all__ = []
