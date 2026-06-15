from manim import *

class ArrayCell(VGroup):
    def __init__(self, value, color=BLUE, side_length=1.0):
        super().__init__()

        self.box = Square(side_length=side_length, color=color)
        self.text = Text(str(value), font_size=28)

        self.text.move_to(self.box.get_center())

        self.add(self.box, self.text)