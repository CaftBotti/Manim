#!/usr/bin env python

class Arithmetics(Scene):
    def construct(self):
        # t = text
        # f = formula
        title = Text('Basic arithmetics',
                     color=YELLOW,
                     font='HGB4_CNKI').scale(2.3)
        copyright = Text('Made by CaftBotti',
                         t2c={'CaftBotti': YELLOW},
                         font='HGB4_CNKI').scale(2)
        eq1 = Text('1+1=2',
                   font='HGB4_CNKI').scale(2)
        eq2 = Text('18+102=120',
                   font='HGB4_CNKI').scale(2)
        eq3 = Text('7-2=5',
                   font='HGB4_CNKI').scale(2)
        eq4 = Text('6-15=-9',
                   font='HGB4_CNKI').scale(2)
        eq5 = TexMobject(r'2\times 3=6',
                         font='HGB4_CNKI').scale(2)
        eq5.to_edge(DOWN, buff=1.5)
        eq6 = TexMobject(r'16\times 23=368',
                         font='HGB4_CNKI').scale(2)
        eq7 = TexMobject(r'6/3=2',
                         font='HGB4_CNKI').scale(2)
        eq7.to_edge(DOWN, buff=1.5)
        eq8 = TexMobject(
            r'195/37\approx 2.702',
            font='HGB4_CNKI').scale(2)
        eq9 = TexMobject(
            r'\sqrt{26} \approx 5.099',
            font='HGB4_CNKI').scale(2)
        eq9.to_edge(DOWN, buff=1.5)
        eq10 = TexMobject(
            r'\sqrt{578} \approx 24.041',
            font='HGB4_CNKI').scale(2)
        eq11 = TexMobject(
            r'\sqrt[3]{1892} \approx 12.368',
            font='HGB4_CNKI').scale(2)
        eq11.to_edge(DOWN, buff=1.5)
        eq12 = TexMobject(
            r'\sqrt[3]{27} =3',
            font='HGB4_CNKI').scale(2)
        eq13 = TexMobject(
            r'3^{5} =243',
            font='HGB4_CNKI').scale(2)
        eq13.to_edge(DOWN, buff=1.5)
        eq14 = TexMobject(
            r'7^{6} =117649',
            font='HGB4_CNKI').scale(2)
        t1 = Text('Additions',
                  font='HGB4_CNKI',
                  color=YELLOW).scale(2)
        t2 = Text('Subtractions',
                  font='HGB4_CNKI',
                  color=YELLOW).scale(2)
        t3 = Text('Multiplications',
                  font='HGB4_CNKI',
                  color=YELLOW).scale(2)
        t3.to_edge(UP, buff=1.5)
        t4 = Text('Divisions',
                  font='HGB4_CNKI',
                  color=YELLOW).scale(2)
        t4.to_edge(UP, buff=1.5)
        t5 = Text('Square roots',
                  font='HGB4_CNKI',
                  color=GREEN).scale(2)
        t5.to_edge(UP, buff=1.5)
        t6 = Text('Cube roots',
                  font='HGB4_CNKI',
                  color=GREEN).scale(2)
        t6.to_edge(UP, buff=1.5)
        t7 = Text('Powers',
                  font='HGB4_CNKI',
                  color=BLUE).scale(2)
        t7.to_edge(UP, buff=1.5)
        # f1 = TexMobject('a^{2} +b^{2}=c^{2}',
        #                 font='HGB4_CNKI',
        #                 color=BLUE).scale(2)
        self.add_sound('beautiful', gain=-11)

        self.play(FadeIn(copyright))
        self.wait(5)
        self.play(FadeOut(copyright))

        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        self.play(Write(t1))
        self.wait(1)
        self.play(t1.move_to, UP * 2)
        self.play(Write(eq1))
        self.wait(1)
        self.play(eq1.move_to, DOWN * 2)
        self.wait(1)
        self.play(Write(eq2))
        self.wait(3)
        self.remove(t1, eq1, eq2)

        self.play(Write(t2))
        self.wait(1)
        self.play(t2.move_to, UP * 2)
        self.play(Write(eq3))
        self.wait(1)
        self.play(eq3.move_to, DOWN * 2)
        self.wait(1)
        self.play(Write(eq4))
        self.remove(t2, eq1, eq2)

        self.play(Transform(t2, t3))
        self.wait(1)
        self.remove(eq1, eq3)
        self.play(Transform(eq3, eq5))
        self.remove(eq2, eq4)
        self.play(Transform(eq4, eq6))
        self.wait(3)
        self.remove(t2)
        # self.remove(t2, eq3, eq4),

        # Lessons:
        # (USE CTRL + / TO ADD OR DELETE COMMENTS OF A PART)
        # The connections of elements are like this:
        #
        # time   text                eq(1)             eq(2)
        #         1#
        #   -      |trans to 2#       1#
        #   |      |                  |trans to 2#      1#
        #   |      |                  |                  |trans to 2#
        #   |      |trans to 3#       |                  |
        #   +      |                  |trans to 3#       |
        #          |                  |                  |trans to 3#
        # If one text connects to 2 eqs, then the code will be like this:
        # self.play(Write(t1))
        # self.wait(1)
        # self.play(t1.move_to, UP * 2)
        # self.play(Write(eq1))
        # self.wait(1)
        # self.play(eq1.move_to, DOWN * 2)
        # self.wait(1)
        # self.play(Write(eq2))
        # self.wait(3)
        # self.remove(t1, eq1, eq2)
        #
        # self.play(Write(t2))
        # self.wait(1)
        # self.play(t2.move_to, UP * 2)
        # self.play(Write(eq3))
        # self.wait(1)
        # self.play(eq3.move_to, DOWN * 2)
        # self.wait(1)
        # self.play(Write(eq4))
        # self.remove(t2, eq1, eq2)
        #
        # self.play(Transform(t2, t3))
        # self.wait(1)
        # self.remove(eq1, eq3)
        # self.play(Transform(eq3, eq5))
        # self.remove(eq2, eq4)
        # self.play(Transform(eq4, eq6))
        # self.wait(3)
        # self.remove(t2)
        #
        # self.play(Transform(t3, t4))
        # self.wait(1)
        # self.remove(eq3)
        # self.remove(eq5)  # = self.remove(eq3, eq5)
        # self.play(Transform(eq5, eq7))
        # self.remove(eq4, eq6)
        # self.play(Transform(eq6, eq8))
        # self.wait(3)
        # self.remove(t3)
        #
        # etc.
        #
        # If one text connects to 3 eqs, then the code will be like this:
        # self.play(Write(t1))
        # self.wait(1)
        # self.play(Write(eq1))
        # self.wait(1)
        # self.play(Write(eq2))
        # self.wait(1)
        # self.play(Write(eq3))
        # self.wait(3)
        # self.remove(t1, eq1, eq2, eq3)
        #
        # self.play(Write(t2))
        # self.wait(1)
        # self.play(Write(eq4))
        # self.wait(1)
        # self.wait(1)
        # self.play(Write(eq5))
        # self.wait(1)
        # self.play(Write(eq6))
        # self.remove(t2)
        #
        # self.play(Transform(t2, t3))
        # self.wait(1)
        # self.remove(eq1)
        # self.play(Transform(eq4, eq7))
        # self.remove(eq2)
        # self.play(Transform(eq5, eq8))
        # self.remove(eq3)
        # self.play(Transform(eq6, eq9))
        # self.wait(3)
        # self.remove(t2)
        #
        # self.play(Transform(t3, t4))
        # self.wait(1)
        # self.remove(eq4)
        # self.remove(eq7)  # = self.remove(eq4, eq7)
        # self.play(Transform(eq7, eq10))
        # self.remove(eq5, eq8)
        # self.play(Transform(eq8, eq11))
        # self.remove(eq6, eq9)
        # self.play(Transform(eq9, eq12))
        # self.wait(3)
        # self.remove(t3)
        #
        # etc.

        self.play(Transform(t3, t4))
        self.wait(1)
        self.remove(eq3)
        self.remove(eq5)  # = self.remove(eq3, eq5)
        self.play(Transform(eq5, eq7))
        self.remove(eq4, eq6)
        self.play(Transform(eq6, eq8))
        self.wait(3)
        self.remove(t3)
        # self.remove(t3, eq5, eq6),

        self.play(Transform(t4, t5))
        self.wait(1)
        self.remove(eq5)
        self.remove(eq7)  # = self.remove(eq5, eq7)
        self.play(Transform(eq7, eq9))
        self.remove(eq6, eq8)
        self.play(Transform(eq8, eq10))
        self.wait(3)
        self.remove(t4)
        # self.remove(t4, eq7, eq8),

        self.play(Transform(t5, t6))
        self.wait(1)
        self.remove(eq7)
        self.remove(eq9)
        self.play(Transform(eq9, eq11))
        self.remove(eq8, eq10)
        self.play(Transform(eq10, eq12))
        self.wait(3)
        self.remove(t5)
        # self.remove(t5, eq9, eq10),

        self.play(Transform(t6, t7))
        self.wait(1)
        self.remove(eq9)
        self.remove(eq11)
        self.play(Transform(eq11, eq13))
        self.remove(eq10, eq12)
        self.play(Transform(eq12, eq14))
        self.wait(3)
        self.remove(t6, eq11, eq12)
