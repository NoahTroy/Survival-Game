import threading , time
from resources import Resources

#Create a food class, with Resources as its base class:
class Food(Resources):
	#Thread this object right from its creation:
	def __init__(self):
		foodThread = threading.Thread(target = self.progress , args = ())
		foodThread.start()

	def progress(self):
		while True:
			#Keep the 18 second delay, but split it up into half-a-second segments, therefore the program can keep checking whether or not it is time to quit, more-efficiently:
			for i in range(0 , 60):
				time.sleep(0.5)
				if (Resources.timeToQuit):
					break

			#Check to make sure the program hasn't been idling for five or more minutes, then update resource amount:
			if ((time.time() - Resources.timeOfLastPrint) < 300):
				Resources.food = Resources.loadResourceAmount('food.dat')
				Resources.eaters = Resources.loadResourceAmount('eaters.dat')
				Resources.food += 2
				Resources.foodToPrint += 2
				Resources.saveResourceAmount((Resources.food - Resources.eaters) , 'food.dat')
			
			if (Resources.timeToQuit):
				break