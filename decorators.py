


def my_decorator(func):
    def wrapper():
        print("I'm wrapper!")
        func()
        print('Wrapped')
    return wrapper()


def say_hello():
    print(f'Hello')


say_hello = my_decorator(say_hello)