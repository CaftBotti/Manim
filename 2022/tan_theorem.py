from manimlib.imports import *
from manimlib.once_useful_constructs.region import *


class IntroduceTanTheorem(TeacherStudentsScene):
    def construct(self):
        self.change_student_modes('happy', 'hooray', 'tease')
        self.teacher_says(
            'Maybe you have heard \\\\the $\\tan$(a+b) theorem',
            target_mode='speaking'
        )
        self.wait(3)
        self.play(RemovePiCreatureBubble(self.teacher, target_mode='happy'))
        self.play(
            Write(
                TexMobject(
                    r'\tan {(a+b)=}\frac{\tan a+\tan b}{1-\tan a \times \tan b}'
                ).move_to(UP * 2).scale(1.3)
            )
        )
        self.wait(2)
        self.teacher_says(
            "Let's proof it today"
        )
        self.change_student_modes(
            'erm', 'happy', 'thinking'
        )
        self.wait(2)
        self.teacher_says(
            'We will use geometry \\\\ to make it interesting!'
        )
        self.change_student_modes(
            'well', 'hooray', 'hesitant'
        )
        self.wait(2)
        self.student_says(
            "Let's go!",
            student_index=2,
            target_mode='happy'
        )
        self.wait(2)
        for object in self.mobjects:
            self.play(
                FadeOut(
                    object
                )
            )


class Proof(Scene):
    def construct(self):
        main_square = Square()
        main_square.scale(3)
        point_r = np.array([-3, -3, 0])
        point_p = np.array([-3, 3, 0])
        point_q = np.array([3, 3, 0])
        point_t = np.array([3, 0, 0])
        point_u = np.array([1.5, 3, 0])
        rt = Line(
            start=point_r, end=point_t
        )
        pq = Line(
            start=point_p, end=point_q
        )
        ru = Line(
            start=point_r, end=point_u
        )
        arc_r = Arc(angle=53.130102354156 * DEGREES).move_to(np.array([-2.6, -2.78, 0]))
        arc_r.scale(0.5)
        arc_u = Arc(angle=53.130102354156 * DEGREES).move_to(np.array([1.12, 2.79, 0]))
        arc_u.scale(0.5)
        arc_t = Arc(angle=26.565051177078 * DEGREES).move_to(np.array([2.88, 0.49, 0]))
        arc_t.scale(0.5)
        arc_t.rotate(90 * DEGREES)
        arc_u.rotate(180 * DEGREES)
        ut = Line(
            start=point_t, end=point_u
        )
        number_plane = NumberPlane()

        a_mark_r = TexMobject('a').move_to(np.array([-2.16, -2.83, 0]))
        a_mark_r.scale(0.8)

        a_mark_t = TexMobject('a').move_to(np.array([2.78, 0.94, 0]))
        a_mark_t.scale(0.8)

        b_mark_r = TexMobject('b').move_to(np.array([-2.35, -2.48, 0]))
        b_mark_r.scale(0.8)

        ab_mark_u = TexMobject('a+b').move_to(np.array([0.46, 2.62, 0]))
        ab_mark_u.scale(0.8)

        side_length = TextMobject('1').move_to(np.array([0, -3.26, 0]))

        tan_a_ts = TextMobject('$\\tan a$').rotate(90 * DEGREES, axis=IN).set_color(WHITE)
        tan_a_ts.move_to(np.array([3.5, -1.5, 0]))

        tan_b_qt = TextMobject('$\\tan b$').rotate(90 * DEGREES, axis=IN).set_color(WHITE)
        tan_b_qt.move_to(np.array([3.5, 1.5, 0]))

        tan_a_tan_b_uq = TextMobject('$\\tan a\\times\\tan b$').scale(0.5)
        tan_a_tan_b_uq.move_to(np.array([2.25, 3.25, 0]))

        one_minus_tan_a_tan_b_pu = TextMobject('$1-\\tan a\\tan b$').scale(0.75)
        one_minus_tan_a_tan_b_pu.move_to(np.array([-0.75, 3.25, 0]))

        one_div_cos_a_rt = TextMobject('$\\frac{1}{\\cos a}$')
        one_div_cos_a_rt.move_to(np.array([0, -1, 0]))
        one_div_cos_a_rt.rotate(26.565051177078 * DEGREES)

        tan_b_div_cos_a_ut = TextMobject('$\\frac{\\tan b}{\\cos a}$')
        tan_b_div_cos_a_ut.move_to(np.array([1.65, 1.3, 0]))

        # Debugging
        self.add(number_plane, main_square, arc_u, arc_t, arc_r, ru, rt, pq, ut, ab_mark_u, a_mark_t, a_mark_r,
                 b_mark_r, side_length, tan_a_ts, tan_b_qt, tan_a_tan_b_uq, one_minus_tan_a_tan_b_pu,
                 one_div_cos_a_rt, tan_b_div_cos_a_ut)
