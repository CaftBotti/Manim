#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Made by CaftBotti
# This is my first manim python animation file.  17:34 11/08/2022 DD MM YYYY

# Importing

import math
import cmath
import pyglet
import manimlib
import a
import random
import hashlib
import interactive_scene
from interactive_scene import *
import manimlib.scene.scene
from manimlib.imports import *
from from_3b1b.active.diffyq.part2.fourier_series import *
from from_3b1b.active.diffyq.part4.fourier_series_scenes import *
from manimlib.fourier import *
from manimlib.mobject.mobject import *
from manimlib.mobject.coordinate_systems import *
from manimlib.mobject.vector_field import *
from manimlib.music_scene import *
from from_3b1b.on_hold.shadows import get_area
from from_3b1b.old.efvgt import *
from from_3b1b.old.eoc.chapter3 import NudgeSideLengthOfCube
from from_3b1b.old.eoc.chapter3 import *
from from_3b1b.old.hyperdarts import *
from manimlib.manim_physics import *
# from manimlib.coordinate_systems2 import *
# from from_3b1b.old.sphere_area import *
from from_3b1b.old.crypto import sha256_tex_mob, bit_string_to_mobject, BitcoinLogo
import pymunk

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
import sequence

sys.setrecursionlimit(80000)
"""Mobjects that represent coordinate systems."""

# from __future__ import annotations

__all__ = [
    "CoordinateSystem",
    "Axes",
    "ThreeDAxes",
    "NumberPlane",
    "PolarPlane",
    "ComplexPlane",
]


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
        self.student_says(
            "Yeah that's absurd",
            target_mode="sassy",
            student_index=1,
            added_anims=[self.teacher.change, "guilty"],
        )
        self.wait()
        self.play(
            RemovePiCreatureBubble(self.students[1]),
            self.teacher.change, "raise_right_hand",
            self.get_student_changes(
                "pondering", "erm", "thinking",
                look_at_arg=self.screen,
            )
        )
        self.look_at(self.screen)
        self.wait(5)
        self.student_says(
            "Who is CaftBotti?",
            target_mode="hooray",
            student_index=0,
            added_anims=[self.teacher.change, "happy"],
        )
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[0]))
        self.wait()
        self.teacher_says(
            "Sodeku King,\\\\and K"
        )
        self.wait(3)


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
            'stroke_color': WHITE,
            'stroke_width': 0,
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
        # ThreeDScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        copyright = Text('Made by CaftBotti',
                         font='HGB4_CNKI',
                         t2c={'CaftBotti': YELLOW}).scale(2)
        copyright2 = TextMobject('李旻昊制作',
                                 font='HGB4_CNKI', ).scale(0.8)
        copyright2.next_to(copyright, direction=DOWN,
                           buff=0.8, aligned_edge=ORIGIN,
                           )
        pp1 = np.array([math.sqrt(2), 0.5, 0])
        pp2 = np.array([-1.414213, 0.5, 0])
        pp3 = np.array([-4, 2.5, 0])
        pp4 = np.array([4, 2.5, 0])
        pp5 = np.array([2.7, 0.6, 0])
        pp6 = np.array([0, 2, 0])
        pp7 = np.array([0, -2, 0])
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
        t9 = TexMobject(r'\sqrt 5 =?').scale(2)
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
        t18 = TextMobject('体积为2的正方体，它的棱长为').scale(1.5)
        t18.move_to(pp6)
        t19 = TexMobject(r'\sqrt [3] {2}').scale(2)
        t19.set_color(YELLOW)
        t20 = TextMobject('我们刚刚看到的那些数，').scale(1.5)
        t20.move_to(pp6)
        t21 = TextMobject('既不是整数，也不是分数').scale(1.5)
        t22 = TextMobject('它们是无限不循环小数'
                          ).scale(1.5)
        t22.set_color(YELLOW)
        t22.move_to(pp7)
        t23 = TextMobject('它们是无理数').scale(2.2)
        t23.set_color(YELLOW)
        thanks = TextMobject('Thanks for watching!').scale(2)
        thanks.set_color('#99FFCC')

        # poi1 = np.array([0.5, 0.5, 0])
        p1 = np.array([0, 0, 0])
        p2 = np.array([0, 1, 0])
        p3 = np.array([1, 1, 0])
        p4 = np.array([1, 0, 0])
        p5 = np.array([0, 2, 0])
        p6 = np.array([2, 3, 0])
        p7 = np.array([3, 1, 0])
        p8 = np.array([1, 1, 1])
        p9 = np.array([0, 1, 1])
        p10 = np.array([1, 0, 1])
        p11 = np.array([0, 0, 1])
        p12 = np.array([2, 2, 2])
        p13 = np.array([0, 2, 2])
        p14 = np.array([2, 0, 2])
        p15 = np.array([0, 0, 2])
        p16 = np.array([0, 0, 0])
        p17 = np.array([0, 2, 0])
        p18 = np.array([2, 2, 0])
        p19 = np.array([2, 0, 0])
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
        # cube1 = Cube(p1, p2, p3, p4, p8, p9, p10, p11)
        cube1 = Cube()
        cube1.set_fill(color=GREEN, opacity=0.3)
        cube1.set_stroke(color=YELLOW)
        # cube2 = Cube(p12, p13, p14, p15, p16, p17, p18, p19)
        cube2 = Cube()
        cube2.set_fill(color=GREEN, opacity=0.3)
        cube2.set_stroke(color=YELLOW)
        # sq1.move_to(poi1)
        self.play(Write(copyright))
        self.wait(3)
        self.play(Write(copyright2))
        self.wait(3)
        self.play(FadeOut(copyright))
        self.play(FadeOut(copyright2))
        self.wait(2)

        self.play(Write(numberplane))
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
        self.play(Write(numberplane))
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
        self.play(FadeOut(numberplane))
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
        self.play(FadeOut(t8))
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
        self.clear()
        # self.play(Write(axes))
        # self.play(Write(cube1))
        # self.wait(3)
        # self.camera_frame.save_state()
        # self.play(self.camera_frame.set_width, cube1.get_width() * 2.5,
        #           self.camera_frame.move_to, cube1,
        #           )
        # self.move_camera(phi=20 * DEGREES, theta=30 * DEGREES, gamma=40 * DEGREES)
        # self.wait(3)
        # self.play(Restore(self.camera_frame))
        # self.wait(3)
        # self.play(Transform(cube1, cube2))
        # self.camera_frame.save_state()
        # self.play(self.camera_frame.set_width, cube1.get_width() * 2.5,
        #           self.camera_frame.move_to, cube2)
        # self.move_camera(phi=20 * DEGREES, theta=30 * DEGREES, gamma=40 * DEGREES)
        # self.wait(3)
        # self.play(Restore(self.camera_frame))
        # self.wait(3)
        self.clear()
        self.play(FadeIn(t18))
        self.play(Write(t19))
        self.wait(3)
        self.clear()
        self.play(Write(t20))
        self.play(Write(t21))
        self.play(Write(t22))
        self.wait(3)
        self.play(FadeOut(t20))
        self.play(FadeOut(t21))
        self.wait(2)
        self.remove(t22)
        self.play(Transform(t22, t23))
        self.wait(3)
        self.clear()
        self.play(Write(thanks))
        self.wait(3)


class RealNumber1(MovingCameraScene, GraphScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': WHITE,
            'stroke_width': 0,
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

    # def setup(self):
    #     GraphScene.setup(self)
    #     # ThreeDScene.setup(self)
    #     MovingCameraScene.setup(self)

    def construct(self):
        numberplane = NumberPlane()
        axes = Axes()
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
        pp6 = np.array([0, 2, 0])
        pp7 = np.array([0, -2, 0])
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
        t9 = TexMobject(r'\sqrt 5 =?').scale(2)
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
        t18 = TextMobject('体积为2的正方体，它的棱长为').scale(2)
        t18.move_to(pp6)
        t19 = TexMobject(r'\sqrt [3] {2}').scale(2)
        t19.set_color(YELLOW)
        t20 = TextMobject('我们刚刚看到的那些数，').scale(1.5)
        t20.move_to(pp6)
        t21 = TextMobject('既不是整数，也不是分数').scale(1.5)
        t22 = Text('它们是无限不循环小数',
                   t2c={'无限不循环小数': YELLOW}).scale(1.5)
        t22.move_to(pp7)
        t23 = TextMobject('它们是无理数').scale(2.2)
        t23.set_color(YELLOW)
        thanks = TextMobject('Thanks for watching!').scale(2)
        thanks.set_color('#99FFCC')

        # poi1 = np.array([0.5, 0.5, 0])
        p1 = np.array([0, 0, 0])
        p2 = np.array([0, 1, 0])
        p3 = np.array([1, 1, 0])
        p4 = np.array([1, 0, 0])
        p5 = np.array([0, 2, 0])
        p6 = np.array([2, 3, 0])
        p7 = np.array([3, 1, 0])
        p8 = np.array([1, 1, 1])
        p9 = np.array([0, 1, 1])
        p10 = np.array([1, 0, 1])
        p11 = np.array([0, 0, 1])
        p12 = np.array([2, 2, 2])
        p13 = np.array([0, 2, 2])
        p14 = np.array([2, 0, 2])
        p15 = np.array([0, 0, 2])
        p16 = np.array([0, 0, 0])
        p17 = np.array([0, 2, 0])
        p18 = np.array([2, 2, 0])
        p19 = np.array([2, 0, 0])
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
        # cube1 = Cube(p1, p2, p3, p4, p8, p9, p10, p11)
        cube1 = Cube()
        cube1.set_fill(color=GREEN, opacity=0.3)
        cube1.set_stroke(color=YELLOW)
        # cube2 = Cube(p12, p13, p14, p15, p16, p17, p18, p19)
        cube2 = Cube()
        cube2.set_fill(color=GREEN, opacity=0.3)
        cube2.set_stroke(color=YELLOW)
        # sq1.move_to(poi1)
        self.play(Write(copyright))
        self.wait(3)
        self.play(Write(copyright2))
        self.wait(3)
        self.play(FadeOut(copyright))
        self.play(FadeOut(copyright2))
        self.wait(2)

        self.play(Write(numberplane))
        self.setup_axes(animate=True)
        self.wait(2)
        self.play(Write(sq1))
        self.camera_frame.save_state()

        self.play(self.camera_frame.set_width, sq1.get_width() * 5,
                  self.camera_frame.move_to, sq1)
        self.play(Write(line1))
        self.wait(3)
        self.play(Restore(self.camera_frame))
        self.wait(3)
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
        self.wait(3)
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
        self.play(FadeOut(numberplane))

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
        self.play(FadeOut(t8))
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
        self.clear()


class RealNumber2(MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': WHITE,
            'stroke_width': 0,
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
        "axes_color": WHITE,
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
        MovingCameraScene.setup(self)

    def construct(self):
        numberplane = NumberPlane()
        axes = ThreeDAxes()
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
        pp6 = np.array([0, 2, 0])
        pp7 = np.array([0, -2, 0])
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
        t9 = TexMobject(r'\sqrt 5 =?').scale(2)
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
        t18 = TextMobject('体积为2的正方体，它的棱长为').scale(2)
        t18.move_to(pp6)
        t19 = TexMobject(r'\sqrt {3} 2').scale(2)
        t19.set_color(YELLOW)
        t20 = TextMobject('我们刚刚看到的那些数，').scale(1.5)
        t20.move_to(pp6)
        t21 = TextMobject('既不是整数，也不是分数').scale(1.5)
        t22 = Text('它们是无限不循环小数',
                   t2c={'无限不循环小数': YELLOW}).scale(1.5)
        t22.move_to(pp7)
        t23 = TextMobject('它们是无理数').scale(2.2)
        t23.set_color(YELLOW)
        thanks = TextMobject('Thanks for watching!').scale(2)
        thanks.set_color('#99FFCC')

        # poi1 = np.array([0.5, 0.5, 0])
        p1 = np.array([0, 0, 0])
        p2 = np.array([0, 1, 0])
        p3 = np.array([1, 1, 0])
        p4 = np.array([1, 0, 0])
        p5 = np.array([0, 2, 0])
        p6 = np.array([2, 3, 0])
        p7 = np.array([3, 1, 0])
        p8 = np.array([1, 1, 1])
        p9 = np.array([0, 1, 1])
        p10 = np.array([1, 0, 1])
        p11 = np.array([0, 0, 1])
        p12 = np.array([2, 2, 2])
        p13 = np.array([0, 2, 2])
        p14 = np.array([2, 0, 2])
        p15 = np.array([0, 0, 2])
        p16 = np.array([0, 0, 0])
        p17 = np.array([0, 2, 0])
        p18 = np.array([2, 2, 0])
        p19 = np.array([2, 0, 0])
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
        # cube1 = Cube(p1, p2, p3, p4, p8, p9, p10, p11)
        cube1 = Cube()
        cube1.set_fill(color=GREEN, opacity=0.3)
        cube1.set_stroke(color=YELLOW)
        # cube2 = Cube(p12, p13, p14, p15, p16, p17, p18, p19)
        cube2 = Cube()
        cube2.set_fill(color=GREEN, opacity=0.3)
        cube2.set_stroke(color=YELLOW)
        self.play(FadeIn(axes))
        self.play(Write(cube1))
        self.wait(3)
        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width, cube1.get_width() * 2.5,
                  self.camera_frame.move_to, cube1,
                  )
        self.move_camera(phi=20 * DEGREES, theta=30 * DEGREES, gamma=40 * DEGREES)
        self.wait(3)
        self.play(Restore(self.camera_frame))
        self.wait(3)
        self.play(Transform(cube1, cube2))
        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width, cube1.get_width() * 2.5,
                  self.camera_frame.move_to, cube2)
        self.move_camera(phi=20 * DEGREES, theta=30 * DEGREES, gamma=40 * DEGREES)
        self.wait(3)
        self.play(Restore(self.camera_frame))
        self.wait(3)
        self.clear()
        self.play(FadeIn(t18))
        self.play(Write(t19))
        self.wait(3)
        self.clear()
        self.play(Write(t20))
        self.play(Write(t21))
        self.play(Write(t22))
        self.wait(3)
        self.play(FadeOut(mobject=[t20, t21]))
        self.wait(2)
        self.remove(t22)
        self.play(Transform(t22, t23))
        self.wait(3)
        self.clear()
        self.play(Write(thanks))
        self.wait(3)


