from re import M
from manim import *
# from manimlib.imports import *

x_center = -6
y_center = -3

class Constraint:
    """ ax1 + bx2 <= c"""
    def __init__(self, a, b, c):
        self.intercepts = []

        if b == 0:
            self.x1_intercept = (c / a) / 2. + x_center 
            self.intercepts.append([x_center, y_center, 0])
            self.intercepts.append([x_center, y_center + (14/2.), 0])
            self.intercepts.append([self.x1_intercept, y_center + (14/2.), 0])
            self.intercepts.append([self.x1_intercept, y_center, 0])

            self.line_start = [self.x1_intercept, y_center + (14/2.), 0]
            self.line_end = [self.x1_intercept, y_center + (-2/2.), 0]

        elif a == 0:
            # self.x2_intercept = (c / b) / 2. + y_center
            pass

        else:
            self.x1_intercept = (c / a) / 2. + x_center 
            self.x2_intercept = (c / b) / 2. + y_center
            self.intercepts.append([x_center, y_center, 0])
            self.intercepts.append([self.x1_intercept, y_center, 0])
            self.intercepts.append([x_center, self.x2_intercept, 0])

            self.line_start = [(-4 / 2.) + x_center, (((c + 4*a) / b) / 2. + y_center), 0]
            self.line_end = [(((c + 3*b) / a) / 2. + x_center), (-3 / 2.) + y_center, 0]

class Objective:
    """ max z = ax1 + bx2"""
    def __init__(self, a, b):
        self.m = -a / b

    def line_coord(self, p):
        """ x2 = mx1 + alpha """
        alpha = p[1] - self.m*p[0]

        x2 = -2*self.m + alpha
        line_start = [-2/2. + x_center, x2/2. + y_center, 0]

        x1 = (-2 - alpha) / self.m
        line_end = [x1/2. + x_center, -2/2. + y_center, 0]

        return line_start, line_end

