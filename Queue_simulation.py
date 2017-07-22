import matplotlib.pyplot as plt
import numpy as np
import threading 
import time

class myThread (threading.Thread):
	def __init__(self, threadID, operationType, timeParameter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.operationType = operationType
		self.timeParameter = timeParameter
		self.exit_flag = False

	def run(self):
		initialTime = time.time()

		while(True):
			nowTime = time.time()
			if (self.operationType == 'A'):
				self.arrive(1,self.timeParameter)
				print(self.operationType)

			elif (self.operationType == 'S' ):
				self.serve(self.timeParameter)
				print(self.operationType)	

			else:
				pass	
			plotData.append(self.showSate())
			

			if ((nowTime - initialTime) >= 25 or (self.exit_flag == True)) :
				print( "\n", nowTime - initialTime)
				self.exit_flag = True
				break


	def arrive(self,i,timeParameter):
		delayTimeParameter = np.random.exponential(scale=timeParameter, size=1)
		e = threading.Event()
		e.wait(delayTimeParameter)
		queue.append(i)
		#print(len(queue))
		
	def serve(self,timeParameter):
		if len(queue) > 0 :
			delayTimeParameter = np.random.exponential(scale=timeParameter, size=1)
			e = threading.Event()
			e.wait(delayTimeParameter) 
			queue.pop()
		else :
			pass

	def showSate(slef):
		state = len(queue)
		print("The Queue is in state : ",state)
		return state

#/////////////////////////////////////////////////////////////////////////////////

queue = []
plotData = []

def monte_carlo_simulation (arrivalRate, serviceRate,plots,x,y):
	# Create new threads
	arriveThread = myThread(1, 'A', arrivalRate)
	serviceThread = myThread(2, 'S', serviceRate )
	# Start new Threads
	arriveThread.start()
	serviceThread.start()
	arriveThread.join()
	serviceThread.join()
	print ("Exiting to Main Thread")

	plt.subplot(plots,x,y)
	plt.plot(plotData)
	queue[:] = []
	plotData[:] = []
	
#/////////////////////////////////////////////////////////////////////////////////

monte_carlo_simulation(5,4,3,2,1)
monte_carlo_simulation(20,2,3,2,2)
monte_carlo_simulation(1,20,3,2,3)
monte_carlo_simulation(10,20,3,2,4)
monte_carlo_simulation(20,10,3,2,5)
plt.show()
