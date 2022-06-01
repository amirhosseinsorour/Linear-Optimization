from manim import *
# from manimlib.imports import *

class SquareToCircle(Scene):
    def construct(self):
        # circle = Circle()
        # square = Square()
        # square.flip(RIGHT)
        # square.rotate(-3 * TAU / 8)
        # circle.set_fill(PINK, opacity=0.5)

        # self.play(Create(square))
        # self.play(Transform(square, circle))
        # self.play(FadeOut(square))

        # Introduction
        title = Tex("Linear Optimization")
        title.scale(2.5)
        creators = Tex("Made by \n Amirhossein Sorour \& Aylar Sedaei")
        creators.scale(0.4)
        creators.move_to([5, -3.7, 0])
        self.play(Write(title), run_time=1.2)
        self.wait(2)
        self.play(Write(creators), run_time=0.7)
        self.wait(2)
        self.play(FadeOut(title))
        self.wait(2)

        y0 = -0.5

        # drawing axes
        self.wait(0.5)
        x_axis = NumberLine([-16, 16, 0.5], numbers_with_elongated_ticks=[])
        x_axis.set_stroke(width=1)
        x_axis.shift([0, y0, 0])
        x_axis.set_color(RED)
        y_axis = NumberLine([-10, 10, 0.5], numbers_with_elongated_ticks=[])
        y_axis.set_stroke(width=1)
        y_axis.set_color(RED)
        y_axis.rotate(PI / 2)
        self.play(Write(x_axis), Write(y_axis))