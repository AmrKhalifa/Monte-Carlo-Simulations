<<<<<<< HEAD

import random
import matplotlib.pyplot as plt

########################################################################################################################
# dice roll method
########################################################################################################################
# 100 side dice (not fair , 51 thehouse's to 49 yours)
'''def rollDice():
	roll = random.randint(1,100)
	if (roll == 100):
		return False
	elif (roll <= 50):
		return False
	elif (100>roll> 50):
		return True
'''
########################################################################################################################
# dice roll method
########################################################################################################################
# 100 side dice (not fair , 51 thehouse's to 49 yours)
def rollDice():
	roll = random.randint(1,100)
	
	if(roll <=50):
			return False
	elif (roll >=51):
			return True

########################################################################################################################
# simple betting
########################################################################################################################
def simple_bettor(funds,initial_wager,wager_count,color):
	global broke_count_simple
	global simple_profit
	value = funds
	wager = initial_wager
	wX =[]
	vY =[]
	currentWager =1
	while (currentWager <= wager_count):
		if (rollDice()):
			value += wager
			wX.append(currentWager)
			vY.append(value)
		else :
			value -= wager
			wX.append(currentWager)
			vY.append(value)
		if (value<=0):
			broke_count_simple +=1
			break;
		currentWager +=1
	plt.plot(wX,vY,color)
	if (value > funds):
		simple_profit+=1
########################################################################################################################
# betting with martinalge strategy
########################################################################################################################
def bet_with_martinagle(funds , initial_wager, wager_count,color):
	value = funds
	wager = initial_wager
	global broke_count_martinagle
	global martinagleProfit
	wX =[]
	vY =[]
	currentWager =1
	previousWager= 'win'
	previousWagerAmount = initial_wager

	while(currentWager<=wager_count):
		if (previousWager == 'win'):
			if (rollDice()):
				value += wager
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if (value <=0):
					broke_count_martinagle+=1
					break;
		elif(previousWager == 'loss'):
			if (rollDice()):
				wager = previousWagerAmount*2
				if (value - wager)<0:
					wager = value
				value += wager
				wager = initial_wager
				previousWager = 'win'
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount*2
				if (value - wager)<0:
					wager = value

				value -= wager
				if(value<=0):
					broke_count_martinagle+=1
					wX.append(currentWager)
					vY.append(value)
					break;
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
		currentWager+=1
	plt.plot(wX,vY,color)

	if (value > funds):
		martinagleProfit+=1

########################################################################################################################
# betting with different multiples function
########################################################################################################################
def bet_with_multiples(funds,initial_wager, wager_count):
	value = funds
	wager = initial_wager
	global broke_count
	global theProfit
	global multiple
	wX =[]
	vY =[]
	currentWager =1
	previousWager= 'win'
	previousWagerAmount = initial_wager

	while(currentWager<=wager_count):
	
		if (previousWager == 'win'):
			if (rollDice()):
				value += wager
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if (value <=0):
					broke_count+=1
					break;
		elif(previousWager == 'loss'):
			if (rollDice()):
				wager = previousWagerAmount*multiple
				if (value - wager)<0:
					wager = value
				value += wager
				wager = initial_wager
				previousWager = 'win'
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount*multiple
				if (value - wager)<0:
					wager = value

				value -= wager
				if(value<=0):
					broke_count+=1
					wX.append(currentWager)
					vY.append(value)
					break;
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
		currentWager+=1
	#plt.plot(wX,vY,color)

	if (value > funds):
		theProfit+=1

########################################################################################################################
# life expectancy analysis :
########################################################################################################################

sampleSize =100
startingFunds = 10000
wagerSize = 100
wagerCount =1000

# counter =0
# broke_count_simple = 0
# broke_count_martinagle = 0
# simple_profit =0.0
# martinagleProfit = 0.0

# while (counter<sampleSize):
# 	simple_bettor(startingFunds,wagerSize,wagerCount,'k')
# 	counter+=1

