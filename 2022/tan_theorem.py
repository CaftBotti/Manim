from manimlib.imports import *


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
