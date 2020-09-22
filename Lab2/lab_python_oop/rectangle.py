from lab_python_oop.figure import GeomFigure
from lab_python_oop.color import GeomFigureColor


class Rectangle(GeomFigure):
    _square_ = 0
    _width_ = 0
    _height_ = 0
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, width_param, height_param):

        self._width_ = width_param
        self._height_ = height_param
        self.colour= GeomFigureColor(color_param)
        ##self.fc = GeomFigureColor()
       ## self.fc.colorproperty = color_param

    def square(self):

        return self._width_*self._height_

    def __repr__(self):
        return '{} {} цвета шириной {} , высотой {} и площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.colour.color,
            self._width_,
            self._height_,
            self.square()
        )