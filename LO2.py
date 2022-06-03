from turtle import position
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

        # Writing Objective Function
        obj_text = Tex("\\textit{Objective Function:}")
        obj_text.scale(0.85)
        obj_text.move_to([4.35, 3, 0])
        self.play(Write(obj_text))
        self.wait(0.2)

        obj_formula = Tex(
            "{\\small $max \  z = 10x_1 + 20x_2$}",
        )
        obj_formula.move_to([4.5, 2.5, 0])
        self.play(Write(obj_formula))
        self.wait(1)

        
        # Writing Constraints
        subject_text = Tex("\\textit{Subject to:}")
        subject_text.scale(0.85)
        subject_text.move_to([4.35, 1.7, 0])
        self.play(Write(subject_text))
        self.wait(0.2)

        const1_text = Tex("$3x_1 + 5x_2 \le 15$")
        const1_text.scale(0.85)
        const1_text.move_to([4.5, 1.2, 0])
        self.play(Write(const1_text))
        self.wait(0.2)

        const2_text = Tex("$5x_1 + 10x_2 \ge 20$")
        const2_text.scale(0.85)
        const2_text.move_to([4.5, 0.7, 0])
        self.play(Write(const2_text))
        self.wait(0.2)

        const3_text = Tex("$x_1, x_2 \ge 0$")
        const3_text.scale(0.85)
        const3_text.move_to([4.5, 0.2, 0])
        self.play(Write(const3_text))
        self.wait(0.2)

        
        #Drawing the lines
        const1_position_list = [[-4, 5.4, 0], [8.33333, -2, 0], [0, 0, 0]]
        const1_line = self.draw_line(const1_position_list[0], const1_position_list[1], color=GREEN)
        self.play(Write(const1_line))
        const1_colored = Polygon(*const1_position_list, fill_color=GREEN)
        self.play(FadeIn(const1_colored))
        
        const2_position_list = [[-4, 4, 0], [8, -2, 0], [0, 0, 0]]
        const2_line = self.draw_line(const2_position_list[0], const2_position_list[1], color=BLUE)
        self.play(Write(const2_line))
        const2_colored = Polygon(*const2_position_list, fill_color=BLUE)
        self.play(FadeIn(const2_colored))
        
        const31_line = self.draw_line([-4, 0, 0], [20, 0, 0], color=GREEN)
        self.play(Write(const31_line))
        const32_line = self.draw_line([0, -2, 0], [0, 16, 0], color=GREEN)
        self.play(Write(const32_line))
        
    def draw_line(self, p1, p2, color=WHITE):
        p1[0] = p1[0] / 2. + self.x0
        p1[1] = p1[1] / 2. + self.y0

        p2[0] = p2[0] / 2. + self.x0
        p2[1] = p2[1] / 2. + self.y0

        line = Line(p1, p2)
        line.set_color(color)
        return line