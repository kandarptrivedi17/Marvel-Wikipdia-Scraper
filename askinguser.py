
class userquestions:

	def __init__(self):
		self.the_question = self.question
		# self.question_phaseone = self.questionphaseone
		# self.question_phasetwo = self.questionphasetwo
		# self.question_phasethree = self.questionphasethree
		# self.question_phasefour = self.questionphasefour
		# self.question_phasefive = self.questionphasefive
		# self.question_phasesix = self.questionphasesix




	def question(self):
		askinginput = input("So, would like to explore? Give 'Y' to enter  and 'N' to quit : ").lower()
		print()

		if askinginput == 'n':
			return('GoodBye!!!!')
			SystemExit()

		elif askinginput == 'y':
			enterphase = input (
							   "Where you want to go?\n\
							   \n\
								Press 1 for Phase One\n\
								Press 2 for Phase Two\n\
								Press 3 for Phase Three\n\
								Press 4 for Phase Four\n\
								Press 5 for Phase Five\n\
								Press 6 for Phase Six\n\
								Type 'Future' for future Movies\n\
								type 'q' to quit.: \n\
								"
								)
			return enterphase

	# def questionphaseone(self):
	# 	movieinput1 = input("For which movie you want information?\n\
	# 					1 for Iron Man\n\
	# 					2 for The Incredible Hulk\n\
	# 					3 for Iron Man 2\n\
	# 					4 for Thor\n\
	# 					5 for Captain America: The First Avenger\n\
	# 					6 for The Avengers\n\
	# 					'q' to go prevoius menu: ->  \n\
	# 					"
	# 					)

	# def questionphasetwo(self):
	# 	movieinput2 = input("For which movie you want information?\n\
	# 					1 for Iron Man 3\n\
	# 					2 for Thor: The Dark World\n\
	# 					3 for Captain America: The Winter Soldier\n\
	# 					4 for Guardians of the Galaxy\n\
	# 					5 for Avengers: Age of Ultron	\n\
	# 					6 for Ant-Man\n\
	# 					'q' to go prevoius menu: ->  \n\
	# 					"
	# 					)
	
	# def questionphasethree(self):
	# 	movieinput3 = input("For which movie you want information?\n\
	# 					1 for Captain America: Civil War\n\
	# 					2 for Doctor Strange\n\
	# 					3 for Guardians of the Galaxy Vol. 2\n\
	# 					4 for Spider-Man: Homecoming\n\
	# 					5 for Thor: Ragnarok\n\
	# 					6 for Black Panther\n\
	# 					7 for Avengers: Infinity War\n\
	# 					8 for Ant-Man and the Wasp\n\
	# 					9 for Captain Marvel\n\
	# 					10 for Avengers: Endgame\n\
	# 					11 for Spider-Man: Far From Home\n\
	# 					'q' to go prevoius menu: ->  \n\
	# 					"
	# 					)

	# def questionphasefour(self):
	# 	movieinput4 = input("For which movie you want information?\n\
	# 					1 for Black Widow\n\
	# 					2 for Shang-Chi and the Legend of the Ten Rings\n\
	# 					3 for Eternals\n\
	# 					4 for Spider-Man: No Way Home\n\
	# 					5 for Doctor Strange in the Multiverse of Madness\n\
	# 					6 for Thor: Love and Thunder\n\
	# 					7 for Black Panther: Wakanda Forever\n\
	# 					'q' to go prevoius menu: ->  \n\
	# 					"
	# 					)

	# def questionphasefive(self):
	# 	movieinput5 = input("For which movie you want information?\n\
	# 					1 for Ant-Man and the Wasp: Quantumania\n\
	# 					2 for Guardians of the Galaxy Vol. 3\n\
	# 					3 for The Marvels\n\
	# 					4 for Deadpool & Wolverine\n\
	# 					5 for Captain America: Brave New World\n\
	# 					6 for Thunderbolts\n\
	# 					'q' to go prevoius menu: ->  \n\
	# 					"
	# 					)

	# def questionphasesix(self):
	# 	movieinput6 = input("For which movie you want information?\n\
	# 					1 for The Fantastic Four: First Steps\n\
	# 					2 for Spider-Man: Brand New Day\n\
	# 					3 for Avengers: Doomsday\n\
	# 					4 for Avengers: Secret Wars\n\
	# 					'q' to go prevoius menu: ->  \n\
	# 					"
	# 					)

answerquestion = userquestions()



		
			