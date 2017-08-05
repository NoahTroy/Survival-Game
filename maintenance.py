#import the necessary packages:
import os , pickle
from resources import Resources

#Create a class in charge of all of the code "maintenence":
class Maintenance:
	#Create a list of all of the files:
	fileList = ['water.dat' , 'drinkers.dat' , 'food.dat' , 'eaters.dat']

	#Define a function to check and make sure all of the necessary files exist:
	def checkFilesExist():
		#Check to make sure the directory in which the files are saved, exists:
		if (not os.path.exists('Saved Data')):
			return False

		#Check for the existence of each file:
		for file in Maintenance.fileList:
			filename = ('Saved Data/' + file)

			if (not os.path.isfile(filename)):
				return False

		#If The the code hasn't returned yet, then all files (and their parent directory) must exist. Therefore, return True:
		return True


	#Define a function to create the data files:
	def createDataFiles():
		#Loop through and create all of the files, with a default value of zero:
		defaultVariable = 0
		#This variable will return True if potential cheating detected:
		isCheating = False

		if (not os.path.exists('Saved Data')):
			os.mkdir('Saved Data')

		for file in Maintenance.fileList:
			filename = ('Saved Data/' + file)
			
			if (not os.path.isfile(filename)):
				openFile = open(filename , 'wb')
				if ((file == 'drinkers.dat') or (file == 'eaters.dat')):
					pickle.dump(1 , openFile)
				else:
					pickle.dump(defaultVariable , openFile)
				openFile.close()
			else:
				isCheating = True

		return isCheating
	
	#Define a function to delete any and all data files within the Saved Data folder, as well as the folder itself:	
	def deleteAllDataFiles():
		if (os.path.exists('Saved Data')):
		
			#Remove all files that should be within the folder, then delete the folder:
			for file in Maintenance.fileList:
				filename = ('Saved Data/' + file)
				
				if (os.path.isfile(filename)):
					os.remove(filename)
					
			os.removedirs('Saved Data')	
				
	#Define a function to load all of the necessary data into static variables in the Resources class:
	def loadData():
		Resources.water = Resources.loadResourceAmount('water.dat')
		Resources.food = Resources.loadResourceAmount('food.dat')
		Resources.drinkers = Resources.loadResourceAmount('drinkers.dat')
		Resources.eaters = Resources.loadResourceAmount('eaters.dat')