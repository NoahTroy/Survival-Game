#Import the necessary classes/packages:
import time
from resources import Resources

#Create a class in charge of executing all of the commands:
class Commands:
	#A method used to identify the command, and call the corresponding method:
	def identifyCommandAndCallCorrectMethod(command):
		if (command == 'help'):
			Commands.help()
		elif (command == 'explain'):
			Commands.explain()
		elif (command == 'quit'):
			Commands.quit()
		elif (command == 'update'):
			Commands.update()
		elif (command == 'show'):
			Commands.show()
		elif (command == 'tasks'):
			Commands.tasks()
		elif (command == 'barter'):
			Commands.barter()
		else:
			print('\nSorry, but the command you entered could not be found.\nPlease check your spelling, and make sure all letters in the command are lowercase.\nIf you need more help, please type the command: "help".\n')


	#A method to execute the help command:
	def help():
		print('\nHELP MENU\nHere, you will find a list of all possible commands:\n\nhelp\t\t---\tDisplays this help menu, which shows all possible commands, as well as an explanation as to what they do.\nexplain\t\t---\tExplains the basic rules, functions, and ways of the game.\nquit\t\t---\tSaves progress and quits the game.\nupdate\t\t---\tShows how many resources have been added since the last update (make sure to update at least once every five minutes; if five minutes have passed since the last update, resources will stop accumulating).\nshow\t\t---\tLists all of your resources, and their quantities to the screen.\ntasks\t\t---\tShows all available tasks that can be carried out.\n')

	#A method to give an explanation as to how the game works:0
	def explain():
		print('\nYou are a cyborg, lost in the middle of a forest.\nEvery 15 seconds, you are able to gather 2 servings of water,\nand every 30 seconds, you are able to gather two servings of food.\nBut, you become thirsty and drink a serving of water every 15 seconds,\nand likewise eat a serving of food every 30 seconds.\nVia bartering, hiring, and other techniques you will discover along the way,\nyour goal is to build yourself a forest "kingdom," where you can live in luxury.\nDon\'t get too caught-up though, for if your food or water hits 0 at any point when\nyou\'re thirsty or hungry, you die, and the game resets.\nGood Luck!\n')

	#A method which quits the game:
	def quit():
		print('\nShutting Down...')
		#Activate termination flag, to stop all threads:
		Resources.timeToQuit = True
		#Pausing to allow all threads to terminate:
		time.sleep(1.5)
		print('Shutdown Complete.\nGoodbye.\n')
		exit()

	#A method to show how much/many resources have been added since either the start of the game, or the last update:
	def update():
		Resources.printResources()
	
	#A method to show the quantity of all available resources and factors:
	def show():
		print('')
		print('Water:\t' , Resources.loadResourceAmount('water.dat'))
		print('Food:\t' , Resources.loadResourceAmount('food.dat'))
		print('Servings Of Water Consumed:\t' , Resources.loadResourceAmount('drinkers.dat'))
		print('Servings Of Food Consumed:\t' , Resources.loadResourceAmount('eaters.dat'))
		print('')
	
	#A method to list all available tasks, and their conditions:
	def tasks():
		pass
	
	#A method to show all items available for trading, as well as what they cost:
	def barter():
		pass