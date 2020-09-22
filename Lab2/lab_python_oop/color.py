class GeomFigureColor:

    def __init__(self,value):
        self._color_ = value

    @property
    def color(self):

        return self._color_

    @color.setter
    def color(self, value):

        self._color_ = value