from abc import ABC, abstractmethod


class GeomFigure():
    __metaclass__ = ABC
    _square_ = 0

    @abstractmethod
    def square(self):

        pass