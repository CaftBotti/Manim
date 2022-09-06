#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Made by CaftBotti
# This is my first manim python animation file.  17:34 11/08/2022 DD MM YYYY

# Importing

import math
from manimlib.imports import *
from from_3b1b.active.diffyq.part2.fourier_series import *
from from_3b1b.active.diffyq.part4.fourier_series_scenes import *
from manimlib.fourier import *
from manimlib.mobject.mobject import *
from manimlib.mobject.coordinate_systems import *
# from manimlib.coordinate_systems2 import *
# from manimlib.coordinate_systems3 import *

import numpy as np
from pydub import AudioSegment
import shutil
import subprocess
import os
import _thread as thread
from time import sleep
import datetime

import manimlib.constants as consts
from manimlib.constants import FFMPEG_BIN
from manimlib.constants import STREAMING_IP
from manimlib.constants import STREAMING_PORT
from manimlib.constants import STREAMING_PROTOCOL
from manimlib.utils.config_ops import digest_config
from manimlib.utils.file_ops import guarantee_existence
from manimlib.utils.file_ops import add_extension_if_not_present
from manimlib.utils.file_ops import get_sorted_integer_files

import sys

sys.setrecursionlimit(80000)


class Ani1(Scene):
    def construct(self):
        # Define variables
        text = TexMobject('3*3=9')
        # Animations
        self.play(Write(text))
        self.wait(3)


class Ani2(Scene):
    def construct(self):
        # Define variables
        text = TexMobject('1+1=2')
        # Animations
        self.play(FadeOut(text))
        self.wait(3)


class Ani3(Scene):
    def construct(self):
        # Define variables
        text = TexMobject('3+3=6')
        # Animations
        self.play(FadeIn(text))
        self.wait(3)


class Ani4(Scene):
    def construct(self):
        # Define variables
        text = TexMobject('My~name~is~baby')
        text2 = TexMobject('I~love~maths')
        text3 = TexMobject('XD')
        text4 = TexMobject('Crescendo~makes~it~easy~for~composers~and~hobbyists~to')
        text5 = TexMobject('create~musical~scores~using~their~keyboard~and~mouse.')
        text6 = TexMobject('Simply~select~the~Lyrics~tool~from~the~toolbar~to~the')
        text7 = TexMobject('right~of~your~score,~then~click~to~place~the~first~lyric.')
        text8 = TexMobject('Tab~or~space~to~move~to~the~next~lyric.')
        text9 = TexMobject('As~you~see,texts~can~move.')
        text10 = Text('Give me a like :)',
                      color=YELLOW,
                      font='HGB4_CNKI').scale(2)
        # Animations
        self.play(Write(text))
        self.wait(3)
        self.remove(text)
        self.play(Write(text2))
        self.wait(3)
        self.remove(text2)
        self.play(Write(text3))
        self.wait(3)
        self.remove(text3)
        self.play(Write(text4))
        self.wait(1)
        self.remove(text4)
        self.play(Write(text5))
        self.wait(5)
        self.remove(text5)
        self.play(Write(text6))
        self.wait(1)
        self.remove(text6)
        self.play(Write(text7))
        self.wait(5)
        self.remove(text7)
        self.play(Write(text8))
        self.wait(3)
        self.play(text8.move_to, UP * 2)
        self.wait(2)
        self.play(Write(text9))
        self.wait(2)
        self.play(text9.move_to, DOWN * 2)
        self.wait(2)
        self.play(Write(text10))
        self.wait(5)


