from Foo import Foo


class Corge:
    __foo: Foo

    def __init__(self, foo: Foo):
        self.__foo = foo
        self.__foo.setCorge(self)
