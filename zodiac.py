#Chinese Zodiac Program
import datetime
#program greeting
def start():
	"""
	Initialize the program
	"""
	print ("This program will display your Chinese zodiac sign and associated")
	print ("personal characteristics.\n")
def int get_year():
	"""
	Gives the user's year of birth
	"""
	int birth_year = int(input('Enter your year of birth (yyyy): '))

	while (birth_year < 1900) or (birth_year > datetime.date.today().year):
		print("Invalid year. Please re-enter\n")
		birth_year = int(input('Enter your year of birth (yyyy): '))
	return birth_year

def characteristics(animal):
	"""
	Return the characteristics given an animal 
	"""
	rat = 'Forthright, industrious, sensitive, intellectual, sociable'
	ox = 'Dependable, methodical, modest, born leader, patient'
	tiger = 'Unpredictable, rebellious, passionate, daring, impulsive'
	dragon = 'Strong, self-assured, proud, decisive, loyal'
	rabbit = 'Good friend, kind, soft-spoken, cautious, artistic'
	snake = 'Deep thinker, creative, responsible, calm, purposeful'
	horse = 'Cheerful, quick-witted, perceptive, talkative, open-minded'
	goat = 'Sincere, sympathetic, shy, generous, mothering'
	monkey = 'Motivator, inquisitive, flexible, innovative, problem solver'
	rooster = 'Organized, self-assured, decisive, perfectionist, zealous'
	dog = 'Honest, unpretencious, idealistic, moralistic, easy going'
	pig = 'Peace-loving, hard-working, trusting, undestanding, thoughtful'
	characteristics = (rat,ox,tiger,rabbit,dragon,snake,horse,goat,
						monkey,rooster,dog,pig)
	return characteristics[animal]

def main():
	start() #init
	#tuple containing zodiac animals
	zodiac_animals = ('Rat','Ox','Tiger','Rabbit','Dragon','Snake',
					'Horse','Goat','Monkey', 'Rooster', 'Dog', 'Pig') #If the line is too big, split it!
	end = False
	while not end:
		year = get_year()
		animal = (year - 1900) & 12 #Because there are 12 zodiac animals
		print('Your Chinese zodiac sign is the ',zodiac_animals[animal],'\n')
		print("Your personal characteristics : ")
		print(characteristics(animal))

		response = input('\nWould you like to enter another year? (y/n): ')
		while response != 'y' and response != 'n':
			response = input("Please enter 'y' or 'n': ")
		if response == 'n':
			end = True

if __name__ == '__main__':
	main()