class Ani5(ThreeDScene):
    def construct(self):
        # Define variables
        copyright = Text('Made by CaftBotti',
                         font='HGB4_CNKI',
                         t2c={'CaftBotti': YELLOW}).scale(2)
        text1 = Text('This is a point',
                     color=YELLOW,
                     font='HGB4_CNKI').scale(2)
        text2 = Text('This is a line',
                     color=YELLOW,
                     font='HGB4_CNKI').scale(2)
        # text3 = Text('This is a plot',
        #             color=YELLOW,
        #             font='HGB4_CNKI').scale(2)
        text = Text('This is a square',
                    color=YELLOW,
                    font='HGB4_CNKI').scale(2)
        txt1 = Text('This is a circle',
                    color=BLUE,
                    font='HGB4_CNKI').scale(2)
        txt2 = Text('This is a triangle',
                    color=BLUE,
                    font='HGB4_CNKI').scale(2)
        txt2.to_edge(UP, buff=1)
        txt3 = Text('This is another triangle',
                    color=BLUE,
                    font='HGB4_CNKI').scale(2)
        txt3.to_edge(UP, buff=1.5)
        txt4 = Text('This is an ellipse',
                    color=GREEN,
                    font='HGB4_CNKI').scale(2)
        txt4.to_edge(UP, buff=1.5)
        txt5 = Text('This is a quadrangle',
                    color=GREEN,
                    font='HGB4_CNKI').scale(2)
        txt5.to_edge(UP, buff=1.5)
        txt6 = Text('This is a cube',
                    color=PURPLE,
                    font='HGB4_CNKI').scale(2)
        txt6.to_edge(UP, buff=1.5)
        txt7 = Text('This is a sphere',
                    color=YELLOW,
                    font='HGB4_CNKI').scale(2)
        txt7.to_edge(UP, buff=1.5)
        txt8 = Text('Thanks for watching!',
                    color=YELLOW,
                    font='HGB4_CNKI',
                    t2c={'T': RED,
                         'h': ORANGE,
                         'a': YELLOW,
                         'n': GREEN,
                         'k': WHITE,
                         's': BLUE,
                         'f': PURPLE,
                         'o': GRAY,
                         'r': YELLOW,
                         'w': GREEN,
                         'c': WHITE,
                         't': PURPLE,
                         'i': RED,
                         'g': ORANGE}).scale(1.5)
        dot1 = Dot(
            color=BLUE
        )
        line1 = Line(
            start=[-1, 0, 0],
            end=[1, 0, 0]
        )
        sq1 = Square()
        cir1 = Circle(
            color=WHITE
        )
        tri1 = Triangle(
            color=WHITE
        )
        p1 = np.array([-1, -1.2, 0])
        p2 = np.array([1.5, -1.2, 0])
        p3 = np.array([2, 1, 0])
        p4 = np.array([-3, 0.3, 0])
        tri2 = Polygon(p1, p2, p3)
        elli1 = Ellipse(
            width=2.0,
            height=1.1,
            color=YELLOW
        )
        sq2 = Polygon(p1, p2, p3, p4)
        sq2.set_stroke(color=YELLOW)
        cube1 = Cube(side_length=2,
                     fill_color=BLUE,
                     stroke_color=BLACK,
                     stroke_width=3)
        sph1 = Sphere()
        # plot1 = {
        #     'y_max': 50,
        #     'y_min': 0,
        #     'x_max': 50,
        #     'x_min': 0,
        #     'y_tick_frequency': 5,
        #     'x_tick_frequency': 5,
        #     'axes_color': BLUE,
        # }
        # Animations
        # -----------------
        self.add_sound('beautiful', gain=-11)
        self.play(FadeIn(copyright))
        self.wait(5)
        self.play(FadeOut(copyright))

        self.play(Write(text1))
        self.wait(1)
        self.play(text1.move_to, UP * 2)

        self.play(Write(dot1))
        self.wait(3)

        self.remove(text1)
        self.remove(dot1)

        # -----------------
        self.play(Write(text2))
        self.wait(1)
        self.play(text2.move_to, UP * 2)

        self.play(Write(line1))
        self.wait(3)

        self.remove(text2)
        self.remove(line1)

        # -----------------
        # self.play(Write(text3))
        # self.wait(1)
        # self.play(text3.move_to, UP * 2)

        # self.play(Write(plot1))
        # self.wait(3)

        # self.remove(text3)
        # self.remove(plot1)

        # -----------------
        self.play(Write(text))
        self.wait(1)
        self.play(text.move_to, UP * 2)
        self.play(Write(sq1))

        self.play(FadeOut(text))
        self.play(FadeOut(sq1))

        # -----------------
        self.play(Write(txt1))
        self.wait(1)
        self.play(txt1.shift, UP * 2)

        self.play(Write(cir1))
        self.wait(3)
        self.remove(txt1)

        self.play(Transform(txt1, txt2))
        self.wait(1)
        self.play(Transform(cir1, tri1))
        self.wait(3)
        self.remove(txt1)

        self.play(Transform(txt2, txt3))
        self.wait(1)
        self.play(Transform(cir1, tri2))
        self.wait(3)
        self.remove(txt2)

        # -----------------
        self.play(Transform(txt3, txt4))
        self.wait(1)
        self.remove(cir1), self.play(Transform(tri2, elli1))

        self.wait(3)
        self.remove(txt3)

        # -----------------
        self.play(Transform(txt4, txt5))
        self.wait(1)
        self.remove(tri2), self.play(Transform(elli1, sq2))

        self.wait(3)
        self.remove(txt4)

        # -----------------
        self.play(Transform(txt5, txt6))
        self.wait(1)
        self.remove(elli1), self.play(Transform(sq2, cube1))
        self.move_camera(phi=40 * DEGREES, theta=0 * DEGREES)

        self.wait(3)
        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0 * DEGREES)
        self.reset_camera()
        self.remove(txt5)

        # -----------------
        self.play(Transform(txt6, txt7))
        self.wait(1)
        self.remove(sq2), self.play(Transform(cube1, sph1))
        self.move_camera(phi=40 * DEGREES, theta=0 * DEGREES)

        self.wait(2)
        self.reset_camera()
        self.play(txt6.move_to, LEFT * 2)
        self.move_camera(phi=0 * DEGREES, gamma=0 * DEGREES)
        self.play(Rotating(txt6, radians=0.5 * PI, axis=OUT, run_time=2))
        self.wait(3)
        self.play(FadeOut(txt6))
        self.play(FadeOut(cube1))

        # -----------------
        self.move_camera(gamma=90 * DEGREES)
        self.play(Write(txt8, rotate=0.5 * PI, axis=OUT))
        self.wait(5)


class Ani6(Scene):
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


class Test(Scene):
    def construct(self):
        # title = Text('Basic arithmetics',
        #              color=YELLOW,
        #              font='HGB4_CNKI').scale(2.3)
        # copyright = Text('Made by CaftBotti',
        #                  t2c={'CaftBotti': YELLOW},
        #                  font='HGB4_CNKI').scale(2)
        eq1 = Text('1+1=2',
                   font='HGB4_CNKI').scale(0.3)
        eq1.to_edge(DOWN, buff=2.2)
        eq2 = Text('18+102=120',
                   font='HGB4_CNKI').scale(0.3)
        eq2.to_edge(DOWN, buff=2.6)
        eq3 = Text('7-2=5',
                   font='HGB4_CNKI').scale(0.3)
        eq3.to_edge(DOWN, buff=3)
        eq4 = Text('6-15=-9',
                   font='HGB4_CNKI').scale(0.3)
        eq4.to_edge(DOWN, buff=1.9)
        eq5 = TexMobject(r'2\times 3=6',
                         font='HGB4_CNKI').scale(0.3)
        eq5.to_edge(DOWN, buff=1)
        eq6 = TexMobject(r'16\times 23=368',
                         font='HGB4_CNKI').scale(0.3)
        eq6.to_edge(DOWN, buff=3.5)
        eq7 = TexMobject(r'6/3=2',
                         font='HGB4_CNKI').scale(0.3)
        eq7.to_edge(DOWN, buff=1.2)
        eq8 = TexMobject(
            r'195/37\approx 2.702',
            font='HGB4_CNKI').scale(0.3)
        eq8.to_edge(DOWN, buff=0.8)
        eq9 = TexMobject(
            r'\sqrt{26} \approx 5.099',
            font='HGB4_CNKI').scale(0.3)
        eq9.to_edge(DOWN, buff=1.5)
        eq10 = TexMobject(
            r'\sqrt{578} \approx 24.041',
            font='HGB4_CNKI').scale(0.3)
        eq10.to_edge(DOWN, buff=4)
        eq11 = TexMobject(
            r'\sqrt[3]{1892} \approx 12.368',
            font='HGB4_CNKI').scale(0.3)
        eq11.to_edge(DOWN, buff=0.1)
        eq12 = TexMobject(
            r'\sqrt[3]{27} =3',
            font='HGB4_CNKI').scale(0.3)
        eq12.to_edge(DOWN, buff=1.1)
        eq13 = TexMobject(
            r'3^{5} =243',
            font='HGB4_CNKI').scale(0.3)
        eq13.to_edge(DOWN, buff=0.5)
        # eq14 = TexMobject(
        #     r'7^{6} =117649',
        #     font='HGB4_CNKI').scale(2)
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
        self.play(Write(t1))
        self.wait(1)
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
        self.play(Write(eq3))
        self.wait(3)
        self.remove(t1, eq1, eq2, eq3)

        self.play(Write(t2))
        self.wait(1)
        self.play(Write(eq4))
        self.wait(1)
        self.wait(1)
        self.play(Write(eq5))
        self.wait(1)
        self.play(Write(eq6))
        self.remove(t2)

        self.play(Transform(t2, t3))
        self.wait(1)
        self.remove(eq1)
        self.play(Transform(eq4, eq7))
        self.remove(eq2)
        self.play(Transform(eq5, eq8))
        self.remove(eq3)
        self.play(Transform(eq6, eq9))
        self.wait(3)
        self.remove(t2)

        self.play(Transform(t3, t4))
        self.wait(1)
        self.remove(eq4)
        self.remove(eq7)  # = self.remove(eq4, eq7)
        self.play(Transform(eq7, eq10))
        self.remove(eq5, eq8)
        self.play(Transform(eq8, eq11))
        self.remove(eq6, eq9)
        self.play(Transform(eq9, eq12))
        self.wait(3)
        self.remove(t3)


