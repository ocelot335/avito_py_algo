import functools


def tracer(func_to_trace):
    recursion_depth = 0

    @functools.wraps(func_to_trace)
    def wrapper(*args, **kwargs):
        nonlocal recursion_depth
        print(
            " " * recursion_depth
            + f"({recursion_depth})Func called: {func_to_trace.__name__}"
        )
        recursion_depth += 1
        result = func_to_trace(*args, **kwargs)
        recursion_depth -= 1
        print(
            " " * recursion_depth + f"({recursion_depth})Func result: {result}"
        )
        return result

    return wrapper


@tracer
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@tracer
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    fibonacci(4)

    print("\n" + "-" * 40 + "\n")

    factorial(4)
