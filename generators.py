def generator_function():
    yield "Hello"
    yield "World"

iterator = iter(generator_function())
print(next(iterator))
print(next(iterator))