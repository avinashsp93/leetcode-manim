import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from manim import *
from components.array_cell import ArrayCell 
from components.pointer import Pointer

class BinarySearch(Scene):
    def construct(self):

        code = Code(
            code_file="./code/p0002_binary_search.py",
            language="python"
        )
        code.scale(0.6)
        code.to_corner(DR)

        self.play(Create(code))
        self.wait()

        cell1 = ArrayCell(3, color=BLUE, side_length=0.5)
        cell2 = ArrayCell(9, color=BLUE, side_length=0.5)
        cell3 = ArrayCell(14, color=BLUE, side_length=0.5)
        cell4 = ArrayCell(21, color=BLUE, side_length=0.5)
        cell5 = ArrayCell(27, color=BLUE, side_length=0.5)
        cell6 = ArrayCell(34, color=BLUE, side_length=0.5)
        cell7 = ArrayCell(42, color=BLUE, side_length=0.5)
        cell8 = ArrayCell(45, color=BLUE, side_length=0.5)
        cell9 = ArrayCell(52, color=BLUE, side_length=0.5)
        cell10 = ArrayCell(58, color=BLUE, side_length=0.5)
        cell11 = ArrayCell(63, color=BLUE, side_length=0.5)
        cell12 = ArrayCell(66, color=BLUE, side_length=0.5)
        cell13 = ArrayCell(71, color=BLUE, side_length=0.5)
        cell14 = ArrayCell(75, color=BLUE, side_length=0.5)
        cell15 = ArrayCell(79, color=BLUE, side_length=0.5)
        cell16 = ArrayCell(83, color=BLUE, side_length=0.5)
        cell17 = ArrayCell(88, color=BLUE, side_length=0.5)
        cell18 = ArrayCell(91, color=BLUE, side_length=0.5)
        cell19 = ArrayCell(95, color=BLUE, side_length=0.5)
        cell20 = ArrayCell(99, color=BLUE, side_length=0.5)

        cells = VGroup(cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20)
        cells.arrange(RIGHT, buff=0.2)

        self.play(Create(cells), run_time=1)
        self.wait()

        self.play(cell7.animate.set_fill(YELLOW, opacity=0.5))
        self.wait()

        lowpointer = Pointer("LOW", BLUE)
        lowpointer.next_to(cells[0], DOWN)
        self.play(Create(lowpointer))

        highpointer = Pointer("HIGH", RED)
        highpointer.next_to(cells[19], DOWN)
        self.play(Create(highpointer))

        targetpointer = Pointer("TARGET", GREEN, start=UP, end=DOWN, textPos=UP)
        targetpointer.next_to(cells[6], UP)
        self.play(Create(targetpointer))

        self.play(lowpointer.animate.next_to(cells[0], DOWN))
        self.play(highpointer.animate.next_to(cells[19], DOWN))
        self.wait()



        midEquation = MathTex(
            "mid = \\frac{low + high}{2}"
        )
        midEquation.scale(0.2)
        midEquation.to_corner(UR)
        self.play(Write(midEquation))
        self.wait()

        midEquationWithValues = MathTex(
            "mid = \\frac{0 + 19}{2} = 9"
        )
        midEquationWithValues.to_corner(UR)
        midEquationWithValues.scale(0.3)
        self.wait()

        self.play(Transform(midEquation, midEquationWithValues))
        self.wait()

        midpointer = Pointer("MID", ORANGE, start=DOWN, end=UP, textPos=DOWN)
        midpointer.next_to(cells[9], DOWN)
        self.play(Create(midpointer)) 
        self.wait()


        self.play(FadeOut(midpointer))
        self.play(highpointer.animate.next_to(cells[8], DOWN))
        self.wait()

        midEquationWithValues = MathTex(
            "mid = \\frac{0 + 8}{2} = 4"
        )
        midEquationWithValues.to_corner(UR)
        midEquationWithValues.scale(0.3)
        self.wait()


        self.play(Transform(midEquation, midEquationWithValues))
        self.wait()


        midpointer = Pointer("MID", ORANGE, start=DOWN, end=UP, textPos=DOWN)
        midpointer.next_to(cells[4], DOWN)
        self.play(Create(midpointer))
        self.wait()




        self.play(FadeOut(midpointer))
        self.play(lowpointer.animate.next_to(cells[5], DOWN))
        self.wait()

        midEquationWithValues = MathTex(
            "mid = \\frac{5 + 8}{2} = 6"
        )
        midEquationWithValues.to_corner(UR)
        midEquationWithValues.scale(0.3)
        self.wait()


        self.play(Transform(midEquation, midEquationWithValues))
        self.wait()


        midpointer = Pointer("MID", ORANGE, start=DOWN, end=UP, textPos=DOWN)
        midpointer.next_to(cells[6], DOWN)
        self.play(Create(midpointer))
        self.wait()