class VisualMethod(Scene):
    def construct(self):

        # Introduction
        title = Tex("Linear Optimization")
        title.scale(2.5)
        creators = Tex("Made by \n Amirhossein Sorour \& Aylar Sedaei")
        creators.scale(0.4)
        creators.move_to([5, -3.7, 0])
        self.play(Write(title), run_time=1.2)
        self.wait(1)
        self.play(Write(creators), run_time=0.7)
        self.wait(1)
        self.play(FadeOut(title))
        self.wait(1)

        # drawing axes
        self.wait(0.5)
        x_axis = NumberLine([-16, 16, 0.5], numbers_with_elongated_ticks=[])
        x_axis.set_stroke(width=1)
        x_axis.shift([0, y_center, 0])
        x_axis.set_color(WHITE)
        y_axis = NumberLine([-10, 10, 0.5], numbers_with_elongated_ticks=[])
        y_axis.set_stroke(width=1)
        y_axis.shift([x_center, 0, 0])
        y_axis.set_color(WHITE)
        y_axis.rotate(PI / 2)
        self.play(Write(x_axis), Write(y_axis))

        # Writing Objective Function
        obj_text = Tex("\\textit{Objective Function:}")
        obj_text.scale(0.85)
        obj_text.move_to([4.5, 3, 0])
        self.play(Write(obj_text))
        self.wait(0.2)

        obj_formula = Tex("{\\small $max \  z = 3x_1 + 2x_2$}")
        obj_formula.scale(0.8)
        obj_formula.set_color(RED_C)
        obj_formula.move_to([4.5, 2.5, 0])
        self.play(Write(obj_formula))
        self.wait(1)

        
        # Writing Constraints
        subject_text = Tex("\\textit{Subject to:}")
        subject_text.scale(0.85)
        subject_text.move_to([4.5, 1.7, 0])
        self.play(Write(subject_text))
        self.wait(0.2)

        const1_text = Tex("$6x_1 + 5x_2 \le 60$")
        const1_text.scale(0.8)
        const1_text.set_color(BLUE_C)
        const1_text.move_to([4.5, 1.2, 0])
        self.play(Write(const1_text))
        self.wait(0.2)

        const2_text = Tex("$x_1 + 2x_2 \le 14$")
        const2_text.scale(0.8)
        const2_text.set_color(GREEN_C)
        const2_text.move_to([4.5, 0.7, 0])
        self.play(Write(const2_text))
        self.wait(0.2)

        const3_text = Tex("$x_1 \le 9$")
        const3_text.scale(0.8)
        const3_text.set_color(LIGHT_PINK)
        const3_text.move_to([4.5, 0.2, 0])
        self.play(Write(const3_text))
        self.wait(0.2)

        const4_text = Tex("$x_1, x_2 \ge 0$")
        const4_text.scale(0.8)
        const4_text.set_color(GOLD_C)
        const4_text.move_to([4.5, -0.3, 0])
        self.play(Write(const4_text))
        self.wait(0.2)


        #Drawing the lines
        xaxis_line = Line([x_center, y_center, 0], [25/2. + x_center, y_center, 0])
        yaxis_line = Line([x_center, y_center, 0], [x_center, 14/2. + y_center, 0])

        xaxis_line.set_color(GOLD_C)
        yaxis_line.set_color(GOLD_C)
        self.play(
            TransformFromCopy(const4_text, xaxis_line),
            TransformFromCopy(const4_text, yaxis_line),
            run_time=0.8
        )
        self.wait(1)

        const1 = Constraint(a=1.2, b=1, c=12)
        const1_line = Line(const1.line_start, const1.line_end)
        const1_line.set_color(BLUE_C)
        const1_feasible = Polygon(*const1.intercepts, stroke_width=0, fill_color = BLUE_C, fill_opacity=0.5)
        const1_region = VGroup(const1_line, const1_feasible)
        self.play(TransformFromCopy(const1_text, const1_region), run_time=0.8)
        self.wait(1)

        const2 = Constraint(a=1, b=2, c=14)
        const2_line = Line(const2.line_start, const2.line_end)
        const2_line.set_color(GREEN_C)
        const2_feasible = Polygon(*const2.intercepts, stroke_width=0, fill_color = GREEN_C, fill_opacity=0.5)
        const2_region = VGroup(const2_line, const2_feasible)
        self.play(TransformFromCopy(const2_text, const2_region), run_time=0.8)
        self.wait(1)

        const3 = Constraint(a=1, b=0, c=9)
        const3_line = Line(const3.line_start, const3.line_end)
        const3_line.set_color(LIGHT_PINK)
        const3_feasible = Polygon(*const3.intercepts, stroke_width=0, fill_color = LIGHT_PINK, fill_opacity=0.5)
        const3_region = VGroup(const3_line, const3_feasible)
        self.play(TransformFromCopy(const3_text, const3_region), run_time=0.8)
        self.wait(1)

        # Draw Feasible Region
        feasible_points = [
            [0, 0, 0],
            [9, 0, 0],
            [9, 1.2, 0],
            [50/7., 24/7., 0],
            [0, 7, 0]
        ]
        for p in feasible_points:
            p[0] = p[0] / 2. + x_center
            p[1] = p[1] / 2. + y_center

        feasible_region = Polygon(*feasible_points, stroke_width=0, fill_color = PURPLE_C, fill_opacity=0.9)
        all_regions = VGroup(const1_feasible, const2_feasible, const3_feasible)
        self.play(Transform(all_regions, feasible_region), run_time=0.8)
        self.wait(1)

        
        # Draw Objective Function
        obj = Objective(a=1, b=5)

        obj_line0_start, obj_line0_end = obj.line_coord([0,-1])
        obj_line0 = DashedLine(
            obj_line0_start,
            obj_line0_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line0.set_color(RED_C)
        self.play(
            TransformFromCopy(obj_formula, obj_line0),
            run_time=0.8
        )
        self.wait(1)

        obj_line1_start, obj_line1_end = obj.line_coord(feasible_points[0][0:2])
        obj_line1 = DashedLine(
            obj_line1_start,
            obj_line1_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line1.set_color(RED_C)
        self.play(
            MoveToTarget(obj_line0, obj_line1),
            run_time=0.8
        )
        self.wait(1)
        
        
