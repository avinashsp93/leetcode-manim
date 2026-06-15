import code
import os
from runpy import run_path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from manim import *
from components.array_cell import ArrayCell 
from components.pointer import Pointer

class LinearSearch(Scene):
    def construct(self):
        # First Scene: Title
        title = Text("Linear Search")
        self.play(Write(title))
        self.wait()

        self.play(title.animate.to_corner(UL))
        self.wait()


        # Second Scene: Code
        code = Code(
            code_file="./code/p0001_linear_search.py",
            tab_width=2,
            background="window",
            paragraph_config={"font_size": 16, "line_spacing": 1.2 },
        )
        self.play(Write(code), run_time=1) # change to 5 later
        self.wait()
        self.play(code.animate.scale(0.9).to_corner(DR))
        self.wait()


        # Third Scene: Array and Indices Setup
        values = [52, 3, 91, 27, 75, 14, 99, 42, 66, 9, 88, 34, 71, 21, 95, 58, 45, 83, 63, 79]
        cells = VGroup(*[
            ArrayCell(v, color=BLUE, side_length=0.5)
            for v in values
        ])
        cells.arrange(RIGHT, buff=0).shift(UP * 2)

        indices = VGroup(*[
            Text(str(i), font_size=20)
            for i in range(len(cells))
        ])

        for idx, cell in zip(indices, cells):
            idx.next_to(cell, UP, buff=0.15).scale(0.6)

        self.play(
            LaggedStart(
                *[FadeIn(cell) for cell in cells],
                lag_ratio=0.1
            ),
            run_time=4
        )
        self.play(
            LaggedStart(
                *[FadeIn(idx) for idx in indices],
                lag_ratio=0.1
            ),
            run_time=2
        )
        self.wait()

        # Fourth Scene: Target, Equation, Pointer and Codeblock Setup
        self.play(cells[13].animate.set_fill(YELLOW, opacity=0.3))
        target = Text("Target: 21", font_size=24)
        target.to_corner(DL).shift(UP * 0.5)
        self.play(Write(target))
        self.wait()

        highlight = SurroundingRectangle(
            code.code_lines[4],
            color=YELLOW,
            buff=0.1
        )

        pointer = Pointer(label="i", color=DARK_BROWN, start=DOWN, end=UP, textPos=DOWN)
        pointer.scale(0.5)
        pointer.next_to(cells[0], DOWN)
        self.play(Create(pointer), Create(highlight))
        self.wait()


        self.play(highlight.animate.become(SurroundingRectangle(
            code.code_lines[5],
        )))
        self.wait()

        equation = MathTex("52 \\neq 21", font_size=24)
        equation.to_corner(DL)
        self.play(Write(equation))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[1], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)))
        self.wait()

        self.play(equation.animate.become(MathTex("3 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()


        self.play(
            pointer.animate.next_to(cells[2], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)))
        self.wait()

        self.play(equation.animate.become(MathTex("91 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()


        self.play(
            pointer.animate.next_to(cells[3], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)), 
                  equation.animate.become(MathTex("27 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()        

        self.play(
            pointer.animate.next_to(cells[4], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("75 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[5], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("14 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[6], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("99 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[7], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("42 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[8], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("66 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[9], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("9 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[10], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("88 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[11], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("34 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()

        self.play(
            pointer.animate.next_to(cells[12], DOWN),
            highlight.animate.become(SurroundingRectangle(code.code_lines[4], color=YELLOW, buff=0.1))
        )
        self.wait()

        self.play(highlight.animate.become(SurroundingRectangle(code.code_lines[5], color=YELLOW, buff=0.1)),
                  equation.animate.become(MathTex("71 \\neq 21", font_size=24).to_corner(DL)))
        self.wait()