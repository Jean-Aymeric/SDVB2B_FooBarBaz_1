from Foo import Foo


class Grault:
    __foo: Foo

    def __init__(self, foo: Foo):
        self.__foo = foo
