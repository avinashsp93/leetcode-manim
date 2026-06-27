from manim import *

class Playground(Scene):
    def construct(self):
        # Lesson 2 : Animations
        
        circle = Circle(radius=1, color=BLUE)        

        self.play(circle.animate.shift(RIGHT))
        self.play(circle.animate.shift(UP))
        self.play(circle.animate.rotate(PI/4))
        self.play(circle.animate.scale(2))
        self.play(circle.animate.set_color(RED))
        
        self.wait(2)