import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validated(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validated(self, instance, value):
        """return validated value or raise ValueError"""


class Quantity(Validated):
    """number greater than zero"""

    def validated(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value


class NonBlank(Validated):
    """a string with at least one non-space character"""

    def validated(self, instance, value):
        value = value.split()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value