class ComplexPlanee1(Scene):

    def construct(self):
        nbp = NumberPlane()
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp))
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: math.e ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee2(Scene):

    def construct(self):
        nbp = NumberPlane()
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp))
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 2
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee3(Scene):

    def construct(self):
        nbp = NumberPlane()
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp))
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 3
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee4(Scene):

    def construct(self):
        nbp = NumberPlane()
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp))
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 4
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee5(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6
                          })
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 0.5
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee6(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6
                          })
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** math.e
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee7(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6
                          })
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** (math.pi * math.e)
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee8(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6
                          })
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** math.sqrt(2)
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee9(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6
                          })
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: math.sqrt(2) ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee10(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6
                          })
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: math.sqrt(3) ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee11(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: 2.2222 ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee12(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: -1 ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee13(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: -z ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee14(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z * z ** z
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee15(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** (z / 2)
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class ComplexPlanee16(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 0
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane1(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 2
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane2(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 3
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane3(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 4
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane4(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 5
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane5(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 6
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane6(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 7
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane7(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 8
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane8(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 9
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class Numberplane9(Scene):

    def construct(self):
        nbp = NumberPlane(x_line_frequency=0.3162277, y_line_frequency=0.3162277,
                          background_line_style={
                              'stroke_opacity': 0.6,
                          },
                          # x_range=[-1000, 1000, 0],
                          # y_range=[-1000, 1000, 0])
                          width=100,
                          height=100)
        nbp2 = ComplexPlane()
        nbp.prepare_for_nonlinear_transform()
        nbp2.prepare_for_nonlinear_transform()  # TODO MUST BE ADDED!
        self.play(Write(nbp), run_time=10)
        self.wait(3)
        self.play(nbp.apply_complex_function,
                  lambda z: z ** 10
                  , run_time=10, )
        self.wait(3)
        self.play(FadeOut(nbp))


class VectorField111(Scene):
    def construct(self):
        plane = NumberPlane()
        circle = Circle().scale(0.25)
        t = ValueTracker(0)
        self.add(plane, circle)
        points = [x * RIGHT + y * UP
                  for x in range(-8, 8, 1)
                  for y in range(-4, 4, 1)
                  ]

        def updater(vec):
            center = circle.get_center(focus)
            vec_center = vec.get_center(focus)
            vx = vec_center[0]
            vy = vec_center[1]
            x = center[0]
            y = center[1]
            # if vx == x and vy > y:
            #     angle = -0.5 * PI
            # else:
            angle = math.atan2(vy - y, vx - x)  # 求夹角
            vec.set_angle(angle)

        def update_path(cir):  # 圆形轨迹
            p = t.get_value()
            y = 2 * math.sin(p)
            x = 2 * math.cos(p)
            cir.move_to(x * RIGHT + y * UP)

        vec_field = []
        for point in points:
            result = Vector().shift(point).add_updater(updater).set_color(YELLOW).scale(0.5)
            vec_field.append(result)
        draw_field = VGroup(*vec_field)  # 向量群
        self.play(Write(draw_field), run_time=3)
        self.wait()
        self.play(circle.move_to, 5 * RIGHT, run_time=3)
        self.wait()
        self.play(circle.move_to, 5 * LEFT, run_time=3)
        self.wait()
        self.play(circle.move_to, 2 * RIGHT, run_time=3)
        circle.add_updater(update_path)
        self.play(t.set_value, 2 * PI, run_time=10)
        self.wait()


# class VectorFieldTest(Scene):
#     def construct(self):
#         nbp = NumberPlane()
#         t = ValueTracker(0)
#         focus = Dot()
#         self.add(nbp, t, focus)
#         point = [x * RIGHT + y * UP
#                  for x in range(-8, 8, 1)
#                  for y in range(-4, 4, 1)]
#
#         def updater(vec):
#             center = focus.get_center()
#             vec_center = vec.get_center()
#             vx = vec_center[0]
#             vy = vec_center[1]
#             x = center[0]
#             y = center[1]
#             angle = math.atan2(vy - y, vx - x)  # 求夹角
#             vec.set_angle(angle)
#
#         def update_path(cir):  # 圆形轨迹
#             p = t.get_value()
#             y = 2 * math.sin(p)
#             x = 2 * math.cos(p)
#             cir.move_to(x * RIGHT + y * UP)
#
#         vec_field = []
#         for point in points:
#             result = Vector().shift(point).add_updater(updater).set_color(YELLOW).scale(0.5)
#             vec_field.append(result)
#         draw_field = VGroup(*vec_field)  # 向量群
#         self.play(Write(draw_field), run_time=3)
#         self.wait()
#         self.play(circle.move_to, 5 * RIGHT, run_time=3)
#         self.wait()
#         self.play(circle.move_to, 5 * LEFT, run_time=3)
#         self.wait()
#         self.play(circle.move_to, 2 * RIGHT, run_time=3)
#         circle.add_updater(update_path)
#         self.play(t.set_value, 2 * PI, run_time=10)
#         self.wait()

class VectorTest(Scene):
    def construct(self):
        func1 = lambda p: np.array([
            p[2] / 2,
            p[1] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func2 = lambda p: np.array([
            p[1] / 3,
            p[0] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func3 = lambda p: np.array([
            p[1] ** 2,
            p[0] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func4 = lambda p: np.array([
            p[1] ** 2,
            p[1] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func5 = lambda p: np.array([
            p[1] ** 2,
            p[1] ** 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func6 = lambda p: np.array([
            p[0] ** 2,
            p[0] ** 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func7 = lambda p: np.array([
            p[2] ** 3,
            p[1] * 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        vec1 = VectorField(func1)
        vec2 = VectorField(func2)
        vec3 = VectorField(func3)
        vec4 = VectorField(func4)
        vec5 = VectorField(func5)
        vec6 = VectorField(func6)
        vec7 = VectorField(func7)
        self.play(Write(vec1))
        self.wait(3)
        self.remove(vec1)
        self.play(Transform(vec1, vec2))
        self.wait(3)
        self.remove(vec1)
        self.play(Transform(vec2, vec3))
        self.wait(3)
        self.remove(vec2)
        self.play(Transform(vec3, vec4))
        self.wait(3)
        self.remove(vec3)
        self.play(Transform(vec4, vec5))
        self.wait(3)
        self.remove(vec4)
        self.play(Transform(vec5, vec6))
        self.wait(3)
        self.remove(vec5)
        self.play(Transform(vec6, vec7))
        self.wait(3)


class StreamTest(Scene):
    def construct(self):
        func1 = lambda p: np.array([
            p[2] / 2,
            p[1] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func2 = lambda p: np.array([
            p[1] / 3,
            p[0] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func3 = lambda p: np.array([
            p[1] ** 2,
            p[0] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        func4 = lambda p: np.array([
            p[1] ** 2,
            p[1] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
            0
        ])
        vec1 = StreamLines(func1)
        vec2 = StreamLines(func2)
        vec3 = StreamLines(func3)
        vec4 = StreamLines(func4)
        self.play(Write(vec1))
        self.wait(3)
        self.remove(vec1)
        self.play(Transform(vec1, vec2))
        self.wait(3)
        self.remove(vec1)
        self.play(Transform(vec2, vec3))
        self.wait(3)
        self.remove(vec2)
        self.play(Transform(vec3, vec4))


class ContiniousMotion(Scene):
    def construct(self):
        func1 = lambda p: np.array([
            math.sin(p[1] / 2),
            math.cos(p[0] / 3),
            0
        ])
        vec1 = AnimatedStreamLines(StreamLines(func1))
        self.add(vec1)
        # vec1.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(10)


# class VectorTest2(Scene):
#     def construct(self):
#         func3 = lambda p: np.array([
#             p[1] ** 2,
#             p[0] / 2,  # If [x] = 1, it's a point center; if [x] = 2, it's a line center; /2 is arrow size
#             0
#         ])
#         vec = VectorField(func3)
#         point = Dot()
#         t = ValueTracker(0)
#         self.play(Write(vec))
#         self.wait(3)
#
#         def updater(vector):
#             center = point.get_center()
#             vec_center = vector.get_center()
#
#         def update_path(point):
#             x = func3
#             y = func3
#             point.move_to(x * RIGHT)
#


# class Testforanimations(Scene, FourierOfPaths):
#     def __init__(self, **kwargs):
#         manimlib.scene.scene.Scene.__init__(self, **kwargs)
#         manimlib.scene.scene.Mobject.__init__(self, **kwargs)
#
#     def main(self, __init__, **kwargs):
#         curr = Mobject
#         return __init__(curr, **kwargs)


class TwoYears(TeacherStudentsScene):
    def construct(self):
        self.teacher_says(
            "I will tell you \\\\ a story."
        )
        self.wait()
        self.student_says(
            "I can't wait",
            target_mode="sassy",
            student_index=2,
        )
        self.play(self.get_student_changes(look_at_arg=self.screen))
        self.wait()
        self.play(RemovePiCreatureBubble(self.students[2]))
        self.wait()
        self.teacher_says(
            "Our King CaftBotti \\\\ met a magic girl\\\\ 2 years ago"
        )
        self.wait(3)
        self.play(RemovePiCreatureBubble(self.teacher))
        self.wait()
        self.teacher_says(
            "Her name was Kelin"
        )
        self.wait(3)
        self.play(RemovePiCreatureBubble(self.teacher))
        self.wait()
        self.teacher_says(
            "Then they started their \\\\ friendship for 2 years long."
        )
        self.wait(3)
        self.student_says(
            "Hooray!",
            target_mode="sassy",
            student_index=1,
        )
        self.wait(2)
        self.play(RemovePiCreatureBubble(self.students[1]))
        # self.play(FadeOut(mobject=(self.students, self.teacher)))
        self.clear()


class ContinuousMotion2(Scene):
    def construct(self):
        func1 = lambda p: np.array([
            math.sin(p[1] / 2),
            math.cos(p[2] / 3),
            0
        ])
        vec1 = AnimatedStreamLines(StreamLines(func1))
        self.add(vec1)
        # vec1.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(10)


class ContinuousMotion3(Scene):
    def construct(self):
        func1 = lambda p: np.array([
            math.sin(p[0] / 2),
            math.cosh(p[2] / 3),
            0
        ])
        vec1 = AnimatedStreamLines(StreamLines(func1))
        self.add(vec1)
        # vec1.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(10)


class ContinuousMotion4(Scene):
    def construct(self):
        func1 = lambda p: np.array([
            math.sin(p[1] / 2),
            math.cos(p[2] / 3),
            0
        ])
        vec1 = AnimatedStreamLines(StreamLines(func1))
        self.add(vec1)
        # vec1.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(10)


class StartCaftbotti(Scene):
    def construct(self):
        copyright = Text('Made by CaftBotti',
                         font='HGB4_CNKI',
                         t2c={'CaftBotti': YELLOW}).scale(2)
        t = TextMobject('李旻昊制作',
                        font='HGB4_CNKI',
                        t2c={'李旻昊': YELLOW}).scale(2)
        # t.move_to, DOWN * 1
        self.play(Write(copyright))
        self.wait(2)
        self.play(Transform(copyright, t))
        self.wait(2)
        self.clear()


class WriteTest(Scene):
    def construct(self):
        text = TextMobject('AAAAAA')
        self.play(Write(text))
        self.wait(3)


class UpdateTest(Scene):
    def construct(self):
        dot = Dot()
        cir = Circle(stroke_color=BLUE)
        cir2 = Circle(radius=2.5)
        self.add(dot, cir)

        def update(obj):
            obj.move_to(cir)

        cir.add_updater(update)
        dot.move_to(cir)
        self.play(MoveAlongPath(mobject=cir, path=cir2), run_time=8)
        cir.remove_updater(update)
        self.wait(3)


class CirLine(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        text = Text("一个有趣的包络线图案", font="Noto Sans").set_color(BLUE)
        text1 = Text("manim模仿复刻练习", font="Noto Sans").set_color(BLUE)
        text1.next_to(text, DOWN).scale(0.8)
        circle = Circle(radius=1.5).set_stroke(color=BLUE, width=1.5)
        dot = Dot().move_to(1.5 * RIGHT).set_color(RED)
        line = Line(3 * LEFT, 3 * RIGHT).set_stroke(color=BLUE_B, width=1.5)
        set = []
        draw = VGroup()
        counter = [0]

        def circle_updater(cir):
            c = Circle(radius=dot.get_center(focus)[1]).set_stroke(color=RED, width=1)
            c.move_to(dot.get_center(focus))
            cir.become(c)

        def draw_updater(d):
            counter[0] += 1
            if (counter[0] % 4) == 0:
                c = circle_f.copy()
                c.set_stroke(color=PINK, width=0.8)
                set.append(c)
                group = VGroup(*set)
                d.become(group)

        circle_f = Circle().add_updater(circle_updater)
        draw.add_updater(draw_updater)
        self.play(Write(text))
        self.play(Write(text1))
        self.wait(2)
        self.play(Unwrite(text))
        self.play(Unwrite(text1))
        self.add(dot, circle_f)
        self.play(Create(circle), Create(line))
        self.play(Rotating(dot, radians=PI, about_point=ORIGIN, run_time=4, rate_func=there_and_back))
        self.wait()
        self.add(draw)
        self.play(MoveAlongPath(dot, circle), rate_func=linear, run_time=12)
        self.wait(3)


class CirLineTest(Scene):
    def construct(self):
        cir = Circle(radius=2.5).set_stroke(color=BLUE, width=1.5)
        dot = Dot()
        set = []
        draw = VGroup()
        counter = [0]

        def circle_updater(circle):
            c = Circle(radius=dot.get_center()[1]).set_stroke(color=RED, width=1)
            c.move_to(dot.get_center())
            circle.become(c)

        def draw_updater(d):
            counter[0] += 1
            if (counter[0] % 4) == 0:
                c = circle_f.copy()
                c.set_stroke(color=PINK, width=0.8)
                set.append(c)
                group = VGroup(*set)
                d.become(group)

        circle_f = Circle().add_updater(circle_updater)
        draw.add_updater(draw_updater)
        self.add(dot, circle_f)
        self.play(Write(cir))
        self.play(Rotating(dot, radians=PI, about_point=ORIGIN, run_time=4, rate_func=there_and_back))
        self.wait()
        self.add(draw)
        self.play(MoveAlongPath(dot, cir), rate_func=linear, run_time=12)
        self.wait(3)


class CirLineTest2(Scene):
    def construct(self):
        cir = Circle(radius=1.5).set_stroke(color=BLUE, width=1.5)
        dot = Dot()
        set = []
        draw = VGroup()
        counter = [0]
        focus = Dot().move_to(np.array([-2, -3, 0]))

        def circle_updater(circle):
            c = Circle(radius=focus.get_center()[1]).set_stroke(color=RED, width=1)
            c.move_to(dot.get_center())
            circle.become(c)

        def draw_updater(d):
            counter[0] += 1
            if (counter[0] % 4) == 0:
                c = circle_f.copy()
                c.set_stroke(color=PINK, width=0.8)
                set.append(c)
                group = VGroup(*set)
                d.become(group)

        circle_f = Circle().add_updater(circle_updater)
        draw.add_updater(draw_updater)
        self.add(dot, circle_f)
        self.play(Write(cir))
        self.play(Rotating(dot, radians=PI, about_point=ORIGIN, run_time=4, rate_func=there_and_back))
        self.wait()
        self.add(draw)
        self.play(MoveAlongPath(dot, cir), rate_func=linear, run_time=12)
        self.wait(3)


class CirLineTest3(GraphScene):
    def setup(self):
        GraphScene.setup(self)

    def construct(self):
        cir = Circle(radius=1.5).set_stroke(color=BLUE, width=1.5)
        dot = Dot()
        set = []
        draw = VGroup()
        counter = [0]
        focus = Dot().move_to(np.array([-2, -3, 0]))
        self.setup_axes(animate=True)

        func8 = self.get_graph(
            lambda x: x ** 2,
            color=BLUE,
            # x_min=-7,
            # x_max=7
        )

        line = Line(start=focus, end=ORIGIN)

        def circle_updater(circle):
            c = Circle(radius=line.get_center()[1]).set_stroke(color=RED, width=1)
            c.move_to(dot.get_center())
            circle.become(c)

        def draw_updater(d):
            counter[0] += 1
            if (counter[0] % 4) == 0:
                c = circle_f.copy()
                c.set_stroke(color=PINK, width=0.8)
                set.append(c)
                group = VGroup(*set)
                d.become(group)

        circle_f = Circle().add_updater(circle_updater)
        draw.add_updater(draw_updater)
        self.add(dot, circle_f, func8)
        self.play(Write(cir))
        self.play(Rotating(dot, radians=PI, about_point=ORIGIN, run_time=4, rate_func=there_and_back))
        self.wait()
        self.add(draw)
        self.play(MoveAlongPath(dot, cir), rate_func=linear, run_time=12)
        self.wait(3)


class UpdateTest2(Scene):
    def construct(self):
        line = Line()
        vgroup = VGroup()

        def updater(line1):
            l = Line(length=line.get_length())
            l.move_to(line)
            line1.become(line)

        # def number_updater(t):
        #     text = Text('line.get_length()').move_to, UP * 2
        #     t.become(text)

        linef = Line().add_updater(updater)
        # vgroup.add_updater(number_updater)
        # text = number_updater(t)
        text = Text('line.get_length()').move_to, UP * 2
        self.add(line, linef, text)
        self.play(line.set_length(2.5))
        self.wait(3)
        self.play(line.set_length(0.5))
        self.wait(3)


class MusicTest(MusicalScene):
    def importar_partitura(self):
        self.music = TexMobject(
            r'''
            \begin{music}
            \startextract
            \notes\zq {dgj}\en
            \zendextract
            \end{music}
            '''
        )

    def construct(self):
        self.play(Write(self.music))
        self.wait(3)


class Formula(Scene):
    def construct(self):
        formula = TexMobject(
            r'''
            \begin{array}{l}
x_{1,2}=\frac{-b+\sqrt[5]{5 a\left(16 H \pm \sqrt{256 H^{2}-5 a N}\right)}}{10 a}\\
\mathrm{X}_{3,4}=\frac{-4 \mathrm{~b}-(1+\sqrt{5}) \sqrt[5]{5 a\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a}+\frac{\sqrt{10-2 \sqrt{5}} \sqrt[5]{5 a\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a} i\\
\mathrm{X}_{5,6}=\frac{-4 \mathrm{~b}-(1+\sqrt{5}) \sqrt[5]{5 a\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right)}}{40 a}+\frac{\sqrt{10-2 \sqrt{5}} \sqrt[5]{5 a\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a} i\\
\mathrm{X}_{7,8}=\frac{-4 \mathrm{~b}-(1-\sqrt{5}) \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right)}}{40 \mathrm{a}}+\frac{\sqrt{10+2 \sqrt{5}} \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right.}}{40 \mathrm{a}} i\\
\mathrm{X}_{9,10}=\frac{-4 \mathrm{~b}-(1-\sqrt{5}) \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right.}}{40 \mathrm{a}} \pm \frac{\sqrt{10+2 \sqrt{5}} \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a} i
\end{array}
            '''
        )
        self.play(Write(formula))


class MusicNotation(MusicalScene):
    def importar_partitura(self):
        self.music = TexMobject(
            r'''
            \begin{music}
            \parindent10mm
            \instrumentnumber{1}
            \setname1{piano}
            \setstaffs1{2}
            \startextract
            \notes\|\zq {dgj}\en
            \zendextract
            \end{music}
            ''',
        )

    def construct(self):
        self.play(Write(self.music))
        self.wait(3)


class GraphTest(GraphScene):
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

    def construct(self):
        plane = NumberPlane()

        self.play(Write(plane))
        self.setup_axes(animate=True)
        t1 = TexMobject('y=x').move_to([-4, 3, 0]).scale(1.7)
        t2 = TexMobject('y=2x').move_to([-4, 3, 0]).scale(1.7)
        t3 = TexMobject('y=3x').move_to([-4, 3, 0]).scale(1.7)
        t4 = TexMobject(r'y=\frac {1}{2}x').move_to([-4, 3, 0]).scale(1.7)
        t5 = TexMobject('y=-x').move_to([-4, 3, 0]).scale(1.7)
        t6 = TexMobject('y=-2x').move_to([-4, 3, 0]).scale(1.7)
        t7 = TexMobject('y=-3x').move_to([-4, 3, 0]).scale(1.7)
        t8 = TexMobject(r'y=-\frac {1}{2}x').move_to([-4, 3, 0]).scale(1.7)
        t9 = TexMobject('y=x').move_to([-4, 3, 0]).scale(1.7)
        t10 = TexMobject('y=x-1').move_to([-4, 3, 0]).scale(1.7)
        t11 = TexMobject('y=x').move_to([-4, 3, 0]).scale(1.7)
        t12 = TexMobject('y=x+1').move_to([-4, 3, 0]).scale(1.7)
        t13 = TexMobject('y=x').move_to([-4, 3, 0]).scale(1.7)
        func1 = self.get_graph(
            lambda x: x,
            color=BLUE,
            x_min=-3,
            x_max=3
        )
        func2 = self.get_graph(
            lambda x: 2 * x,
            color=YELLOW,
            x_min=-3,
            x_max=3
        )
        func3 = self.get_graph(
            lambda x: 3 * x,
            color=RED,
            x_min=-3,
            x_max=3
        )
        func4 = self.get_graph(
            lambda x: (1 / 2) * x,
            color=GREEN,
            x_min=-3,
            x_max=3
        )
        func5 = self.get_graph(
            lambda x: -x,
            color=BLUE,
            x_min=-3,
            x_max=3
        )
        func6 = self.get_graph(
            lambda x: -2 * x,
            color=GRAY,
            x_min=-3,
            x_max=3
        )
        func7 = self.get_graph(
            lambda x: -3 * x,
            color=YELLOW,
            x_min=-3,
            x_max=3
        )
        func8 = self.get_graph(
            lambda x: (- 1 / 2) * x,
            color=WHITE,
            x_min=-3,
            x_max=3
        )
        func9 = self.get_graph(
            lambda x: x,
            color=PURPLE,
            x_min=-3,
            x_max=3
        )
        func10 = self.get_graph(
            lambda x: x - 1,
            color=GREEN,
            x_min=-3,
            x_max=3
        )
        func11 = self.get_graph(
            lambda x: x,
            color=BLUE,
            x_min=-3,
            x_max=3
        )
        func12 = self.get_graph(
            lambda x: x + 1,
            color=GREEN,
            x_min=-3,
            x_max=3
        )
        func13 = self.get_graph(
            lambda x: x,
            color=GREEN,
            x_min=-3,
            x_max=3
        )

        self.wait(3)
        self.play(Write(func1))
        self.play(Write(t1))
        self.wait(3)
        self.play(Transform(func1, func2))
        self.play(Transform(t1, t2))
        self.wait(2)
        self.remove(func1)
        self.play(Transform(func2, func3))
        self.remove(t1)
        self.play(Transform(t2, t3))
        self.wait(2)
        self.remove(func2)
        # self.remove(t2)
        self.play(Transform(func3, func4))
        self.remove(t2)
        self.play(Transform(t3, t4))
        self.wait(2)
        self.remove(func3)
        # self.remove(t3)
        self.play(Transform(func4, func5))
        self.remove(t3)
        self.play(Transform(t4, t5))
        self.wait(2)
        self.remove(func4)
        # self.remove(t4)
        self.play(Transform(func5, func6))
        self.remove(t4)
        self.play(Transform(t5, t6))
        self.wait(2)
        self.remove(func5)
        # self.remove(t5)
        self.play(Transform(func6, func7))
        self.remove(t5)
        self.play(Transform(t6, t7))
        self.wait(2)
        self.remove(func6)
        # self.remove(t6)
        self.play(Transform(func7, func8))
        self.remove(t6)
        self.play(Transform(t7, t8))
        self.wait(2)
        self.remove(func7)
        # self.remove(t7)
        self.play(Transform(func8, func9))
        self.remove(t7)
        self.play(Transform(t8, t9))
        self.wait(2)
        self.remove(func8)
        # self.remove(t8)
        self.play(Transform(func9, func10))
        self.remove(t8)
        self.play(Transform(t9, t10))
        self.wait(2)
        self.remove(func9)
        #
        self.play(Transform(func10, func11))
        self.remove(t9)
        self.play(Transform(t10, t11))
        self.wait(2)
        self.remove(func10)
        #
        self.play(Transform(func11, func12))
        self.remove(t10)
        self.play(Transform(t11, t12))
        self.wait(2)
        self.remove(func11)
        #
        self.play(Transform(func12, func13))
        self.remove(t11)
        self.play(Transform(t12, t13))
        self.wait(2)
        #


class PiGraph(TeacherStudentsScene):
    def construct(self):
        self.teacher_says('今天我们一起研究\\\\一次函数图像吧')
        self.wait(3)
        self.student_thinks('那一定会超级神奇', student_index=2)
        self.play(
            self.teacher.change, "raise_right_hand",
            self.get_student_changes(
                "pondering", "erm", "thinking",
                look_at_arg=self.screen,
            )
        )
        self.wait(3)
        self.teacher_says('看一看图像与函数\\\\之间有什么关系。')
        self.wait(2)
        self.teacher_says('视频中只展示了\\\\函数图像的一小段，\\\\以便清晰地看到图像变化。')
        self.wait(2)
        self.student_says("Let's go")
        self.wait(2)


class ThanksForWatch(Scene):
    def construct(self):
        t = TextMobject('Thanks for watching!').scale(2).set_color('#99FFCC')
        self.play(Write(t))
        self.wait(3)


class EndThanks(PatreonEndScreen):
    CONFIG = {
        "specific_patrons": [
            'Grant Sanderson',
            'Tony Crane',
            'Caft Botti',
            'Kelin K',
            '邝琳琳',
            '刘贺文',
            '张霁翔',
            '孙英博',
            'Ndjaka Magredison',
            '蒋文迪',
            'Manim',
        ]
    }


# class EqualationGroupTest(Scene):
#     def construct(self):


# class EqMap(Scene):
#     cfg = dict(
#         eq_level=None,
#         eq_depth=None,
#         eq_wait=None
#     )
#     def construct(self):
#         cfg = dict(
#             eq_level=None,
#             eq_depth=None,
#             eq_wait=None
#         )
#         if cfg.eq_level is not None:
#             if cfg.eq_depth is not None:
#                 if cfg.eq_wait is not None:
#                     circle_color = '#EE0000'
#                     radius = cfg.eq_level / 2
#                     location = cfg.eq_location
#                     wait = cfg.eq_wait
#                     c = Circle(radius=radius, color=circle_color, center=location, fill_color=circle_color,
#                                fill_opacity=circle_color)
#                     self.play(FadeOut(c))
#                     self.wait(wait)
#                     return self
# \begin{array}{c}
#   (i\pi)^{2}=(i\pi)\times(i\pi)=i^{2}\times\pi^{2}=-\pi^{2}\\
#   (i\pi)^{3}=i\times i\times i \times \pi^3=-i\pi^3 \\
# (i\pi)^4=i^4\times\pi^4=\pi^4\\
# (i\pi)^5=-i\pi^5\\
# (i\pi)^6=-\pi^6\\
# (i\pi)^7=-i\pi^7\\
# \vdots
# \end{array}

class EulerFormula(Scene):
    def construct(self):
        eulerformula = TexMobject(r'e^{i \pi} +1=0').set_color(YELLOW).scale(2)
        ep3 = TexMobject(r'e^{3}=e\times e\times e').scale(2)
        epn2 = TexMobject(r'e^{-2}=\frac{1}{e}\times\frac{1}{e}').scale(2)
        epfrac = TexMobject(r'e^{\frac{1}{2}}=\sqrt e').scale(2)
        scary = TexMobject(r'e^{-\frac{2}{3}}=\frac{1}{\sqrt[3]e}\times\frac{1}{\sqrt[3]e').scale(2)
        # whatabout = TexMobject(r'但是e^{i \pi}呢?')
        definition = TexMobject(
            r'e=\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\cdots').scale(1.4)
        definition2 = TexMobject(
            r'e^{x}=\frac{1}{0!}+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+\frac{x^{5}}{5!}+\cdots').scale(
            1.4)
        # definex = TexMobject(r'设x=i\pi,则')
        definition3 = TexMobject(
            r'e^{i\pi}=\frac{1}{0!}+\frac{i\pi}{1!}+\frac{(i\pi)^{2}}{2!}+\frac{(i\pi)^{3}}{3!}+\frac{(i\pi)^{4}}{4!}+\frac{(i\pi)^{5}}{5!}+\cdots')
        #         calc = TexMobject(r'''
        #         \begin{eqnarray}
        #
        #   (i\pi)^{2} & = & (i\pi)\times(i\pi) & = & i^{2}\times\pi^{2} & = & -\pi^{2}\\
        #   (i\pi)^{3} & = & i\times i\times i \times \pi^3 & = & -i\pi^3 \\
        # (i\pi)^4 & = & i^4\times\pi^4 & = & \pi^4\\
        # (i\pi)^5 & = & -i\pi^5\\
        # (i\pi)^6 & = & -\pi^6\\
        # (i\pi)^7 & = & -i\pi^7\\
        # \vdots
        # \end{eqnarray}''')
        calc = TexMobject(r'''
         \begin{array}{c}
   (i\pi)^{2}=(i\pi)\times(i\pi)=i^{2}\times\pi^{2}=-\pi^{2}\\
   (i\pi)^{3}=i\times i\times i \times \pi^3=-i\pi^3 \\
(i\pi)^4=i^4\times\pi^4=\pi^4\\
 (i\pi)^5=-i\pi^5\\
 (i\pi)^6=-\pi^6\\
 (i\pi)^7=-i\pi^7\\
 \vdots
 \end{array}''')
        calc2 = TexMobject(
            r'e^{i\pi}=(\frac{1}{0!}-\frac{\pi^2}{2!}+\frac{\pi^4}{4!}-\frac{\pi^6}{6!}+\cdot\cdot\cdot)+(\frac{\pi}{1!}-\frac{\pi^3}{3!}+\frac{\pi^5}{5!}-\frac{\pi^7}{7!}+\cdot\cdot\cdot)i').scale(
            0.9)
        calc3 = TexMobject(r'e^{i\pi}=\cos\pi+i\sin\pi=-1+0i=-1')
        t1 = TexMobject('\mbox{这是伟大的欧拉公式}').move_to(DOWN * 1).set_color(BLUE)
        t2 = TextMobject('e的虚数次幂意味着什么?').set_color(YELLOW)
        t3 = TextMobject('我们知道正整数次幂是什么意思').move_to(UP * 3)
        t4 = TextMobject('负数幂是倒数的幂').move_to(UP * 3)
        t5 = TextMobject('分数幂用平方根、立方根等来解释').move_to(UP * 3)
        t6 = TextMobject('所以这样“恐怖”的东西也能算出来').move_to(UP * 3)
        t7 = TexMobject(r'\mbox{但是}e^{i\pi}\mbox{呢?}')
        # t7 = TextMobject('但是') + TextMobject(r'e^{i \\pi}') + TextMobject('呢?')
        t8 = TextMobject('回忆一下e的定义').move_to(UP * 3)
        t9 = TexMobject(r'\mbox{对于任何数字x},e^x\mbox{的值是}').move_to(UP * 3)
        t10 = TexMobject(r'\mbox{设}x=i\pi,\mbox{则}').move_to(UP * 3)
        t11 = TextMobject('仔细看一下它的分子').move_to(UP * 3).set_color(YELLOW)
        t12 = TextMobject('这些项在实数和虚数之间交替，我们分别合并实数和虚数').move_to(UP * 3).set_color('#99FFCC')
        t13 = TexMobject(r'\mbox{第一个括号里的项正好是}\cos\pi, \mbox{第二个括号里的项是}\sin\pi').move_to(UP * 3)
        t14 = TextMobject('这就是伟大的欧拉公式。').move_to(UP * 3).set_color(BLUE)
        self.play(Write(eulerformula))
        self.wait(3)
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        self.play(FadeOut(eulerformula))
        self.wait(1)
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2, t3))
        self.wait(2)
        self.play(Write(ep3))
        self.wait(2)
        self.clear()
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(epn2))
        self.wait(3)
        self.clear()
        self.play(Write(t5))
        self.wait(2)
        self.play(Write(epfrac))
        self.wait(3)
        self.clear()
        self.play(Write(t6))
        self.wait(2)
        self.play(Write(scary))
        self.wait(3)
        self.clear()
        self.play(Write(t7))
        self.wait(2)
        self.play(Transform(t7, t8))
        self.wait(2)
        self.play(Write(definition))
        self.wait(3)
        self.remove(t7)
        self.play(Transform(t8, t9))
        self.wait()
        self.play(Transform(definition, definition2))
        self.wait(2)
        self.remove(t8)
        self.play(Transform(t9, t10))
        self.wait()
        self.remove(definition)
        self.play(Transform(definition2, definition3))
        self.wait(3)
        self.remove(t9)
        self.play(Transform(t10, t11))
        self.wait()
        self.remove(definition2)
        self.play(Transform(definition3, calc))
        self.wait(3.5)
        self.remove(t10)
        self.play(Transform(t11, t12))
        self.wait(2)
        self.remove(definition3)
        self.play(Transform(calc, calc2))
        self.wait(2)
        self.remove(t11)
        self.play(Transform(t12, t13))
        self.wait(2)
        self.remove(calc)
        self.play(Transform(calc2, calc3))
        self.wait(3)
        self.remove(t12)
        self.play(Transform(t13, t14))
        self.wait(2)
        self.remove(calc2)
        self.play(Transform(calc3, eulerformula))
        self.wait(3)


class EulerFormulaEnglish(Scene):
    def construct(self):
        eulerformula = TexMobject(r'e^{i \pi} +1=0').set_color(YELLOW).scale(2)
        ep3 = TexMobject(r'e^{3}=e\times e\times e').scale(2)
        epn2 = TexMobject(r'e^{-2}=\frac{1}{e}\times\frac{1}{e}').scale(2)
        epfrac = TexMobject(r'e^{\frac{1}{2}}=\sqrt e').scale(2)
        scary = TexMobject(r'e^{-\frac{2}{3}}=\frac{1}{\sqrt[3]e}\times\frac{1}{\sqrt[3]e').scale(2)
        # whatabout = TexMobject(r'但是e^{i \pi}呢?')
        definition = TexMobject(
            r'e=\frac{1}{0!}+\frac{1}{1!}+\frac{1}{2!}+\frac{1}{3!}+\frac{1}{4!}+\frac{1}{5!}+\cdots').scale(1.4)
        definition2 = TexMobject(
            r'e^{x}=\frac{1}{0!}+\frac{x}{1!}+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\frac{x^{4}}{4!}+\frac{x^{5}}{5!}+\cdots').scale(
            1.4)
        # definex = TexMobject(r'设x=i\pi,则')
        definition3 = TexMobject(
            r'e^{i\pi}=\frac{1}{0!}+\frac{i\pi}{1!}+\frac{(i\pi)^{2}}{2!}+\frac{(i\pi)^{3}}{3!}+\frac{(i\pi)^{4}}{4!}+\frac{(i\pi)^{5}}{5!}+\cdots')
        #         calc = TexMobject(r'''
        #         \begin{eqnarray}
        #
        #   (i\pi)^{2} & = & (i\pi)\times(i\pi) & = & i^{2}\times\pi^{2} & = & -\pi^{2}\\
        #   (i\pi)^{3} & = & i\times i\times i \times \pi^3 & = & -i\pi^3 \\
        # (i\pi)^4 & = & i^4\times\pi^4 & = & \pi^4\\
        # (i\pi)^5 & = & -i\pi^5\\
        # (i\pi)^6 & = & -\pi^6\\
        # (i\pi)^7 & = & -i\pi^7\\
        # \vdots
        # \end{eqnarray}''')
        calc = TexMobject(r'''
         \begin{array}{c}
   (i\pi)^{2}=(i\pi)\times(i\pi)=i^{2}\times\pi^{2}=-\pi^{2}\\
   (i\pi)^{3}=i\times i\times i \times \pi^3=-i\pi^3 \\
(i\pi)^4=i^4\times\pi^4=\pi^4\\
 (i\pi)^5=-i\pi^5\\
 (i\pi)^6=-\pi^6\\
 (i\pi)^7=-i\pi^7\\
 \vdots
 \end{array}''')
        calc2 = TexMobject(
            r'e^{i\pi}=(\frac{1}{0!}-\frac{\pi^2}{2!}+\frac{\pi^4}{4!}-\frac{\pi^6}{6!}+\cdot\cdot\cdot)+(\frac{\pi}{1!}-\frac{\pi^3}{3!}+\frac{\pi^5}{5!}-\frac{\pi^7}{7!}+\cdot\cdot\cdot)i').scale(
            0.9)
        calc3 = TexMobject(r'e^{i\pi}=\cos\pi+i\sin\pi=-1+0i=-1')
        t1 = TexMobject('\mbox{This is the great formula of Euler}').move_to(DOWN * 1).set_color(BLUE)
        t2 = TexMobject(r'\mbox{What does }e^i \mbox{ actually mean}?').set_color(YELLOW)
        t3 = TextMobject('We know the meaning of \\\\positive integer power').move_to(UP * 3)
        t4 = TextMobject('The negative power is fractal').move_to(UP * 3)
        t5 = TextMobject('Fractal power is explained by\\\\ square roots,etc').move_to(UP * 3)
        t6 = TextMobject('...so we can work out the "scary" thing').move_to(UP * 3)
        t7 = TexMobject(r'\mbox{But how about }e^{i\pi}\mbox{?}')
        # t7 = TextMobject('但是') + TextMobject(r'e^{i \\pi}') + TextMobject('呢?')
        t8 = TextMobject('Recall the definition of e').move_to(UP * 3)
        t9 = TexMobject(r'\mbox{For any x},\mbox{the value of }e^x \mbox{ is}').move_to(UP * 3)
        t10 = TexMobject(r'\mbox{Let }x=i\pi,\mbox{then}').move_to(UP * 3)
        t11 = TextMobject('Look carefully at the numerator').move_to(UP * 3).set_color(YELLOW)
        t12 = TextMobject(
            'These terms alternate between real and imaginary numbers.\\\\ We combine real and imaginary numbers respectively').move_to(
            UP * 3).set_color('#99FFCC')
        t13 = TexMobject(
            # r'\mbox{Terms in the 1st parentheses are }\cos\pi, \\ \mbox{2st parentheses are }\sin\pi').move_to(UP * 3)
            r'''
            \begin{array}{c}
            \mbox{Terms in the 1st parentheses are }\cos\pi, \\ \mbox{2nd parentheses are }\sin\pi
            \end{array}
            '''
        ).move_to(UP * 3)
        t14 = TextMobject('This is the great Euler formula.').move_to(UP * 3).set_color(BLUE)
        self.play(Write(eulerformula))
        self.wait(3)
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(t1))
        self.play(FadeOut(eulerformula))
        self.wait(1)
        self.play(Write(t2))
        self.wait(2)
        self.play(Transform(t2, t3))
        self.wait(2)
        self.play(Write(ep3))
        self.wait(2)
        self.clear()
        self.play(Write(t4))
        self.wait(2)
        self.play(Write(epn2))
        self.wait(3)
        self.clear()
        self.play(Write(t5))
        self.wait(2)
        self.play(Write(epfrac))
        self.wait(3)
        self.clear()
        self.play(Write(t6))
        self.wait(2)
        self.play(Write(scary))
        self.wait(3)
        self.clear()
        self.play(Write(t7))
        self.wait(2)
        self.play(Transform(t7, t8))
        self.wait(2)
        self.play(Write(definition))
        self.wait(3)
        self.remove(t7)
        self.play(Transform(t8, t9))
        self.wait()
        self.play(Transform(definition, definition2))
        self.wait(2)
        self.remove(t8)
        self.play(Transform(t9, t10))
        self.wait()
        self.remove(definition)
        self.play(Transform(definition2, definition3))
        self.wait(3)
        self.remove(t9)
        self.play(Transform(t10, t11))
        self.wait()
        self.remove(definition2)
        self.play(Transform(definition3, calc))
        self.wait(3.5)
        self.remove(t10)
        self.play(Transform(t11, t12))
        self.wait(2)
        self.remove(definition3)
        self.play(Transform(calc, calc2))
        self.wait(2)
        self.remove(t11)
        self.play(Transform(t12, t13))
        self.wait(2)
        self.remove(calc)
        self.play(Transform(calc2, calc3))
        self.wait(3)
        self.remove(t12)
        self.play(Transform(t13, t14))
        self.wait(2)
        self.remove(calc2)
        self.play(Transform(calc3, eulerformula))
        self.wait(3)


class EndThanks2(PatreonEndScreen):
    CONFIG = {
        "specific_patrons": [
            'Leonhard Euler',
            'Grant Sanderson',
            'Tony Crane',
            'Caft Botti',
            'Kelin K',
            'Ndjaka Magredison',
            'Manim',
        ]
    }


class StartCaftbotti2(Scene):
    def construct(self):
        # text = TextMobject('Thanks for watching!').scale(2).set_color('#99FFCC')
        t = Text('Made by CaftBotti', t2c={'CaftBotti': YELLOW}, font='HGB4_CNKI').scale(2)
        self.play(Write(t))
        self.wait(3)
        self.play(FadeOut(t))


# class SetTest(Scene):
#     def construct(self):
#         # dot_set = np.array.arange([0, 2, 0], [2, 0, 0], [0, -2, 0], [-2, 0, 0])
#         dot_set = Circle()
#         # dotp = np.array([])
#         function = lambda z: z ** 2
#
#         dot = Dot()
#         dot.apply_function(function)
#         for dot in dot_set:
#             dot.set_color(GREEN)
#             self.add(dot)
#             self.play(Write(dot))


# class AnimationTest(Scene):
#     def construct(self):
#         circle = Circle()
#         dot = Dot()
#         line = Line(start=circle, end=dot)
#
#         def updater():
#             # circle = Circle()
#             # dot = Dot()
#             # line = Line(start=circle.get_center(), end=dot.get_center)
#
#             for dot in circle:
#                 dot.get_center()
#                 line = Line(start=circle, end=dot)
#
#         dot.add_updater(updater)
#         line.add_updater(updater)
#         self.add(circle, dot)
#         self.wait(2)
#         self.play(MoveAlongPath(dot, cir), rate_func=linear, run_time=12)


class UpdaterTest(Scene):
    def construct(self):
        label = TexMobject('This is a label')
        dot = Dot()
        label.next_to(dot, RIGHT, buff=SMALL_BUFF)
        self.add(label, dot)

        def label_updater(obj):
            obj.next_to(dot, RIGHT, buff=SMALL_BUFF)

        # TODO this is very important
        # You can also use updater without def updater:
        # m means text
        # label.add_updater(lambda m: m.next_to(dot, RIGHT, buff=SMALL_BUFF)

        # Or use UpdateFromFunc, it only works in play()
        # self.play(dot.shift, UP * 2,
        #           UpdateFromFunc(label, label_updater))

        # lambda d means decimal

        label.add_updater(label_updater)
        self.add(label)
        self.play(dot.shift, UP * 2)
        self.wait(2)


class UpdaterTest2(GraphScene):
    def construct(self):
        numberline = NumberPlane()
        self.play(Write(numberline))
        number = DecimalNumber(0)
        circle = Circle(radius=2)
        dot = Dot(fill_opacity=0)  # This invisible dot is a good idea
        # number.add_updater()
        number.add_updater(lambda d: d.next_to(dot, UP * 0.1))
        number.add_updater(lambda d: d.set_value(dot.get_center()[0]))
        self.add(number)
        self.play(dot.move_to, RIGHT * 2, rate_func=there_and_back, run_time=5)
        self.wait(3)
        self.play(MoveAlongPath(dot, circle), run_time=8)
        self.wait(3)
        # number.rotate()
        # self.setup_axes(animate=True)
        # function = self.get_graph(number.add_updater(lambda d: d.set_value(dot.get_center()[0])))
        # self.add(function)


# class UpdaterTest2Graph(UpdaterTest2):
#     def construct(self):
#         axes = Axes()
#         def get_number_updater(obj):
#             obj.next_to()


# class UpdaterTest3(Scene):
#     def construct(self):
#         line = Line(start=np.array([-3, 0, 0]), end=np.array([-1, 3, 0]))
#         dot = Dot(fill_opacity=0)
#         def line_updater(obj):
#             obj.next_to(dot)
#             obj.rotate(angle=2 * PI)
#
#         def draw_updater(line1):
#             global counter
#             counter = 0
#             if (counter % 4) == 0:
#                 l = line1.copy()
#                 set.append(l)
#                 group = VGroup(*set)
#                 d.become(group)
#         dot.add_updater(line_updater)
#         line.add_updater(draw_updater)
#         self.add(dot, line)
#         self.play(dot.move_to, LEFT * 3, run_time=3)


class Warning1(Scene):
    def construct(self):
        t1 = TexMobject('EMERGENCY WARNING').set_color(RED).move_to(UP * 2)
        t2 = TexMobject("Please wait for an earthquake warning.\\ Don't worry.").scale(1.6)
        self.add(t1, t2)
        self.wait(10)


class UpdaterTest4(Scene):
    def construct(self):
        vt = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        self.add(number)
        self.play(vt.set_value, 100, rate_func=linear, run_time=100)
        self.wait(2)


class UpdaterTest5(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        line = Line()
        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(line.get_length()))
        self.add(number)
        self.play(line.set_length, 3, rate_func=linear, run_time=8)


class UpdaterTest6(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        line = Line()
        line2 = Line(start=np.array([0, 0, 0]), end=np.array([3, -1, 0]))
        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(line.get_length()))
        self.add(number)
        self.play(Transform(line, line2), rate_func=linear, run_time=8)
        self.wait(2)


# TODO
class UpdaterTest7(GraphScene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        line = Line()
        line2 = Line(start=np.array([0, 0, 0]), end=np.array([3, -1, 0]))
        line3 = Line(start=np.array([2, 6, 0]), end=np.array([-2, -3, 0]))
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(line.get_length()))
        self.add(number)
        self.wait(3)
        self.play(Transform(line, line2), rate_func=linear, run_time=8)
        number.remove_updater(lambda m: m.set_value(line.get_length()))
        self.remove(line)
        number.add_updater(lambda m: m.set_value(line2.get_length()))
        self.wait(3)
        self.play(Transform(line2, line3), rate_func=linear, run_time=8)
        self.wait(2)


class UpdaterTest8(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        line = Square()
        line2 = Circle()
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(line)))
        self.add(number)
        self.play(Transform(line, line2), rate_func=linear, run_time=8)
        self.wait(2)


class UpdaterTest9(GraphScene):
    def construct(self):
        # global number_value
        numberplane = NumberPlane()
        self.add(numberplane)
        self.setup_axes()
        line = Square()
        line2 = Circle()
        number = DecimalNumber(0, num_decimal_places=5)

        # number.add_updater(lambda m: m.set_value(get_area(line)))
        def number_updater(obj):
            obj.add_updater(lambda m: m.set_value(get_area(line)))

        # self.get_graph(lambda x: x.set_value(get_area(line)))
        number.add_updater(number_updater)
        # if number.get_value() != 0:
        number_value = number.get_value()
        graph = self.get_graph(
            x_values=[0, number_value],
            y_values=[0, number_value],
            # func=lambda x: 0
            func=number_value
        )
        graph.add_updater(number_updater)
        self.add(number, graph)
        self.play(Transform(line, line2), rate_func=linear, run_time=8)
        self.wait(2)
        # def move_dot()

        # self.t_offset = 0
        # orbit = self.get_graph(lambda x: math.sin(x))  # Ellipse(color=GREEN).scale(2.5)
        # planet = Dot(fill_opacity=0)
        # planet.move_to(orbit.point_from_proportion(0))
        #
        # def update_planet(mob, dt):
        #     rate = dt * 0.3
        #     mob.move_to(orbit.point_from_proportion((self.t_offset + rate) % 1))
        #     self.t_offset += rate
        #
        # planet.add_updater(update_planet)
        # self.add(orbit, planet)
        # self.wait(4)


class EpicycloidSceneSimple(Scene):
    def construct(self):
        radius1 = 2.4
        radius2 = radius1 / 3
        self.epy(radius1, radius2)

    def epy(self, r1, r2):
        # Manim circle
        c1 = Circle(radius=r1, color=BLUE)
        # Small circle
        c2 = Circle(radius=r2, color=PURPLE).rotate(PI)
        c2.next_to(c1, RIGHT, buff=0)
        c2.start = c2.copy()
        # Dot
        # .points[0] return the start path coordinate
        # .points[-1] return the end path coordinate
        dot = Dot(c2.points[0], color=RED)
        # Line
        line = Line(c2.get_center(), dot.get_center()).set_stroke(BLACK, 2.5)
        # Path
        path = VMobject(color=RED)
        # Path can't have the same coord twice, so we have to dummy point
        path.set_points_as_corners([dot.get_center(), dot.get_center() + UP * 0.001])
        # Path group
        path_group = VGroup(line, dot, path)
        # Alpha, from 0 to 1:
        alpha = ValueTracker(0)

        self.play(Write(line), Write(c1), Write(c2), Write(dot))

        # update function of path_group
        def update_group(group):
            l, mob, previus_path = group
            mob.move_to(c2.points[0])
            old_path = path.copy()
            # See manimlib/mobject/types/vectorized_mobject.py
            old_path.append_vectorized_mobject(Line(old_path.points[-1], mob.get_center()))
            old_path.make_smooth()
            l.put_start_and_end_on(c2.get_center(), mob.get_center())
            path.become(old_path)

        # update function of small circle
        def update_c2(c):
            c.become(c.start)
            c.rotate(TAU * alpha.get_value(), about_point=c1.get_center())
            c.rotate(TAU * (r1 / r2) * alpha.get_value(), about_point=c.get_center())

        path_group.add_updater(update_group)
        c2.add_updater(update_c2)
        self.add(c2, path_group)
        self.play(
            alpha.set_value, 1,
            rate_func=linear,
            run_time=6
        )
        self.wait(2)
        c2.clear_updaters()
        path_group.clear_updaters()
        self.play(FadeOut(VGroup(c1, c2, path_group)))


class Clock(VGroup):
    CONFIG = {}

    def __init__(self, hh=0, mh=0, radius=3, color=WHITE, **kwargs):
        super().__init__(**kwargs)
        # Define body
        body = Circle(radius=radius, color=WHITE)
        body.flip()
        body.rotate(- 4 * 360 / 12 * DEGREES)
        self.body = body
        center_body = Dot(body.get_center())
        numbers = self.get_numbers(body)
        ticks = self.get_ticks(body)

        # Define hour
        hour = hh + mh / 60
        hour_tracker = ValueTracker(hour)
        self.ht = hour_tracker

        # Define hands
        minute_hand = self.get_minute_hand(body, hour_tracker.get_value() % 1 * 60)
        hour_hand = self.get_hour_hand(body, hour_tracker.get_value())

        # Define dashed lines
        dashed_lines = self.get_dashed_lines(body, hour_hand, minute_hand)
        self.dl = dashed_lines

        self.hh = hour_hand
        self.mh = minute_hand

        self.add(
            body,
            ticks,
            numbers,
            minute_hand,
            hour_hand,
            dashed_lines,
            center_body,
        )

    def add_updaters(self):
        self.mh.add_updater(
            lambda mob: mob.become(
                self.get_minute_hand(self.body, self.ht.get_value() % 1 * 60))
        )
        self.hh.add_updater(
            lambda mob: mob.become(
                self.get_hour_hand(
                    self.body,
                    self.ht.get_value()
                )
            )
        )
        self.dl.add_updater(
            lambda mob: mob.become(
                self.get_dashed_lines(self.body, self.hh, self.mh)
            )
        )

    def suspend_updaters(self):
        for mob in [self.mh, self.hh, self.dl]:
            mob.suspend_updating()

    def resume_updaters(self):
        for mob in [self.mh, self.hh, self.dl]:
            mob.resume_updating()

    def get_hour_hand(self, body: Circle, hour, a_prop=0.4):
        # print("Hour from class: " + str(hour))
        prop = hour / 12
        guide_line = Line(
            body.get_center(),
            body.point_from_proportion(prop % 1)
        )
        hour_hand = Arrow(
            body.get_center(),
            guide_line.point_from_proportion(a_prop),
            buff=0,
            color=RED
        )
        hour_hand.rotate(2 * PI / 12, about_point=body.get_center())
        return hour_hand

    def get_minute_hand(self, body: Circle, minutes, a_prop=0.7):
        prop = minutes / 60
        guide_line = Line(
            body.get_center(),
            body.point_from_proportion(prop % 1)
        )
        hour_hand = Arrow(
            body.get_center(),
            guide_line.point_from_proportion(a_prop),
            buff=0,
            color=BLUE
        )
        hour_hand.rotate(2 * PI / 12, about_point=body.get_center())
        return hour_hand

    def get_dashed_lines(self, body: Circle, hh: Arrow, mh: Arrow):
        hhv = hh.get_unit_vector()
        mhv = mh.get_unit_vector()

        hhd = Line(
            body.get_center(),
            body.get_center() + hhv * self.body.get_height() * 0.97 / 2,
            color=hh.get_color(),
            stroke_width=1
        )
        mhd = Line(
            body.get_center(),
            body.get_center() + mhv * self.body.get_height() * 0.97 / 2,
            color=mh.get_color(),
            stroke_width=1
        )
        return VGroup(hhd, mhd)

    def get_numbers(self, body: Circle, prop=0.85, scale=0.8):
        numbers = VGroup(*[TexMobject(f"{i}") for i in list(range(1, 13))])
        for i, n in enumerate(numbers):
            point = body.point_from_proportion(i / 12)
            guide_line = Line(body.get_center(), point)
            n.scale(scale)
            n.move_to(guide_line.point_from_proportion(prop))
        return numbers

    def get_ticks(self, body: Circle, size_prop=0.04, stroke_width=1):
        ticks = VGroup()
        for i in range(60):
            point = body.point_from_proportion(i / 60)
            guide_line = Line(body.get_center(), point)
            size = size_prop * 2 if i % 5 == 0 else size_prop
            tick = Line(
                guide_line.point_from_proportion(1 - size),
                point
            )
            ticks.add(tick)
        return ticks


class ParaFuncTest(Scene):
    def construct(self):
        func = ParametricFunction(
            lambda t: np.array([2 * np.sin(t), 2, 0]), t_min=0, t_max=2 * PI
        )
        self.add(func)
        self.wait(6)


class UpdaterTest10(GraphScene):
    def construct(self):
        # global number_value
        numberplane = NumberPlane()
        self.add(numberplane)
        self.setup_axes()
        line = Square()
        line2 = Circle()
        vt = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=5)

        # numberv = ChangeDecimalToValue(decimal_mob=number)
        # numberv = CountInDecimal()

        # number.add_updater(lambda m: m.set_value(get_area(line)))
        def number_updater(obj):
            obj.add_updater(lambda m: m.set_value(vt.get_value(get_area(line))))

        # self.get_graph(lambda x: x.set_value(get_area(line)))
        number.add_updater(number_updater)
        # if number.get_value() != 0:
        number_value = number

        # number_value.add_updater(lambda m: m.set_value(number))
        def number_value_updater(obj):
            obj.add_updater(lambda m: m.set_value(number))

        # graph = self.get_graph(
        #     x_values=[],
        #     y_values=[],
        #     # func=lambda x: 0
        #     func=number_value_updater(obj)
        #
        # ).add_updater(number_value_updater)
        graph = FunctionGraph(function=number_updater)

        graph.add_updater(number_updater)
        self.add(number, graph)
        self.play(Transform(line, line2), rate_func=linear, run_time=8)
        self.wait(2)


# class GraphExample(Scene):
#     def construct(self):
#         axes = Axes()
#         # axes.add_coordinate_labels()
#
#         self.play(Write(axes, lag_ratio=0.01, run_time=1))
#
#         # Axes.get_graph会返回传入方程的图像
#         sin_graph = axes.get_graph(
#             lambda x: 2 * math.sin(x),
#             color=BLUE,
#         )
#         # 默认情况下，它在所有采样点(x, f(x))之间稍微平滑地插值
#         # 但是，如果图形有棱角，可以将use_smoothing设为False
#         relu_graph = axes.get_graph(
#             lambda x: max(x, 0),
#             use_smoothing=False,
#             color=YELLOW,
#         )
#         # 对于不连续的函数，你可以指定间断点来让它不试图填补不连续的位置
#         step_graph = axes.get_graph(
#             lambda x: 2.0 if x > 3 else 1.0,
#             discontinuities=[3],
#             color=GREEN,
#         )
#
#         # Axes.get_graph_label可以接受字符串或者mobject。如果传入的是字符串
#         # 那么将将其当作LaTeX表达式传入Tex中
#         # 默认下，label将生成在图像的右侧，并且匹配图像的颜色
#         sin_label = axes.get_axis_label(sin_graph, "\\sin(x)")
#         relu_label = axes.get_axis_label(relu_graph, Text("ReLU"))
#         step_label = axes.get_axis_label(step_graph, Text("Step"), x=4)
#
#         self.play(
#             ShowCreation(sin_graph),
#             FadeIn(sin_label, RIGHT),
#         )
#         self.wait(2)
#         self.play(
#             ReplacementTransform(sin_graph, relu_graph),
#             FadeTransform(sin_label, relu_label),
#         )
#         self.wait()
#         self.play(
#             ReplacementTransform(relu_graph, step_graph),
#             FadeTransform(relu_label, step_label),
#         )
#         self.wait()
#
#         parabola = axes.get_graph(lambda x: 0.25 * x**2)
#         parabola.set_stroke(BLUE)
#         self.play(
#             FadeOut(step_graph),
#             FadeOut(step_label),
#             ShowCreation(parabola)
#         )
#         self.wait()
#
#         # 你可以使用Axes.input_to_graph_point（缩写Axes.i2gp）来找到图像上的一个点
#         dot = Dot(color=RED)
#         dot.move_to(axes.i2gp(2, parabola))
#         self.play(FadeIn(dot, scale=0.5))
#
#         # ValueTracker存储一个数值，可以帮助我们制作可变参数的动画
#         # 通常使用updater或者f_always让其它mobject根据其中的数值来更新
#         x_tracker = ValueTracker(2)
#         f_always(
#             dot.move_to,
#             lambda: axes.i2gp(x_tracker.get_value(), parabola)
#         )
#
#         self.play(x_tracker.animate.set_value(4), run_time=3)
#         self.play(x_tracker.animate.set_value(-2), run_time=3)
#         self.wait()


class Play(GraphScene):
    CONFIG = {
        "y_max": 8,
        "y_axis_height": 5,
    }

    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=False)

        def func(x):
            return 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5

        def rect(x):
            return 2.775 * (x - 1.5) + 3.862

        recta = self.get_graph(rect, x_min=-1, x_max=5)
        graph = self.get_graph(func, x_min=0.2, x_max=9)
        graph.set_color(BLUE)
        input_tracker_p1 = ValueTracker(1.5)
        input_tracker_p2 = ValueTracker(2.5)  # 3.5 was original coordinate

        def get_x_value(input_tracker):
            return input_tracker.get_value()

        def get_y_value(input_tracker):
            return graph.underlying_function(get_x_value(input_tracker))

        def get_x_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), 0)

        def get_y_point(input_tracker):
            return self.coords_to_point(0, get_y_value(input_tracker))

        def get_graph_point(input_tracker):
            return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))

        def get_v_line(input_tracker):
            return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

        def get_h_line(input_tracker):
            return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)

        #
        input_triangle_p1 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p1 = RegularPolygon(n=3, start_angle=0)
        for triangle in input_triangle_p1, output_triangle_p1:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)
        #
        input_triangle_p2 = RegularPolygon(n=3, start_angle=TAU / 4)
        output_triangle_p2 = RegularPolygon(n=3, start_angle=0)
        for triangle in input_triangle_p2, output_triangle_p2:
            triangle.set_fill(WHITE, 1)
            triangle.set_stroke(width=0)
            triangle.scale(0.1)

        #
        x_label_p1 = TexMobject("a")
        output_label_p1 = TexMobject("f(a)")
        x_label_p2 = TexMobject("b")
        output_label_p2 = TexMobject("f(b)")
        v_line_p1 = get_v_line(input_tracker_p1)
        v_line_p2 = get_v_line(input_tracker_p2)
        h_line_p1 = get_h_line(input_tracker_p1)
        h_line_p2 = get_h_line(input_tracker_p2)
        graph_dot_p1 = Dot(color=WHITE)
        graph_dot_p2 = Dot(color=WHITE)

        # reposition mobjects
        x_label_p1.next_to(v_line_p1, DOWN)
        x_label_p2.next_to(v_line_p2, DOWN)
        output_label_p1.next_to(h_line_p1, LEFT)
        output_label_p2.next_to(h_line_p2, LEFT)
        input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
        input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
        output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
        output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
        graph_dot_p1.move_to(get_graph_point(input_tracker_p1))
        graph_dot_p2.move_to(get_graph_point(input_tracker_p2))

        self.play(
            ShowCreation(graph),
        )

        n = 25
        list1 = [None] * (n + 1)
        for i in range(0, n + 1):
            list1[i] = self.get_secant_slope_group(
                3.5 - 2 * i / n, graph, dx=0.001,
                df_label=None,
                dx_label=None,
                dx_line_color="#942357",
                df_line_color="#3f7d5c",
                secant_line_color=RED,
            )

        for j in range(n - 1):
            self.remove(list1[j])
            self.add(list1[j + 1])
            self.wait(0.1)


class UpdaterTest11(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        square = Square()
        circle = Circle()
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
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.play(Transform(square, circle), run_time=8)
        self.wait(3)
        number.clear_updaters()
        self.remove(square)
        number.add_updater(lambda m: m.set_value(get_area(circle)))
        self.play(Transform(circle, tri2), run_time=8)
        self.wait(3)
        number.clear_updaters()
        self.remove(circle)
        number.add_updater(lambda m: m.set_value(get_area(tri2)))
        self.play(Transform(tri2, elli1), run_time=8)
        self.wait(3)
        number.clear_updaters()
        self.remove(tri2)
        number.add_updater(lambda m: m.set_value(get_area(elli1)))
        self.play(Transform(elli1, sq2), run_time=8)
        self.wait(2)


class UpdaterTest12(Scene):
    def construct(self):
        t = TexMobject('Hello')
        fps = 1 / self.camera.frame_rate
        update_t = update_move_func(
            t, [1, 2, 0], fps, run_time=3, func=smooth
        )
        t.add_updater(update_t)
        # self.play(Write(t))
        anim = Write(t)
        self.add(t)
        turn_animation_into_updater(anim)
        self.wait(3)
        t.clear_updaters()
        self.wait(3)


class UpdaterTest13(Scene):
    def construct(self):
        tri = Triangle()
        sq = Square()
        tri.add_updater(lambda mob, dt: mob.rotate(0.3 * DEGREES))
        sq.add_updater(lambda mob, dt: mob.rotate(-0.2 * DEGREES))
        anim1 = FadeToColor(tri, GREEN)
        self.add(tri)
        self.add(sq)
        cycle_animation(
            anim1,
            run_time=3,
        )
        self.wait(3)
        self.play(Write(TextMobject('Hello')))
        self.wait(10)
        tri.clear_updaters()
        self.wait(2)


class UpdaterTest14(Scene):
    def construct(self):
        tri = Triangle()
        sq = Square()
        tri.add_updater(lambda mob, dt: mob.rotate(0.3 * DEGREES))
        sq.add_updater(lambda mob, dt: mob.rotate(-0.2 * DEGREES))
        anim1 = FadeToColor(tri, GREEN)
        self.add(tri)
        self.add(sq)
        cycle_animation(
            anim1,
            run_time=3,
        )
        self.wait(3)
        self.play(Write(TextMobject('Hello')))
        self.wait(10)
        tri.clear_updaters()
        self.wait(2)
        numberline = NumberPlane()
        self.play(Write(numberline))
        number = DecimalNumber(0)
        circle = Circle(radius=2)
        dot = Dot(fill_opacity=0)  # This invisible dot is a good idea
        # number.add_updater()
        number.add_updater(lambda d: d.next_to(dot, UP * 0.1))
        number.add_updater(lambda d: d.set_value(dot.get_center()[0]))
        self.add(number)
        self.play(dot.move_to, RIGHT * 2, rate_func=there_and_back, run_time=5)
        self.wait(3)
        self.play(MoveAlongPath(dot, circle), run_time=8)
        self.wait(3)


# class CodeTest(Scene):
#     def construct(self):
#         code = Code(
#             R'''
#             a.py
#             '''
#         )
#         self.play(Write(code))
#         self.wait(3)


# class CodeTest(CodeMobject):
#     CONFIG = {
#         "template_tex_file": R'C:\beibi\a\a.py',
#         "indent_level": 4,
#         "propagate_style_to_family": False,
#         "repeat_cursor_dist": 0.15,
#     }


class CodeTest2(Scene):
    def construct(self):
        # Intro
        I = TextMobject("Code Mobject").move_to(ORIGIN).set_color(BLUE)

        I1 = Text('''Code Mobject adalah salah satu Mobject atau Preset yang dapat menampilkan kode
dari berbagai bahasa pemrograman dengan highlight sesuai dengan style yang tersedia.''').scale(0.5)
        I2 = Text("Berikut adalah 18 Style yang telah tersedia.").scale(0.5)

        self.play(Write(I))
        self.wait()
        self.play(Uncreate(I))
        self.play(Write(I1))
        self.wait()
        self.play(Uncreate(I1))
        self.play(Write(I2))
        self.wait()
        self.play(Uncreate(I2))
        self.wait()
        # CodeMobject
        code = '''from manim import*
class CodeFromString(Scene):
    def construct(self):
        code = \''' Tulis Kode di sini
\'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(Write(rendered_code))
        self.wait()
        self.play(Uncreate(rendered_code))
'''
        # rendered_code = Code(code=code, tab_width=4, background="window",
        #                    language="Python", font="Monospace")
        # self.play(Write(rendered_code))
        # self.wait()
        # self.play(Uncreate(rendered_code))
        code_styles_list = {0: "autumn", 1: "borland", 2: "bw", 3: "colorful",
                            4: "default", 5: "emacs", 6: "friendly", 7: "fruity",
                            8: "manni", 9: "monokai", 10: "murphy", 11: "native",
                            12: "pastie", 13: "perldoc", 14: "rrt", 15: "tango",
                            16: "trac", 17: "vim", 18: "vs"}
        for number, styles in code_styles_list.items():
            listing = Code(
                code=code,
                tab_width=4,
                background_stroke_width=1,
                background_stroke_color=WHITE,
                insert_line_no=True,
                # style=Code.styles_list[number],
                background="window",
                language="python",
            )
            listing.scale(0.8)
            Title1 = Text(f"This is code_style {number} name : {styles}", font="consolas", color=BLUE).next_to(listing,
                                                                                                               1.5 * UP)
            ccc = VGroup(Title1, listing)
            D = VGroup()
            D.add(ccc).arrange_in_grid()

            self.play(Write(ccc))
            self.wait()
            self.play(FadeOut(ccc))
            self.wait()

        Z = Text("Thanks For Watching").set_color_by_gradient(GREEN, YELLOW)
        self.play(Write(Z))
        self.wait()
        self.play(Uncreate(Z))
        self.wait()


class CodeLine(Text):
    CONFIG = {
        't2c': {
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'return': "#C594C5",
            'def': "#C594C5",
            "int": "#569CD6",
            'interpolate': "#60B4B4",
            'interpolate_mobject': "#60B4B4",
            '"': "#60B4B4",
            "'": "#60B4B4",
            'start': "#FAB763",
            'end': "#FAB763",
            'alpha': "#FAB763",
            ":": "#FA9044",
            "+": "#FA9044",
            "*": "#FA9044",
            "-": "#FA9044",
            "=": "#FA9044",
            ",": GREY,
            "digit": "#569CD6",
            " x": "#9CDCFE",
            "ss": "#9CDCFE",
            "String": "#4EC9B0",
            "class": "#569CD6",
            "MyBox": "#4EC9B0",
            "function": "#569CD6",
            "gcd": "#DCDCAA",
            ".": GREY,
            "box": "#9CDCFE",
            "self": "#D86066",
            "shift": "#569CD6",
            "play": "#569CD6",
            "Square": "#569CD6",
            "add_updater": "#569CD6",
            "UP": "#FAB763",
            "DOWN": "#FAB763",
            "LEFT": "#FAB763",
            "RIGHT": "#FAB763",
            "ORIGIN": "#FAB763",
            "PI": "#FAB763",
            "args": "#FAB763",
            "kwargs": "#FAB763",
            "(": GREY,
            ")": GREY,
            "generate_target": "#569CD6",
            "MoveToTarget": "#569CD6",
            "anims_from_play_args": "#569CD6",
            "Scene": "#4EC9B0",
            "Rotating": "#569CD6",
            "\{": GREY,
            "\}": GREY,
            # "become": "#569CD6"
        },
        'font': 'Fira Code Medium',
        'size': 0.64,
        'color': "#e0e0e0",
        "stroke_width": 0,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class Scene17(Scene):
    def construct(self):
        t1 = CodeLine("math_object").scale(1.2)
        t2 = CodeLine("mobject").scale(1.2)
        t3 = CodeLine(".generate_target()").scale(1.2).next_to(t2, buff=0.12).shift(LEFT * 3)
        self.play(Write(t1))
        self.wait()
        self.play(Transform(t1, t2))
        self.play(t2.shift, LEFT * 3, FadeIn(t3, LEFT))
        self.wait()
        self.play(t2.to_corner, UL,
                  UpdateFromFunc(t3, lambda a: a.next_to(t2, buff=0.12)))
        cir = Circle(radius=1.5).move_to(np.array([-3.5, -0.5, 0]))
        t_cur = TexMobject("current").next_to(cir, DOWN)
        t_tar = TexMobject("target").next_to(t_cur, DOWN).set_opacity(0.7)
        self.play(ShowCreation(cir), Write(t_cur), Write(t_tar))
        code = VGroup(
            CodeLine("mobject.target = Square().shift(RIGHT*3)").scale(1.2),
            CodeLine("self.play(MoveToTarget(mobject))").scale(1.2)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(t2, DOWN, aligned_edge=LEFT)
        sq = Square(side_length=3, color=BLUE).shift(RIGHT * 3.5 + DOWN * 0.5)
        self.wait()
        self.play(Write(code[0]))
        self.wait()
        self.play(ShowCreation(sq),
                  t_tar.become, TexText("target").next_to(sq, DOWN))
        self.wait()
        self.play(Write(code[1]))
        self.wait()
        sqk = sq.copy()
        self.play(ReplacementTransform(cir, sqk),
                  t_cur.next_to, sq, DOWN,
                  t_tar.shift, DOWN / 2, run_time=1.5)
        self.wait(2)
        code_n = CodeLine(r"self.play(mobject.become,{'mobject':Square().shift(RIGHT*3)})").scale(1.1)
        code_n.align_to(code, UL)
        code_n[27:34].set_color("#99C794")
        self.play(FadeOut(t2, DOWN), FadeOut(t3, DOWN), FadeOut(code[0]), FadeOut(code[1], UP),
                  FadeIn(code_n))
        self.wait()
        ft = "庞门正道标题体"
        code_play = VGroup(
            CodeLine("# Scene中play的定义", t2f={"中": ft, "的定义": ft}).set_color(GREY),
            CodeLine("def play(self, *args, **kwargs):"),
            CodeLine("..."),
            CodeLine("animations = self.anims_from_play_args(*args, **kwargs)"),
            CodeLine("...")).scale(1.1).arrange(DOWN, aligned_edge=LEFT).align_to(code_n, LEFT).shift(UP * 2.4)
        code_play[2:].shift(RIGHT * 0.95)
        self.play(Write(code_play), FadeOut(sq), FadeOut(sqk), FadeOut(t_tar), FadeOut(t_cur), code_n.shift, DOWN * 2.3)
        self.wait()
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(code_n[10:24])),
                  ShowCreationThenFadeAround(SurroundingRectangle(code_play[1][15:20])))
        self.wait()
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(code_n[25:-1])),
                  ShowCreationThenFadeAround(code_play[1][22:30]))
        self.wait()
        code_ex = VGroup(
            CodeLine("mobject.generate_target()"),
            CodeLine("mobject.target = Square().shift(RIGHT*3)"),
            CodeLine("self.play(MoveToTarget(mobject))")
        ).scale(1.2).arrange(DOWN, aligned_edge=LEFT).next_to(code_n, DOWN, buff=0.7, aligned_edge=LEFT)
        bc = BackgroundRectangle(code_ex, buff=0.25)
        self.play(FadeIn(bc))
        self.play(Transform(code_n[10:24].copy(), code_ex[0]))
        self.wait()
        self.play(Transform(code_n[10:-1].copy(), code_ex[1]))
        self.wait()
        self.play(Transform(code_n[0:10].copy(), code_ex[2]))
        self.wait()


class Scene18(Scene):
    def construct(self):
        sq1 = VGroup(Square(side_length=1, color=BLUE), TexMobject("1")).shift(LEFT * 2)
        sq2 = VGroup(Square(side_length=1, color=RED), TexMobject("2")).shift(RIGHT * 2)
        axes = Axes(axis_config={"include_tip": False, }, y_range=[-6, 6, 1], x_range=[-10, 10, 1])
        # co1 = VGroup(
        #     CodeLine(r"self.play(Rotating(sq1, PI,"),
        #     CodeLine(r"about_point=ORIGIN))")
        # )

        # co1[1].next_to(co1[0][2], DR, buff=0.4)
        # co1.to_corner(UL)
        # co1[1][0:11].set_color("#FAB763")

        # co2 = VGroup(
        #     CodeLine(r"self.play(sq2.rotate,"),
        #     CodeLine(r"{'angle':PI,"),
        #     CodeLine(r"'about_point':ORIGIN})"),
        # )
        # co2[1].next_to(co2[0][2], DR, buff=0.4)
        # co2[2].next_to(co2[1], DOWN, aligned_edge=LEFT, buff=0.1)
        # co2.to_corner(UR)
        # co2[1][2:7].set_color("#99C794")
        # co2[2][1:12].set_color("#99C794")

        co1 = CodeLine(r"self.play(Rotating(sq1, PI, about_point=ORIGIN))", t2c={"about_point": "#FAB763"}).to_corner(
            UL)
        co2 = CodeLine(r"self.play(sq2.rotate, {'angle':PI,'about_point':ORIGIN})",
                       t2c={
                           "about_point": "#99C794", "angle": "#99C794"
                       }).next_to(co1, DOWN, aligned_edge=LEFT)

        self.play(ShowCreation(axes))
        self.play(Write(sq1), Write(sq2))
        self.play(Write(co1), Write(co2))
        self.wait()
        self.play(Rotating(sq1, angle=PI, about_point=ORIGIN),
                  sq2.rotate, {"angle": PI, "about_point": ORIGIN},
                  run_time=5, rate_func=linear)
        self.wait()
        code2 = VGroup(
            CodeLine("sq2.generate_target()"),
            CodeLine("sq2.target=sq2.rotate(PI,about_point=ORIGIN)", t2c={"about_point": "#FAB763"}),
            CodeLine("self.play(MoveToTarget(sq2))")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(co2, DOWN, aligned_edge=LEFT, buff=0.8)
        self.play(axes.shift, DOWN * 2,
                  sq2.shift, DOWN * 2,
                  FadeOut(sq1, DOWN * 2))
        self.play(Transform(co2[10:20].copy(), code2[0]))
        sq2c = VGroup(Square(side_length=1, color=RED, stroke_opacity=0.3), Tex("2", fill_opacity=0.3)).shift(
            LEFT * 2 + DOWN * 2).rotate(PI)
        self.add(sq2c)
        t_tar = TexText("target").scale(0.6).next_to(sq2c, UP)
        self.play(Transform(co2[10:-1].copy(), code2[1]))
        self.play(FadeIn(t_tar))
        self.add(t_tar)
        self.play(sq2c.rotate, {"angle": PI, "about_point": DOWN * 2}, t_tar.shift, RIGHT * 4)
        self.play(Transform(co2[0:9].copy(), code2[2]))
        self.play(sq2.rotate, {"angle": PI, "about_point": DOWN * 2}, run_time=2)
        self.wait()
        sq1.shift(DOWN * 2)
        self.play(FadeOut(sq2), FadeOut(sq2c), FadeIn(sq1), FadeOut(code2), FadeOut(co2), FadeOut(t_tar))
        self.play(sq1.shift, RIGHT * 3, axes.shift, RIGHT * 3)
        _4 = CodeLine("aaaa")
        code1 = VGroup(
            CodeLine("def interpolate_mobject(self, alpha):"),
            CodeLine("..."),
            CodeLine("self.mobject.rotate(", t2c={"rotate": "#569CD6"}),
            CodeLine("alpha * self.angle,"),
            CodeLine("axis=self.axis,"),
            CodeLine("about_point=self.about_point,"),
            CodeLine("about_edge=self.about_edge,"),
            CodeLine(")")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(co1, DOWN, aligned_edge=LEFT, buff=0.8)
        code1[1:].shift(RIGHT * _4.get_width())
        code1[3:7].shift(RIGHT * _4.get_width())
        code1[4][0:4].set_color("#FAB763")
        code1[5][0:11].set_color("#FAB763")
        code1[6][0:10].set_color("#FAB763")
        code1[5][-4:-1].set_color("#e0e0e0")
        self.play(Write(code1))
        self.wait()
        enve = VGroup()
        sq1c = sq1.copy()
        sq1c[0].set_stroke(opacity=0.2)
        sq1c[1].set_fill(opacity=0.2)
        sq1c.save_state()

        def en_anim(obj, alpha):
            obj.restore()
            obj.rotate(PI * alpha, about_point=np.array([3, -2, 0]))

        def en_anim2(obj):
            k = sq1c.copy()
            k[0].set_stroke(width=1)
            obj.add(k.copy())

        self.add(sq1c, enve)
        self.play(UpdateFromAlphaFunc(sq1c, en_anim),
                  UpdateFromFunc(enve, en_anim2), run_time=3, rate_func=linear)
        self.wait()
        self.play(Rotating(sq1, PI, about_point=np.array([3, -2, 0])),
                  UpdateFromFunc(enve, lambda a: a.remove(enve[0])),
                  run_time=3, rate_func=linear)
        self.remove(sq1c)
        self.wait()


class AllPointsIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        # digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        for index, points in enumerate(obj.get_all_points()):
            point_id = Text(str(index)) \
                .scale(self.scale_factor).set_color(self.color)
            point_id.move_to(points)
            self.add(point_id)


class Scene12(Scene):
    def construct(self):
        cir = Circle(radius=2).shift(LEFT * 3)
        pol = RegularPolygon(8, color=BLUE_D).scale(2).shift(RIGHT * 3)
        self.play(ShowCreation(cir), ShowCreation(pol))
        self.wait()
        ptc = AllPointsIndex(cir, color=YELLOW_B)
        ptp = AllPointsIndex(pol, color=PURPLE_A)
        self.play(FadeIn(ptc), FadeIn(ptp))
        self.wait()
        self.play(cir.shift, UP * 1.3, ptc.shift, UP * 1.3,
                  pol.shift, UP * 1.3, ptp.shift, UP * 1.3)
        self.wait()
        brace_group = VGroup(
            VGroup(*[Text("(    )", font="Consolas").scale(0.7) for i in range(8)]).arrange(RIGHT),
            VGroup(*[Text("(    )", font="Consolas").scale(0.7) for i in range(8)]).arrange(RIGHT),
            VGroup(*[Text("(    )", font="Consolas").scale(0.7) for i in range(8)]).arrange(RIGHT),
        ).arrange(DOWN).set_color(GOLD_D)
        brace_group.move_to(DOWN * 2)
        self.play(Write(brace_group))
        self.wait()
        num_group = VGroup(
            VGroup(
                *[Text(f"{i}", color=YELLOW_B).scale(0.5).move_to(brace_group[i // 8][i % 8].get_center() + LEFT * 0.2)
                  for i in range(24)]),
            VGroup(
                *[Text(f"{i}", color=PURPLE_A).scale(0.5).move_to(brace_group[i // 8][i % 8].get_center() + RIGHT * 0.2)
                  for i in range(24)]),
        )
        for i in range(24):
            self.play(TransformFromCopy(ptc[i], num_group[0][i]),
                      TransformFromCopy(ptp[i], num_group[1][i]),
                      run_time=max([abs((i - 12.5) / 12), 0.1]))
        self.wait()
        pol_ = pol.copy()
        self.play(TransformFromCopy(cir, pol_), rate_func=linear, run_time=1.8)
        self.wait()
        self.remove(pol_)
        self.play(FadeOut(brace_group, DOWN),
                  FadeOut(num_group, DOWN),
                  cir.shift, DOWN * 1.3, ptc.shift, DOWN * 1.3,
                  pol.shift, DOWN * 1.3, ptp.shift, DOWN * 1.3)
        self.wait()
        sq = Square(side_length=4, color=BLUE_D).move_to(pol.get_center())
        pts = AllPointsIndex(sq, color=PURPLE_A)
        self.play(ReplacementTransform(pol, sq),
                  ReplacementTransform(ptp, pts))
        self.wait()
        sq2 = Polygon(*[sq.data["points"][i] for i in [0, 1, 3, 4, 6, 7, 9, 10]], color=BLUE)
        pts2 = AllPointsIndex(sq2, color=GREEN_A)
        self.play(ReplacementTransform(sq, sq2),
                  ReplacementTransform(pts, pts2))
        self.wait()
        self.play(TransformFromCopy(cir, sq2.copy()), run_time=2, rate_func=linear)
        self.wait()


class OneDay(Scene):
    def construct(self):
        vt1 = ValueTracker(0)
        # vt2 = ValueTracker(0)
        number1 = DecimalNumber(0, num_decimal_places=3).move_to(UP * 1.5)
        number2 = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit='\\%').move_to(DOWN * 1.5)
        number1.add_updater(lambda m: m.set_value(vt1.get_value()))
        number2.add_updater(lambda m: m.set_value(vt1.get_value() / 86400 * 100))
        self.add(number1)
        self.add(number2)
        self.play(vt1.set_value, 86400, rate_func=linear, run_time=86400)
        # self.play(vt.set_value, 100, rate_func=linear, run_time=86400)
        # self.wait(2)


class OneDayTest(Scene):
    def construct(self):
        vt1 = ValueTracker(0)
        vt2 = ValueTracker(0)
        number1 = DecimalNumber(0, num_decimal_places=3).move_to(UP * 1.5)
        number2 = DecimalNumber(0, num_decimal_places=3, include_sign=True, unit='\\%').move_to(DOWN * 1.5)
        number1.add_updater(lambda m: m.set_value(vt1.get_value()))
        number2.add_updater(lambda m: m.set_value(vt1.get_value() / 5 * 100))
        # number2.add_updater(lambda m: m + '%')
        self.add(number1)
        self.add(number2)
        self.play(vt1.set_value, 5, rate_func=linear, run_time=5)
        # self.play(vt2.set_value, 5, rate_func=linear, run_time=5)
        # self.wait(2)


# 查索引用：
def debugTeX(self, texm, scale_factor=0.6, text_color=RED):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="SimSun").scale(scale_factor).set_color(text_color)
        tex_id.move_to(j)
        self.add(tex_id)


class Chapter_01(Scene):
    def construct(self):
        t1 = ValueTracker(0.001)
        t2 = ValueTracker(1)
        t3 = ValueTracker(0.001)
        tex_color = {"{k}": RED_A, "{f(x)}": YELLOW}
        position = [UP, DOWN, LEFT, RIGHT, UR, UL, DR, DL]
        # Axes() = from manimlib.mobject.coordinate_systems import *

        axes = Axes(x_range=(0, 5), y_range=(0, 5), height=5, width=5).shift(np.array([-3, 0, 0]))
        x_y = axes.get_axis_labels()
        curve1 = axes.get_graph(lambda x: x, color=YELLOW).add_updater(
            lambda obj: obj.become(axes.get_graph(lambda x: x, x_range=[0, t1.get_value()], color=YELLOW)))
        l1_h = axes.get_graph(curve1.get_graph).add_updater(
            lambda obj: obj.become(axes.get_graph(t1.get_value(), curve1)))
        l1_v = axes.get_graph(0.001, curve1).add_updater(
            lambda obj: obj.become(axes.get_graph(t1.get_value(), curve1)))
        tex1 = TexMobject(r"{f(x)}={k}x({k}\ne 0)", tex_to_color_map=tex_color).shift(UP * 2 + RIGHT * 3)

        self.play(LaggedStart(*[Write(axes), FadeIn(x_y)]))
        self.add(l1_h, l1_v, curve1)
        self.play(t1.set_value, 4, rate_func=linear)
        self.play(Uncreate(l1_h), Uncreate(l1_v))
        self.play(Write(tex1))
        self.wait(2)

        curve1.clear_updaters()
        curve1.add_updater(
            lambda obj: obj.become(axes.get_graph(lambda x: t2.get_value() * x, x_range=[0, 4], color=YELLOW)))
        axis = NumberLine(x_range=[1, 4], include_numbers=True).shift(np.array([4, -2.4, 0]))
        triangle = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(PI).add_updater(
            lambda obj: obj.move_to(np.array([2.5 + t2.get_value() - 1, -2.1, 0])))
        tex2 = TexMobject("{k}=", tex_to_color_map=tex_color).add_updater(lambda obj: obj.next_to(triangle, UP))
        num = DecimalNumber(1).add_updater(lambda obj: obj.set_value(t2.get_value()).next_to(tex2, RIGHT * 0.5))

        self.play(FadeIn(axis, shift=UP))
        self.add(triangle, num, tex2)
        self.play(t2.set_value, 4, run_time=5.5, rate_func=there_and_back)
        self.wait(2.8)

        curve1.clear_updaters()
        triangle.clear_updaters()
        num.clear_updaters()
        tex2.clear_updaters()
        self.play(LaggedStart(*[FadeOut(i, shift=DOWN) for i in tex1]), LaggedStart(
            *[FadeOut(num, shift=DOWN), FadeOut(tex2, shift=DOWN), FadeOut(triangle, shift=DOWN * 2),
              FadeOut(axis, shift=DOWN * 3)]), run_time=2)

        curve2 = axes.get_graph(lambda x: 5 * x, x_range=[0, 4], color=RED_A)
        y1 = axes.get_graph_label(curve1, "y_{1}=x")
        y2 = axes.get_graph_label(curve2, "y_{2}=5x")
        k1 = Tex("k_{1}", color=YELLOW).shift(RIGHT * 2 + UP * 2)
        k2 = Tex("k_{2}", color=RED_A).shift(RIGHT * 4 + UP * 2)
        tex3 = Tex("<").next_to(k1, RIGHT * 2.5)
        self.play(ShowCreation(curve2))
        self.play(LaggedStart(*[Write(y1), Write(y2)]))
        self.wait(3)
        self.play(LaggedStart(*[GrowFromCenter(k1), GrowFromCenter(k2)]))
        self.play(Write(tex3))
        self.wait(2)
        self.play(LaggedStart(
            *[FadeOut(k1), FadeOut(k2), FadeOut(tex3), FadeOut(y1), FadeOut(y2), FadeOut(curve1), FadeOut(curve2)]))

        def get_tangent(a, b, step):
            curve_group = VGroup()
            for n in np.arange(0, 4, step):
                k = 2 * a * n + b
                y1 = a * (n ** 2)
                curve = axes.get_graph(lambda x: k * x - k * (n) + y1, color=BLUE_B)
                curve_group.add(curve)
            return curve_group

        def get_point_of_tangency(a, b, step):
            dot_group = VGroup()
            for n in np.arange(0, 4, step):
                dot = SmallDot(axes.coords_to_point(n, a * (n ** 2) + b * n), color=BLUE_B)
                dot_group.add(dot)
            return dot_group

        def get_x_dots(step):
            dot_group = VGroup()
            for n in np.arange(0, 4, step):
                dot = SmallDot(axes.coords_to_point(n, 0), color=TEAL)
                dot_group.add(dot)
            return dot_group

        curve3 = axes.get_graph(lambda x: 0.3 * (x ** 2), x_range=[0, 4], color=YELLOW).add_updater(
            lambda obj: obj.become(axes.get_graph(lambda x: 0.3 * (x ** 2), x_range=[0, t3.get_value()], color=YELLOW)))
        l2_h = axes.get_h_line_to_graph(0.001, curve3).add_updater(
            lambda obj: obj.become(axes.get_h_line_to_graph(t3.get_value(), curve3)))
        l2_v = axes.get_v_line_to_graph(0.001, curve3).add_updater(
            lambda obj: obj.become(axes.get_v_line_to_graph(t3.get_value(), curve3)))
        self.add(curve3, l2_h, l2_v)
        self.play(t3.set_value, 4, run_time=2, rate_func=linear)
        self.play(Uncreate(l2_h), Uncreate(l2_v))
        self.wait(2)
        curve3.clear_updaters()

        dot_g1 = get_x_dots(0.5)
        dot_g2 = get_point_of_tangency(0.3, 0, 0.5)
        tangent_g1 = get_tangent(0.3, 0, 0.5)
        tangent_g2 = get_tangent(0.3, 0, 0.2)
        tangent_g3 = get_tangent(0.3, 0, 0.1)
        tangent_g4 = get_tangent(0.3, 0, 0.08)
        self.play(LaggedStart(*[FadeIn(i, shift=DOWN * n) for i, n in zip(dot_g1, np.arange(0, 4, 0.5))]))
        self.play(LaggedStart(*[ReplacementTransform(a, b) for a, b in zip(dot_g1, dot_g2)]))
        self.play(LaggedStart(*[ReplacementTransform(c, d) for c, d in zip(dot_g2, tangent_g1)]))
        self.wait(4.5)
        self.play(ReplacementTransform(tangent_g1, tangent_g2))
        self.play(ReplacementTransform(tangent_g2, tangent_g3))
        self.play(ReplacementTransform(tangent_g3, tangent_g4))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeOut(i, shift=random.choice(position) * 3) for i in tangent_g4]))
        self.play(FadeOut(curve3), FadeOut(axes), FadeOut(x_y))


class Chapter_02(Scene):
    def construct(self):
        tex_color = {"{x_{1}}": TEAL_B, "{x_{2}}": TEAL_C, "{y_{1}}": BLUE_B, "{y_{2}}": BLUE_C, "{k}": RED_A}

        axes = Axes(x_range=(0, 5), y_range=(0, 5), height=5, width=5).shift(np.array([-3, 0, 0]))
        x_y = axes.get_axis_labels()
        curve = axes.get_graph(lambda x: 0.53 * x + 0.5, x_range=[0, 4], color=YELLOW)
        self.wait(6)
        self.play(LaggedStart(*[Write(axes), FadeIn(x_y)]))
        self.play(ShowCreation(curve))
        self.wait(1.5)
        d1 = Dot(axes.coords_to_point(0.7, 0.53 * 0.7 + 0.5), color=TEAL_B)
        d2 = Dot(axes.coords_to_point(2.1, 0.53 * 2.1 + 0.5), color=TEAL_C)
        tex1 = MTex("({x_{1}}, {y_{1}})", tex_to_color_map=tex_color).next_to(d1, RIGHT * 0.5)
        tex2 = MTex("({x_{2}}, {y_{2}})", tex_to_color_map=tex_color).next_to(d2, RIGHT * 0.5)
        tex3 = MTex("{y_{1}} = {k} {x_{1}} + b ", tex_to_color_map=tex_color).shift(RIGHT * 3.5 + UP * 2)
        tex4 = MTex("{y_{2}} = {k} {x_{2}} + b ", tex_to_color_map=tex_color).next_to(tex3, DOWN * 0.8,
                                                                                      aligned_edge=LEFT)
        tex5 = MTex("{y_{1}} - {y_{2}} = {k} {x_{1}} - {k} {x_{2}} + b - b", tex_to_color_map=tex_color).next_to(tex4,
                                                                                                                 DOWN * 0.8)

        self.play(LaggedStart(*[FadeIn(d1, shift=UP), FadeIn(d2, shift=UP * 1.5)]))
        self.wait(1)
        self.play(LaggedStart(*[FadeIn(tex1, shift=UP), FadeIn(tex2, shift=UP * 1.5)]))
        self.wait(4)
        self.play(LaggedStart(*[
            ReplacementTransform(tex1[1:3].copy(), tex3[4:6]),
            ReplacementTransform(tex1[4:6].copy(), tex3[0:2]),
            ReplacementTransform(tex2[1:3].copy(), tex4[4:6]),
            ReplacementTransform(tex2[4:6].copy(), tex4[0:2])]),
                  *[Write(tex3[i]) for i in range(len(tex3)) if i != 4 and i != 5 and i != 0 and i != 1],
                  *[Write(tex4[i]) for i in range(len(tex4)) if i != 4 and i != 5 and i != 0 and i != 1],
                  )
        self.wait(1)
        self.play(LaggedStart(*[
            ReplacementTransform(tex3[0:2], tex5[0:2], path_arc=PI),
            ReplacementTransform(tex4[0:2], tex5[3:5], path_arc=PI)]),
                  Write(tex5[2])
                  )
        self.play(Write(tex5[5]))
        self.play(LaggedStart(*[
            ReplacementTransform(tex3[3:6], tex5[6:9], path_arc=PI),
            ReplacementTransform(tex4[3:6], tex5[10:13], path_arc=PI),
            ReplacementTransform(tex3[6][1], tex5[13][1], path_arc=PI),
            ReplacementTransform(tex4[6][1], tex5[13][3], path_arc=PI)]),
                  *[Write(tex5[9]), Write(tex5[13][0]), Write(tex5[13][2])],
                  *[FadeOut(tex3[2]), FadeOut(tex3[6][0]), FadeOut(tex4[2]), FadeOut(tex4[6][0])]
                  )

        tex6 = MTex("{y_{1}} - {y_{2}} = {k} ( {x_{1}} -  {x_{2}} )", tex_to_color_map=tex_color).shift(
            tex5.get_center())
        tex7 = MTex("{{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}}  = {k}", tex_to_color_map=tex_color).shift(
            tex5.get_center())
        tex8 = MTex(" {k} = {{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}} ", tex_to_color_map=tex_color).shift(
            tex5.get_center())
        self.play(TransformMatchingMTex(tex5, tex6))
        self.play(TransformMatchingMTex(tex6, tex7))
        self.play(TransformMatchingMTex(tex7, tex8))
        self.play(ShowCreationThenDestructionAround(tex8))
        self.wait(19)

        self.play(LaggedStart(
            *[FadeOut(tex8), FadeOut(axes), FadeOut(curve), FadeOut(d1), FadeOut(d2), FadeOut(tex1), FadeOut(tex2),
              FadeOut(x_y)]))


class Chapter_03(Scene):
    def construct(self):
        tex_color1 = {r"$ \Delta x $": TEAL_D, "$x_{0}$": BLUE_D, "$x$": GOLD_E, "$y$": YELLOW,
                      r"$ \Delta y$": PURPLE_C}
        tex_color2 = {
            "{x}": GOLD_E,
            r"{\Delta x}": TEAL_D,
            "{x_{0}}": BLUE_D,
            r"\Delta y": PURPLE_C,
            "{x_{1}}": TEAL_B,
            "{x_{2}}": TEAL_C,
            "{y_{1}}": BLUE_B,
            "{y_{2}}": BLUE_C,
            "{k}": RED_A
        }

        definition = TexText(
            "假设函数", "$y$", "$=f$", "(", "$x$", r")在\\点",
            "$x_{0}$", r"处的邻域内有定义\\当自变量",
            "$x$", "在", "$x_{0}$", "处取得增量", r"$ \Delta x $\\",
            "相应的函数取得增量", r"$ \Delta y$ ", "如果", r"$ \Delta y \over  \Delta x $", "在", r"$ \Delta x $",
            r"$\rightarrow 0  $\\",
            r"时的极限存在", "那么称函数", "$y$", "$=f$", "(", "$x$", ")  在点  ", "$x_{0}$ ", "处可导"
        ).set_color_by_tex_to_color_map(tex_color1)
        definition[16][0:2].set_color(PURPLE_C)
        definition[16][3:].set_color(TEAL_D)
        tex1 = MTex(
            r"f^{\prime}({x})=\lim _{{\Delta x} \rightarrow 0} {f({x_{0}}+{\Delta x})-f({x_{0}}) \over {\Delta x}}",
            tex_to_color_map=tex_color2)
        tex2 = MTex(r"f^{\prime}({x})=\lim _{{\Delta x} \rightarrow 0} {{\Delta y} \over {\Delta x}}",
                    tex_to_color_map=tex_color2)
        callout = MTex(r"{\Delta y}\\ \Uparrow ", tex_to_color_map=tex_color2).next_to(tex1[7:15].get_center(),
                                                                                       UP * 2.5)
        tex3 = MTex(" {k} = {{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}} ", tex_to_color_map=tex_color2).to_corner(UL)
        tex4 = MTex("{k} ={{\Delta y} \over {\Delta x}}", tex_to_color_map=tex_color2).to_corner(UL)

        self.play(Write(definition), run_time=2.5)
        self.wait(29)
        self.play(TransformMatchingShapes(definition, tex1), run_time=1.5)
        self.wait(7)
        self.play(tex1[:7].animate.set_fill(opacity=0.3), tex1[16:].animate.set_fill(opacity=0.3))
        self.wait(4)
        self.play(Write(callout))
        self.play(
            ReplacementTransform(callout[0], tex2[7]),
            FadeOut(tex1[7:16]),
            *[FadeOut(tex1[i]) for i in range(len(tex2)) if
              i != 7 and i != 8 and i != 9 and i != 10 and i != 11 and i != 12 and i != 13 and i != 14 and i != 15],
            *[Write(tex2[i]) for i in range(len(tex2)) if i != 7],
            FadeOut(callout[1]), run_time=1.5
        )
        self.wait(6)
        self.play(FadeIn(tex3))
        self.play(FadeOut(tex3[2:]))
        self.play(FadeIn(tex4[2:]), ReplacementTransform(tex3[:2], tex4[:2]))
        self.play(Indicate(tex4[2:]), Indicate(tex2[7:]))
        self.play(tex4[:2].animate.next_to(tex2, LEFT * 0.5), FadeOut(tex4[2:]))
        self.wait(5)
        self.play(FadeOut(tex4[:2]), FadeOut(tex2))


class Chapter_04(Scene):
    def construct(self):
        frame = self.camera.frame
        tex_color = {"{x_{1}}": TEAL_B, "{x_{2}}": TEAL_C, "{y_{1}}": BLUE_B, "{y_{2}}": BLUE_C, "{k}": RED_A}
        tex_color2 = {
            "{x}": GOLD_E,
            r"{\Delta x}": TEAL_D,
            "{x_{0}}": BLUE_D,
            r"\Delta y": PURPLE_C,
            "{k}": RED_A
        }

        axes = Axes(x_range=(0, 5), y_range=(0, 5), height=5, width=5).shift(np.array([-3, 0, 0]))
        x_y = axes.get_axis_labels()
        curve = axes.get_graph(lambda x: 0.3 * (x ** 2), x_range=[0, 4], color=BLUE)
        fx = axes.get_graph_label(curve, "f(x)=0.3x^{2}")

        self.play(LaggedStart(*[Write(axes), FadeIn(x_y)]))
        self.play(ShowCreation(curve))
        self.wait(2)
        self.play(Write(fx))
        self.wait(4)

        d1 = Dot(axes.coords_to_point(1, 0.3))
        d1_pos = MTex("({1}, {0.3})", tex_to_color_map={"{1}": TEAL_B, "{0.3}": BLUE_B}).next_to(d1, LEFT * 0.5)
        d2 = Dot(axes.coords_to_point(3, 2.7))
        d2_pos = MTex("({3}, {2.7})", tex_to_color_map={"{3}": TEAL_B, "{2.7}": BLUE_B}).next_to(d2, LEFT * 0.5)

        tangent_l = axes.get_graph(lambda x: (2 * 1 * 0.3) * x - (2 * 1 * 0.3) * 1 + 0.3 * (1 ** 2))
        tangent_l_copy = DashedVMobject(tangent_l.copy())
        l1 = axes.get_graph(lambda x: 1.2 * x - 0.9)
        l1_copy = DashedVMobject(l1.copy())
        tex1 = MTex(r" {k} = {{y_{1}} - {y_{2}} \over {x_{1}} -  {x_{2}}} ", tex_to_color_map=tex_color).shift(
            UP * 2 + RIGHT * 5)
        tex2 = MTex(r"{k_{1}} = {{{0.3} - {2.7}} \over {{1} - {3}} }",
                    tex_to_color_map={"{1}": TEAL_B, "{0.3}": BLUE_B, "{3}": TEAL_B, "{2.7}": BLUE_B,
                                      "{k_{1}}": RED_B}).next_to(tex1, DOWN * 0.8)
        tex3 = MTex(r"{k_{1}} = {1.2}", tex_to_color_map={"{k_{1}}": RED_B, "{1.2}": GOLD}).next_to(tex1, DOWN,
                                                                                                    aligned_edge=LEFT)

        self.play(LaggedStart(*[FadeIn(d1), FadeIn(d1_pos, shift=UP)]))
        self.play(GrowFromCenter(tangent_l))
        self.wait(10)
        self.play(LaggedStart(*[FadeIn(d2), FadeIn(d2_pos, shift=UP)]))
        self.play(Write(tex1))
        self.play(Write(tex2))
        self.play(TransformMatchingShapes(tex2, tex3))
        self.play(LaggedStart(*[ReplacementTransform(tangent_l, l1), FadeIn(tangent_l_copy)]))
        self.wait(11)

        def get_line(pos):
            n_pos = axes.point_to_coords(pos)
            k = (n_pos[1] - 0.3 * (1 ** 2)) / (n_pos[0] - 1)
            b = 0.3 - 1 * k
            return lambda x: k * x + b

        t = ValueTracker(3)
        d3 = d2.copy().set_color(ORANGE).add_updater(
            lambda obj: obj.move_to(axes.coords_to_point(t.get_value(), 0.3 * (t.get_value() ** 2))))
        l2 = axes.get_graph(get_line(d3.get_center()), color=GREEN_D).add_updater(
            lambda obj: obj.become(axes.get_graph(get_line(d3.get_center()), color=GREEN_D)))
        l3 = Line(color=YELLOW).add_updater(lambda obj: obj.put_start_and_end_on(d1.get_center(), np.array(
            [d3.get_center()[0], d1.get_center()[1], 0])))
        l4 = Line(color=ORANGE).add_updater(lambda obj: obj.put_start_and_end_on(d3.get_center(), np.array(
            [d3.get_center()[0], d1.get_center()[1], 0])))
        brace1 = Brace(l3, direction=DOWN * 2).add_updater(
            lambda obj: obj.become(Brace(l3, direction=DOWN * 2).set_color(YELLOW))).set_color(YELLOW)
        tex4 = MTex(r"{\Delta x}", tex_to_color_map={r"{\Delta x}": TEAL_D}).add_updater(
            lambda obj: obj.next_to(brace1, DOWN * 0.8))
        brace2 = Brace(l4, direction=RIGHT * 2).add_updater(
            lambda obj: obj.become(Brace(l4, direction=RIGHT * 2).set_color(ORANGE))).set_color(ORANGE)
        tex5 = MTex(r"{\Delta y}", tex_to_color_map={r"{\Delta y}": PURPLE_C}).add_updater(
            lambda obj: obj.next_to(brace2, RIGHT * 0.8))

        self.play(frame.animate.shift(LEFT * 2 + DOWN).set_width(10), LaggedStart(*[FadeOut(l1), FadeIn(l1_copy)]),
                  LaggedStart(*[ShowCreation(l2), ShowCreation(l3), ShowCreation(l4), ShowCreation(brace1),
                                ShowCreation(brace2), ShowCreation(tex4), ShowCreation(tex5)]), run_time=2)
        self.add(l2, l3, l4, d3, d1, brace1, brace2, tex4, tex5)
        self.play(t.animate.set_value(1.00000001), run_time=6)
        self.play(t.animate.set_value(3), run_time=5)
        self.play(frame.animate.to_default_state())

        tex6 = MTex(r"{k}=\lim_{{\Delta x} \to 0} {0.3({x}+ {\Delta x})^{2} - 0.3{x}^2 \over {\Delta x}}",
                    tex_to_color_map=tex_color2, font_size=36).next_to(tex3, DOWN)
        tex7 = MTex(r"{k}=\lim_{{\Delta x} \to 0} 0.3{\Delta x}+0.6{x}", tex_to_color_map=tex_color2,
                    font_size=36).next_to(tex3, DOWN)
        tex8 = MTex("{k}=0.6", tex_to_color_map=tex_color2, font_size=36).next_to(tex7, DOWN)
        tex9 = MTex(r"{\Delta x} \ne 0", tex_to_color_map=tex_color2, font_size=36).next_to(tex8, DOWN)
        self.play(Write(tex6))
        self.play(TransformMatchingShapes(tex6, tex7))
        self.wait(10)
        self.play(Write(tex8))
        self.play(Write(tex9))
        self.wait(12)

        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(
                    np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


class End(Scene):
    def construct(self):
        t = TexText("@E{r}{s}net", tex_to_color_map={"{r}": "#0088FF", "{s}": "#B46F00"}, font_size=100)
        self.play(FadeIn(t), run_time=2)


def R(pos, color):
    re = Rectangle(height=0.5, width=1).shift(np.array(pos)).set_color(color)
    l1 = Line(np.array([re.get_edge_center(LEFT)[0] - 0.5, re.get_edge_center(LEFT)[1], 0]), re.get_edge_center(LEFT))
    l2 = Line(np.array([re.get_edge_center(RIGHT)[0] + 0.5, re.get_edge_center(RIGHT)[1], 0]),
              re.get_edge_center(RIGHT))
    return VGroup(re, l1, l2)


class ErsFadeInFromRandom(LaggedStart):
    CONFIG = {
        "directions": [DL, DOWN, DR, RIGHT, UR, UP, UL, LEFT],
        "magnitude": 0.5,
        "lag_ratio": 0
    }

    def __init__(self, text, **kwargs):
        digest_config(self, kwargs)
        super().__init__(
            *[FadeInFromPoint(obj, point=random.choice(self.directions) * self.magnitude)
              for obj in text],
            **kwargs
        )


class chapter_01(Scene):
    def construct(self):
        tex_color = {r"$n$": BLUE_B, r"$m_{1}$": TEAL_A, r"$m_{2}$": TEAL_B, r"$m_{3}$": TEAL_C, r"$m_{n} $": TEAL_D,
                     r"$N$": BLUE_D}

        title = Title("分类加法计数原理", stroke_color=BLACK)
        self.wait(10)
        self.play(Write(title))

        definition1 = TextMobject(r"完成某件事有", r"$n$", r"类办法，在第一类中\\有", r"$m_{1}$",
                                  "种不同的方法，第二类中有",
                                  r"$m_{2}$", r"种不同的方法，\\则完成这件事共有", r"$N$", "$=$", r"$m_{1}$", " $+$",
                                  r"$m_{2}$", "$+$", r"$m_{3}$", r"$ +\cdots +$", r"$m_{n} $",
                                  "种不同的方法").set_color_by_tex_to_color_map(tex_color)
        self.play(Write(definition1))
        self.wait(16)
        # self.play(LaggedStart(*[FadeOut(i) for i in definition1[:7]], *[FadeOut(i) for i in definition1[16:]],
        #                       definition1[7:16].shift(UP * 2.5 + LEFT * 4)))

        tex1 = TextMobject(r"""1""",
                           tex_to_color_map={"{m_{1}}": TEAL_A, "{m_{2}}": TEAL_B, "{m_{3}}": TEAL_C, "{m_{n}}": TEAL_D,
                                             "{N}": BLUE_D}).shift(np.array([-4.5, -1, 0]))
        self.play(LaggedStart(*[
            ReplacementTransform(definition1[9].copy(), tex1[2:4], path_arc=-PI),
            ReplacementTransform(definition1[11].copy(), tex1[4:6], path_arc=-PI),
            ReplacementTransform(definition1[13].copy(), tex1[6:8], path_arc=-PI),
            # ReplacementTransform(definition1[15].copy(), tex1[9:11], path_arc=-PI)]),
            #       *[Write(tex1[:2]), Write(tex1[8:9])], run_time=2.5)
        ]))
        self.wait(5)

        r1 = R([3, 1, 0], TEAL_A)
        r2 = R([3, 0, 0], TEAL_B)
        r3 = R([3, -1, 0], TEAL_C)
        r4 = R([3, -3, 0], TEAL_C)
        tex2 = TexMobject(r"\vdots").shift(np.array([3, -2, 0]))
        self.play(LaggedStart(*[Transform(tex1[2:4].copy(), r1), Transform(tex1[4:6].copy(), r2),
                                Transform(tex1[6:8].copy(), r3), Transform(tex1[9:11].copy(), r4),
                                # Transform(tex1[8].copy(), tex2)]), run_time=1.5)
                                ]))

        l1 = Line(np.array([2, -3.7, 0]), np.array([2, 1, 0]))
        l2 = Line(np.array([4, -3.7, 0]), np.array([4, 1, 0]))
        l3 = Line(np.array([4, -3.7, 0]), np.array([3.5, -3.7, 0]))
        l4 = Line(np.array([2, -3.7, 0]), np.array([2.5, -3.7, 0]))
        u = TexMobject("220V").shift(np.array([3, -3.7, 0])).scale(0.5)
        d1 = Dot(np.array([2, -3.7, 0])).set_color(YELLOW)
        d2 = Dot(np.array([2, -3, 0])).set_color(YELLOW)
        d3 = Dot(np.array([2, -1, 0])).set_color(YELLOW)
        d4 = Dot(np.array([2, 0, 0])).set_color(YELLOW)
        p1 = TracedPath(d1.get_center, stroke_color=YELLOW, stroke_width=4)
        p2 = TracedPath(d2.get_center, stroke_color=YELLOW, stroke_width=4)
        p3 = TracedPath(d3.get_center, stroke_color=YELLOW, stroke_width=4)
        p4 = TracedPath(d4.get_center, stroke_color=YELLOW, stroke_width=4)

        self.play(
            LaggedStart(*[GrowFromCenter(l1), GrowFromCenter(l2), GrowFromCenter(l3), GrowFromCenter(l4), FadeIn(u)]))
        self.play(FadeIn(d1))
        self.add(p1, p2, p3, p4)
        self.play(MoveAlongPath(d1, l1))
        self.play(d1.shift, RIGHT * 2)
        self.play(d1.shift, DOWN * (l2.get_length()))
        self.play(LaggedStart(*[
            ReplacementTransform(d1.copy(), d2),
            ReplacementTransform(d1.copy(), d2),
            ReplacementTransform(d1.copy(), d3),
            ReplacementTransform(d1.copy(), d4)
        ]))
        # self.play(LaggedStart(*[d2.shift(RIGHT * 2), d3.shift(RIGHT * 2), d4.shift(RIGHT * 2)]))
        # self.play(LaggedStart(*[d2.move_to,np.array([4, -3.7, 0]), d3.move_to,np.array([4, -3.7, 0]),
        #                         d4.move_to,np.array([4, -3.7, 0])]))

        tex3 = TexMobject("{N}=", tex_to_color_map={"{N}": BLUE_D}).shift(LEFT)
        tex4 = TexMobject("1").next_to(tex3, RIGHT * 0.8).set_color(YELLOW)
        tex5 = TexMobject("2").next_to(tex3, RIGHT * 0.8).set_color(YELLOW)
        tex6 = TexMobject("3").next_to(tex3, RIGHT * 0.8).set_color(YELLOW)

        self.play(Write(tex3))
        # self.play(Transform(p1.copy(), tex4))
        # self.play(Transform(p4.copy(), tex5), FadeOut(tex4))
        # self.play(Transform(p3.copy(), tex6), FadeOut(tex5))
        self.play(FadeOut(tex6))

        ani_g = []
        num_g = VGroup()
        for i in range(4, 114514, 1000):
            num = TexMobject(f"{i}").next_to(tex3, RIGHT * 0.8).set_color(YELLOW)
            tex = TexMobject(f"{i}").next_to(tex3, RIGHT * 0.8).set_color(YELLOW).scale(0.00001)
            transform = FadeTransform(p3.copy(), tex)
            ani_g.append(transform)
            num_g.add(num)
        self.play(LaggedStart(*[FadeIn(i, rate_func=there_and_back) for i in num_g]), LaggedStart(*[a for a in ani_g]))

        tex7 = MTex("n").set_color(TEAL_D).next_to(tex3, RIGHT * 0.8)
        self.play(FadeTransform(p2.copy(), tex7))

        s_g = VGroup()
        for x in range(-8, 8):
            for y in range(-5, 5):
                s = Square(side_length=1, stroke_color=BLACK, fill_color=BLACK, fill_opacity=1).shift(
                    np.array([x, y, 0]))
                s_g.add(s)
        self.play(*[FadeIn(i) for i in s_g])


# TODO this is done very well
class GridUpdateTest(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # square.add_updater(square.apply_function(self.func))
        # self.play(Transform(square, circle), run_time=8)
        # self.wait(3)
        # number.clear_updaters()
        # self.remove(square)
        # number.add_updater(lambda m: m.set_value(get_area(circle)))
        # self.play(Transform(circle, tri2), run_time=8)
        # self.wait(3)
        # number.clear_updaters()
        # self.remove(circle)
        # number.add_updater(lambda m: m.set_value(get_area(tri2)))
        # self.play(Transform(tri2, elli1), run_time=8)
        # self.wait(3)
        # number.clear_updaters()
        # self.remove(tri2)
        # number.add_updater(lambda m: m.set_value(get_area(elli1)))
        # self.play(Transform(elli1, sq2), run_time=8)
        # self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: math.e ** z, square.apply_complex_function,
                  lambda z: math.e ** z,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest02(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(circle)))
        self.add(number)
        self.add(circle)
        self.play(numberplane.apply_complex_function, lambda z: z ** 2,
                  circle.apply_complex_function,
                  lambda z: z ** 2,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest03(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(elli1)))
        self.add(number)
        self.add(elli1)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** 2,
                  elli1.apply_complex_function,
                  lambda z: z ** 2,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest04(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(tri2)))
        self.add(number)
        self.add(tri2)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** 2,
                  tri2.apply_complex_function,
                  lambda z: z ** 2,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest05(Scene):
    def construct(self):
        numberplane = NumberPlane()
        self.add(numberplane)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(sq2)))
        self.add(number)
        self.add(sq2)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** 2,
                  sq2.apply_complex_function,
                  lambda z: z ** 2,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class Whatever(Scene):
    def construct(self):
        a = Cube()
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(VolumsOfNBalls, a))
        self.add(number)
        self.wait(2)


class ArabicTest(Scene):
    def construct(self):
        t = TexMobject(r'''
        \RL مرحب
        ''')
        self.play(Write(t))
        self.wait(3)


class GridUpdateTest06(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(cube)))
        self.add(number)
        self.add(cube)
        # self.wait(2)
        self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** 2,
                  cube.apply_complex_function,
                  lambda z: z ** 2,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest07(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: 2.2222 ** z,
                  square.apply_complex_function,
                  lambda z: 2.2222 ** z,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


# TODO this class makes the area of shapes ** 2
class GridUpdateTest08(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** 3,
                  square.apply_complex_function,
                  lambda z: z ** 3,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest09(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(circle)))
        self.add(number)
        self.add(circle)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** 3,
                  circle.apply_complex_function,
                  lambda z: z ** 3,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest10(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: cmath.tan(z) ** z,
                  square.apply_complex_function,
                  lambda z: cmath.tan(2) ** z,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest11(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: cmath.sqrt(z) ** z,
                  square.apply_complex_function,
                  lambda z: cmath.sqrt(2) ** z,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest12(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** cmath.sqrt(z),
                  square.apply_complex_function,
                  lambda z: z ** cmath.sqrt(z),
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest13(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** cmath.sin(z),
                  square.apply_complex_function,
                  lambda z: z ** cmath.sin(z),
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest14(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square()
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** cmath.sqrt(math.e ** z),
                  square.apply_complex_function,
                  lambda z: z ** cmath.sqrt(math.e ** z),
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest15(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square(color=RED)
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: z ** cmath.e ** cmath.pi,
                  square.apply_complex_function,
                  lambda z: z ** cmath.e ** cmath.pi,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest16(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square(color=RED)
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: cmath.sinh(z) ** cmath.e,
                  square.apply_complex_function,
                  lambda z: cmath.sinh(z) ** cmath.e,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class GridUpdateTest17(ThreeDScene):
    def construct(self):
        numberplane = NumberPlane()
        # axes = ThreeDAxes()
        self.add(numberplane)
        # self.add(axes)
        numberplane.prepare_for_nonlinear_transform()
        square = Square(color=RED)
        circle = Circle()
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
        cube = Cube()
        sq2 = Polygon(p1, p2, p3, p4)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        self.add(number)
        self.add(square)
        # self.wait(2)
        # self.set_camera_orientation(phi=40 * DEGREES, theta=40 * DEGREES)
        self.wait(2)
        self.play(numberplane.apply_complex_function, lambda z: cmath.sqrt(z) ** cmath.e,
                  square.apply_complex_function,
                  lambda z: cmath.sqrt(z) ** cmath.e,
                  run_time=10, )
        # square.add_updater(square.apply_function(self.func))
        self.wait(3)


class SurfaceAreaTest(Scene):
    def construct(self):
        cube = Cube()
        sphere = Sphere(radius=2.5)
        self.add(cube)
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(cube)))
        self.add(number)
        self.wait(2)
        self.play(Transform(cube, sphere))
        self.wait(2)


class AAATest(Scene):
    def construct(self):
        a = TexMobject('a')
        self.play(Write(a))
        self.wait(3)


class AnotherTest(GraphScene):
    def construct(self):
        # class Axes:
        #     def get_lines_to_point(self, point) -> VGroup:
        #         """Generate both horizontal and vertical lines from the axis to a point.
        #
        #         Parameters
        #         ----------
        #         point
        #             A point on the scene.
        #         kwargs
        #             Additional parameters to be passed to :meth:`get_line_from_axis_to_point`
        #
        #         Returns
        #         -------
        #         :class:`~.VGroup`
        #             A :class:`~.VGroup` of the horizontal and vertical lines.
        #
        #
        #         .. seealso::
        #             :meth:`~.CoordinateSystem.get_vertical_line`
        #             :meth:`~.CoordinateSystem.get_horizontal_line`
        #
        #         Examples
        #         --------
        #         .. manim:: GetLinesToPointExample
        #             :save_last_frame:
        #
        #             class GetLinesToPointExample(Scene):
        #                 def construct(self):
        #                     ax = Axes()
        #                     circ = Circle(radius=0.5).move_to([-4, -1.5, 0])
        #
        #                     lines_1 = ax.get_lines_to_point(circ.get_right(), color=GREEN_B)
        #                     lines_2 = ax.get_lines_to_point(circ.get_corner(DL), color=BLUE_B)
        #                     self.add(ax, lines_1, lines_2, circ)
        #         """
        #
        #         return VGroup(
        #             self.get_horizontal_line(point, **kwargs),
        #             self.get_vertical_line(point, **kwargs),
        #         )
        vt = ValueTracker(0)
        vt2 = ValueTracker(0)
        # vt.add_updater(vt.set_value,5, rate_func=linear, run_time=5)
        numberplane = NumberPlane()
        self.add(numberplane)
        axes = Axes()
        self.add(axes)
        square = Square()
        circle = Circle()
        number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number.add_updater(lambda m: m.set_value(get_area(square)))
        numberv = number.get_value()

        number_time = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 1.6, 0]))
        number_time.add_updater(lambda m: m.set_value(vt.get_value()))
        number_timev = number_time.get_value()
        self.add(number, number_time)
        # dot = Dot(axes.coords_to_point(number_timev, numberv))
        dot = Dot()
        dot.add_updater(lambda m: m.move_to(np.array([number_timev, numberv, 0])))
        # dot = Dot(np.array([number_timev, numberv, 0]))
        # lines = axes.get_lines_to_point(axes.c2p(2, 2))
        self.add(dot)
        # self.play(vt.set_value, 2)
        self.play(Transform(square, circle), run_time=10), (vt.set_value, 2)
        # self.play(vt.set_value, 2)


class Testt(GraphScene):
    def construct(self):
        self.setup_axes(animate=True)
        path = VMobject()

        vt = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        self.add(number)
        # self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        self.wait(2)

        dot_x = Dot()
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot()
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot()
        # dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number.get_value(), 0])).become(dot_copy))
        self.bring_to_back(self.axes)
        # dot.copy()
        # self.add(dot.copy())
        # dot.start_new_path(point=dot)
        # dot.has_new_path_started()
        # dot_path = dot.get_subpaths()
        # def path_updater():

        # path_group = VGroup(dot)
        # def path_updater(_):
        #     path = VMobject(color=RED)
        #     old_path = path.copy()
        #     path.become(old_path)
        # def update_group(group):
        #     # c, f_d, d_d, d = group
        #     c = group
        #     f_d = group
        #     d_d = group
        #     d = group
        #     # d.move_to(self.coords_to_point(dot_guide.get_center()[0], 0))
        #     radius = get_norm(dot.get_center() - dot.get_center())
        #     new_c = Circle(radius=radius)
        #     new_c.move_to(dot)
        #     c.become(new_c)
        #     f_d.become(DashedLine(dot.get_center(), dot.get_center()))
        #     d_d.become(DashedLine(dot.get_center(), dot.get_center()))
        dot_copy = dot.copy().set_stroke(WHITE, opacity=1)

        # dot.add_updater(lambda obj: obj.become(dot_copy))
        # path_group.add_updater(update_group)
        # self.add(dot)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        # self.add(dot.copy())
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))
        self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        # for _ in range(dot_x + dot_y):
        # dot = Dot().move_to(np.array([number.get_value(),number.get_value(),0]))
        # self.add(dot)


class CopyTest(Scene):
    def construct(self):
        dot = Dot()
        dot_copy = dot.copy()
        self.play(Write(dot_copy))
        self.wait(3)


class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.shift, UP)
        self.play(dot.shift, LEFT)
        self.wait()


class TesttWithoutComment(GraphScene):
    def construct(self):
        axes = Axes()
        self.add(axes)
        # self.setup_axes(animate=True)
        path = VMobject()

        vt = ValueTracker(0)
        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        self.add(number)
        self.wait(2)

        dot_x = Dot()
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot()
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot()
        # self.bring_to_back(self.axes)

        dot_copy = dot.copy().set_stroke(WHITE, opacity=1)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))
        self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        # line = Square()
        # line2 = Circle()
        # number = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        # number.add_updater(lambda m: m.set_value(get_area(line))


class DecimalToGraph1(GraphScene):
    def construct(self):
        axes = Axes()
        self.add(axes)
        # self.setup_axes(animate=True)
        path = VMobject()

        vt = ValueTracker(0)
        # vt2 = ValueTracker(0)
        # vt.add_updater(lambda obj: obj.set_value(10))
        # vt.set_value( 10, rate_func=linear, run_time=10)
        # vt.add_updater(vt.set_value(10, rate_func=linear, run_time=10))
        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        self.add(number)
        line = Square()
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        self.add(number2)
        self.wait(2)

        dot_x = Dot()
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot()
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot()
        # self.bring_to_back(self.axes)

        dot_copy = dot.copy().set_stroke(WHITE, opacity=1)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        # while self.play(vt.set_value, 10, rate_func=linear, run_time=10):
        #     # self.play(Transform(line, line2))
        #     pass
        # def vt_updater(obj):
        #     self.play(vt.set_value,10, run_time=10, rate_func=linear)
        # vt.add_updater(vt_updater)
        # vt.add_updater(lambda m: self.play(m.set_value,10, run_time=10, rate_func=linear))

        vg = VGroup()
        vg.add_updater(lambda m: self.play(Transform(line, line2), run_time=10))
        #                          and self.play(vt.set_value,10,rate_func=linear,run_time=10))

        # self.play(vt.set_value,10,rate_func=linear,run_time=10)
        # self.play(Transform(line, line2),run_time=10)  # and self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        # func = self.play(vt.set_value, 10, rate_func=linear, run_time=10)
        # vt.add_updater(lambda m: self.play(m.set_value(10),run_time=10, rate_func=linear))
        # vt.add_updater(self.play(vt.set_value(10), rate_func=linear, run_time=10))
        # vt
        # vt.add_updater(self.play(vt.set_value, 10, rate_func=linear, run_time=10))
        # vt.clear_updaters()
        # self.play(Transform(line, line2))
        vg.clear_updaters()
        self.wait(3)
        # number.add_updater(self.play(number.set_value, 10))


# TODO this is done very very well!
class DecimalToGraph2(GraphScene, MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        axes = Axes(x_min=-3, x_max=13)
        self.add(axes)

        path = VMobject()

        vt = ValueTracker(0)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        self.add(number)
        line = Square()
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5).move_to(np.array([-4, 2.6, 0]))
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        self.add(number2)
        self.wait(2)

        dot_x = Dot()
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot()
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot()

        dot_copy = dot.copy().set_stroke(WHITE, opacity=1)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        # number3 = dot.get_x()
        # dot.add_updater(lambda obj: obj.move_to(np.array([number, number2.get_value(), 0])))
        # self.play(vt.set_value,10,run_time=10,rate_func=linear)

        vg = VGroup()
        # vg.add_updater(lambda m: self.play(Transform(line, line2), run_time=10))
        # vt.add_updater(lambda m: m.move_to(number3))

        # self.play(LaggedStart(*[self.play(vt.set_value, 10, run_time=10, rate_func=linear)],
        #                       [self.play(Transform(line, line2), run_time=10, rate_func=linear)]),
        #           )

        # self.play(AnimationGroup(vt.set_value, 10, run_time=10, rate_func=linear),
        #                         Transform(line, line2), run_time=10, rate_func=linear)
        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.play(Transform(line, line2),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )

        vg.clear_updaters()
        self.wait(3)
        # number.add_updater(self.play(number.set_value, 10))


class DecimalToGraphFinal(GraphScene, MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        axes = Axes(x_min=-3, x_max=13, color=BLUE)
        self.add(axes)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.add(number)
        line = Square()
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.add(number2)
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(Transform(line, line2),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(3)


# TODO I'm lazy to find it
class DecimalToGraphWithDashedLineExample(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)

    def construct(self):
        axes = Axes(x_min=-3, x_max=13, axes_color=BLUE)
        self.add(axes)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        dl1 = DashedLine()
        dl2 = DashedLine()

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.add(number)
        line = Square()
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.add(number2)
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))
        # dl1.add_updater(lambda m: m.set_length(number2.get_value()))
        # dl2.add_updater(lambda m: m.set_length(number.get_value()))
        # dl1 = DashedLine(start=dot_x, end=dot).set_length(number2.get_value())
        #
        # dl2 = DashedLine(start=dot_y, end=dot).set_length(number.get_value())
        dl1.add_updater(lambda m: m.move_to(DashedLine(start=dot_x, end=dot, rotate=90 * DEGREES)))
        dl2.add_updater(lambda m: m.move_to(DashedLine(start=dot_y, end=dot)))
        self.add(dl1, dl2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(Transform(line, line2),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(3)


class DecimalToGraphFinal2(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup_axes()
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        })
        self.add(numberplane)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.add(number)
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.add(number2)
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: z ** 2,
                  line.apply_complex_function,
                  lambda z: z ** 2,
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(3)


class DecimalToGraphFinal3(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=30,
            height=30,
            x_min=-30, x_max=30, y_min=-30, y_max=30)
        numberplane_fade = NumberPlane(background_line_style={
            'stroke_opacity': 0.3,
            'stroke_color': GREY
        }).apply_complex_function(lambda z: z ** 2)
        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=30, height=30,
            x_min=-30, x_max=30, y_min=-30, y_max=30)
        # self.add(numberplane)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        # self.add(number)
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        # self.add(number2)
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        # self.add(path, dot)
        self.play(Write(path), Write(dot), Write(numberplane), Write(line))
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: z ** 2,
                  line.apply_complex_function,
                  lambda z: z ** 2,
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # self.play(Transform(numberplane, numberplane_fade))
        # self.play(numberplane.set_color, GREY, numberplane.set_opacity, 0.5)
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)


class DecimalToGraphFinal4(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)
        # ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=80,
            height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=80, height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.play(Write(path), Write(dot), Write(numberplane), Write(line))
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: z ** 3,
                  line.apply_complex_function,
                  lambda z: z ** 3,
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # Optional, if the function graph is so incredible
        self.play(self.camera_frame.scale, 3.2)
        self.wait()
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)


class DecimalToGraphFinal5(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)
        # ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=80,
            height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=80, height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.play(Write(path), Write(dot), Write(numberplane), Write(line))
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: cmath.sin(z),
                  line.apply_complex_function,
                  lambda z: cmath.sin(z),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # Optional, if the function graph is so incredible
        self.play(self.camera_frame.scale, 3.2)
        self.wait()
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)


class DecimalToGraphFinal6(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)
        # ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=80,
            height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=80, height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        # If the code runs slow, use add()
        # self.play(Write(path), Write(dot), Write(numberplane), Write(line))
        self.add(path, dot, numberplane, line)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: cmath.cos(z),
                  line.apply_complex_function,
                  lambda z: cmath.cos(z),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # Optional, if the function graph is so incredible
        # self.play(self.camera_frame.scale, 3.2)
        self.wait()
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)


class DecimalToGraphFinal7(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)
        # ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=80,
            height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=80, height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        # If the code runs slow, use add()
        self.play(Write(path), Write(dot), Write(numberplane), Write(line))
        # self.add(path, dot, numberplane, line)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: cmath.tan(z),
                  line.apply_complex_function,
                  lambda z: cmath.tan(z),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # Optional, if the function graph is so incredible
        # self.play(self.camera_frame.scale, 3.2)
        self.wait()
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)


class DecimalToGraphFinal8(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)
        # ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=80,
            height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=80, height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        # If the code runs slow, use add()
        self.play(Write(path), Write(dot), Write(numberplane), Write(line))
        # self.add(path, dot, numberplane, line)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: cmath.sinh(z),
                  line.apply_complex_function,
                  lambda z: cmath.sinh(z),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # Optional, if the function graph is so incredible
        # self.play(self.camera_frame.scale, 3.2)
        self.wait()
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)

class DecimalToGraphFinal9(GraphScene, MovingCameraScene):
    CONFIG = {
        'axis_config': {
            'stroke_color': BLUE,
            'stroke_width': 0,
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
        MovingCameraScene.setup(self)
        # ZoomedScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)
        numberplane = NumberPlane(background_line_style={
            'stroke_opacity': 0.6
        }, x_line_frequency=1, y_line_frequency=1,
            width=80,
            height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        numberplane2 = NumberPlane(background_line_style={
            'stroke_opacity': 0.5,
            'stroke_color': YELLOW
        }, x_line_frequency=1, y_line_frequency=1, width=80, height=80,
            x_min=-30, x_max=30, y_min=-30, y_max=30)

        path = VMobject()

        t1 = TexMobject('x=').move_to(np.array([4, -1.6, 0]))
        t2 = TexMobject('y=').move_to(np.array([4, -2.6, 0]))

        vt = ValueTracker(0)

        self.add(t1, t2)

        number = DecimalNumber(0, num_decimal_places=5)
        number.add_updater(lambda m: m.set_value(vt.get_value()))
        number.add_updater(lambda m: m.next_to(t1, direction=RIGHT,
                                               aligned_edge=ORIGIN))
        self.play(Write(number))
        line = Square(color=YELLOW)
        line.set_color(YELLOW)
        line2 = Circle()
        number2 = DecimalNumber(0, num_decimal_places=5)
        number2.add_updater(lambda m: m.set_value(get_area(line)))
        number2.add_updater(lambda m: m.next_to(t2, direction=RIGHT,
                                                aligned_edge=ORIGIN))
        self.play(Write(number2))
        self.wait(2)

        dot_x = Dot(color=YELLOW)
        dot_x.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), 0, 0])))
        dot_y = Dot(color=YELLOW)
        dot_y.add_updater(lambda obj: obj.move_to(np.array([0, number2.get_value(), 0])))

        self.add(dot_x, dot_y)
        dot = Dot(color=BLUE)

        dot_copy = dot.copy().set_color(YELLOW)

        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        # If the code runs slow, use add()
        self.play(Write(path), Write(dot), Write(numberplane), Write(line2))
        # self.add(path, dot, numberplane, line)
        dot.add_updater(lambda obj: obj.move_to(np.array([number.get_value(), number2.get_value(), 0])))
        dot.add_updater(lambda obj: self.add(dot_copy))

        numberplane.prepare_for_nonlinear_transform()

        self.wait(2)

        self.play(self.camera_frame.move_to, np.array([5, 0, 0]))
        self.wait()
        self.play(numberplane.apply_complex_function,
                  lambda z: cmath.cosh(z),
                  line2.apply_complex_function,
                  lambda z: cmath.cosh(z),
                  vt.set_value, 10, run_time=10, rate_func=linear,
                  )
        self.wait(2)
        # Optional, if the function graph is so incredible
        # self.play(self.camera_frame.scale, 3.2)
        self.wait()
        self.play(numberplane.fade, 0.5)
        self.play(Write(numberplane2))
        self.wait(3)


class ZoomInTest(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        a = TexMobject('A')
        nbp = NumberPlane()
        self.play(Write(a), Write(nbp))
        self.wait(2)
        self.play(self.camera_frame.scale, 2.8)
        self.wait()


class PiSceneTest(TeacherStudentsScene):
    def construct(self):
        self.student_says(
            "Hooray!",
            target_mode="happy",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="hooray",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="thinking",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="speaking",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="confused",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="angry",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="sad",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="shruggie",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="surprised",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="well",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="pleading",
            student_index=1,
        )
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="plain",
            student_index=1,
        )
        self.student_says(
            "Hooray!",
            target_mode="plain",
            student_index=1,
        )
        self.wait(2)
        self.wait(2)
        self.student_says(
            "Hooray!",
            target_mode="hooray",
            student_index=1,
        )
        self.wait(2)


class PiSceneTest2(TeacherStudentsScene):
    def construct(self):
        # self.get_student_changes(
        #     'hooray', 'well', 'dance_kick'
        # )
        self.change_student_modes(
            'hooray', 'well', 'dance_kick'
        )
        self.play(self.teacher.change, 'hooray')
        # self.wait(2)
        # self.play(self.teacher.change, 'happy')
        # self.wait(2)
        # self.play(Write(self.screen))
        # self.wait(2)
        # self.play(Write(TexMobject('Hello').shift_onto_screen()))
        # self.wait(2)
        # self.screen.CONFIG(
        #     self.change_student_modes(
        #         'hooray', 'well', 'dance_kick'
        #     ),
        #     self.play(self.teacher.change, 'hooray')
        # )

        self.play(Write(self.screen))
        self.wait(2)


class AskAboutWhenProbabilityIsIntuitive(TeacherStudentsScene):
    def construct(self):
        words = TextMobject("What makes probability\\\\more intuitive?")
        words.move_to(self.hold_up_spot, DOWN)
        words.shift_onto_screen()

        self.play(
            self.teacher.change, "speaking",
            self.get_student_changes(
                "pondering", "sassy", "happy",
                look_at_arg=self.screen,
            )
        )
        self.wait(2)

        self.play(
            self.teacher.change, "raise_right_hand",
            FadeInFrom(words, DOWN),
            self.get_student_changes("erm", "pondering", "confused")
        )
        self.wait(2)
        self.play(
            words.scale, 2,
            words.center,
            words.to_edge, UP,
            self.teacher.change, "pondering", 3 * UP,
            self.get_student_changes(
                "pondering", "thinking", "thinking",
                look_at_arg=3 * UP,
            )
        )
        self.wait(6)


class PiSceneTest3(TeacherStudentsScene):
    def construct(self):
        self.play(Write(self.pi_creature, mode='hooray'))
        self.wait(2)
        self.play(Write(self.screen))
        self.screen.add(self.pi_creature)
        self.wait(2)


class PiSceneTest4(TeacherStudentsScene):
    def construct(self):
        self.play(Write(self.screen))
        text = TexMobject(r'\rm Hello').move_to(self.screen)
        text.shift_onto_screen()
        self.play(Write(text))
        self.wait(2)


class EmergencyOccured(Scene):
    def construct(self):
        t1 = TexMobject('AN EMERGENCY OCCURED').move_to(UP * 2.5).set_color(RED).scale(1.5)
        t2 = TexMobject('Please wait for emergency release').set_color(RED)
        self.add(t1, t2)
        self.wait(15)


class BlankScene3Seconds(Scene):
    def construct(self):
        self.wait(3)


class CountDown(Scene):
    def construct(self):
        vt1 = ValueTracker(5)
        vt2 = ValueTracker()
        zero = TexMobject('0').scale(2).set_color(RED).move_to(LEFT * 3)
        co = TexMobject(':').scale(2).set_color(RED)


class VeryLongBlankScene(Scene):
    def construct(self):
        t1 = TexMobject('FIND SHELTER BEFORE COUNTDOWN ENDS').set_color(BLACK).move_to(UP * 2.5).scale(0.8)
        self.wait(600)


# class FindShelterBeforeCountdown(Scene):
#     def construct(self):
#         t1 = TexMobject('FIND SHELTER BEFORE COUNTDOWN ENDS').set_color(BLACK).move_to(UP * 2.5).scale(0.8)
#         c001 = TexMobject('05:00').scale(2).set_color(RED)
#         c001 = TexMobject('04:59').scale(2).set_color(RED)
#         c001 = TexMobject('04:58').scale(2).set_color(RED)
#         c001 = TexMobject('04:57').scale(2).set_color(RED)
#         c001 = TexMobject('04:56').scale(2).set_color(RED)
#         c001 = TexMobject('04:55').scale(2).set_color(RED)
#         c001 = TexMobject('04:54').scale(2).set_color(RED)
#         c001 = TexMobject('04:53').scale(2).set_color(RED)
#         c001 = TexMobject('04:52').scale(2).set_color(RED)
#         c001 = TexMobject('04:51').scale(2).set_color(RED)
#         c001 = TexMobject('04:50').scale(2).set_color(RED)
#         c001 = TexMobject('04:49').scale(2).set_color(RED)
#         c001 = TexMobject('04:48').scale(2).set_color(RED)
#         c001 = TexMobject('04:47').scale(2).set_color(RED)
#         c001 = TexMobject('04:46').scale(2).set_color(RED)
#         c001 = TexMobject('04:45').scale(2).set_color(RED)
#         c001 = TexMobject('04:44').scale(2).set_color(RED)
#         c001 = TexMobject('04:43').scale(2).set_color(RED)
#         c001 = TexMobject('04:42').scale(2).set_color(RED)
#         c001 = TexMobject('04:41').scale(2).set_color(RED)
#         c001 = TexMobject('04:40').scale(2).set_color(RED)
#         c001 = TexMobject('04:39').scale(2).set_color(RED)
#         c001 = TexMobject('04:38').scale(2).set_color(RED)
#         c001 = TexMobject('04:37').scale(2).set_color(RED)
#         c001 = TexMobject('04:36').scale(2).set_color(RED)
#         c001 = TexMobject('04:35').scale(2).set_color(RED)
#         c001 = TexMobject('04:34').scale(2).set_color(RED)
#         c001 = TexMobject('04:33').scale(2).set_color(RED)
#         c001 = TexMobject('04:32').scale(2).set_color(RED)
#         c001 = TexMobject('04:31').scale(2).set_color(RED)
#         c001 = TexMobject('04:30').scale(2).set_color(RED)
#         c001 = TexMobject('04:29').scale(2).set_color(RED)
#         c001 = TexMobject('04:28').scale(2).set_color(RED)
#         c001 = TexMobject('04:27').scale(2).set_color(RED)
#         c001 = TexMobject('04:26').scale(2).set_color(RED)
#         c001 = TexMobject('04:25').scale(2).set_color(RED)
#         c001 = TexMobject('04:24').scale(2).set_color(RED)
#         c001 = TexMobject('04:23').scale(2).set_color(RED)
#         c001 = TexMobject('04:22').scale(2).set_color(RED)
#         c001 = TexMobject('04:21').scale(2).set_color(RED)
#         c001 = TexMobject('04:20').scale(2).set_color(RED)
#         c001 = TexMobject('04:19').scale(2).set_color(RED)
#         c001 = TexMobject('04:18').scale(2).set_color(RED)
#         c001 = TexMobject('04:17').scale(2).set_color(RED)
#         c001 = TexMobject('04:16').scale(2).set_color(RED)
#         c001 = TexMobject('04:15').scale(2).set_color(RED)
#         c001 = TexMobject('04:14').scale(2).set_color(RED)
#         c001 = TexMobject('04:13').scale(2).set_color(RED)
#         c001 = TexMobject('04:12').scale(2).set_color(RED)
#         c001 = TexMobject('04:11').scale(2).set_color(RED)
#         c001 = TexMobject('04:10').scale(2).set_color(RED)
#         c001 = TexMobject('04:09').scale(2).set_color(RED)
#         c001 = TexMobject('04:08').scale(2).set_color(RED)
#         c001 = TexMobject('04:07').scale(2).set_color(RED)
#         c001 = TexMobject('04:06').scale(2).set_color(RED)
#         c001 = TexMobject('04:05').scale(2).set_color(RED)
#         c001 = TexMobject('04:04').scale(2).set_color(RED)
#         c001 = TexMobject('04:03').scale(2).set_color(RED)
#         c001 = TexMobject('04:02').scale(2).set_color(RED)
#         c001 = TexMobject('04:01').scale(2).set_color(RED)
#         00c100 = TexMobject('04:00').scale(2).set_color(RED)
#
#         c001 = TexMobject('03:59').scale(2).set_color(RED)
#         c001 = TexMobject('03:58').scale(2).set_color(RED)
#         c001 = TexMobject('03:57').scale(2).set_color(RED)
#         c001 = TexMobject('03:56').scale(2).set_color(RED)
#         c001 = TexMobject('03:55').scale(2).set_color(RED)
#         c001 = TexMobject('03:54').scale(2).set_color(RED)
#         c001 = TexMobject('03:53').scale(2).set_color(RED)
#         c001 = TexMobject('03:52').scale(2).set_color(RED)
#         c001 = TexMobject('03:51').scale(2).set_color(RED)
#         c001 = TexMobject('03:50').scale(2).set_color(RED)
#         c001 = TexMobject('03:49').scale(2).set_color(RED)
#         c001 = TexMobject('03:48').scale(2).set_color(RED)
#         c001 = TexMobject('03:47').scale(2).set_color(RED)
#         c001 = TexMobject('03:46').scale(2).set_color(RED)
#         c001 = TexMobject('03:45').scale(2).set_color(RED)
#         c001 = TexMobject('03:44').scale(2).set_color(RED)
#         c001 = TexMobject('03:43').scale(2).set_color(RED)
#         c001 = TexMobject('03:42').scale(2).set_color(RED)
#         c001 = TexMobject('03:41').scale(2).set_color(RED)
#         c001 = TexMobject('03:40').scale(2).set_color(RED)
#         c001 = TexMobject('03:39').scale(2).set_color(RED)
#         c001 = TexMobject('03:38').scale(2).set_color(RED)
#         c001 = TexMobject('03:37').scale(2).set_color(RED)
#         c001 = TexMobject('03:36').scale(2).set_color(RED)
#         c001 = TexMobject('03:35').scale(2).set_color(RED)
#         c001 = TexMobject('03:34').scale(2).set_color(RED)
#         c001 = TexMobject('03:33').scale(2).set_color(RED)
#         c001 = TexMobject('03:32').scale(2).set_color(RED)
#         c001 = TexMobject('03:31').scale(2).set_color(RED)
#         c001 = TexMobject('03:30').scale(2).set_color(RED)
#         c001 = TexMobject('03:29').scale(2).set_color(RED)
#         c001 = TexMobject('03:28').scale(2).set_color(RED)
#         c001 = TexMobject('03:27').scale(2).set_color(RED)
#         c001 = TexMobject('03:26').scale(2).set_color(RED)
#         c001 = TexMobject('03:25').scale(2).set_color(RED)
#         c001 = TexMobject('03:24').scale(2).set_color(RED)
#         c001 = TexMobject('03:23').scale(2).set_color(RED)
#         c001 = TexMobject('03:22').scale(2).set_color(RED)
#         c001 = TexMobject('03:21').scale(2).set_color(RED)
#         c001 = TexMobject('03:20').scale(2).set_color(RED)
#         c001 = TexMobject('03:19').scale(2).set_color(RED)
#         c001 = TexMobject('03:18').scale(2).set_color(RED)
#         c001 = TexMobject('03:17').scale(2).set_color(RED)
#         c001 = TexMobject('03:16').scale(2).set_color(RED)
#         c001 = TexMobject('03:15').scale(2).set_color(RED)
#         c001 = TexMobject('03:14').scale(2).set_color(RED)
#         c001 = TexMobject('03:13').scale(2).set_color(RED)
#         c001 = TexMobject('03:12').scale(2).set_color(RED)
#         c001 = TexMobject('03:11').scale(2).set_color(RED)
#         c001 = TexMobject('03:10').scale(2).set_color(RED)
#         c001 = TexMobject('03:09').scale(2).set_color(RED)
#         c001 = TexMobject('03:08').scale(2).set_color(RED)
#         c001 = TexMobject('03:07').scale(2).set_color(RED)
#         c001 = TexMobject('03:06').scale(2).set_color(RED)
#         c001 = TexMobject('03:05').scale(2).set_color(RED)
#         c001 = TexMobject('03:04').scale(2).set_color(RED)
#         c001 = TexMobject('03:03').scale(2).set_color(RED)
#         c001 = TexMobject('03:02').scale(2).set_color(RED)
#         c001 = TexMobject('03:01').scale(2).set_color(RED)
#         00c100 = TexMobject('03:00').scale(2).set_color(RED)
#
#         c001 = TexMobject('02:59').scale(2).set_color(RED)
#         c001 = TexMobject('02:58').scale(2).set_color(RED)
#         c001 = TexMobject('02:57').scale(2).set_color(RED)
#         c001 = TexMobject('02:56').scale(2).set_color(RED)
#         c001 = TexMobject('02:55').scale(2).set_color(RED)
#         c001 = TexMobject('02:54').scale(2).set_color(RED)
#         c001 = TexMobject('02:53').scale(2).set_color(RED)
#         c001 = TexMobject('02:52').scale(2).set_color(RED)
#         c001 = TexMobject('02:51').scale(2).set_color(RED)
#         c001 = TexMobject('02:50').scale(2).set_color(RED)
#         c001 = TexMobject('02:49').scale(2).set_color(RED)
#         c001 = TexMobject('02:48').scale(2).set_color(RED)
#         c001 = TexMobject('02:47').scale(2).set_color(RED)
#         c001 = TexMobject('02:46').scale(2).set_color(RED)
#         c001 = TexMobject('02:45').scale(2).set_color(RED)
#         c001 = TexMobject('02:44').scale(2).set_color(RED)
#         c001 = TexMobject('02:43').scale(2).set_color(RED)
#         c001 = TexMobject('02:42').scale(2).set_color(RED)
#         c001 = TexMobject('02:41').scale(2).set_color(RED)
#         c001 = TexMobject('02:40').scale(2).set_color(RED)
#         c001 = TexMobject('02:39').scale(2).set_color(RED)
#         c001 = TexMobject('02:38').scale(2).set_color(RED)
#         c001 = TexMobject('02:37').scale(2).set_color(RED)
#         c001 = TexMobject('02:36').scale(2).set_color(RED)
#         c001 = TexMobject('02:35').scale(2).set_color(RED)
#         c001 = TexMobject('02:34').scale(2).set_color(RED)
#         c001 = TexMobject('02:33').scale(2).set_color(RED)
#         c001 = TexMobject('02:32').scale(2).set_color(RED)
#         c001 = TexMobject('02:31').scale(2).set_color(RED)
#         c001 = TexMobject('02:30').scale(2).set_color(RED)
#         c001 = TexMobject('02:29').scale(2).set_color(RED)
#         c001 = TexMobject('02:28').scale(2).set_color(RED)
#         c001 = TexMobject('02:27').scale(2).set_color(RED)
#         c001 = TexMobject('02:26').scale(2).set_color(RED)
#         c001 = TexMobject('02:25').scale(2).set_color(RED)
#         c001 = TexMobject('02:24').scale(2).set_color(RED)
#         c001 = TexMobject('02:23').scale(2).set_color(RED)
#         c001 = TexMobject('02:22').scale(2).set_color(RED)
#         c001 = TexMobject('02:21').scale(2).set_color(RED)
#         c001 = TexMobject('02:20').scale(2).set_color(RED)
#         c001 = TexMobject('02:19').scale(2).set_color(RED)
#         c001 = TexMobject('02:18').scale(2).set_color(RED)
#         c001 = TexMobject('02:17').scale(2).set_color(RED)
#         c001 = TexMobject('02:16').scale(2).set_color(RED)
#         c001 = TexMobject('02:15').scale(2).set_color(RED)
#         c001 = TexMobject('02:14').scale(2).set_color(RED)
#         c001 = TexMobject('02:13').scale(2).set_color(RED)
#         c001 = TexMobject('02:12').scale(2).set_color(RED)
#         c001 = TexMobject('02:11').scale(2).set_color(RED)
#         c001 = TexMobject('02:10').scale(2).set_color(RED)
#         c001 = TexMobject('02:09').scale(2).set_color(RED)
#         c001 = TexMobject('02:08').scale(2).set_color(RED)
#         c001 = TexMobject('02:07').scale(2).set_color(RED)
#         c001 = TexMobject('02:06').scale(2).set_color(RED)
#         c001 = TexMobject('02:05').scale(2).set_color(RED)
#         c001 = TexMobject('02:04').scale(2).set_color(RED)
#         c001 = TexMobject('02:03').scale(2).set_color(RED)
#         c001 = TexMobject('02:02').scale(2).set_color(RED)
#         c001 = TexMobject('02:01').scale(2).set_color(RED)
#         00c100 = TexMobject('02:00').scale(2).set_color(RED)
#
#         c001 = TexMobject('01:59').scale(2).set_color(RED)
#         c001 = TexMobject('01:58').scale(2).set_color(RED)
#         c001 = TexMobject('01:57').scale(2).set_color(RED)
#         c001 = TexMobject('01:56').scale(2).set_color(RED)
#         c001 = TexMobject('01:55').scale(2).set_color(RED)
#         c001 = TexMobject('01:54').scale(2).set_color(RED)
#         c001 = TexMobject('01:53').scale(2).set_color(RED)
#         c001 = TexMobject('01:52').scale(2).set_color(RED)
#         c001 = TexMobject('01:51').scale(2).set_color(RED)
#         c001 = TexMobject('01:50').scale(2).set_color(RED)
#         c001 = TexMobject('01:49').scale(2).set_color(RED)
#         c001 = TexMobject('01:48').scale(2).set_color(RED)
#         c001 = TexMobject('01:47').scale(2).set_color(RED)
#         c001 = TexMobject('01:46').scale(2).set_color(RED)
#         c001 = TexMobject('01:45').scale(2).set_color(RED)
#         c001 = TexMobject('01:44').scale(2).set_color(RED)
#         c001 = TexMobject('01:43').scale(2).set_color(RED)
#         c001 = TexMobject('01:42').scale(2).set_color(RED)
#         c001 = TexMobject('01:41').scale(2).set_color(RED)
#         c001 = TexMobject('01:40').scale(2).set_color(RED)
#         c001 = TexMobject('01:39').scale(2).set_color(RED)
#         c001 = TexMobject('01:38').scale(2).set_color(RED)
#         c001 = TexMobject('01:37').scale(2).set_color(RED)
#         c001 = TexMobject('01:36').scale(2).set_color(RED)
#         c001 = TexMobject('01:35').scale(2).set_color(RED)
#         c001 = TexMobject('01:34').scale(2).set_color(RED)
#         c001 = TexMobject('01:33').scale(2).set_color(RED)
#         c001 = TexMobject('01:32').scale(2).set_color(RED)
#         c001 = TexMobject('01:31').scale(2).set_color(RED)
#         c001 = TexMobject('01:30').scale(2).set_color(RED)
#         c001 = TexMobject('01:29').scale(2).set_color(RED)
#         c001 = TexMobject('01:28').scale(2).set_color(RED)
#         c001 = TexMobject('01:27').scale(2).set_color(RED)
#         c001 = TexMobject('01:26').scale(2).set_color(RED)
#         c001 = TexMobject('01:25').scale(2).set_color(RED)
#         c001 = TexMobject('01:24').scale(2).set_color(RED)
#         c001 = TexMobject('01:23').scale(2).set_color(RED)
#         c001 = TexMobject('01:22').scale(2).set_color(RED)
#         c001 = TexMobject('01:21').scale(2).set_color(RED)
#         c001 = TexMobject('01:20').scale(2).set_color(RED)
#         c001 = TexMobject('01:19').scale(2).set_color(RED)
#         c001 = TexMobject('01:18').scale(2).set_color(RED)
#         c001 = TexMobject('01:17').scale(2).set_color(RED)
#         c001 = TexMobject('01:16').scale(2).set_color(RED)
#         c001 = TexMobject('01:15').scale(2).set_color(RED)
#         c001 = TexMobject('01:14').scale(2).set_color(RED)
#         c001 = TexMobject('01:13').scale(2).set_color(RED)
#         c001 = TexMobject('01:12').scale(2).set_color(RED)
#         c001 = TexMobject('01:11').scale(2).set_color(RED)
#         c001 = TexMobject('01:10').scale(2).set_color(RED)
#         c001 = TexMobject('01:09').scale(2).set_color(RED)
#         c001 = TexMobject('01:08').scale(2).set_color(RED)
#         c001 = TexMobject('01:07').scale(2).set_color(RED)
#         c001 = TexMobject('01:06').scale(2).set_color(RED)
#         c001 = TexMobject('01:05').scale(2).set_color(RED)
#         c001 = TexMobject('01:04').scale(2).set_color(RED)
#         c001 = TexMobject('01:03').scale(2).set_color(RED)
#         c001 = TexMobject('01:02').scale(2).set_color(RED)
#         c001 = TexMobject('01:01').scale(2).set_color(RED)
#         00c100 = TexMobject('01:00').scale(2).set_color(RED)
#
#         c001 = TexMobject('00:59').scale(2).set_color(RED)
#         c001 = TexMobject('00:58').scale(2).set_color(RED)
#         c001 = TexMobject('00:57').scale(2).set_color(RED)
#         c001 = TexMobject('00:56').scale(2).set_color(RED)
#         c001 = TexMobject('00:55').scale(2).set_color(RED)
#         c001 = TexMobject('00:54').scale(2).set_color(RED)
#         c001 = TexMobject('00:53').scale(2).set_color(RED)
#         c001 = TexMobject('00:52').scale(2).set_color(RED)
#         c001 = TexMobject('00:51').scale(2).set_color(RED)
#         c001 = TexMobject('00:50').scale(2).set_color(RED)
#         c001 = TexMobject('00:49').scale(2).set_color(RED)
#         c001 = TexMobject('00:48').scale(2).set_color(RED)
#         c001 = TexMobject('00:47').scale(2).set_color(RED)
#         c001 = TexMobject('00:46').scale(2).set_color(RED)
#         c001 = TexMobject('00:45').scale(2).set_color(RED)
#         c001 = TexMobject('00:44').scale(2).set_color(RED)
#         c001 = TexMobject('00:43').scale(2).set_color(RED)
#         c001 = TexMobject('00:42').scale(2).set_color(RED)
#         c001 = TexMobject('00:41').scale(2).set_color(RED)
#         c001 = TexMobject('00:40').scale(2).set_color(RED)
#         c001 = TexMobject('00:39').scale(2).set_color(RED)
#         c001 = TexMobject('00:38').scale(2).set_color(RED)
#         c001 = TexMobject('00:37').scale(2).set_color(RED)
#         c001 = TexMobject('00:36').scale(2).set_color(RED)
#         c001 = TexMobject('00:35').scale(2).set_color(RED)
#         c001 = TexMobject('00:34').scale(2).set_color(RED)
#         c001 = TexMobject('00:33').scale(2).set_color(RED)
#         c001 = TexMobject('00:32').scale(2).set_color(RED)
#         c001 = TexMobject('00:31').scale(2).set_color(RED)
#         c001 = TexMobject('00:30').scale(2).set_color(RED)
#         c001 = TexMobject('00:29').scale(2).set_color(RED)
#         c001 = TexMobject('00:28').scale(2).set_color(RED)
#         c001 = TexMobject('00:27').scale(2).set_color(RED)
#         c001 = TexMobject('00:26').scale(2).set_color(RED)
#         c001 = TexMobject('00:25').scale(2).set_color(RED)
#         c001 = TexMobject('00:24').scale(2).set_color(RED)
#         c001 = TexMobject('00:23').scale(2).set_color(RED)
#         c001 = TexMobject('00:22').scale(2).set_color(RED)
#         c001 = TexMobject('00:21').scale(2).set_color(RED)
#         c001 = TexMobject('00:20').scale(2).set_color(RED)
#         c001 = TexMobject('00:19').scale(2).set_color(RED)
#         c001 = TexMobject('00:18').scale(2).set_color(RED)
#         c001 = TexMobject('00:17').scale(2).set_color(RED)
#         c001 = TexMobject('00:16').scale(2).set_color(RED)
#         c001 = TexMobject('00:15').scale(2).set_color(RED)
#         c001 = TexMobject('00:14').scale(2).set_color(RED)
#         c001 = TexMobject('00:13').scale(2).set_color(RED)
#         c001 = TexMobject('00:12').scale(2).set_color(RED)
#         c001 = TexMobject('00:11').scale(2).set_color(RED)
#         c001 = TexMobject('00:10').scale(2).set_color(RED)
#         c001 = TexMobject('00:09').scale(2).set_color(RED)
#         c001 = TexMobject('00:08').scale(2).set_color(RED)
#         c001 = TexMobject('00:07').scale(2).set_color(RED)
#         c001 = TexMobject('00:06').scale(2).set_color(RED)
#         c001 = TexMobject('00:05').scale(2).set_color(RED)
#         c001 = TexMobject('00:04').scale(2).set_color(RED)
#         c001 = TexMobject('00:03').scale(2).set_color(RED)
#         c001 = TexMobject('00:02').scale(2).set_color(RED)
#         c001 = TexMobject('00:01').scale(2).set_color(RED)
#         c1 = TexMobject('00:00').scale(2).set_color(RED)


class TexFalling(SpaceScene):
    def construct(self):
        ground = Line(LEFT * 5, RIGHT * 5, color=ORANGE).shift(DOWN)
        self.add(ground)
        self.make_static_body(ground)
        forms = [
            r"e^{i\pi}+1=0",
            r"\cos(x+y)=\cos x \cos y - \sin x \sin y",
            r"\displaystyle \int_{-\infty }^{\infty }e^{-x^{2}}\,dx={\sqrt {\pi }}",
            r"\rm{This is a text. Made by Caft Botti.}"
        ]
        cols = [RED, BLUE, YELLOW, WHITE]
        for f, col in zip(forms, cols):
            text = TexMobject(f, color=col).move_to(UP * 3.5)
            self.add(text)
            self.make_rigid_body(text[0])
            self.wait(5)
            cir = Circle().scale(3).move_to(UP * 3.8)
            self.make_rigid_body(cir)
            self.add(cir)
            self.wait(5)


class ElectricFieldExampleScene(Scene):
    def construct(self):
        charge1 = Charge(-1, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN)
        charge3 = Charge(-1, UP)
        field = ElectricField(charge1, charge2, charge3)
        self.add(charge1, charge2, charge3)
        self.add(field)
        self.wait(3)


class RayExampleScene(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        a = Lens(-5, 1, **lens_style).shift(LEFT)
        a2 = Lens(5, 1, **lens_style).shift(RIGHT)
        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [a, a2], color=RED)
            for i in np.linspace(-2, 2, 10)
        ]
        self.add(a, a2, *b)
        self.wait(3)


class MultiPendulumExample(SpaceScene):
    def construct(self):
        p = MultiPendulum(RIGHT, LEFT)
        self.add(p)
        self.make_rigid_body(p.bobs)
        p.start_swinging()
        self.add(TracedPath(p.bobs[-1].get_center, stroke_color=BLUE))
        self.wait(10)


class PendulumExample(SpaceScene):
    def construct(self):
        pends = VGroup(*[Pendulum(i) for i in np.linspace(1, 5, 7)])
        self.add(pends)
        for p in pends:
            self.make_rigid_body(p.bobs)
            p.start_swinging()
        self.wait(10)


class PhysicTest(SpaceScene):
    def construct(self):
        t1 = TextMobject(r'''
        有利于作战的天气、时令，比不上有利于作战的地理形势，\\
        比不上作战中的人心所向、内部团结。\\
        （比如一座）方圆三里的小城，只有方圆七里的外城，\\
        采用四面包围的方式攻城却不能取胜。采用四面包围的方式攻城，\\
        一定是得到有利于作战的天气、时令了，不能取胜，\\
        这是因为有利于作战的时令比不上有利于作战的地理形势啊。\\
        城墙并不是不高，护城河并不是不深，武器装备也并不是不精良，\\
        粮食供给也并不是不充足，（但是守城一方）还是弃城而逃，\\
        这是因为作战的地理形势（再好），也比不上人心所向、内部团结啊。\\
        所以说：使百姓定居下来（而不迁到其它的地方去），\\
        不能依靠划定疆域的界限，巩固国防不能靠山河的险要，\\
        震慑天下不能靠武力的强大。能施行“仁政”的君王，帮助支持他的人就多；\\
        不能施行“仁政”的君主，支持帮助他的人就少。支持帮助他的人少到了极点，\\
        连内外亲属也会背叛他；支持帮助他的人多到了极点，天下所有人都会归顺他。\\
        凭着天下人都归顺他的条件，去攻打那连亲属都反对背叛的君主，\\
        所以能行“仁政”的君主不战则已，（如果）战斗就一定会取得胜利。\\
        ''').move_to(UP * 4)
        l = Line(LEFT * 5, RIGHT * 5, color=ORANGE).shift(DOWN)
        self.add(t1, l)
        self.make_rigid_body(t1)
        self.make_static_body(l)
        self.wait(20)


class PhysicTest2(SpaceScene):
    def construct(self):
        t1 = TextMobject(r'''
        有利于作战的天气、时令，比不上有利于作战的地理形势，\\
        比不上作战中的人心所向、内部团结。\\
        （比如一座）方圆三里的小城，只有方圆七里的外城，\\
        采用四面包围的方式攻城却不能取胜。采用四面包围的方式攻城，\\
        一定是得到有利于作战的天气、时令了，不能取胜，\\
        这是因为有利于作战的时令比不上有利于作战的地理形势啊。\\
        城墙并不是不高，护城河并不是不深，武器装备也并不是不精良，\\
        粮食供给也并不是不充足，（但是守城一方）还是弃城而逃，\\
        这是因为作战的地理形势（再好），也比不上人心所向、内部团结啊。\\
        所以说：使百姓定居下来（而不迁到其它的地方去），\\
        不能依靠划定疆域的界限，巩固国防不能靠山河的险要，\\
        震慑天下不能靠武力的强大。能施行“仁政”的君王，帮助支持他的人就多；\\
        不能施行“仁政”的君主，支持帮助他的人就少。支持帮助他的人少到了极点，\\
        连内外亲属也会背叛他；支持帮助他的人多到了极点，天下所有人都会归顺他。\\
        凭着天下人都归顺他的条件，去攻打那连亲属都反对背叛的君主，\\
        所以能行“仁政”的君主不战则已，（如果）战斗就一定会取得胜利。\\
        ''').move_to(UP * 4)
        l = Line(LEFT * 5, RIGHT * 5, color=ORANGE).shift(DOWN)
        l2 = l
        l3 = Line(LEFT * 5, UP * 2.5, color=BLUE).shift(DOWN)
        l4 = Line(LEFT * 5, UP * 2.5, color=BLUE).shift(DOWN)
        self.add(t1, l, l2, l3, l4)
        self.make_rigid_body(t1)
        self.make_static_body(l, l2, l3, l4)
        # l2.add_updater(lambda obj: obj.rotate(20))
        self.play(l2.rotate, 20, run_time=35)
        # self.wait(20)


class PhysicTest3(SpaceScene):
    def construct(self):
        l1 = Line(np.array([-2, -2, 0]), np.array([2, -2, 0]))
        l2 = Line(np.array([-2, -2, 0]), np.array([2, -2, 0])).set_color(BLUE)
        l3 = Line(np.array([-2, -2, 0]), np.array([-2, 2, 0]))
        l4 = Line(np.array([2, -2, 0]), np.array([2, 2, 0]))
        l5 = Line(np.array([0, -2, 0]), np.array([2, 2, 0]))
        t1 = TextMobject('ABC')
        self.add(l1, l2, l3, l4)
        self.make_static_body(l1)
        # self.make_static_body(Transform(l2, l5))# , l3, l4)
        self.make_rigid_body(t1, l2, l5)
        self.play(Transform(l2, l5), run_time=10)
        self.wait(3)

        formula = TexMobject(
            r'''
            \begin{array}{l}
x_{1,2}=\frac{-b+\sqrt[5]{5 a\left(16 H \pm \sqrt{256 H^{2}-5 a N}\right)}}{10 a}\\
\mathrm{X}_{3,4}=\frac{-4 \mathrm{~b}-(1+\sqrt{5}) \sqrt[5]{5 a\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a}+\frac{\sqrt{10-2 \sqrt{5}} \sqrt[5]{5 a\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a} i\\
\mathrm{X}_{5,6}=\frac{-4 \mathrm{~b}-(1+\sqrt{5}) \sqrt[5]{5 a\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right)}}{40 a}+\frac{\sqrt{10-2 \sqrt{5}} \sqrt[5]{5 a\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a} i\\
\mathrm{X}_{7,8}=\frac{-4 \mathrm{~b}-(1-\sqrt{5}) \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right)}}{40 \mathrm{a}}+\frac{\sqrt{10+2 \sqrt{5}} \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}+\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right.}}{40 \mathrm{a}} i\\
\mathrm{X}_{9,10}=\frac{-4 \mathrm{~b}-(1-\sqrt{5}) \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 \mathrm{aN}}\right.}}{40 \mathrm{a}} \pm \frac{\sqrt{10+2 \sqrt{5}} \sqrt[5]{5 \mathrm{a}\left(16 \mathrm{H}-\sqrt{256 \mathrm{H}^{2}-5 a \mathrm{~N}}\right)}}{40 a} i
\end{array}
            '''
        )
        self.make_rigid_body(formula)
        self.play(Write(formula))
        self.wait(30)


class PhysicTest4(SpaceScene, PiCreatureScene):
    def construct(self):
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        p1 = self.pi_creature()
        l = Line(LEFT * 5, RIGHT * 5, color=ORANGE).shift(DOWN)
        self.add(p1, l)
        self.make_rigid_body(p1)
        self.make_static_body(l)
        self.wait(20)


class RandomTest(Scene):
    def construct(self):
        while True:
            #t = TexMobject(random.random())
            v = hashlib.sha256()
            v.update(random.random())
            g = v.hexdigest()
            print(g)


class ThisISjustaTEST(InteractiveScene):
    def construct(self):
        self.enable_selection()
        self.enable_interaction()
        self.play(Write(Square()), run_time=10)
        self.wait(3)

# from manimlib.code import *
# from manimlib.mobject.vector_field_editted import *
# from vector_field import *
# from manimlib.coordinate_systems2 import *
# from manimlib.coordinate_systems3 import *
# from manimlib.mobject.vector_filed_editted import *
