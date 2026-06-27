from manim import *

class Playground(Scene):
    def construct(self):
        # Lesson 4 : Animation Chaining
        
        circle = Circle(radius=1, color=BLUE)        
        self.play(Create(circle))

        self.play(circle.animate.shift(RIGHT + UP).scale(0.8).set_color(GREEN).rotate(PI/4), run_time=2)