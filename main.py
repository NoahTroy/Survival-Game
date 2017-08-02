#import the necessary classes/modules:
from maintenance import Maintenance
import time
from water import Water

#Create the main class, from which everything else is run:
class Main:
	#Check to make sure all files are accounted for; if not, create them:
	if (not Maintenance.checkFilesExist()):
		#If not all of the necessary files exist, create them, and check/take care of possible tampering with the files:
		if (Maintenance.createDataFiles()):
			print('It has been detected that one or more files may have been tampered with.\nCheating is not tolerated under any circumstances.\nWe will give you the benefit of the doubt for now, but do not try to cheat again.\nAs a precautionary measure, all of your progress has been reset, and the game has terminated.')
			Maintenance.deleteAllDataFiles()
			exit()
		
		#Print the welcome message to screen, with a delay, as this must be a first-time player:
		welcomeMessage = 'Welcome.\nWelcome to your new life.\nTen years ago, you were falsely accused of first degree murder,\nand you were sentenced to life in prison.\nThere, you were tortured, experimented on, made half human.\nThe rest of you? Robot.\nYou are a cyborg.\nBut, thanks to a prison break, you managed to escape.\nHere you are now: lost in the middle of a forest, forced to survive on your own.\nIt is your choice how to do so.\nIn a minute, you will be let into the main control consol,\nfrom which you must issue commands, to keep yourself alive.\nGood Luck.\n\nOh, and by the way, if you ever need help, don\'t be afraid to ask...\n\n\n'
		
		for chr in welcomeMessage:
			print(chr , end = '')
			time.sleep(0.06)
			
	else:
		#Add code here to load-up all of the extra files into the variables in the resources class, such as how many people should be fetching water. Probably should add this as a method in the Maintenance class.