class Ani8(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': WHITE
        },
        'max_val': {
            "x_min": -100,
            "x_max": 100,
            "y_min": -100,
            "y_max": 100
        },
        "graph_origin": ORIGIN,
        "y_line_frequency": 1,
        "x_line_frequency": 1,
        "axes_color": BLUE,
        "x_min": -100,
        "x_max": 100, "y_min": -100,
        "y_max": 100,
        "x_axis_width": 200,
        "y_axis_height": 200,
        'get_axis': 0,
        'x_labeled_nums': range(-100, 100, 1),
        'y_labeled_nums': range(-100, 100, 1)
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
        # MUST BE ADDED IF 2 OR MORE SCENES TOGETHER!

    def construct(self):
        title = Text('Function Graphs',
                     color=YELLOW,
                     font='HGB4_CNKI').scale(2.3)
        copyright = Text('Made by CaftBotti',
                         t2c={'CaftBotti': YELLOW},
                         font='HGB4_CNKI').scale(2)
        dot = Dot()

        t1 = Text('y=x',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t1.move_to([-5.3, 3, 0])
        t2 = Text('y=x+1',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t2.move_to([-5.3, 3, 0])
        t3 = Text('y=2x',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t3.move_to([-5.3, 3, 0])
        t4 = Text('y=2x+1',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t4.move_to([-5.3, 3, 0])
        t5 = Text('y=-x',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t5.move_to([-5.3, 3, 0])
        t6 = Text('y=-3x',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t6.move_to([-5.3, 3, 0])
        t7 = Text('y=-3x-2',
                  font='HGB4_CNKI',
                  slant=ITALIC).scale(1)
        t7.move_to([-5.3, 3, 0])
        t8 = TexMobject('y & = x^{2}',
                        font='HGB4_CNKI',
                        slant=ITALIC).scale(1)
        t8.move_to([-5.3, 3, 0])
        t9 = TexMobject(
            'y & = x^{2}+1',

            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t9.move_to([-5.3, 3, 0])
        t10 = TexMobject(
            'y & = x^{3}',

            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t10.move_to([-5.3, 3, 0])
        t11 = TexMobject(
            r'y = \frac{\cos y}{\tan xy} ',

            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t11.move_to([-5.3, 3, 0])
        t11 = TexMobject(
            r'y = \frac{\cos y}{\tan xy} ',

            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t11.move_to([-5.3, 3, 0])
        t12 = TexMobject(
            r'y = \frac{\cos x}{\tan 8} +\frac{\sin \cos x^{6}\sin x }{\sin 590^{2} +61^{8}}     ',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t12.move_to([-3, 3, 0])
        t13 = TexMobject(
            r'x \bmod x^{25}>0.3  ',

            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t13.move_to([-5.3, 3, 0])
        t14 = TexMobject(
            r'y=\log_{3}{x^{\pi}}',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t14.move_to([-5.3, 3, 0])
        t15 = TexMobject(
            r'y=\sin x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t15.move_to([-5.3, 3, 0])
        t16 = TexMobject(
            r'y=\cos x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t16.move_to([-5.3, 3, 0])
        t17 = TexMobject(
            r'y=\tan x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t17.move_to([-5.3, 3, 0])
        t18 = TexMobject(
            r'y=\sinh x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t18.move_to([-5.3, 3, 0])
        t19 = TexMobject(
            r'y=\cosh x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t19.move_to([-5.3, 3, 0])
        t20 = TexMobject(
            r'y=\tanh x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t20.move_to([-5.3, 3, 0])
        t21 = TexMobject(
            r'y=\frac {\sin x}{\tan 8}',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t21.move_to([-5.3, 3, 0])
        t22 = TexMobject(
            r'y=\sin \cos x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t22.move_to([-5.3, 3, 0])
        t23 = TexMobject(
            r'y=\sin \tan x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t23.move_to([-5.3, 3, 0])
        t24 = TexMobject(
            r'y=\sin \sin x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t24.move_to([-5.3, 3, 0])
        t25 = TexMobject(
            r'y=\sin \tan \cos x',
            font='HGB4_CNKI',
            slant=ITALIC).scale(1)
        t25.move_to([-5.3, 3, 0])
        thanks = Text('Thanks for watching!',
                      font='HGB4_CNKI', ).scale(2)
        # numberplane = NumberPlane(x_range = (0, 7),
        #     y_range = (0, 5),
        #     x_length = 7,
        #     axis_config={"include_numbers": True},)

        self.add_sound('beautiful')

        self.play(FadeIn(copyright))
        self.wait(5)
        self.play(FadeOut(copyright))
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        self.setup_axes(animate=True)

        func1 = self.get_graph(
            lambda x: x,
            color=GREEN,
            # x_min=-7,
            # x_max=7
        )
        func2 = self.get_graph(
            lambda x: x + 1,
            color=BLUE,
            # x_min=-7,
            # x_max=7
        )
        func3 = self.get_graph(
            lambda x: 2 * x,
            color=ORANGE,
            # x_min=-7,
            # x_max=7
        )
        func4 = self.get_graph(
            lambda x: 2 * x + 1,
            color=YELLOW,
            # x_min=-7,
            # x_max=7
        )
        func5 = self.get_graph(
            lambda x: -x,
            color=PURPLE,
            # x_min=-7,
            # x_max=7
        )
        func6 = self.get_graph(
            lambda x: -x * 3,
            color=RED,
            # x_min=-7,
            # x_max=7
        )
        func7 = self.get_graph(
            lambda x: -x * 3 - 2,
            color=WHITE,
            # x_min=-7,
            # x_max=7
        )
        func8 = self.get_graph(
            lambda x: x ** 2,
            color=BLUE,
            # x_min=-7,
            # x_max=7
        )
        func9 = self.get_graph(
            lambda x: x ** 2 + 1,
            color=GREEN,
            # x_min=-7,
            # x_max=7
        )
        func10 = self.get_graph(
            lambda x: x ** 3,
            color=YELLOW,
            # x_min=-7,
            # x_max=7
        )
        func11 = self.get_graph(
            lambda x: math.cos(x) / math.tan(5),
            color=MAROON_A,
            # x_min=-7,
            # x_max=7
        )
        func12 = self.get_graph(
            lambda x: math.cos(x) / math.tan(8) + math.sin(math.cos(x ** 6 * math.sin(x))) / math.sin(
                (590 ** 2) + (61 ** 8)),
            color=PURPLE_E,
            # x_min=-7,
            # x_max=7
        )
        func13 = self.get_graph(
            lambda x: x % x ** 25 > 0.3,
            color=GRAY,
            # x_min=-7,
            # x_max=7
        )
        func14 = self.get_graph(
            lambda x: np.log(x ** PI) / np.log(3),
            color=BLUE_B
        )
        func15 = self.get_graph(
            lambda x: math.sin(x),
            color=GREEN_C
        )
        func16 = self.get_graph(
            lambda x: math.cos(x),
            color=RED_C
        )
        func17 = self.get_graph(
            lambda x: math.tan(x),
            color=WHITE
        )
        func18 = self.get_graph(
            lambda x: math.sinh(x),
            color=YELLOW
        )
        func19 = self.get_graph(
            lambda x: math.cosh(x),
            color=ORANGE
        )
        func20 = self.get_graph(
            lambda x: math.tanh(x),
            color=BLUE_A
        )
        func21 = self.get_graph(
            lambda x: math.sin(x) / math.tan(8),
            color=MAROON_B
        )
        func22 = self.get_graph(
            lambda x: math.sin(math.cos(x)),
            color=GREEN_C
        )
        func23 = self.get_graph(
            lambda x: math.sin(math.tan(x)),
            color=GOLD_C
        )
        func24 = self.get_graph(
            lambda x: math.sin(math.sin(x)),
            color=RED_B
        )
        func25 = self.get_graph(
            lambda x: math.sin(math.tan(math.cos(x))),
            color=PURPLE
        )

        # self.play(Write(numberplane))

        self.play(Write(dot))

        self.play(FadeIn(t1))
        self.wait(2)
        self.play(Write(func1))

        self.wait(5)
        self.remove(t1)
        self.play(Transform(t1, t2))
        self.remove(func1)
        self.play(Transform(func1, func2))

        self.wait(5)
        self.remove(t1, t2)
        self.play(Transform(t2, t3))
        self.remove(func1, func2)
        self.play(Transform(func2, func3))

        self.wait(5)
        self.remove(t2, t3)
        self.play(Transform(t3, t4))
        self.remove(func2, func3)
        self.play(Transform(func3, func4))

        self.wait(5)
        self.remove(t3, t4)
        self.play(Transform(t4, t5))
        self.remove(func3, func4)
        self.play(Transform(func4, func5))

        self.wait(5)
        self.remove(t4, t5)
        self.play(Transform(t5, t6))
        self.remove(func4, func5)
        self.play(Transform(func5, func6))

        self.wait(5)
        self.remove(t5, t6)
        self.play(Transform(t6, t7))
        self.remove(func5, func6)
        self.play(Transform(func6, func7))

        self.wait(5)
        self.remove(t6, t7)
        self.play(Transform(t7, t8))
        self.remove(func6, func7)
        self.play(Transform(func7, func8))

        self.wait(5)
        self.remove(t7, t8)
        self.play(Transform(t8, t9))
        self.remove(func7, func8)
        self.play(Transform(func8, func9))

        self.wait(5)
        self.remove(t8, t9)
        self.play(Transform(t9, t10))
        self.remove(func8, func9)
        self.play(Transform(func9, func10))

        self.wait(5)
        self.remove(t9, t10)
        self.play(Transform(t10, t11))
        self.remove(func9, func10)
        self.play(Transform(func10, func11))

        self.wait(5)
        self.remove(t10, t11)
        self.play(Transform(t11, t12))
        self.remove(func10, func11)
        self.play(Transform(func11, func12))

        # self.wait(5)
        # self.remove(t11, t12)
        # self.play(Transform(t12, t13))
        # self.remove(func11, func12)
        # self.play(Transform(func12, func13))
        # # self.activate_zooming(animate=True)
        # self.camera_frame.save_state()
        # self.play(self.camera_frame.set_width, dot.get_width() * 200,
        #           self.camera_frame.move_to, dot)

        self.wait(5)
        self.remove(t11, t12)
        self.play(Transform(t12, t13))
        self.remove(func11, func12)
        self.play(Transform(func12, func13))

        # self.wait(5)
        # self.play(Restore(self.camera_frame))
        # self.remove(t12, t13)
        # self.play(Transform(t13, t14))
        # self.remove(func12, func13)
        # self.play(Transform(func13, func14))

        self.wait(5)
        self.remove(t12, t13)
        self.play(Transform(t13, t14))
        self.remove(func12, func13)
        self.play(Transform(func13, func14))
        self.wait(2)
        # self.activate_zooming(animate=True)
        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width, dot.get_width() * 500,
                  self.camera_frame.move_to, dot)

        self.wait(5)
        self.play(Restore(self.camera_frame))
        self.remove(t13, t14)
        self.play(Transform(t14, t15))
        self.remove(func13, func14)
        self.play(Transform(func14, func15))

        self.wait(5)
        self.remove(t14, t15)
        self.play(Transform(t15, t16))
        self.remove(func14, func15)
        self.play(Transform(func15, func16))

        self.wait(5)
        self.remove(t15, t16)
        self.play(Transform(t16, t17))
        self.remove(func15, func16)
        self.play(Transform(func16, func17))

        self.wait(5)
        self.remove(t16, t17)
        self.play(Transform(t17, t18))
        self.remove(func16, func17)
        self.play(Transform(func17, func18))

        self.wait(5)
        self.add_sound(r'C:\beibi\a\media\designs\sounds\indian', gain=-9)
        self.remove(t17, t18)
        self.play(Transform(t18, t19))
        self.remove(func17, func18)
        self.play(Transform(func18, func19))

        self.wait(5)
        self.remove(t18, t19)
        self.play(Transform(t19, t20))
        self.remove(func18, func19)
        self.play(Transform(func19, func20))

        self.wait(5)
        self.remove(t19, t20)
        self.play(Transform(t20, t21))
        self.remove(func19, func20)
        self.play(Transform(func20, func21))

        self.wait(5)
        self.remove(t20, t21)
        self.play(Transform(t21, t22))
        self.remove(func20, func21)
        self.play(Transform(func21, func22))

        self.wait(5)
        self.remove(t21, t22)
        self.play(Transform(t22, t23))
        self.remove(func21, func22)
        self.play(Transform(func22, func23))

        self.wait(5)
        self.remove(t22, t23)
        self.play(Transform(t23, t24))
        self.remove(func22, func23)
        self.play(Transform(func23, func24))

        self.wait(5)
        self.remove(t23, t24)
        self.play(Transform(t24, t25))
        self.remove(func23, func24)
        self.play(Transform(func24, func25))

        self.wait(5)
        self.remove(t23, t24)
        self.remove(func23, func24)
        self.play(FadeOut(dot))
        self.play(FadeOut(self.axes))
        self.play(Write(thanks))
        self.wait(3)


class DrawAnAxis(GraphScene, Scene, Axes):
    def setup(self):
        Scene.setup(self)
        GraphScene.setup(self)
        Axes.get_axes(self)

    CONFIG = {
        "graph_origin": ORIGIN,
        "y_line_frequency": 1,
        "x_line_frequency": 1,
        "axes_color": MAROON_A,
        "x_min": -3,
        "x_max": 3, "y_min": -10,
        "y_max": 10,
        "x_axis_width": 14,
        "y_axis_height": 8,

    }

    def construct(self):
        my_plane = NumberPlane(background_line_style={"stroke_color": GREEN, "stroke_opacity": 0.4})

        self.add(my_plane)
        self.setup_axes()
        self.wait()


class Plot1(GraphScene):
    CONFIG = {
        "y_max": 50,
        "y_min": 0,
        "x_max": 7,
        "x_min": 0,
        "y_tick_frequency": 5,
        "x_tick_frequency": 0.5,
        "axes_color": BLUE,
        "y_labeled_nums": range(0, 60, 10),
        "x_labeled_nums": list(np.arange(2, 7.0 + 0.5, 0.5)),
        "x_label_decimal": 1,
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal": 3
    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x: x ** 2,
                               color=GREEN,
                               x_min=2,
                               x_max=4
                               )
        self.play(
            ShowCreation(graph),
            run_time=2
        )
        self.wait()


class WhyWouldYouCare(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "Who cares!",
            target_mode="sassy",
            student_index=2,
            added_anims=[self.teacher.change, "guilty"],
        )
        self.wait()
        self.play(
            RemovePiCreatureBubble(self.students[2]),
            self.teacher.change, "raise_right_hand",
            self.get_student_changes(
                "pondering", "erm", "thinking",
                look_at_arg=self.screen,
            )
        )
        self.look_at(self.screen)
        self.wait(5)


class NumberLineExample(Scene):
    def construct(self):
        l0 = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        )

        l1 = NumberLine(
            x_range=[-10, 10, 2],
            unit_size=0.5,
            numbers_with_elongated_ticks=[-2, 4],
            include_numbers=True,
            font_size=24,
        )
        num6 = l1.numbers[8]
        num6.set_color(RED)

        l2 = NumberLine(
            x_range=[-2.5, 2.5 + 0.5, 0.5],
            length=12,
            decimal_number_config={"num_decimal_places": 2},
            include_numbers=True,
        )

        l3 = NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=10 * DEGREES,
        )

        line_group = VGroup(l0, l1, l2, l3).arrange(DOWN, buff=1)
        self.add(line_group)


class NumberPlaneExample(Scene):
    CONFIG = {
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        },
        "y_axis_config": {
            "label_direction": DR,
        },
        "background_line_style": {
            "stroke_color": BLUE_D,
            "stroke_width": 2,
            "stroke_opacity": 1,
        },
        # Defaults to a faded version of line_config
        "faded_line_style": None,
        "x_line_frequency": 1,
        "y_line_frequency": 1,
        "faded_line_ratio": 1,
        "make_smooth_after_applying_functions": True,
    }

    def construct(self):
        number_plane = NumberPlane()
        self.add(number_plane)


class NumberPlaneScaled(Scene):
    def construct(self):
        number_plane = NumberPlane(
            x_range=(-4, 11, 1),
            y_range=(-3, 3, 1),
            x_length=5,
            y_length=2,
        ).move_to(LEFT * 3)

        number_plane_scaled_y = NumberPlane(
            x_range=(-4, 11, 1),
            x_length=5,
            y_length=4,
        ).move_to(RIGHT * 3)

        self.add(number_plane)
        self.add(number_plane_scaled_y)


class CoordsToPointExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()

        # a dot with respect to the axes
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2, 2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((2, 2, 0), color=RED)

        self.add(plane, dot_scene, ax, dot_axes, lines)


class LineGraphExample(CoordinateSystem, Scene):
    def setup(self):
        Scene.setup(self)

    def construct(self):
        plane = NumberPlane(
            x_range=(0, 7),
            y_range=(0, 5),
            x_length=7,
            axis_config={"include_numbers": True},
        )
        plane.center()
        line_graph = plane.plot_line_graph(
            x_values=[0, 1.5, 2, 2.8, 4, 6.25],
            y_values=[1, 3, 2.25, 4, 2.5, 1.75],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3, fill_color=PURPLE),
            stroke_width=4,
        )
        self.add(plane, line_graph)


class ANP(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.play(Write(numberplane))


# class Ani9(Scene):
#     def construct(self):
#         func1 = lambda p: np.array([
#             p[2] / 2,
#             p[1] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
#             0
#         ])
#         func2 = lambda p: np.array([
#             p[1] / 3,
#             p[0] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
#             0
#         ])
#         vf1 = VectorField(func1)
#         vf2 = VectorField(func2)
#         self.play(*[GrowArrow(vec) for vec in vf1])
#         self.wait(3)
#
#         self.play(Transform(vf1, vf2))


class Ani11(FourierOfTexPaths):
    CONFIG = {
        'n_vectors': 50,
        'run_time': 10,
        'tex_class': TexMobject,
        'tex': r'\Sigma'
    }


class Ani12(FourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 20,
        'tex_class': TexMobject,
        'tex': r'\infty'
    }


class Ani13(FourierOfPaths):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 20,
        'tex_class': TexMobject,
        'tex': 'CaftBotti'

    }


class Ani14(FourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\sum',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'wait_before_start': 3
    }


class Ani15(FourierFromSVG):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 20,
        'n_cycles': 1,
        'file_name': 'PiCreatures_plain'
    }


class Ani16(FourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\prod',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'wait_before_start': 3
    }


class Ani17(FourierOfPaths):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 20,
        'tex_class': TextMobject,
        'tex': 'Caft Botti',
        'wait_before_start': 3
    }


class Ani18(FourierOfPaths):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 20,
        'tex_class': TextMobject,
        'tex': 'Caft Botti',
        'wait_before_start': 3,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR)
    }


class Ani19(FourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\mathrm{Caft~Botti}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'wait_before_start': 3
    }


class Ani20(AbstractFourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\mathrm{Caft~Botti}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ani21(FourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\mathrm{Caft~Botti}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(UL),
        'zoom_factor': 0.1,
        'scale_zoom_camera_to_full_screen': True,
        'zoom_camera_to_full_screen_config': {
            'run_time': 3,
            'func': smooth
        },
        'wait_before_start': 3
    }


class Ani22(AbstractFourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\mathrm{Caft~Botti}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(UL),
        'zoom_factor': 0.1,
        'scale_zoom_camera_to_full_screen': True,
        'zoom_camera_to_full_screen_config': {
            'run_time': 12,
            'func': lambda t: there_and_back_with_pause(t, 1 / 10)
        },
        'wait_before_start': 3
    }


class Ani23(FourierFromSVG):
    # Invalid
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'file_name': 'caftbotti',
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ani24(FourierFromSVG):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'file_name': 'caftbotti',
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'scale_zoom_camera_to_full_screen': True,
        'zoom_camera_to_full_screen_config': {
            'run_time': 12,
            'func': lambda t: there_and_back_with_pause(t, 1 / 10)
        },
        'wait_before_start': 3
    }


class Ani25(FourierOfTexSymbol):
    CONFIG = {
        'n_vectors': 120,
        'run_time': 100,
        'slow_factor': 0.05,
        'tex_class': TexMobject,
        'tex': r'\mathrm{Caft~Botti}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'scale_zoom_camera_to_full_screen': True,
        'zoom_camera_to_full_screen_config': {
            'run_time': 12,
            'func': lambda t: there_and_back_with_pause(t, 1 / 10)
        },
        'wait_before_start': 3
    }


class Zero(FourierOfPaths):
    CONFIG = {
        'n_vectors': 15,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '0',
        'time_per_symbol': 5,
        # 'file_name': '0',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class One(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '1',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Two(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '2',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Three(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '3',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Four(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '4',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Five(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '5',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Six(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '6',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Seven(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '7',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Eight(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '8',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Nine(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': '9',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class AC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'A',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class BC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'B',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class CC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'C',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class DC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'D',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class EC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'E',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class FC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'F',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'G',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class HC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'H',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class IC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'I',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class JC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'J',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class KC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'K',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class LC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'L',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class MC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'M',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class NC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'N',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class OC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'O',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class PC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'P',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class QC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'Q',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class RC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'R',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class SC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'S',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class TC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'T',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class UC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'U',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class VC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'V',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class WC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'W',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class XC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'X',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class YC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'Y',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class ZC(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'Z',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class AL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'a',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class BL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'b',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class CL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'c',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class DL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'd',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class EL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'e',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class FL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'f',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'g',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class HL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'h',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class IL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'i',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class JL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'j',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class KL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'k',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class LL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'l',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class ML(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'm',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class NL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'n',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class OL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'o',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class PL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'p',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class QL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'q',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class RL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'r',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class SL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 's',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class TL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 't',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class UL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'u',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class VL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'v',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class WL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'w',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class XL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'x',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class YL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'y',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class ZL(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TextMobject,
        'tex': 'z',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class La(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'a',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lb(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'b',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lc(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'c',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ld(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'd',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Le(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'e',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lf(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'f',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lg(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'g',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lh(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'h',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Li(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'i',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lj(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'j',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lk(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'k',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ll(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'l',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lm(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'm',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ln(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'n',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lo(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'o',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lp(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'p',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lq(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'q',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lr(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'r',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ls(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 's',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lt(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 't',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lu(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'u',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lv(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'v',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lw(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'w',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lx(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'x',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ly(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'y',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Lz(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': 'z',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk1(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\alpha',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk2(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\beta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk3(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\gamma',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk4(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\delta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk5(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\epsilon',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk6(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\varepsilon',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk7(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\zeta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk8(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\eta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk9(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\theta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk10(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\vartheta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk11(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\iota',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk12(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\kappa',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk13(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\lambda',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk14(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\mu',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk15(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\nu',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk16(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\xi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk17(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'o',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk18(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\pi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk19(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\varpi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk20(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\rho',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk21(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\varrho',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk22(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\sigma',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk23(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\varsigma',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk24(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\tau',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk25(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\upsilon',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk26(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\phi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk27(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\varphi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk28(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\chi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk29(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\psi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Gk30(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\omega',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC1(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Gamma',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC2(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Delta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC3(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Theta',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC4(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Lambda',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC5(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Xi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC6(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Pi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC7(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Gamma',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC8(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Sigma',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC9(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Upsilon',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC10(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Phi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC11(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Psi',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class GkC12(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\Omega',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op1(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'+',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op2(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'-',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op3(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\times',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op4(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'/',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op5(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'<',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op6(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'>',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op7(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'=',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op8(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\approx',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op9(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\propto',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op10(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\infty',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op11(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\frac{m}{n}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op12(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\sqrt{m}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op13(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\int',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op14(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\{ \}',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op15(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\oint',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op16(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\flat',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op17(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\natural',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Op18(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.2,
        'tex_class': TexMobject,
        'tex': r'\sharp',
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja1(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'あ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja2(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'い',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 3,
            "cairo_line_width_multiple": 0.05,
        },
        'wait_before_start': 3
    }


class Ja3(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'う',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja4(FourierOfPaths):
    CONFIG = {
        'n_vectors': 1150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'え',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja5(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'お',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


# TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

class Ja6(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'か',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja7(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'き',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja8(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'く',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja9(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'け',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja10(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'こ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja11(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'さ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja12(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'し',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja13(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'す',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja14(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'せ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja15(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'そ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja16(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'た',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja17(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ち',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja18(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'つ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja19(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'て',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja20(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'と',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja21(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'な',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja22(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'に',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja23(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ぬ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


# TODO +++++++++++++++++++++++++++++++++++++++++++++++++++


class Ja24(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ね',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja25(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'の',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja26(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'は',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja27(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ひ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja28(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ふ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja29(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'へ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja30(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ほ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja31(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ま',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja32(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'み',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja33(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'む',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja34(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'め',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja35(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'も',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja36(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'や',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja37(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ゆ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja38(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'よ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja39(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ら',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja40(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'り',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja41(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'る',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja42(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'れ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja43(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ろ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja44(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'わ',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja45(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'を',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja46(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ん',
        "tex_config": {
            "stroke_color": YELLOW,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


# class Ja47(FourierOfPaths):
#     CONFIG = {
#         'n_vectors': 150,
#         'run_time': 100,
#         'slow_factor': 0.2,
#         'tex_class': TextMobject,
#         'tex': 'ぬ',
#         'include_zoom_camera': True,
#         'zoom_position': lambda zc: zc.to_corner(DR),
#         'zoom_factor': 0.1,
#         'wait_before_start': 3
#     }


class Ja48(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ア',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja49(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'イ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja50(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ウ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja51(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'エ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja52(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'オ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja53(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'カ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja54(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'キ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


# TODO +++++++++++++++++++++++++++++++++++++++++++++


class Ja55(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ク',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja56(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ケ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja57(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'コ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja58(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'サ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja59(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'シ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja60(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ス',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja61(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'セ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja62(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ソ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja63(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'タ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja64(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'チ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja65(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ツ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja66(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'テ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja67(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ト',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja68(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ナ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja69(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ニ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja70(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ヌ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja71(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ネ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja72(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ノ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja73(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ハ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja74(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ヒ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja75(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'フ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja76(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ヘ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja77(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ホ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja78(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'マ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja79(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ミ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja80(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ム',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja81(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'メ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja82(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'モ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja83(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ヤ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja84(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ユ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja85(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ヨ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja86(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ワ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja87(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ヲ',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class Ja88(FourierOfPaths):
    CONFIG = {
        'n_vectors': 150,
        'run_time': 100,
        'slow_factor': 0.1,
        'tex_class': TextMobject,
        'tex': 'ン',
        "tex_config": {
            "stroke_color": GREEN,
            "fill_opacity": 0,
            "stroke_width": 3,
        },
        'circle_config': {
            'stroke_opacity': 0.5
        },
        'time_per_symbol': 10,
        'include_zoom_camera': True,
        'zoom_position': lambda zc: zc.to_corner(DR),
        'zoom_factor': 0.1,
        'wait_before_start': 3
    }


class NumberPlanee(Scene):
    CONFIG = {
        'axis_config': {

        }
    }

    def setup(self):
        Scene.setup(self)
        # GraphScene.setup(self)
        # CoordinateSystem.setup(self)

    # def get_axis(self, min_val, max_val, axis_config):
    #     new_config = merge_config([
    #         axis_config,
    #         {"x_min": min_val, "x_max": max_val},
    #         self.number_line_config,
    #     ])
    #     return NumberLine(**new_config)

    def construct(self):
        # self.setup_axes(animate=False)
        numberplane = NumberPlane()
        point = Dot()
        p1 = np.array([0, 0, 0])
        p2 = np.array([1, 1, 0])
        line1 = Line(start=p1, end=p2)
        point.move_to(p1)
        # numberplane.get_axis(min_val=-8, max_val=8, axis_config={
        #     "x_min": min_val, "x_max": max_val
        # })
        # self.play(Write(numberplane))
        self.play(Write(numberplane))
        self.wait(3)
        self.play(Write(point))
        self.wait(3)
        self.play(Write(line1))
        self.wait(3)


class RealNumber(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': WHITE
        },
        'max_val': {
            "x_min": -100,
            "x_max": 100,
            "y_min": -100,
            "y_max": 100
        },
        "graph_origin": ORIGIN,
        "y_line_frequency": 1,
        "x_line_frequency": 1,
        "axes_color": BLUE,
        "x_min": -100,
        "x_max": 100, "y_min": -100,
        "y_max": 100,
        "x_axis_width": 200,
        "y_axis_height": 200,
        'get_axis': 0,
        'x_labeled_nums': range(-100, 100, 1),
        'y_labeled_nums': range(-100, 100, 1)
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        copyright = Text('Made by CaftBotti',
                         font='HGB4_CNKI',
                         t2c={'CaftBotti': YELLOW}).scale(2)
        copyright2 = TextMobject('李旻昊制作',
                                 font='HGB4_CNKI', ).scale(0.5)
        copyright2.next_to(copyright, direction=DOWN,
                           buff=0.5, aligned_edge=ORIGIN,
                           )
        pp1 = np.array([math.sqrt(2), 0.5, 0])
        pp2 = np.array([-1.414213, 0.5, 0])
        pp3 = np.array([-4, 2.5, 0])
        pp4 = np.array([4, 2.5, 0])
        pp5 = np.array([2.7, 0.6, 0])
        t1 = Text('A', font='HGB4_CNKI')
        t1.move_to(pp2)
        t2 = Text('B', font='HGB4_CNKI')
        t2.move_to(pp1)
        t3 = TexMobject(r'A(?,0)', font='HGB4_CNKI').scale(2)
        t3.move_to(pp3)
        t4 = TexMobject(r'B(?,0)', font='HGB4_CNKI').scale(2)
        t4.move_to(pp4)
        t5 = TexMobject('a')
        t5.move_to(pp5)
        t6 = TexMobject('a^{2}=1^{2}+2^{2}').scale(2)
        t6.move_to(pp3)
        t7 = TexMobject('a^{2}=5').scale(2)
        t7.move_to(pp3)
        t8 = TexMobject(r'a=\sqrt 5').scale(2)
        t8.move_to(pp3)
        t9 = TexMobject(r'\sqrt 5 =?')
        t10 = TexMobject(r'2^{2}<5<3^{2}').scale(2)
        t10.set_color(YELLOW)
        t11 = TexMobject(r'2<\sqrt 5 <3').scale(2)
        t11.set_color(YELLOW)
        t12 = TexMobject(r'2.2^{2}<5<2.3^{2}').scale(2)
        t12.set_color(YELLOW)
        t13 = TexMobject(r'2.2<\sqrt 5 <2.3').scale(2)
        t13.set_color(YELLOW)
        t14 = TexMobject(r'...').scale(2)
        t14.set_color(YELLOW)
        t15 = TextMobject('事实上，').scale(2)
        t16 = TexMobject(r'\sqrt 5 \approx 2.2360679...').scale(2)
        t17 = TexMobject(r'\sqrt 2 \approx 1.4142135...').scale(2)
        # poi1 = np.array([0.5, 0.5, 0])
        p1 = np.array([0, 0, 0])
        p2 = np.array([0, 1, 0])
        p3 = np.array([1, 1, 0])
        p4 = np.array([1, 0, 0])
        p5 = np.array([0, 2, 0])
        p6 = np.array([2, 3, 0])
        p7 = np.array([3, 1, 0])
        point1 = Dot(np.array([math.sqrt(2), 0, 0]))
        point2 = Dot(np.array([-1.414213, 0, 0]))
        sq1 = Polygon(p1, p2, p3, p4)
        sq1.set_stroke(color=WHITE)
        sq2 = Polygon(p5, p6, p7, p4)
        sq2.set_stroke(color=YELLOW)
        circle1 = Circle(radius=math.sqrt(2))
        circle1.set_stroke(color=YELLOW)
        triangle1 = Polygon(p1, p4, p5)
        triangle1.set_stroke(color=GREEN)
        line1 = Line(start=np.array([0, 0, 0]), end=np.array([1, 1, 0]))
        line1.set_stroke(color=GREEN)
        # sq1.move_to(poi1)
        self.play(Write(copyright))
        self.wait(3)
        self.play(Write(copyright2))
        self.wait(3)
        self.play(FadeOut(copyright))
        self.play(FadeOut(copyright2))
        self.wait(2)

        self.setup_axes(animate=True)
        self.wait(2)
        self.play(Write(sq1))
        self.camera_frame.save_state()

        self.play(self.camera_frame.set_width, sq1.get_width() * 5,
                  self.camera_frame.move_to, sq1)
        self.play(Write(line1))
        self.wait(3)
        self.play(Restore(self.camera_frame))
        self.wait(5)
        self.play(Write(circle1))
        self.wait(3)
        self.play(Write(point1))
        self.wait(3)
        self.play(Write(point2))
        self.wait(3)
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(3)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(5)
        self.clear()
        self.wait(3)
        self.setup_axes(animate=True)
        self.play(Write(triangle1))
        self.wait(3)
        self.play(Write(sq2))
        self.wait(3)
        self.camera_frame.save_state()

        self.play(self.camera_frame.set_width, sq2.get_width() * 5,
                  self.camera_frame.move_to, sq2)
        self.wait()
        self.play(Write(t5))
        self.play(Restore(self.camera_frame))
        self.wait(3)
        self.play(Write(t6))
        self.wait(3)
        self.remove(t6)
        self.play(Transform(t6, t7))
        self.wait(3)
        self.remove(t6)
        self.play(Transform(t7, t8))
        self.wait(3)
        self.play(FadeOut(triangle1))
        self.play(FadeOut(sq2))
        self.play(FadeOut(self.axes))
        self.play(FadeOut(t5))
        self.wait()
        self.remove(t7)
        self.play(Transform(t8, t9))
        self.wait(3)
        self.play(t8.move_to, UP * 2)
        self.play(Write(t10))
        self.wait(3)
        self.remove(t10)
        self.play(Transform(t10, t11))
        self.wait(3)
        self.remove(t10)
        self.play(Transform(t11, t12))
        self.wait(3)
        self.remove(t11)
        self.play(Transform(t12, t13))
        self.wait(3)
        self.remove(t12)
        self.play(Transform(t13, t14))
        self.wait(3)
        self.play(FadeOut(t13))
        self.play(FadeOut(t9))
        self.play(FadeIn(t15))
        self.wait()
        self.play(t15.move_to, UP * 2)
        self.wait()
        self.play(Write(t16))
        self.wait(3)
        self.play(FadeOut(t15))
        self.remove(t16)
        self.play(Transform(t16, t17))
        self.wait(3)