# print("The death rate in simple betting is : ", (broke_count_simple/sampleSize)*100)
# print("The survival rate in simple betting is : ", 100-(broke_count_simple/sampleSize)*100)
# print("The profit rate in simple betting is : ", (simple_profit/sampleSize)*100)
# print("=*"*10)

# counter=0

# while (counter<sampleSize):
# 	bet_with_martinagle(startingFunds,wagerSize,wagerCount,'r')
# 	counter+=1

# print("The death rate with Martinagle strategey is : ", (broke_count_martinagle/sampleSize)*100)
# print("The survival rate with Martinagle strategey is : ", 100-(broke_count_martinagle/sampleSize)*100)
# print("The profit rate in Martinagle betting is : ", (martinagleProfit/sampleSize)*100)

# plt.axhline(0,color = 'r')
# plt.axhline(10000,color = 'g')
# plt.show()

#######################################################################################################################
# analysis of multiplies 
#######################################################################################################################

# lower_bust = 31
# higher_profit = 63

# for i in range (1,100):
# 	sampleSizeForMultiplies = 1000
# 	broke_count = 0.0
# 	theProfit = 0.0
# 	multiple = random.uniform(0.1,5.0)
# 	currentSample = 1

# 	while(currentSample <= sampleSizeForMultiplies):
# 		bet_with_multiples(startingFunds,wagerSize,wagerCount)
# 		currentSample+=1

# 	if((broke_count/sampleSizeForMultiplies)*100.00 < lower_bust) and ((theProfit/sampleSizeForMultiplies)*100.00>higher_profit):
# 		print ("*"*20)
# 		print("found a winner , the multiple was : ", multiple)
# 		print("broke rate is :", (broke_count/sampleSizeForMultiplies)*100.00)
# 		print("profit rate  was : ", (theProfit/sampleSizeForMultiplies)*100.00)
# 		print ("*"*20)
# 		print("\n")

# 	else :
# 		pass
# 		print ("=*="*20)
# 		print("found a loser! , the multiple was : ", multiple)
# 		print("broke rate is :", (broke_count/sampleSizeForMultiplies)*100.00)
# 		print("profit rate  was : ", (theProfit/sampleSizeForMultiplies)*100.00)
# 		print ("=*="*20)
# 		print("\n")
			
#################################################################
#################################################################			

########################################################################################################################
# D'Alembert Strategy 
########################################################################################################################

def dAlembert(funds,initial_wager, wager_count):

	value = funds
	wager = initial_wager
	currentWager = 1
	previousWager = 'win'
	previousWagerAmount = initial_wager

	global da_busts
	global dA_profit

	while (currentWager <= wager_count):

		if(previousWager == 'win'):
			if(wager == initial_wager):
				pass
			else:
				wager -= initial_wager

			#print("\n current wager :" , wager , " value :" , value)	

			if (rollDice())	:
				value += wager
				#print (" \n we won ,current value :" , value)
				previousWagerAmount = wager
			else:
				value -=wager
				previousWager = 'loss'
				previousWagerAmount = wager
				if (value <=0):
					da_busts +=1
					break;

				#print("\n we lost , current value :" , value)

				
		elif (previousWager =='loss'):
			wager = previousWagerAmount +initial_wager
			if ((value - wager)<=0):
				wager = value
			#print(" \n we lost the last wager , current wager :", wager , " value " , value)	

			if (rollDice()):
				value += wager
				previousWagerAmount = wager
				previousWager = 'win'
				#print ("\nwe won ,current value :" , value)

			else:
				if (value <= 0):
					da_busts += 1
					break;
				value -= wager_count
				previousWager = 'loss'
				previousWagerAmount = wager
				#print("\nwe lost , current value :" , value)
				

		currentWager += 1

	if (value > funds):
		dA_profit+=1	
	print (value)	


################################################################################
da_busts =0
dA_profit =0

for __ in range (1,100):
	dAlembert(startingFunds,wagerSize,wagerCount)
=======

