from manim import *

class Pointer(VGroup):
    def __init__(self, label="P", color=YELLOW, start=DOWN, end=UP, textPos=DOWN):
        super().__init__()

        self.arrow = Arrow(
            start=start,
            end=end,
            buff=0
        ).scale(0.6)

        self.text = Text(label, font_size=24, color=color)
        self.text.next_to(self.arrow, textPos, buff=0.1)

        self.add(self.arrow, self.text)