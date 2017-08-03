import pickle

#Create a resources class, the parent class to each resource, which progresses the game:
class Resources:
	#Create a quit-marker variable:
	timeToQuit = False

	#Create variables to store the amount of each resource:
	water = 0
	waterToPrint = 0
	food = 0
	foodToPrint = 0
	
	#Create a class method which loads its resource data:
	def loadResourceAmount(filename):
		filepath = ('Saved Data/' + filename)

		file = open(filepath , 'rb')
		value = pickle.load(file)
		file.close()

		return value

	#Create a class method which writes updated data to its corresponding file:
	def saveResourceAmount(value , filename):
		filepath = ('Saved Data/' + filename)

		file = open(filepath , 'wb')
		pickle.dump(value , file)
		file.close()

	#Create a class method which prints resource amount updates to the screen:
	def printResources():
		print('\n+' , Resources.waterToPrint , ' water...' , '\n' , '+' , Resources.foodToPrint , ' food...' , '\n' , sep = '')
		Resources.waterToPrint = 0
		Resources.foodToPrint = 0