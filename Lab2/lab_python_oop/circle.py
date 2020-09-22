from lab_python_oop.figure import GeomFigure
from lab_python_oop.color import GeomFigureColor
import math


class Circle(GeomFigure):
    _radius_ = 0
    _square_ = 0
    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self,  color, radius,):
        self._radius_ = radius
        self.colour = GeomFigureColor(color)

    def square(self):
        return float(math.pi) * self._radius_ * self._radius_

    def __repr__(self):
        return '{} {} цвета радиусом {} и площадью {}.'.format(
            Circle.get_figure_type(),
            self.colour.color,
            self._radius_,
            self.square()
        )
