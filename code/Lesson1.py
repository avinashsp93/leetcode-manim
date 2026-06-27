from manim import *

class Playground(Scene):
    def construct(self):
        # Lesson 1 : Objects + Positioning + Creation
        
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=GREEN)
        text = Text("Start")

        # Positioning

        circle.shift(UP * 3)
        text.shift(DOWN * 2)

        self.play(Create(circle), Create(square), Create(text))
        self.wait(2)