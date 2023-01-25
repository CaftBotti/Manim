from manimlib.imports import *


class SineEg(GraphScene, MovingCameraScene, GetIntersections):
    CONFIG = {
        'max_val': {
            "x_min": -20,
            "x_max": 20,
            "y_min": -20,
            "y_max": 20
        },
        'x_axis_label': '',
        'y_axis_label': '',
        "graph_origin": ORIGIN,
        "y_line_frequency": 1,
        "x_line_frequency": 1,
        "axes_color": '#999999',
        "x_min": -20,
        "x_max": 20, "y_min": -20,
        "y_max": 20,
        "x_axis_width": 80,
        "y_axis_height": 80,
        'get_axis': 0,
        'x_labeled_nums': range(-20, 20, 1),
        'y_labeled_nums': range(-20, 20, 1),
        "camera_config": {
            "camera_frame_rate": 100
        }
    }
    def setup(self):
        MovingCameraScene.setup(self)
    def construct(self):
        RUN_TIME = 100
        ROTATE_DEGREE = 360
        self.camera_frame_rate = 100
        self.setup_axes(animate=True)
        circle = Circle(radius=2)
        circle.set_color(RED)
        moving_dot = Dot()
        moving_dot.move_to(RIGHT * 2)
        dot_x = Dot().move_to(RIGHT * 2)
        dot_y = Dot().move_to(UP * 2)
        line_x = Line()
        line_y = Line()
        line_x.add_updater(
            lambda m: m.become(
                Line(start=np.array([moving_dot.get_x(), moving_dot.get_y(), 0]),
                    end=np.array([moving_dot.get_x(), 0, 0])).set_color(BLUE)
            )
        )
        line_y.add_updater(
            lambda m: m.become(
                Line(start=np.array([moving_dot.get_x(), moving_dot.get_y(), 0]), 
                    end=np.array([0, moving_dot.get_y(), 0])).set_color(GREEN)
            )
        )
        system = VGroup(line_y, line_x, moving_dot)
        vt_line_x = ValueTracker()
        vt_line_x.add_updater(
            lambda v: v.set_value(moving_dot.get_y())
        )
        vt_line_y = ValueTracker()
        vt_line_y.add_updater(
            lambda v: v.set_value(moving_dot.get_x())
        )
        sin = TextMobject('sin')
        sin.move_to(UP * 3.2)
        sin.set_color(BLUE)
        degree = ValueTracker()
        dec_degree1 = DecimalNumber(num_decimal_places=5, unit=r'^{\circ}')
        dec_degree1.set_color(YELLOW)
        dec_degree1.next_to(sin, direction=RIGHT)
        dec_degree1.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        eq1 = TextMobject('=')
        eq1.next_to(dec_degree1, direction=RIGHT, buff=0.8)
        cos = TextMobject('cos')
        cos.set_color(GREEN)
        cos.next_to(sin, direction=DOWN)
        dec_degree2 = DecimalNumber(num_decimal_places=5, unit=r'^{\circ}')
        dec_degree2.set_color(YELLOW)
        dec_degree2.next_to(cos, direction=RIGHT)
        dec_degree2.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        eq2 = TextMobject('=')
        eq2.next_to(dec_degree2, direction=RIGHT, buff=0.8)
        dec_x = DecimalNumber(vt_line_x.get_value(), num_decimal_places=8)
        dec_x.set_color(BLUE)
        dec_x.next_to(eq1, direction=RIGHT)
        # Choose this or the next: the first one may make much error and the 2nd is finer
        # dec_x.add_updater(lambda v: v.set_value(moving_dot.get_y() / 2))
        dec_x.add_updater(lambda v: v.set_value(math.sin(degree.get_value() * DEGREES)))
        dec_y = DecimalNumber(vt_line_y.get_value(), num_decimal_places=8)
        dec_y.set_color(GREEN)
        dec_y.next_to(eq2, direction=RIGHT)
        # dec_y.add_updater(lambda v: v.set_value(moving_dot.get_x() / 2))
        dec_y.add_updater(lambda v: v.set_value(math.cos(degree.get_value() * DEGREES)))
        tan = TextMobject('tan').move_to(LEFT * 5.4 + DOWN * 3)
        tan.set_color(PURPLE_A)
        dec_degree3 = DecimalNumber(num_decimal_places=5, unit=r'^{\circ}')
        dec_degree3.set_color(YELLOW)
        dec_degree3.next_to(tan, direction=RIGHT)
        dec_degree3.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        eq3 = TextMobject('=')
        eq3.next_to(dec_degree3, direction=RIGHT, buff=0.8)

        number = TextMobject('0.0000000000')
        frac_line = Line(start=np.array([- number.get_width() / 2, 0, 0]),
                         end=np.array([number.get_width() / 2, 0, 0]))
        frac_line.shift(UP * tan.get_y())
        dec_up = DecimalNumber(num_decimal_places=8)
        dec_up.set_color(BLUE)
        dec_up.next_to(frac_line, direction=UP)
        dec_down = DecimalNumber(num_decimal_places=8)
        dec_down.set_color(GREEN)
        dec_down.next_to(frac_line, direction=DOWN)
        dec_up.add_updater(
            lambda v: v.set_value(math.sin(degree.get_value() * DEGREES))
        )
        dec_down.add_updater(
            lambda v: v.set_value(math.cos(degree.get_value() * DEGREES))
        )
        equals = TextMobject('=')
        equals.next_to(frac_line, direction=RIGHT)
        dec_tan = DecimalNumber(num_decimal_places=8)
        dec_tan.set_color(PURPLE_A)
        dec_tan.next_to(equals, direction=RIGHT)
        dec_tan.add_updater(
            lambda v: v.set_value(math.tan(degree.get_value() * DEGREES))
        )
        rotating_line = Line()
        rotating_line.add_updater(
            lambda m: m.become(
                Line(start=ORIGIN, end=moving_dot.get_center()).set_color(YELLOW)
            )
        )
        static_line = Line(start=ORIGIN, end=RIGHT * 2)
        static_line.set_color(YELLOW)
        dec_angle_value = DecimalNumber(num_decimal_places=3, unit=r'^{\circ}')
        dec_angle_value.scale(0.5)
        dec_angle_value.move_to(RIGHT * 0.5)
        dec_angle_value.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        dec_angle_value_path = Arc(radius=1, start_angle=0, angle=PI, center=ORIGIN)
        dec_angle_value_path.set_opacity(0)
        angle_size = TextMobject('Angle size:')
        angle_size.move_to(UP * 3 + LEFT * 5.5)
        angle_size_dec = DecimalNumber(num_decimal_places=3, unit=r'^{\circ}')
        angle_size_dec.set_color(YELLOW)
        angle_size_dec.add_updater(
            lambda v: v.set_value(degree.get_value())
        )
        angle_size_dec.next_to(angle_size)
        line = Line(start=ORIGIN)
        
        def get_further_line(line, added_length_scale, start=line.get_start(), end=line.get_end(), *args, **kwargs):
            end_dot = Dot()
            end_dot.move_to(
                np.array([
                    (end[0] - start[0]) * added_length_scale,
                    (end[1] - start[1]) * added_length_scale,
                    (end[2] - start[2]) * added_length_scale,
                ])
            )
            return Line(start=start, end=end_dot.get_center())
          
        final_line = Line()
        final_line.add_updater(
            lambda m: m.become(
                get_further_line(line=line, added_length_scale=50, end=moving_dot.get_center()).set_color(YELLOW)
            )
        )
        rotating_line2 = Line(start=ORIGIN, end=LEFT * 2)
        moving_dot2 = Dot()
        moving_dot2.move_to(LEFT * 2)
        moving_dot2.set_opacity(0)
        rotating_line2.add_updater(
            lambda m: m.become(
                Line(start=ORIGIN, end=moving_dot.get_center()).set_color(YELLOW)
            )
        )
        line2 = Line(start=ORIGIN)
        final_line2 = Line()
        final_line2.add_updater(
            lambda m: m.become(
                get_further_line(line=line2, added_length_scale=50, end=moving_dot2.get_center())\
                .set_color(YELLOW).set_opacity(0.5)
            )
        )
        circle2 = Circle()
        circle2.rotate(PI)

        tan_line = Line()
        tan_line.add_updater(
            lambda m: m.become(
                Line(start=RIGHT * 2, end=RIGHT * 2 + UP * math.tan(degree.get_value() * DEGREES) * 2)\
                .set_color(PURPLE_A)
            )
        )
        
        #self.add(final_line, final_line2, dec_degree1, tan_line)
        self.play(Write(circle))
        self.wait(2)
        self.play(Write(system))
        self.play(FadeIn(VGroup(dec_x, dec_y, sin, cos, tan, dec_degree1, dec_degree2, dec_degree3,
                 dec_tan, dec_up, dec_down, equals, frac_line, rotating_line, dec_angle_value_path, dec_angle_value,
                 angle_size_dec, angle_size, eq1, eq2, eq3, static_line, final_line2, final_line, tan_line)))
        self.wait(2)
        self.play(degree.set_value, ROTATE_DEGREE, MoveAlongPath(moving_dot, circle), run_time=RUN_TIME, rate_func=linear,
                 *[MoveAlongPath(moving_dot2, circle2, run_time=RUN_TIME, rate_func=linear,)],
                 *[MoveAlongPath(dec_angle_value, dec_angle_value_path, run_time=RUN_TIME, rate_func=linear)]
        )
        self.wait(2)
