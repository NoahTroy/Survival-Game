import threading , time
from resources import Resources

#Create a water class, with Resources as its base class:
class Water(Resources):
	def __init__(self):
		waterThread = threading.Thread(target = self.progress , args = ())
		waterThread.start()

	def progress(self):
		while True:
			#Keep the 18 second delay, but split it up into half-a-second segments, therefore the program can keep checking whether or not it is time to quit, more-efficiently:
			for i in range(0 , 36):
				time.sleep(0.5)
				if (Resources.timeToQuit):
					break

			Resources.water = Resources.loadResourceAmount('water.dat')
			Resources.water += 1
			Resources.saveResourceAmount(Resources.water, 'water.dat')
		
			print('+1 water gathered...')