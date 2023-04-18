import cProfile
import time


def profile(func):
    """Decorator for run function profile."""

    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + ".prof"
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(profile_filename)
        return result

    return wrapper


def timer(func):
    """Decorator for measure time function."""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        print(f"Time of {func.__name__}: {duration:.05f}")
        return result

    return wrapper
