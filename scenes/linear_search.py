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
        # title = Text("Linear Search")
        # self.play(Write(title))
        # self.wait()

        # self.play(title.animate.to_corner(UL))
        # self.wait()


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


        # Third Scene: Array and Indices
        values = [3, 9, 14, 21, 27, 34, 42, 45, 52, 58, 63, 66, 71, 75, 79, 83, 88, 91, 95, 99]
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

        # Fourth Scene: Pointer
        pointer = Pointer(label="i", color=DARK_BROWN, start=DOWN, end=UP, textPos=DOWN)
        pointer.next_to(cells[0], DOWN).scale(0.7).shift(UP * 0.5)
        self.play(Create(pointer))
        self.wait()

        highlight = SurroundingRectangle(
            code.code_lines[4],
            color=YELLOW,
            buff=0.1
        )

        self.play(Create(highlight))
        self.wait()