import random
import matplotlib.pyplot as plt

########################################################################################################################
# dice roll method
########################################################################################################################
# 100 side dice (not fair , 51 thehouse's to 49 yours)
'''def rollDice():
	roll = random.randint(1,100)
	if (roll == 100):
		return False
	elif (roll <= 50):
		return False
	elif (100>roll> 50):
		return True
'''
########################################################################################################################
# dice roll method
########################################################################################################################
# 100 side dice (not fair , 51 thehouse's to 49 yours)
def rollDice():
	roll = random.randint(1,100)
	
	if(roll <=50):
			return False
	elif (roll >=51):
			return True

########################################################################################################################
# simple betting
########################################################################################################################
def simple_bettor(funds,initial_wager,wager_count,color):
	global broke_count_simple
	global simple_profit
	value = funds
	wager = initial_wager
	wX =[]
	vY =[]
	currentWager =1
	while (currentWager <= wager_count):
		if (rollDice()):
			value += wager
			wX.append(currentWager)
			vY.append(value)
		else :
			value -= wager
			wX.append(currentWager)
			vY.append(value)
		if (value<=0):
			broke_count_simple +=1
			break;
		currentWager +=1
	plt.plot(wX,vY,color)
	if (value > funds):
		simple_profit+=1
########################################################################################################################
# betting with martinalge strategy
########################################################################################################################
def bet_with_martinagle(funds , initial_wager, wager_count,color):
	value = funds
	wager = initial_wager
	global broke_count_martinagle
	global martinagleProfit
	wX =[]
	vY =[]
	currentWager =1
	previousWager= 'win'
	previousWagerAmount = initial_wager

	while(currentWager<=wager_count):
		if (previousWager == 'win'):
			if (rollDice()):
				value += wager
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if (value <=0):
					broke_count_martinagle+=1
					break;
		elif(previousWager == 'loss'):
			if (rollDice()):
				wager = previousWagerAmount*2
				if (value - wager)<0:
					wager = value
				value += wager
				wager = initial_wager
				previousWager = 'win'
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount*2
				if (value - wager)<0:
					wager = value

				value -= wager
				if(value<=0):
					broke_count_martinagle+=1
					wX.append(currentWager)
					vY.append(value)
					break;
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
		currentWager+=1
	plt.plot(wX,vY,color)

	if (value > funds):
		martinagleProfit+=1

########################################################################################################################
# betting with different multiples function
########################################################################################################################
def bet_with_multiples(funds,initial_wager, wager_count):
	value = funds
	wager = initial_wager
	global broke_count
	global theProfit
	global multiple
	wX =[]
	vY =[]
	currentWager =1
	previousWager= 'win'
	previousWagerAmount = initial_wager

	while(currentWager<=wager_count):
	
		if (previousWager == 'win'):
			if (rollDice()):
				value += wager
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if (value <=0):
					broke_count+=1
					break;
		elif(previousWager == 'loss'):
			if (rollDice()):
				wager = previousWagerAmount*multiple
				if (value - wager)<0:
					wager = value
				value += wager
				wager = initial_wager
				previousWager = 'win'
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount*multiple
				if (value - wager)<0:
					wager = value

				value -= wager
				if(value<=0):
					broke_count+=1
					wX.append(currentWager)
					vY.append(value)
					break;
				previousWager = 'loss'
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
		currentWager+=1
	#plt.plot(wX,vY,color)

	if (value > funds):
		theProfit+=1

########################################################################################################################
# life expectancy analysis :
########################################################################################################################

sampleSize =100
startingFunds = 10000
wagerSize = 100
wagerCount =1000

# counter =0
# broke_count_simple = 0
# broke_count_martinagle = 0
# simple_profit =0.0
# martinagleProfit = 0.0

# while (counter<sampleSize):
# 	simple_bettor(startingFunds,wagerSize,wagerCount,'k')
# 	counter+=1

