from manim import *
from colour import Color


class Intro(Scene):

	def construct(self):
		title_string = "Edit Distance"
		self.camera.background_color = "#FFFFFF"
		title = Text(title_string, font="Noto Sans", color=BLACK).move_to(UP)
		for letter in title:
			self.play(FadeIn(letter), run_time = 1 / len(title_string))

		logo = ImageMobject("../img/logo.png")
		logo.scale(0.5)
		logo.next_to(title, DOWN)
		self.play(FadeIn(logo), run_time = 1)
		self.wait(1)
		self.play(FadeOut(logo, title), run_time = 1)



class Sequence(Text):
	def __init__(self, text, font_size=60, **kwargs):
		Text.__init__(self, text,  weight=BOLD, font='Latin Modern Mono Caps',
				font_size=font_size,
				t2c={'a': GREEN_E, 'c':BLUE_E, 'g':GOLD_E, 't':RED_E, 'n':PURPLE_E, 
					'A': GREEN_E, 'C':BLUE_E, 'G':GOLD_E, 'T':RED_E, 'N':PURPLE_E},
				**kwargs)

class Txt(Text):
	def __init__(self, text, color=BLACK, **kwargs):
		Text.__init__(self, text, font="Noto Sans", color=color, **kwargs)





class Problem(Scene):

	def construct(self):

		self.camera.background_color = "#FFFFFF"

        # create title
		title = Txt("Edit Distance").to_edge(UP)
		for letter in title:
			self.play(FadeIn(letter), run_time = 0.05)
		title_line = Line(LEFT*6, RIGHT*6, color=BLACK)
		title_line.next_to(title, DOWN)
		self.play(Create(title_line))

        # definition
		problem_text = [
				"Minimum number of edits required to", 
				"transform one string to another" 
		]
		problem = VGroup( *[Txt(line, font_size=30) for line in problem_text]) \
				.arrange(direction=DOWN).next_to(title_line, DOWN)
		self.add(problem)
		self.wait(2)

		# reference/query example
		ref = VGroup(Txt("R", weight=BOLD), Txt("eference"), Txt(":   "),
				Sequence("GATTACA ")) \
				.arrange(direction=RIGHT).next_to(problem, DOWN*2)
		ref.shift(LEFT*1.55)
		self.add(ref)
		self.wait(1)
		self.remove(ref[1])
		self.play(ApplyMethod(ref[0].next_to, ref[2], LEFT))

		query = VGroup(Txt("Q", weight=BOLD), Txt("uery"), Txt(":   "),
				Sequence("GTTTAAC ")) \
				.arrange(direction=RIGHT).next_to(ref, DOWN)
		query.align_to(ref, RIGHT)
		self.add(query)
		self.wait(1)
		self.remove(query[1])
		self.play(ApplyMethod(query[0].next_to, query[2], LEFT))
		self.wait(2)

		# types of edits
		# sub
		substitution = BackgroundRectangle(VGroup(ref[3][1], query[3][1]), 
				fill_color=BLUE_A, fill_opacity=1)
		substitution.set_z_index(ref.z_index-1)
		self.add(substitution)
		edits = VGroup(
					Txt("Substitution", color=BLUE_E), 
					Txt("Insertion", color=GREEN_E), 
					Txt("Deletion", color=RED_E)
				).arrange(direction=DOWN, center=True).next_to(problem, DOWN*9)
		self.add(edits[0])
		self.wait(1)

        # ins
		self.play(ApplyMethod(ref[3][5:].shift, RIGHT*0.5))
		insertion = BackgroundRectangle(query[3][5],
				fill_color=GREEN_A, fill_opacity=1)
		insertion.stretch_about_point(2.5, 1, insertion.get_bottom())
		insertion.set_z_index(ref.z_index-1)
		self.add(insertion)
		self.add(edits[1])
		self.wait(1)

        # del
		deletion = BackgroundRectangle(ref[3][6], 
				fill_color=RED_A, fill_opacity=1)
		deletion.stretch_about_point(2.5, 1, insertion.get_top())
		deletion.set_z_index(ref.z_index-1)
		self.add(deletion)
		self.add(edits[2])
		self.wait(2)
