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

class GraphicalMethod(Scene):
    def construct(self):

        # Introduction
        title = Tex("Linear Optimization")
        title.scale(2.5)
        subject = Tex("Solving Linear Programming Problems by Graphical Method")
        subject.scale(0.6)
        subject.move_to([0, -1, 0])
        creators = Tex("Made by \n Amirhossein Sorour \& Aylar Sedaei")
        creators.scale(0.4)
        creators.move_to([5, -3.7, 0])
        self.play(Write(title), run_time=1.2)
        self.wait(1)
        self.play(Write(subject), run_time=1.8)
        self.wait(1)
        self.play(Write(creators), run_time=0.7)
        self.wait(3)
        self.play(FadeOut(VGroup(title, subject)))
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
        self.wait(0.5)

        obj_formula = Tex("{\\small $max \  z = x_1 + 5x_2$}")
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
        self.wait(1)

        const1_text = Tex("$6x_1 + 5x_2 \le 60$")
        const1_text.scale(0.8)
        const1_text.set_color(BLUE_C)
        const1_text.move_to([4.5, 1.2, 0])
        self.play(Write(const1_text))
        self.wait(1)

        const2_text = Tex("$x_1 + 2x_2 \le 14$")
        const2_text.scale(0.8)
        const2_text.set_color(GREEN_C)
        const2_text.move_to([4.5, 0.7, 0])
        self.play(Write(const2_text))
        self.wait(1)

        const3_text = Tex("$x_1 \le 9$")
        const3_text.scale(0.8)
        const3_text.set_color(LIGHT_PINK)
        const3_text.move_to([4.5, 0.2, 0])
        self.play(Write(const3_text))
        self.wait(1)

        const4_text = Tex("$x_1, x_2 \ge 0$")
        const4_text.scale(0.8)
        const4_text.set_color(GOLD_C)
        const4_text.move_to([4.5, -0.3, 0])
        self.play(Write(const4_text))
        self.wait(2)


        #Drawing the lines
        xaxis_line = Line([x_center, y_center, 0], [27/2. + x_center, y_center, 0])
        yaxis_line = Line([x_center, y_center, 0], [x_center, 14/2. + y_center, 0])

        xaxis_line.set_color(GOLD_C)
        yaxis_line.set_color(GOLD_C)
        self.play(
            TransformFromCopy(const4_text, xaxis_line),
            TransformFromCopy(const4_text, yaxis_line),
            run_time=0.8
        )
        self.wait(2)

        const1 = Constraint(a=1.2, b=1, c=12)
        const1_line = Line(const1.line_start, const1.line_end)
        const1_line.set_color(BLUE_C)
        const1_feasible = Polygon(*const1.intercepts, stroke_width=0, fill_color = BLUE_C, fill_opacity=0.5)
        const1_region = VGroup(const1_line, const1_feasible)
        self.play(TransformFromCopy(const1_text, const1_region), run_time=0.8)
        self.wait(2)

        const2 = Constraint(a=1, b=2, c=14)
        const2_line = Line(const2.line_start, const2.line_end)
        const2_line.set_color(GREEN_C)
        const2_feasible = Polygon(*const2.intercepts, stroke_width=0, fill_color = GREEN_C, fill_opacity=0.5)
        const2_region = VGroup(const2_line, const2_feasible)
        self.play(TransformFromCopy(const2_text, const2_region), run_time=0.8)
        self.wait(2)

        const3 = Constraint(a=1, b=0, c=9)
        const3_line = Line(const3.line_start, const3.line_end)
        const3_line.set_color(LIGHT_PINK)
        const3_feasible = Polygon(*const3.intercepts, stroke_width=0, fill_color = LIGHT_PINK, fill_opacity=0.5)
        const3_region = VGroup(const3_line, const3_feasible)
        self.play(TransformFromCopy(const3_text, const3_region), run_time=0.8)
        self.wait(2)

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
        self.play(FadeTransform(all_regions, feasible_region), run_time=0.8)
        self.wait(2)

        
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
        self.wait(2)

        obj_line1_start, obj_line1_end = obj.line_coord([0, 0])
        obj_line1 = DashedLine(
            obj_line1_start,
            obj_line1_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line1.set_color(RED_C)
        obj_dot1 = Dot(feasible_points[0])
        obj_dot1.set_color(YELLOW_C)
        obj1 = VGroup(obj_line1, obj_dot1)
        self.play(
            FadeTransform(obj_line0, obj1),
            run_time=0.8
        )
        self.wait(2)
        
        obj1_text = Tex("$x_1 = 0 \quad x_2 = 0 \quad z = 0 $")
        obj1_text.scale(0.6)
        obj1_text.set_color(YELLOW_C)
        obj1_text.move_to([0.5, 2.5, 0])
        self.play(
            TransformFromCopy(obj_dot1, obj1_text),
            run_time=0.8
        )
        self.wait(2)
        
        obj_line2_start, obj_line2_end = obj.line_coord([9, 0])
        obj_line2 = DashedLine(
            obj_line2_start,
            obj_line2_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line2.set_color(RED_C)
        obj_dot2 = Dot(feasible_points[1])
        obj_dot2.set_color(YELLOW_C)
        obj2 = VGroup(obj_line2, obj_dot2)
        self.play(
            FadeTransform(obj1, obj2),
            run_time=0.8
        )
        self.wait(2)

        obj2_text = Tex("$x_1 = 9 \quad x_2 = 0 \quad z = 9 $")
        obj2_text.scale(0.6)
        obj2_text.set_color(YELLOW_C)
        obj2_text.move_to([0.5, 2, 0])
        self.play(
            TransformFromCopy(obj_dot2, obj2_text),
            run_time=0.8
        )
        self.wait(2)

        
        obj_line3_start, obj_line3_end = obj.line_coord([9, 1.2])
        obj_line3 = DashedLine(
            obj_line3_start,
            obj_line3_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line3.set_color(RED_C)
        obj_dot3 = Dot(feasible_points[2])
        obj_dot3.set_color(YELLOW_C)
        obj3 = VGroup(obj_line3, obj_dot3)
        self.play(
            FadeTransform(obj2, obj3),
            run_time=0.8
        )
        self.wait(2)

        obj3_text = Tex("$x_1 = 9 \quad x_2 = 1.2 \quad z = 15 $")
        obj3_text.scale(0.6)
        obj3_text.set_color(YELLOW_C)
        obj3_text.move_to([0.5, 1.5, 0])
        self.play(
            TransformFromCopy(obj_dot3, obj3_text),
            run_time=0.8
        )
        self.wait(2)

        
        obj_line4_start, obj_line4_end = obj.line_coord([50 / 7., 24 / 7.])
        obj_line4 = DashedLine(
            obj_line4_start,
            obj_line4_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line4.set_color(RED_C)
        obj_dot4 = Dot(feasible_points[3])
        obj_dot4.set_color(YELLOW_C)
        obj4 = VGroup(obj_line4, obj_dot4)
        self.play(
            FadeTransform(obj3, obj4),
            run_time=0.8
        )
        self.wait(2)

        obj4_text = Tex("$x_1 = \\frac{50}{7} \quad x_2 = \\frac{24}{7} \quad z = \\frac{170}{7} $")
        obj4_text.scale(0.6)
        obj4_text.set_color(YELLOW_C)
        obj4_text.move_to([0.5, 1, 0])
        self.play(
            TransformFromCopy(obj_dot4, obj4_text),
            run_time=0.8
        )
        self.wait(2)

        
        obj_line5_start, obj_line5_end = obj.line_coord([0, 7])
        obj_line5 = DashedLine(
            obj_line5_start,
            obj_line5_end,
            dash_length=0.1,
            dashed_ratio=0.75
        )
        obj_line5.set_color(RED_C)
        obj_dot5 = Dot(feasible_points[4])
        obj_dot5.set_color(YELLOW_C)
        obj5 = VGroup(obj_line5, obj_dot5)
        self.play(
            FadeTransform(obj4, obj5),
            run_time=0.8
        )
        self.wait(2)

        obj5_text = Tex("$x_1 = 0 \quad x_2 = 7 \quad z = 35 $")
        obj5_text.scale(0.6)
        obj5_text.set_color(YELLOW_C)
        obj5_text.move_to([0.5, 0.5, 0])
        self.play(
            TransformFromCopy(obj_dot5, obj5_text),
            run_time=0.8
        )
        self.wait(2)

        
        optimal_x1_text = Tex("$x_1^* = 0$")
        optimal_x2_text = Tex("$x_2^* = 7$")
        optimal_z_text = Tex("$z^* = 35$")
        optimal_x1_text.move_to([0.5, 1.9, 0])
        optimal_x2_text.move_to([0.5, 1.1, 0])
        optimal_z_text.move_to([0.5, 0.3, 0])
        optimal_solution_text = VGroup(optimal_x1_text, optimal_x2_text, optimal_z_text)
        optimal_solution_text.scale(1)
        optimal_solution_text.set_color(TEAL_C)
        
        self.play(
            FadeOut(obj1_text), FadeOut(obj2_text), FadeOut(obj3_text), FadeOut(obj4_text),
            ReplacementTransform(obj5_text, optimal_solution_text),
            run_time=0.8
        )
        self.wait(2)

        box = Rectangle(height=2.5, width=2, stroke_color=TEAL_A)
        box.move_to(optimal_solution_text.get_center())
        optimal_solution_title = Tex("$Optimal \  Solution:$")
        optimal_solution_title.set_color(MAROON_A)
        optimal_solution_title.scale(0.6)
        optimal_solution_title.move_to([0.5, 2.8, 0])
        self.play(Write(VGroup(box, optimal_solution_title)))
        self.wait(2)
