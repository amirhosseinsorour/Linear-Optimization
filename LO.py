from manim import *
# from manimlib.imports import *

class VisualMethod(Scene):
    def construct(self):

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

        y0 = -3
        x0 = -5.5

        # drawing axes
        self.wait(0.5)
        x_axis = NumberLine([-16, 16, 0.5], numbers_with_elongated_ticks=[])
        x_axis.set_stroke(width=1)
        x_axis.shift([0, y0, 0])
        x_axis.set_color(WHITE)
        y_axis = NumberLine([-10, 10, 0.5], numbers_with_elongated_ticks=[])
        y_axis.set_stroke(width=1)
        y_axis.shift([x0, 0, 0])
        y_axis.set_color(WHITE)
        y_axis.rotate(PI / 2)
        self.play(Write(x_axis), Write(y_axis))