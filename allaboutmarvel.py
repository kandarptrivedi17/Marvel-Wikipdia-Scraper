print()
from greetandlogo import initialgreet
print()
from phaseone import finalwiki
from phasetwo import secondwiki
from phasethree import thirdwiki
from phasefour import fourthwiki
from phasefive import fifthwiki
from phasesix import sixthwiki
from future import futurefilms
from askinguser import answerquestion


avengers = (".") * 170
print(avengers)
print()

while True:
	askinginput = input("So, would like to explore? Give 'Y' to enter  and 'N' to quit : ").lower()
	print()
	
	if askinginput == 'n':
		print('GoodBye!!!!')
		break

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

	if enterphase == '1':
		print()
		(finalwiki.intropara())
		print()
		print(finalwiki.movieslist())
		print()
		movieinput1 = input("For which movie you want information?\n\
							1 for Iron Man\n\
							2 for The Incredible Hulk\n\
							3 for Iron Man 2\n\
							4 for Thor\n\
							5 for Captain America: The First Avenger\n\
							6 for The Avengers\n\
							'q' to go prevoius menu: ->  \n\
							"
							)						

		if movieinput1 == '1':
			(finalwiki.ironman())		
		elif movieinput1 == '2':
			(finalwiki.incrediblehulk())
		elif movieinput1 == '3':
			(finalwiki.ironmantwo())
		elif movieinput1 == '4':
			(finalwiki.thormovie())
		elif movieinput1 == '5':
			(finalwiki.captainamerica())
		elif movieinput1 == '6':
			(finalwiki.theavengers())	
		elif movieinput1 == 'q':
			(answerquestion.question())
		else:
			print("Check your input")
			continue
		
	elif enterphase == '2':
		print()
		(secondwiki.intropara())
		print()
		print(secondwiki.movieslist())
		print()
		movieinput2 = input("For which movie you want information?\n\
							1 for Iron Man 3\n\
							2 for Thor: The Dark World\n\
							3 for Captain America: The Winter Soldier\n\
							4 for Guardians of the Galaxy\n\
							5 for Avengers: Age of Ultron	\n\
							6 for Ant-Man\n\
							'q' to go prevoius menu: ->  \n\
							"
							)

		if movieinput2 == '1':
			(secondwiki.ironmanthree())
		elif movieinput2 == '2':
			(secondwiki.thordarkworld())
		elif movieinput2 == '3':
			(secondwiki.captainamericawintersoldier())
		elif movieinput2 == '4':
			(secondwiki.gaurdianofgalaxy())
		elif movieinput2 == '5':
			(secondwiki.ageofultron())
		elif movieinput2 == '6':
			(secondwiki.antman())
		elif movieinput2 == 'q':
			print(answerquestion.question())
		else:
			print("Check your input")

	elif enterphase == '3':
		print()
		(thirdwiki.intropara())
		print()
		print(thirdwiki.movieslist())
		print()
		movieinput3 = input("For which movie you want information?\n\
							1 for Captain America: Civil War\n\
							2 for Doctor Strange\n\
							3 for Guardians of the Galaxy Vol. 2\n\
							4 for Spider-Man: Homecoming\n\
							5 for Thor: Ragnarok\n\
							6 for Black Panther\n\
							7 for Avengers: Infinity War\n\
							8 for Ant-Man and the Wasp\n\
							9 for Captain Marvel\n\
							10 for Avengers: Endgame\n\
							11 for Spider-Man: Far From Home\n\
							'q' to go prevoius menu: ->  \n\
							"
							)
		if movieinput3 == '1':
			(thirdwiki.civilwar())
		elif movieinput3 == '2':
			(thirdwiki.doctorstrange())
		elif movieinput3 == '3':
			(thirdwiki.gaurdiangalaxytwo())
		elif movieinput3 == '4':
			(thirdwiki.spiderhomecoming())
		elif movieinput3 == '5':
			(thirdwiki.thorragnarok())
		elif movieinput3 == '6':
			(thirdwiki.blackpanther())
		elif movieinput3 == '7':
			(thirdwiki.infinitywar())
		elif movieinput3 == '8':
			(thirdwiki.antmanwasp())
		elif movieinput3 == '9':
			(thirdwiki.captainmarvel())
		elif movieinput3 == '10':
			(thirdwiki.endgame())
		elif movieinput3 == '11':
			(thirdwiki.spiderfarfromhome())
		elif movieinput3 == 'q':
			print(answerquestion.question())
		else:
			print("Check your input")

	elif enterphase == '4':
		print()
		(fourthwiki.intropara())
		print()
		print(fourthwiki.movieslist())
		print()
		movieinput4 = input("For which movie you want information?\n\
							1 for Black Widow\n\
							2 for Shang-Chi and the Legend of the Ten Rings\n\
							3 for Eternals\n\
							4 for Spider-Man: No Way Home\n\
							5 for Doctor Strange in the Multiverse of Madness\n\
							6 for Thor: Love and Thunder\n\
							7 for Black Panther: Wakanda Forever\n\
							'q' to go prevoius menu: ->  \n\
							"
							)
		if movieinput4 == '1':
			(fourthwiki.blackwidow())
		elif movieinput4 == '2':
			(fourthwiki.shangchiandtenrings())
		elif movieinput4 == '3':
			(fourthwiki.theeternals())
		elif movieinput4 == '4':
			(fourthwiki.spidernowayhome())
		elif movieinput4 == '5':
			(fourthwiki.doctorstrangemultiverse())
		elif movieinput4 == '6':
			(fourthwiki.thorlovethunder())
		elif movieinput4 == '7':
			(fourthwiki.wakandaforever())
		elif movieinput4 == 'q':
			print(answerquestion.question())
		else:
			print("Check your input")

	elif enterphase == '5':
		print()
		(fifthwiki.intropara())
		print()
		print(fifthwiki.movieslist())
		print()
		movieinput5 = input("For which movie you want information?\n\
							1 for Ant-Man and the Wasp: Quantumania\n\
							2 for Guardians of the Galaxy Vol. 3\n\
							3 for The Marvels\n\
							4 for Deadpool & Wolverine\n\
							5 for Captain America: Brave New World\n\
							6 for Thunderbolts\n\
							'q' to go prevoius menu: ->  \n\
							"
							)

		if movieinput5 == '1':
			(fifthwiki.antmanquantumania())
		elif movieinput5 == '2':
			(fifthwiki.gurdianofgalaxythree())
		elif movieinput5 == '3':
			(fifthwiki.the_marvels())
		elif movieinput5 == '4':
			(fifthwiki.deadpoolwolverine())
		elif movieinput5 == '5':
			(fifthwiki.captainamericanewworld())
		elif movieinput5 == '6':
			(fifthwiki.thethunderbolts())
		elif movieinput5 == 'q':
			print(answerquestion.question())
		else:
			print("Check your input")

	elif enterphase == '6':
		print()
		(sixthwiki.intropara())
		print()
		print(sixthwiki.movieslist())
		print()
		movieinput6 = input("For which movie you want information?\n\
							1 for The Fantastic Four: First Steps\n\
							2 for Spider-Man: Brand New Day\n\
							3 for Avengers: Doomsday\n\
							4 for Avengers: Secret Wars\n\
							'q' to go prevoius menu: ->  \n\
							"
							)

		if movieinput6 == '1':
			(sixthwiki.thefantasticfour())
		elif movieinput6 == '2':
			(sixthwiki.spiderbrandnewday())
		elif movieinput6 == '3':
			(sixthwiki.avengersdoomsday())
		elif movieinput6 == '4':
			(sixthwiki.avengerssecretwars())
		elif movieinput5 == 'q':
			print(answerquestion.question())
		else:
			print("Check your input")
						

	elif enterphase == ('future').lower():
		print()
		(futurefilms.intropara())
		print()
		print(futurefilms.movieslist())
	elif enterphase == 'q':
		break

	else:
		print("Check the input....")
		continue