# print("The death rate in simple betting is : ", (broke_count_simple/sampleSize)*100)
# print("The survival rate in simple betting is : ", 100-(broke_count_simple/sampleSize)*100)
# print("The profit rate in simple betting is : ", (simple_profit/sampleSize)*100)
# print("=*"*10)

# counter=0

# while (counter<sampleSize):
# 	bet_with_martinagle(startingFunds,wagerSize,wagerCount,'r')
# 	counter+=1

# print("The death rate with Martinagle strategey is : ", (broke_count_martinagle/sampleSize)*100)
# print("The survival rate with Martinagle strategey is : ", 100-(broke_count_martinagle/sampleSize)*100)
# print("The profit rate in Martinagle betting is : ", (martinagleProfit/sampleSize)*100)

# plt.axhline(0,color = 'r')
# plt.axhline(10000,color = 'g')
# plt.show()

#######################################################################################################################
# analysis of multiplies 
#######################################################################################################################

# lower_bust = 31
# higher_profit = 63

# for i in range (1,100):
# 	sampleSizeForMultiplies = 1000
# 	broke_count = 0.0
# 	theProfit = 0.0
# 	multiple = random.uniform(0.1,5.0)
# 	currentSample = 1

# 	while(currentSample <= sampleSizeForMultiplies):
# 		bet_with_multiples(startingFunds,wagerSize,wagerCount)
# 		currentSample+=1

# 	if((broke_count/sampleSizeForMultiplies)*100.00 < lower_bust) and ((theProfit/sampleSizeForMultiplies)*100.00>higher_profit):
# 		print ("*"*20)
# 		print("found a winner , the multiple was : ", multiple)
# 		print("broke rate is :", (broke_count/sampleSizeForMultiplies)*100.00)
# 		print("profit rate  was : ", (theProfit/sampleSizeForMultiplies)*100.00)
# 		print ("*"*20)
# 		print("\n")

# 	else :
# 		pass
# 		print ("=*="*20)
# 		print("found a loser! , the multiple was : ", multiple)
# 		print("broke rate is :", (broke_count/sampleSizeForMultiplies)*100.00)
# 		print("profit rate  was : ", (theProfit/sampleSizeForMultiplies)*100.00)
# 		print ("=*="*20)
# 		print("\n")
			
#################################################################
#################################################################			

########################################################################################################################
# D'Alembert Strategy 
########################################################################################################################

def dAlembert(funds,initial_wager, wager_count):

	value = funds
	wager = initial_wager
	currentWager = 1
	previousWager = 'win'
	previousWagerAmount = initial_wager

	global da_busts
	global dA_profit

	while (currentWager <= wager_count):

		if(previousWager == 'win'):
			if(wager == initial_wager):
				pass
			else:
				wager -= initial_wager

			#print("\n current wager :" , wager , " value :" , value)	

			if (rollDice())	:
				value += wager
				#print (" \n we won ,current value :" , value)
				previousWagerAmount = wager
			else:
				value -=wager
				previousWager = 'loss'
				previousWagerAmount = wager
				if (value <=0):
					da_busts +=1
					break;

				#print("\n we lost , current value :" , value)

				
		elif (previousWager =='loss'):
			wager = previousWagerAmount +initial_wager
			if ((value - wager)<=0):
				wager = value
			#print(" \n we lost the last wager , current wager :", wager , " value " , value)	

			if (rollDice()):
				value += wager
				previousWagerAmount = wager
				previousWager = 'win'
				#print ("\nwe won ,current value :" , value)

			else:
				if (value <= 0):
					da_busts += 1
					break;
				value -= wager_count
				previousWager = 'loss'
				previousWagerAmount = wager
				#print("\nwe lost , current value :" , value)
				

		currentWager += 1

	if (value > funds):
		dA_profit+=1	
	print (value)	


################################################################################
da_busts =0
dA_profit =0

for __ in range (1,100):
	dAlembert(startingFunds,wagerSize,wagerCount)
>>>>>>> 8bf8ba86b372e7bac1a5ab5c8f94fe464ed93e9f
