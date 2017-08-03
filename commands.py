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
		else:
			print('\nSorry, but the command you entered could not be found.\nPlease check your spelling, and make sure all letters in the command are lowercase.\nIf you need more help, please type the command: "help".\n')


	#A method to execute the help command:
	def help():
		print('\nHELP MENU\nHere, you will find a list of all possible commands:\n\nhelp\t\t---\tDisplays this help menu, which shows all possible commands, as well as an explanation as to what they do.\nexplain\t\t---\tExplains the basic rules, functions, and ways of the game.\nquit\t\t---\tSaves progress and quits the game.\nupdate\t\t---\tShows how many resources have been added since the last update.\nshow\t\t---\tLists all of your resources, and their quantities to the screen.\n')

	#A method to give an explanation as to how the game works:0
	def explain():
		print('\nAn explanation will be added here soon.\n')

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