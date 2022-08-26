# Manim
# NEWS: Fourier graphs package is available!
Some manim projects Made by CaftBotti

These files are about shapes, arithmetics and function changes, and so on.

All the resources are PUBLIC. Everyone can use them.

Now I have more than 82,186 bytes of code. 2843 lines.

I don't want to tell you more.:)


class HelloMyFriend(Scene):

    def construct(self):
    
        # Define variables
        
        text1 = TexMobject('Welcome to visit CaftBotti and Manim's world!')
        
        text2 = TexMobject('Have a good time! :)')
        
        # Animations
        
        self.play(Write(text1))
        
        self.wait(3)
        
        self.remove(text1)
        
        self.play(Transform(text1, text2)
        
        self.wait(3)
        
        self.play(FadeOut(text1)  # When t1 trans to t2, it's t1 in fact
        
        self.wait()
