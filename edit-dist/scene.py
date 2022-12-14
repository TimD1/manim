from manim import *
from colour import Color

HORIZONTAL = 0
VERTICAL = 1

MATCH = 0
DELETE = 1
INSERT = 2
W = 0.45 # letter width

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
		Text.__init__(self, str(text), font="Noto Sans", color=color, **kwargs)





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
		query[1].shift(DOWN*0.12)
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
		self.play(ApplyMethod(ref[3][5:].shift, RIGHT*0.45))
		insertion = BackgroundRectangle(query[3][5],
				fill_color=GREEN_A, fill_opacity=1)
		insertion.stretch_about_point(2.5, VERTICAL, insertion.get_bottom())
		insertion.set_z_index(ref.z_index-1)
		self.add(insertion)
		self.add(edits[1])
		self.wait(1)

		# del
		deletion = BackgroundRectangle(ref[3][6], 
				fill_color=RED_A, fill_opacity=1)
		deletion.stretch_about_point(2.5, VERTICAL, insertion.get_top())
		deletion.set_z_index(ref.z_index-1)
		self.add(deletion)
		self.add(edits[2])
		self.wait(2)
		self.remove(edits)

		# slide over insertion
		self.play(ApplyMethod(ref[3][4].shift, RIGHT*0.45),
				  ApplyMethod(insertion.shift, LEFT*0.45)
		)
		self.wait()

		# show all inserted, all deleted
		self.remove(substitution)
		self.play(ApplyMethod(ref[3][4:].align_to, ref[3][3].get_right(), LEFT), 
				  ApplyMethod(deletion.align_to, ref[3].get_left(), LEFT),
				  ApplyMethod(insertion.align_to, deletion.get_left(), LEFT),
				  ApplyMethod(query[3].align_to, deletion.get_left(), LEFT),
		)
		self.play(deletion.animate.stretch_about_point(7.38, HORIZONTAL, deletion.get_left()),
					insertion.animate.stretch_about_point(7.38, HORIZONTAL, insertion.get_left()),
					)

		# show terrible edit distance 14
		dists = []
		for i in range(len(ref[3]) + len(query[3])):
			if i < len(ref[3]):
				dists.append(Txt(i+1, font_size=20).next_to(ref[3][i], UP*0.5))
			else:
				dists.append(Txt(i+1, font_size=20)
						.next_to(query[3][i-len(ref[3])], UP)
						.align_to(dists[0].get_top(), UP))
		for i in range(len(dists)):
			self.add(dists[i])
			self.wait(0.1)
		self.wait()
		for i in range(len(dists)):
			self.remove(dists[i])

		# revert to earlier alignment
		self.add(substitution)
		self.play(
				deletion.animate.stretch_about_point(1/7.38, HORIZONTAL, deletion.get_right()).align_to(query[3].get_left(), LEFT),
				insertion.animate.stretch_about_point(1/7.38, HORIZONTAL, insertion.get_left()).align_to(ref[3][5].get_left(), LEFT),
				query[3].animate.align_to(ref[3].get_left(), LEFT),
				ref[3][5:].animate.align_to(ref[3][6].get_left(), LEFT),
		)
		self.wait()
		dists = [ Txt(1, font_size=20).next_to(ref[3][1], UP*0.5) ]
		dists.append(Txt(2, font_size=20)
				.next_to(query[3][5], UP)
				.align_to(dists[0].get_top(), UP))
		dists.append(Txt(3, font_size=20).next_to(ref[3][6], UP*0.5))
		for i in range(3):
			self.add(dists[i])
			self.wait(0.1)

		# add time at end
		self.wait(3)



class TextAlignment():

	def __init__(self, scene, title):
		ref = VGroup(Txt("R: ", weight=BOLD), Sequence("GATTACA")) \
				.arrange(direction=RIGHT).next_to(title, DOWN*3).shift(LEFT)
		ref[1].align_to(ref[0].get_right()+RIGHT*W/2, LEFT)
		scene.add(ref)

		query = VGroup(Txt("Q: ", weight=BOLD), Sequence("GTTTAAC")) \
				.arrange(direction=RIGHT).next_to(ref, DOWN)
		query[1].align_to(ref[0].get_right()+RIGHT*W/2, LEFT)
		query.align_to(ref, RIGHT)
		scene.add(query)
		scene.wait(1)

		rseq = ref[1]
		qseq = query[1]
		rlen = len(rseq)
		qlen = len(qseq)
		maxlen = len(rseq) + len(qseq)
		count = 0
		runtime = 1
		for x in range(40):
			shift_list = []
			ridx = 0
			qidx = 0
			power = 0
			while power < maxlen:
				rem = x % 3
				if rem == 0: # ref and idx align
					if ridx < rlen:
						shift_list.append( rseq[ridx].animate.align_to(
								ref[0].get_right()+RIGHT*W/2, LEFT).shift(power*RIGHT*W),
						)
					ridx += 1
					if qidx < qlen:
						shift_list.append( qseq[qidx].animate.align_to(
								ref[0].get_right()+RIGHT*W/2, LEFT).shift(power*RIGHT*W),
						)
					qidx += 1
				elif rem == 1:
					if ridx < rlen:
						shift_list.append( rseq[ridx].animate.align_to(
								ref[0].get_right()+RIGHT*W/2, LEFT).shift(power*RIGHT*W),
						)
					ridx += 1
				else:
					if qidx < qlen:
						shift_list.append( qseq[qidx].animate.align_to(
								ref[0].get_right()+RIGHT*W/2, LEFT).shift(power*RIGHT*W),
						)
					qidx += 1

				power += 1
				x //= 3

			scene.play(*shift_list, run_time = max(runtime, 0.1))
			runtime *= 0.9



class Intuition(Scene):

	def construct(self):

		self.camera.background_color = "#FFFFFF"

		# create title
		title = Txt("Minimum Edit Distance Algorithm").to_edge(UP)
		for letter in title:
			self.play(FadeIn(letter), run_time = 0.05)
		title_line = Line(LEFT*6, RIGHT*6, color=BLACK)
		title_line.next_to(title, DOWN)
		self.play(Create(title_line))

		# naive approach
		alignment = TextAlignment(self, title)

		self.wait(3)
