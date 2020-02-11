

class A:
    def method(self):
        print(A.__name__)


class B(A):
    def method(self):
        print(B.__name__)


class D(B):
    def method(self):
        print(D.__name__)


class F(D, B, A):
    pass


def lazy_property(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property
