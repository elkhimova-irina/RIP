# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

if __name__ == "__main__":
    r = Rectangle("синего", 6, 12)
    c = Circle("зеленого", 6)
    s = Square("красного", 6)
    print(r.__repr__())
    print(c.__repr__())
    print(s.__repr__())

