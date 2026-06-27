from manim import *

class Playground(Scene):
    def construct(self):
        # Lesson 3 : Simultaneous Animations
        
        circle = Circle(radius=1, color=BLUE)        
        square = Square(side_length=2, color=GREEN)
        text = Text("Meet")

        circle.shift(LEFT * 2)
        square.shift(RIGHT * 2)
        
        self.play(Create(circle), Create(square), Create(text))

        self.play(circle.animate.shift(RIGHT * 2), square.animate.shift(LEFT * 2))
        self.play(FadeOut(text))
        
        self.wait(2)