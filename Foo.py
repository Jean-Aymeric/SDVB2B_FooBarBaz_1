from Bar import Bar
from Baz import Baz
from Corge import Corge
from Grault import Grault
from Qux import Qux


class Foo:
    __bar: Bar
    __bazs: [Baz]
    __qux: Qux
    __graults: [Grault]
    __corge: Corge | None

    def __init__(self, bar: Bar):
        self.__bar = bar
        self.__bazs = []
        self.__qux = Qux()
        self.__graults = []
        self.__corge = None

    def addBaz(self, baz):
        self.__bazs.append(baz)

    def addGrault(self):
        self.__graults.append(Grault(self))

    def setCorge(self, corge: Corge):
        self.__corge = corge
