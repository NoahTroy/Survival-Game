import threading , time
from resources import Resources

#Create a water class, with Resources as its base class:
class Water(Resources):
	#Thread this object right from its creation:
	def __init__(self):
		waterThread = threading.Thread(target = self.progress , args = ())
		waterThread.start()

	def progress(self):
		while True:
			#Keep the 18 second delay, but split it up into half-a-second segments, therefore the program can keep checking whether or not it is time to quit, more-efficiently:
			for i in range(0 , 30):
				time.sleep(0.5)
				if (Resources.timeToQuit):
					break

			#Check to make sure the program hasn't been idling for five or more minutes, then update resource amount:
			if ((time.time() - Resources.timeOfLastPrint) < 300):
				Resources.water = Resources.loadResourceAmount('water.dat')
				Resources.drinkers = Resources.loadResourceAmount('drinkers.dat')
				Resources.water += 2
				Resources.waterToPrint += 2
				Resources.saveResourceAmount((Resources.water - Resources.drinkers) , 'water.dat')

			if (Resources.timeToQuit):
				break